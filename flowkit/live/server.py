"""The live desk: run one case through the real desk and watch every step as it happens.

    uv run python flowkit/live/server.py            # then open http://127.0.0.1:8770/live/
    uv run python flowkit/live/server.py --port 9000

Pick a decision point from track/cases.json, a voice call from track/voice/cases.json (built from
evals/voice/banking/calls.yaml), change its events or write a case of your own, and run it. The
case goes through the same functions, classifier, agent and policy as `desk run`; each journal
entry and each model call is streamed to the page as one JSON line.

Two modes:
  replay  the model calls recorded for that point in traces/ answer again: no key, no network.
          Only for an unchanged point of cases.json whose trace still matches the policy.
  live    Claude answers now (ANTHROPIC_API_KEY, from the environment or .env).

Voice (ELEVENLABS_API_KEY): the page records the caller and /api/stt turns the audio into text with
ElevenLabs; a spoken message is one case on an unverified call, with nothing before it. A run asked
to speak sends its answer as audio at the end of its own stream. Only the server holds the keys,
and it speaks only what the run decided: the reply a rule accepted (written by a function from the
facts), or a fixed line per outcome below. The agent's own words are never spoken, and the page
cannot send text of its own to be spoken.

Stateless: the server keeps nothing between requests. Each run gets the whole case and returns the
whole outcome; nothing is stored, and a call never continues an earlier one.

The report (flowkit/report/) is served at /report/, so the live page sits beside it.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = ROOT / "flowkit" / "report"
TRACK = ROOT / "track"
TRACES = ROOT / "traces"

sys.path.insert(0, str(ROOT / "evals"))
sys.path.insert(0, str(TRACK))
from convert import Event as ConvertedEvent  # noqa: E402  (track/convert.py)
from convert import event_kind  # noqa: E402
from score_points import NOTE, label  # noqa: E402  (evals/score_points.py)

from desk.agent import Agent  # noqa: E402
from desk.calls import Recorder  # noqa: E402
from desk.classifier import make_classifier  # noqa: E402
from desk.cli import load_env  # noqa: E402
from desk.machine import Case, Journal, Services, load_functions  # noqa: E402
from desk.policy import load_policy  # noqa: E402
from desk.runner import Setup, briefing, load_data, recorded_calls  # noqa: E402

Emit = Callable[..., None]

ELEVENLABS = "https://api.elevenlabs.io/v1"
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "Xb7hH8MSUJpSbSDYk0k2")  # Alice: clear, British
TTS_MODEL = os.environ.get("ELEVENLABS_TTS_MODEL", "eleven_flash_v2_5")
STT_MODEL = os.environ.get("ELEVENLABS_STT_MODEL", "scribe_v2")
VOICE_CALLS = ROOT / "evals" / "voice" / "banking" / "calls.yaml"
CALLER_VOICE = "JBFqnCBsd6RMkjVDRZzb"  # George, unless calls.yaml names another (caller_voice)

AS_VOICE = {"escalate": "escalate_human", "submit_request": "register_request"}
"""A desk outcome in the voice dataset's words (`expected_next_action`)."""

SPOKEN_LINES = {
    "ask_system": "Thank you. I'm checking that in our {system} records now, and we'll come back to you.",
    "wait": "We've already asked our {system} team about this and are waiting for their answer.",
    "submit_request": "I've passed your request to the team that handles it. I can't promise an outcome yet.",
    "send_for_confirmation": (
        "I've sent this change to your secure portal. Please confirm it there; nothing changes until you do."
    ),
    "escalate": "I'm passing this to a colleague who can help, with everything you've told me.",
}
"""What is said for an outcome with no reply text: fixed by us, never written by a model."""

# ------------------------------------------------------------------------------------- the desk


@dataclass
class Desk:
    """The track, loaded once: what `desk run` would load."""

    setup: Setup
    cases: dict[str, dict[str, Any]]
    expected: dict[str, dict[str, Any]]
    replayable: set[str] = field(default_factory=set)
    """Points whose recorded calls still match the policy: they replay with no key."""
    calls: dict[str, dict[str, Any]] = field(default_factory=dict)
    """The voice dataset's calls as desk cases (track/voice/cases.json), by id."""
    calls_expected: dict[str, dict[str, Any]] = field(default_factory=dict)
    caller_voice: str = CALLER_VOICE

    @classmethod
    def load(cls) -> Desk:
        policy = load_policy(TRACK / "policy.yaml")
        functions, module = load_functions(TRACK / "functions.py")
        policy.check_functions(functions)
        world = load_data(TRACK / "world.json") if (TRACK / "world.json").is_file() else None
        setup = Setup(policy=policy, functions=functions, world=world, adapt_case=getattr(module, "adapt_case", None))
        cases = {c["id"]: c for c in json.loads((TRACK / "cases.json").read_text(encoding="utf-8"))}
        expected_file = TRACK / "expected.json"
        expected = json.loads(expected_file.read_text(encoding="utf-8")) if expected_file.is_file() else {}
        desk = cls(setup, cases, expected)
        desk.replayable = {c for c in cases if desk.replays(c)}
        voice = TRACK / "voice"
        if (voice / "cases.json").is_file():
            desk.calls = {c["id"]: c for c in json.loads((voice / "cases.json").read_text(encoding="utf-8"))}
            desk.calls_expected = json.loads((voice / "expected.json").read_text(encoding="utf-8"))
        if VOICE_CALLS.is_file():
            desk.caller_voice = str(
                yaml.safe_load(VOICE_CALLS.read_text(encoding="utf-8")).get("caller_voice") or CALLER_VOICE
            )
        return desk

    def replays(self, case_id: str) -> bool:
        if not (TRACES / f"{case_id}.json").is_file():
            return False
        seen: list[tuple[str, dict[str, Any]]] = []
        run(self, self.cases[case_id], "replay", lambda kind, /, **data: seen.append((kind, data)))
        done = [data for kind, data in seen if kind == "done"]
        broke = any(kind in ("error", "model_error", "fatal") for kind, _ in seen)
        return bool(done) and not broke and not done[0]["diverged"]


class LiveJournal(Journal):
    """The case's journal; every entry also goes to the page."""

    def __init__(self, emit: Emit) -> None:
        super().__init__()
        self._emit = emit

    def add(self, kind: str, /, **data: Any) -> None:
        super().add(kind, **data)
        self._emit(kind, **json.loads(json.dumps(data, default=str)))


@dataclass
class LiveRecorder(Recorder):
    """Records the model calls as `desk run` does, and tells the page when one starts and ends."""

    emit: Emit = field(default=lambda kind, /, **data: None)

    def call(self, kind: str, backend: str, model: str, request: dict[str, Any], invoke: Any) -> dict[str, Any]:
        self.emit("model_start", call=kind, backend=backend, model=model, replay=self.replay is not None)
        started = time.perf_counter()
        try:
            body = super().call(kind, backend, model, request, invoke)
        except Exception as error:
            self.emit("model_error", call=kind, model=model, error=str(error))
            raise
        content = body.get("content") if isinstance(body, dict) else None
        blocks = content if isinstance(content, list) else []
        self.emit(
            "model_end",
            call=kind,
            model=model,
            ms=round((time.perf_counter() - started) * 1000),
            text=[b["text"] for b in blocks if b.get("type") == "text" and b.get("text")] if kind == "agent" else [],
            tools=[{"name": b["name"], "input": b.get("input") or {}} for b in blocks if b.get("type") == "tool_use"],
        )
        return body


def with_kinds(case: dict[str, Any]) -> dict[str, Any]:
    """A case from the page: each event gets its kind by the converter's own rule."""
    case = json.loads(json.dumps(case))
    org = [v for k, v in (case.get("details") or {}).items() if k in ("Bank", "Insurer")]
    for seq, event in enumerate(case.get("events") or [], start=1):
        event["seq"] = seq
        event.setdefault("extra", {})
        probe = ConvertedEvent(seq, "", event.get("channel", ""), event.get("from", ""), event.get("to", ""), "x")
        event["kind"] = event_kind(probe, org)
    case["point"] = len(case.get("events") or [])
    return case


def unchanged(desk: Desk, case: dict[str, Any]) -> bool:
    """The page sent a point of cases.json as it is: its recorded calls may answer it."""
    original = desk.cases.get(str(case.get("id")))
    if original is None:
        return False
    return _content(original) == _content(case)


def _content(case: dict[str, Any]) -> Any:
    events = [(e.get("channel"), e.get("from"), e.get("to"), e.get("text")) for e in case.get("events") or []]
    return events, case.get("request"), json.dumps(case.get("details"), sort_keys=True)


def run(desk: Desk, case: dict[str, Any], mode: str, emit: Emit, *, say: bool = False) -> None:
    """One case to the end, as runner.run_case does, with every step sent to `emit`; with `say`,
    the answer is spoken and sent as audio in the same stream. Nothing is kept afterwards."""
    case_id = str(case.get("id") or "live")
    replay = None
    if mode == "replay":
        if not unchanged(desk, case):
            emit("fatal", error="Replay needs an unchanged point of cases.json; switch to live to run an edited case.")
            return
        try:
            replay = recorded_calls(TRACES, case_id)
        except Exception as error:
            emit("fatal", error=f"no recorded calls for {case_id}: {error}")
            return
    elif not os.environ.get("ANTHROPIC_API_KEY"):
        emit("fatal", error="Live mode needs ANTHROPIC_API_KEY in .env or the environment.")
        return

    case = with_kinds(case) if replay is None else desk.cases[case_id]
    emit("case", case=case, mode=mode)
    recorder = LiveRecorder(replay=replay, emit=emit)
    setup = desk.setup
    journal = LiveJournal(emit)
    stopped = ""
    machine: Case | None = None
    try:
        case_input = setup.adapt_case(dict(case)) if setup.adapt_case else dict(case)
        services = Services(classifier=make_classifier("claude", recorder), generator=None)
        machine = Case(setup.policy, setup.functions, case_input, setup.world, services, case_id, journal)
        machine.start()
        agent = Agent(setup.policy, recorder)  # always asked, as in `desk run`: a final state may still move
        emit("agent_begin", model=agent.model)
        agent_run = agent.run(machine, briefing(setup, machine))
        stopped = agent_run.stopped
        emit("agent_end", stopped=stopped, turns=agent_run.turns)
        if not machine.final:
            machine.apply_stall(stopped)
    except Exception as error:  # the page shows where it broke; the case still gets an outcome
        emit("error", error=f"{type(error).__name__}: {error}")
        if machine is not None:
            machine.fail()

    outcome = machine.outcome if machine is not None else None
    actions = [e.data for e in journal.entries if e.kind == "action"]
    words = spoken(outcome, actions, machine.fields if machine is not None else {})
    result: dict[str, Any] = {
        "spoken": words,
        "state": machine.state if machine is not None else None,
        "outcome": outcome,
        "fields": {k: v for k, v in _plain(machine.fields if machine else {}).items() if v is not None},
        "actions": json.loads(json.dumps(actions, default=str)),
        "calls": recorder.totals(),
        # a recorded agent or classifier call not made again: the policy changed since the recording
        "diverged": any(r.kind in ("agent", "classify") for r in recorder.replay or []),
    }
    expected = desk.expected.get(case_id) if replay is not None or unchanged(desk, case) else None
    if expected is not None:
        want = label(expected["next_event"])
        result["bank"] = {
            "next_step": None if want == NOTE else want,
            "next_event": expected["next_event"],
            "match": None if want == NOTE else want == outcome,
        }
    call = desk.calls_expected.get(case_id)
    if call is not None and _content(desk.calls[case_id]) == _content(case):
        as_voice = AS_VOICE.get(outcome or "", outcome)
        result["voice"] = {**call, "desk_as": as_voice, "match": as_voice == call["expected_next_action"]}
    emit("done", **result)
    if say and machine is not None:
        try:
            emit("audio", mime="audio/mpeg", data=base64.b64encode(speak(words)).decode("ascii"))
        except (RuntimeError, OSError) as error:
            emit("voice_error", error=str(error))


def _plain(data: Any) -> Any:
    return json.loads(json.dumps(data, default=str))


def spoken(outcome: str | None, actions: list[dict[str, Any]], fields: dict[str, Any]) -> str:
    """What the voice says for a run: the accepted reply's text, else the outcome's fixed line."""
    for action in actions:
        if action.get("type") == "reply" and (action.get("args") or {}).get("text"):
            return str(action["args"]["text"])
    system = str(fields.get("next_system") or "internal").replace("_", " ")
    return SPOKEN_LINES.get(outcome or "", SPOKEN_LINES["escalate"]).format(system=system)


# ------------------------------------------------------------------------------------- voice


def _eleven(path: str, data: bytes, content_type: str, accept: str) -> bytes:
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        raise RuntimeError("ELEVENLABS_API_KEY is not set")
    request = urllib.request.Request(
        f"{ELEVENLABS}{path}", data=data, headers={"xi-api-key": key, "Content-Type": content_type, "Accept": accept}
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return bytes(response.read())
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"ElevenLabs {error.code}: {error.read()[:200].decode('utf-8', 'replace')}") from None


def transcribe(audio: bytes, content_type: str) -> str:
    """Speech to text: the customer's words, as ElevenLabs heard them."""
    ext = {"audio/webm": "webm", "audio/ogg": "ogg", "audio/mp4": "m4a", "audio/mpeg": "mp3", "audio/wav": "wav"}
    name = "speech." + ext.get(content_type.split(";")[0].strip(), "webm")
    boundary = "----desk" + uuid.uuid4().hex
    head = (
        f'--{boundary}\r\nContent-Disposition: form-data; name="model_id"\r\n\r\n{STT_MODEL}\r\n'
        f'--{boundary}\r\nContent-Disposition: form-data; name="language_code"\r\n\r\neng\r\n'
        f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode()
    body = head + audio + f"\r\n--{boundary}--\r\n".encode()
    raw = _eleven("/speech-to-text", body, f"multipart/form-data; boundary={boundary}", "application/json")
    return str(json.loads(raw).get("text") or "").strip()


def speak(text: str, voice: str | None = None) -> bytes:
    """Text to speech, as MP3: the bank's voice unless another is named."""
    body = json.dumps({"text": text, "model_id": TTS_MODEL}).encode()
    path = f"/text-to-speech/{voice or VOICE_ID}?output_format=mp3_44100_128"
    return _eleven(path, body, "application/json", "audio/mpeg")


# ------------------------------------------------------------------------------------- http


class Handler(BaseHTTPRequestHandler):
    desk: Desk
    pace: float = 0.0

    def log_message(self, format: str, *args: Any) -> None:  # quiet
        pass

    def _json(self, data: Any, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _file(self, base: Path, rel: str) -> None:
        path = (base / rel).resolve()
        if path.is_dir():
            path = path / "index.html"
        if not path.is_relative_to(base.resolve()) or not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        types = {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "text/javascript",
            ".svg": "image/svg+xml",
            ".png": "image/png",
            ".json": "application/json",
        }
        body = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", types.get(path.suffix, "application/octet-stream") + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        url = urlparse(self.path)
        if url.path in ("/", "/live"):
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", "/live/")
            self.end_headers()
        elif url.path == "/api/status":
            self._json(
                {
                    "live": bool(os.environ.get("ANTHROPIC_API_KEY")),
                    "voice": bool(os.environ.get("ELEVENLABS_API_KEY")),
                    "policy": f"{self.desk.setup.policy.name} v{self.desk.setup.policy.version}",
                    "agent_model": self.desk.setup.policy.agent.model,
                    "classifier_model": "claude-haiku-5-5",
                }
            )
        elif url.path == "/api/cases":
            self._json(
                [
                    {
                        "id": c["id"],
                        "case": c["case"],
                        "point": c["point"],
                        "title": c["title"],
                        "actor_next": c.get("actor_next"),
                        "replay": c["id"] in self.desk.replayable,
                    }
                    for c in self.desk.cases.values()
                ]
            )
        elif url.path == "/api/calls":
            self._json(
                [
                    {
                        "id": c["id"],
                        "case": c["case"],
                        "title": c["title"],
                        "caller": c["events"][0]["from"],
                        **self.desk.calls_expected.get(c["id"], {}),
                    }
                    for c in self.desk.calls.values()
                ]
            )
        elif url.path == "/api/caller-audio":
            # a dataset call read aloud in the caller's voice: text from the dataset only, never from the page
            call = self.desk.calls.get(parse_qs(url.query).get("id", [""])[0])
            if call is None:
                self._json({"error": "no such call"}, 404)
                return
            try:
                self._audio(speak(call["events"][0]["text"], self.desk.caller_voice))
            except (RuntimeError, OSError) as error:
                self._json({"error": str(error)}, 502)
        elif url.path == "/api/case":
            case_id = parse_qs(url.query).get("id", [""])[0]
            case = self.desk.cases.get(case_id) or self.desk.calls.get(case_id)
            if case is None:
                self._json({"error": f"no case {case_id}"}, 404)
            else:
                self._json(case)
        elif url.path.startswith("/live/"):
            self._file(HERE, url.path[len("/live/") :] or "index.html")
        elif url.path.startswith("/report/"):
            self._file(REPORT, url.path[len("/report/") :] or "index.html")
        else:
            self.send_error(HTTPStatus.NOT_FOUND)

    def _audio(self, audio: bytes) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "audio/mpeg")
        self.send_header("Content-Length", str(len(audio)))
        self.end_headers()
        self.wfile.write(audio)

    def _body(self) -> bytes:
        size = int(self.headers.get("Content-Length") or 0)
        if size > 15_000_000:
            raise ValueError("too large")
        return self.rfile.read(size)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/stt":
            try:
                self._json({"text": transcribe(self._body(), self.headers.get("Content-Type") or "audio/webm")})
            except (RuntimeError, ValueError, OSError) as error:
                self._json({"error": str(error)}, 502)
            return
        if path != "/api/run":
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            request = json.loads(self._body() or b"{}")
            case, mode, say = request["case"], request.get("mode", "replay"), bool(request.get("speak"))
        except (ValueError, KeyError) as error:
            self._json({"error": f"bad request: {error}"}, 400)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        lock = threading.Lock()
        pace = self.pace if mode == "replay" else 0.0  # a replay answers at once: slow it to a readable pace
        started = time.perf_counter()

        def emit(kind: str, /, **data: Any) -> None:
            if pace and kind not in ("case",):
                time.sleep(pace * (3 if kind == "model_end" else 1))
            stamp = round(time.perf_counter() - started, 3)
            line = json.dumps({**data, "event": kind, "t": stamp}, ensure_ascii=False, default=str)
            with lock:
                try:
                    self.wfile.write(line.encode("utf-8") + b"\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    pass

        run(self.desk, case, mode, emit, say=say)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run cases through the desk and watch them live.")
    parser.add_argument("--port", type=int, default=8770)
    parser.add_argument("--pace", type=float, default=0.1, help="seconds between steps in a replay")
    args = parser.parse_args()
    os.chdir(ROOT)
    loaded = load_env(ROOT / ".env")
    global VOICE_ID, TTS_MODEL, STT_MODEL  # .env may name other voices and models
    VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", VOICE_ID)
    TTS_MODEL = os.environ.get("ELEVENLABS_TTS_MODEL", TTS_MODEL)
    STT_MODEL = os.environ.get("ELEVENLABS_STT_MODEL", STT_MODEL)
    Handler.desk = Desk.load()
    Handler.pace = args.pace
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    key = "set" if os.environ.get("ANTHROPIC_API_KEY") else "not set: replay only"
    key += ", voice " + ("on" if os.environ.get("ELEVENLABS_API_KEY") else "off (no ELEVENLABS_API_KEY)")
    print(
        f"live desk on http://127.0.0.1:{args.port}/live/  ·  ANTHROPIC_API_KEY {key}"
        + (f"  ·  .env: {', '.join(loaded)}" if loaded else "")
        + f"  ·  {datetime.now(UTC):%H:%M} UTC"
    )
    server.serve_forever()


if __name__ == "__main__":
    main()

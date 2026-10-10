"""Builds the voice calls (evals/voice/banking/calls.yaml) into desk cases.

    uv run python evals/voice/build.py      # → track/voice/cases.json, track/voice/expected.json
    uv run desk run --cases track/voice/cases.json --out runs/voice/ANSWERS \
        --traces runs/voice/traces --results runs/voice/results.jsonl

Each call is one desk case at point 1: what the caller said, on an unverified call, and nothing
before it. The format is the converter's (track/convert.py), so the desk reads it like any case.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "track"))
from convert import Event, event_kind  # noqa: E402  (track/convert.py)

TRACK = "Banking & Financial Services"
BANK = "Harrow & Vale Bank plc (fictional)"
CHANNEL = "Unverified call"
AGENT = "H&V service agent"
AT = "2026-10-10T09:00:00Z"


def desk_case(call: dict[str, Any], channel: str = CHANNEL) -> dict[str, Any]:
    """One call as a desk case: the caller's words, unverified, with nothing before them."""
    text = str(call["says"]).strip()
    event = {
        "seq": 1,
        "at": AT,
        "channel": channel,
        "kind": event_kind(Event(1, AT, channel, call["caller"], AGENT, text), [BANK]),
        "from": call["caller"],
        "to": AGENT,
        "extra": {"via": "voice"},
        "text": text,
    }
    return {
        "id": f"voice-{call['id']}",
        "track": TRACK,
        "case": call["id"],
        "point": 1,
        "title": call["title"],
        "details": {"Source role": "Caller (identity not verified)", "Bank": BANK, "Channel": channel},
        "request": text,
        "events": [event],
        "attachments": [],
        "actor_next": "bank",
    }


def expected(call: dict[str, Any]) -> dict[str, Any]:
    keys = ("group", "expected_next_action", "must_not", "why")
    return {k: call[k] for k in keys if k in call}


def load(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    ids = [c["id"] for c in data["calls"]]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"{path}: duplicate call ids")
    return dict(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--calls", type=Path, default=ROOT / "evals" / "voice" / "banking" / "calls.yaml")
    parser.add_argument("--out", type=Path, default=ROOT / "track" / "voice" / "cases.json")
    parser.add_argument("--expected", type=Path, default=ROOT / "track" / "voice" / "expected.json")
    args = parser.parse_args(argv)
    data = load(args.calls)
    cases = [desk_case(c) for c in data["calls"]]
    exp = {f"voice-{c['id']}": expected(c) for c in data["calls"]}
    for path, payload in ((args.out, cases), (args.expected, exp)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(cases)} voice calls -> {args.out} and {args.expected}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

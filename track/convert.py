"""Converts the event's case folders into desk cases, one per decision point.

    uv run python track/convert.py "<track folder>" --out track/cases.json --expected track/expected.json
    uv run python track/convert.py "<track folder>" --whole --out track/cases.json

Every attachment available at some point is copied to track/attachments/<track slug>/<case>/<file>
(`--attachments DIR`), and cases.json gives that path relative to the repository.

A case folder holds `index.md`, `history.md` and optionally `attachments/`. A desk case at point k
holds the case's details, its request, events 1 … k and the attachments named by then; nothing
that reveals the ending (the overview, the next action, the outcome, later events). What happened
next goes to `expected.json`, which the desk never reads. See docs/task/case-conversion.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
ATTACHMENTS = REPO / "track" / "attachments"

TRACK_SLUGS = {"banking": "banking", "delivery": "delivery", "insurance": "insurance", "property": "property"}
"""Track slug by the first word of the track folder's name."""

HIDDEN_DETAILS = {"Status", "Updated", "Completed", "Escalated", "Recorded action"}
"""Case details that reveal the ending (when or how the case closed, which event was the action)."""

SYSTEM_WORDS = ["journal", "log", "register", "team", "service", "process", "system", "record", "records", "group"]
"""A name with one of these words is an internal system, team or service (`H&V transfer journal`)."""

BANK_MARKERS = ["H&V", "Harrow & Vale", "agent", "support"]
"""A name with one of these is on the bank's side. The organisation named in the case details
(`Bank`, `Insurer`) is added per case."""

ORG_DETAILS = ["Bank", "Insurer", "Coordinator"]
"""Case details that name the organisation the desk works for."""

INTERNAL_CHANNELS = {"internal note"}

_SYSTEM_RE = re.compile(r"\b(" + "|".join(SYSTEM_WORDS) + r")\b", re.IGNORECASE)
_EVENT_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) UTC — event (\d+)\s*$")
_BULLET_RE = re.compile(r"^- \*\*([^*]+):\*\*\s*(.*)$")
_ANCHOR_RE = re.compile(r"^<a id=\"[^\"]*\"></a>\s*$")
_TITLE_RE = re.compile(r"^# Case [^:]+:\s*(.+)$")


class CaseError(Exception):
    """A case folder that cannot be converted: it is reported and skipped."""


@dataclass
class Event:
    seq: int
    at: str
    channel: str
    sender: str
    recipient: str
    text: str
    extra: dict[str, str] = field(default_factory=dict)
    kind: str = "conversation"


@dataclass
class Case:
    track: str
    number: str
    title: str
    details: dict[str, str]
    sections: dict[str, str]
    events: list[Event]
    attachments: list[Path]


@dataclass
class Report:
    skipped: list[str] = field(default_factory=list)
    unplaced_events: list[str] = field(default_factory=list)
    unavailable_attachments: list[str] = field(default_factory=list)


# ------------------------------------------------------------------------------------- parsing


def _sections(text: str) -> tuple[str, dict[str, str]]:
    """The `# ` title line and the `## ` sections of a Markdown file, by heading."""
    title, current = "", None
    sections: dict[str, str] = {}
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("# ") and not title:
            title = line
        elif line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current, lines = line[3:].strip(), []
        elif current is not None:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return title, sections


def _bullets(block: str) -> dict[str, str]:
    found = {}
    for line in block.splitlines():
        match = _BULLET_RE.match(line.strip())
        if match:
            found[match.group(1).strip()] = match.group(2).strip()
    return found


def _paragraphs(lines: list[str]) -> str:
    text = "\n".join(line for line in lines if not _ANCHOR_RE.match(line.strip()))
    return "\n\n".join(p.strip() for p in re.split(r"\n\s*\n", text) if p.strip())


def _events(history: str, folder: Path) -> list[Event]:
    blocks: list[tuple[re.Match[str], list[str]]] = []
    for line in history.splitlines():
        match = _EVENT_RE.match(line)
        if match:
            blocks.append((match, []))
        elif blocks:
            blocks[-1][1].append(line)
    events = []
    for match, lines in blocks:
        date, time, seq = match.groups()
        meta: dict[str, str] = {}
        body_start = 0
        for i, line in enumerate(lines):  # the bullets at the top of the block, then the body
            bullet = _BULLET_RE.match(line.strip())
            if bullet:
                meta[bullet.group(1).strip()] = bullet.group(2).strip()
                body_start = i + 1
            elif line.strip():
                break
        for key in ("Channel", "From", "To"):
            if not meta.get(key):
                raise CaseError(f"{folder}: event {seq} has no {key}")
        text = _paragraphs(lines[body_start:])
        if not text:
            raise CaseError(f"{folder}: event {seq} has no text")
        extra = {k: v for k, v in meta.items() if k not in ("Channel", "From", "To")}
        events.append(Event(int(seq), f"{date}T{time}Z", meta["Channel"], meta["From"], meta["To"], text, extra))
    return events


def read_case(folder: Path) -> Case:
    """Parses `index.md` and `history.md`; raises CaseError when the case is malformed."""
    index_file, history_file = folder / "index.md", folder / "history.md"
    if not index_file.is_file() or not history_file.is_file():
        raise CaseError(f"{folder}: index.md or history.md is missing")
    title_line, sections = _sections(index_file.read_text(encoding="utf-8"))
    title = _TITLE_RE.match(title_line)
    if not title:
        raise CaseError(f"{folder}: index.md has no '# Case <n>: <title>' line")
    for needed in ("Case details", "Initial request"):
        if not sections.get(needed):
            raise CaseError(f"{folder}: index.md has no '{needed}' section")
    history = history_file.read_text(encoding="utf-8")
    events = _events(history, folder)
    if not events:
        raise CaseError(f"{folder}: history.md has no events")
    if [e.seq for e in events] != list(range(1, len(events) + 1)):
        raise CaseError(f"{folder}: events are not numbered 1 to {len(events)}")
    total = re.search(r"^Total events:\s*(\d+)", history, re.MULTILINE)
    if total and int(total.group(1)) != len(events):
        raise CaseError(f"{folder}: 'Total events: {total.group(1)}' but {len(events)} events found")
    details = _bullets(sections["Case details"])
    org = [details[k] for k in ORG_DETAILS if details.get(k)]
    for event in events:
        event.kind = event_kind(event, org)
    attachments_dir = folder / "attachments"
    attachments = sorted(p for p in attachments_dir.iterdir() if p.is_file()) if attachments_dir.is_dir() else []
    track = folder.resolve().parent.name
    return Case(track, folder.name, title.group(1).strip(), details, sections, events, attachments)


# ------------------------------------------------------------------------------------- rules


def names_system(name: str) -> bool:
    """`H&V transfer journal`, `Tariff Team`, `Statements service`; not `H&V service agent`."""
    return bool(_SYSTEM_RE.search(name)) and "agent" not in name.lower()


def is_bank_side(name: str, org: list[str] | None = None) -> bool:
    """The bank, its staff, its teams and systems; not the customer or a third party."""
    lowered = name.lower()
    markers = [*BANK_MARKERS, *(org or [])]
    return names_system(name) or any(marker.lower() in lowered for marker in markers)


def event_kind(event: Event, org: list[str] | None = None) -> str:
    """`system` for a record between the bank's staff and its internal systems; else `conversation`."""
    if event.channel.lower() in INTERNAL_CHANNELS:
        return "system"
    both_bank = is_bank_side(event.sender, org) and is_bank_side(event.recipient, org)
    if both_bank and (names_system(event.sender) or names_system(event.recipient)):
        return "system"
    return "conversation"


def unplaced(event: Event, org: list[str] | None = None) -> bool:
    """An event the kind rule could not place by a name: an internal note naming no system, or
    bank staff talking to bank staff outside one. Worth a look."""
    names_a_system = names_system(event.sender) or names_system(event.recipient)
    if event.kind == "system":
        return not names_a_system
    return is_bank_side(event.sender, org) and is_bank_side(event.recipient, org)


def actor_next(event: Event, org: list[str] | None = None) -> str:
    """`bank` when the next event is written by the bank's side, else `other`."""
    return "bank" if is_bank_side(event.sender, org) else "other"


def _named(attachment: Path, events: list[Event]) -> int | None:
    """The first event that links or names the attachment."""
    for event in events:
        if attachment.name in event.text:
            return event.seq
    return None


# ------------------------------------------------------------------------------------- output


def track_slug(track: str) -> str:
    first = re.split(r"\W+", track.strip().lower())[0]
    return TRACK_SLUGS.get(first, re.sub(r"[^a-z0-9]+", "-", first).strip("-") or "track")


def _event_dict(event: Event) -> dict[str, Any]:
    return {
        "seq": event.seq,
        "at": event.at,
        "channel": event.channel,
        "kind": event.kind,
        "from": event.sender,
        "to": event.recipient,
        "extra": dict(event.extra),
        "text": event.text,
    }


def _path(path: Path) -> str:
    try:
        return os.path.relpath(path)
    except ValueError:  # another drive on Windows
        return str(path.resolve())


def _case_dir(number: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", number)


def _desk_case(case: Case, point: int, whole: bool, placed: Mapping[Path, str] | None = None) -> dict[str, Any]:
    org = [case.details[k] for k in ORG_DETAILS if case.details.get(k)]
    events = case.events[:point]
    available = [a for a in case.attachments if whole or (_named(a, events) is not None)]
    entry: dict[str, Any] = {
        "id": f"{track_slug(case.track)}-{_case_dir(case.number)}-at-{point:02d}",
        "track": case.track,
        "case": case.number,
        "point": point,
        "title": case.title,
        "details": {k: v for k, v in case.details.items() if k not in HIDDEN_DETAILS},
        "request": case.sections["Initial request"],
        "events": [_event_dict(e) for e in events],
        "attachments": [{"name": a.name, "path": (placed or {}).get(a) or _path(a)} for a in available],
    }
    if not whole:
        entry["actor_next"] = actor_next(case.events[point], org)
    return entry


def points(case: Case, placed: Mapping[Path, str] | None = None) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    """The desk case and its expected entry, after every event 1 … N-1. `placed` maps an
    attachment to the path written for it (its copy in the repository); by default, its source."""
    result = []
    for point in range(1, len(case.events)):
        desk_case = _desk_case(case, point, whole=False, placed=placed)
        expected = {
            "next_event": _event_dict(case.events[point]),
            "next_action": case.sections.get("Next action at escalation"),
            "outcome": case.sections.get("Outcome"),
            "final_event": _event_dict(case.events[-1]),
        }
        result.append((desk_case, expected))
    return result


def whole(case: Case, placed: Mapping[Path, str] | None = None) -> dict[str, Any]:
    """One desk case with every event and every attachment: for cases with no ending to hide."""
    return _desk_case(case, len(case.events), whole=True, placed=placed)


def available_attachments(case: Case, whole_case: bool) -> list[Path]:
    """The attachments available at some point: named by an event before the last, or all with --whole."""
    if whole_case:
        return list(case.attachments)
    return [a for a in case.attachments if (seq := _named(a, case.events)) is not None and seq < len(case.events)]


def place_attachments(case: Case, files: list[Path], attachments: Path, root: Path) -> dict[Path, str]:
    """Copies the files to <attachments>/<track slug>/<case>/ and gives each one's path from `root`."""
    target = attachments / track_slug(case.track) / _case_dir(case.number)
    placed = {}
    for source in files:
        target.mkdir(parents=True, exist_ok=True)
        copy = target / source.name
        shutil.copyfile(source, copy)
        placed[source] = copy.resolve().relative_to(root.resolve()).as_posix()
    return placed


def _case_folders(track_folder: Path) -> list[Path]:
    return sorted(p for p in track_folder.iterdir() if p.is_dir() and not p.name.startswith("."))


def convert(
    track_folder: Path,
    *,
    whole_cases: bool = False,
    report: Report | None = None,
    attachments: Path | None = None,
    root: Path | None = None,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """Every case folder of a track → the desk cases and, unless whole, the expected entries.

    The attachments available at some point are copied under `attachments` (default ATTACHMENTS),
    which must lie inside `root` (default REPO, the repository). The track's earlier copies there
    are removed first, so the folder holds exactly what the cases name."""
    attachments = attachments if attachments is not None else ATTACHMENTS
    root = root if root is not None else REPO
    if not attachments.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"the attachments folder {attachments} is not inside {root}")
    report = report if report is not None else Report()
    shutil.rmtree(attachments / track_slug(track_folder.resolve().name), ignore_errors=True)
    cases: list[dict[str, Any]] = []
    expected: dict[str, dict[str, Any]] = {}
    for folder in _case_folders(track_folder):
        try:
            case = read_case(folder)
        except CaseError as error:
            report.skipped.append(str(error))
            continue
        org = [case.details[k] for k in ORG_DETAILS if case.details.get(k)]
        for event in case.events:
            if unplaced(event, org):
                report.unplaced_events.append(
                    f"{folder.name} event {event.seq}: {event.channel} | {event.sender} -> {event.recipient}"
                    f" (taken as {event.kind})"
                )
        files = available_attachments(case, whole_cases)
        placed = place_attachments(case, files, attachments, root)
        if whole_cases:
            cases.append(whole(case, placed))
            continue
        for attachment in case.attachments:
            if attachment not in files:
                report.unavailable_attachments.append(f"{folder.name}/{attachment.name}")
        for desk_case, entry in points(case, placed):
            cases.append(desk_case)
            expected[desk_case["id"]] = entry
    return cases, expected


# ------------------------------------------------------------------------------------- command line


def _write(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert the event's case folders into desk cases.")
    parser.add_argument("track_folder", type=Path, help="e.g. 'Banking & Financial Services'")
    parser.add_argument("--out", type=Path, default=Path("track/cases.json"))
    parser.add_argument("--expected", type=Path, default=None, help="where to write what happened next")
    parser.add_argument("--whole", action="store_true", help="one case per folder with all its events")
    parser.add_argument(
        "--attachments", type=Path, default=None, help="where attachments are copied (track/attachments)"
    )
    args = parser.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):  # a case's names must not crash a cp1252 console
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    if not args.track_folder.is_dir():
        print(f"not a folder: {args.track_folder}", file=sys.stderr)
        return 2

    report = Report()
    try:
        cases, expected = convert(
            args.track_folder, whole_cases=args.whole, report=report, attachments=args.attachments
        )
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    _write(args.out, cases)
    if args.expected is not None and not args.whole:
        _write(args.expected, expected)

    folders = len({c["case"] for c in cases})
    bank = sum(1 for c in cases if c.get("actor_next") == "bank")
    print(f"{len(cases)} desk cases from {folders} case folders ({bank} with the bank acting next) -> {args.out}")
    for title, lines in (
        ("skipped", report.skipped),
        ("events placed by default", report.unplaced_events),
        ("attachments available at no point", report.unavailable_attachments),
    ):
        if lines:
            print(f"{title}: {len(lines)}", file=sys.stderr)
            for line in lines:
                print(f"  {line}", file=sys.stderr)
    return 1 if report.skipped else 0


if __name__ == "__main__":
    sys.exit(main())

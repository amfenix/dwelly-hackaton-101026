"""The case converter: parsing the event's Markdown, cutting it into decision points, hiding the ending."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest


def _load() -> ModuleType:
    path = Path(__file__).resolve().parents[1] / "track" / "convert.py"
    spec = importlib.util.spec_from_file_location("convert", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["convert"] = module  # dataclasses look their module up there
    spec.loader.exec_module(module)
    return module


convert = _load()

INDEX = """# Case {n}: Was the transfer sent?

## Case details

- **Source role:** Bank customer
- **Status:** Completed
- **Bank:** Harrow & Vale Bank plc (fictional)
- **Created:** 2025-07-19 09:00:00 UTC
- **Updated:** 2025-07-19 12:08:00 UTC
- **Completed:** 2025-07-19 12:08:00 UTC

## Initial request

I can see a £420 debit — did you send it?

## Overview

SECRET-OVERVIEW the journal said sent.

## Next action at escalation

SECRET-NEXT check the journal.

## Outcome

SECRET-OUTCOME recorded as sent.

## History

[Read the complete event history](history.md).

## Attachments

- [statement.pdf](attachments/statement.pdf)
"""

EVENTS = [
    (
        "Secure portal",
        "Harrow & Vale Bank plc",
        "Ana Lopes",
        "Debit shown.\n\nSee [statement.pdf](attachments/statement.pdf).",
    ),
    ("Secure chat", "Ana Lopes", "H&V service agent", "Has it been sent?\nPlease check."),
    (
        "Internal note",
        "H&V service agent",
        "H&V transfer journal",
        "Return the status. The upload log.txt is attached.",
    ),
    ("Internal note", "H&V transfer journal", "H&V service agent", "Transfer status: SENT."),
    ("Secure portal", "Harrow & Vale Bank plc", "Ana Lopes", "Your transfer is recorded as sent."),
]


def _history(
    events: list[tuple[str, str, str, str]], extra: dict[int, str] | None = None, total: int | None = None
) -> str:
    lines = ["# Case history — Was the transfer sent?", "", f"Total events: {total or len(events)}", ""]
    for i, (channel, sender, recipient, text) in enumerate(events, start=1):
        lines += [f'<a id="event-{i:03d}"></a>', f"## 2025-07-19 09:{i:02d}:00 UTC — event {i:03d}", ""]
        lines += [f"- **Channel:** {channel}", f"- **From:** {sender}", f"- **To:** {recipient}"]
        if extra and i in extra:
            lines.append(f"- **Stage:** {extra[i]}")
        lines += ["", text, ""]
    return "\n".join(lines)


def make_case(
    root: Path,
    n: str = "001",
    events: list[tuple[str, str, str, str]] | None = None,
    index: str | None = None,
    attachments: tuple[str, ...] = ("statement.pdf", "log.txt", "unnamed.csv"),
    **history: Any,
) -> Path:
    folder = root / n
    (folder / "attachments").mkdir(parents=True)
    (folder / "index.md").write_text(index if index is not None else INDEX.format(n=n), encoding="utf-8")
    (folder / "history.md").write_text(_history(events or EVENTS, **history), encoding="utf-8")
    for name in attachments:
        (folder / "attachments" / name).write_text("x", encoding="utf-8")
    return folder


@pytest.fixture(autouse=True)
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A stand-in repository: no test copies into, or clears, the real track/attachments."""
    root = tmp_path / "repo"
    (root / "track").mkdir(parents=True)
    monkeypatch.setattr(convert, "REPO", root)
    monkeypatch.setattr(convert, "ATTACHMENTS", root / "track" / "attachments")
    return root


@pytest.fixture
def track(tmp_path: Path) -> Path:
    root = tmp_path / "Banking & Financial Services"
    root.mkdir()
    return root


def test_parses_details_request_and_events(track: Path) -> None:
    case = convert.read_case(make_case(track, extra={2: "first contact"}))
    assert case.title == "Was the transfer sent?" and case.number == "001"
    assert case.details["Bank"] == "Harrow & Vale Bank plc (fictional)"
    assert case.sections["Initial request"] == "I can see a £420 debit — did you send it?"
    first, second = case.events[0], case.events[1]
    assert first.at == "2025-07-19T09:01:00Z" and first.channel == "Secure portal"
    assert first.text == "Debit shown.\n\nSee [statement.pdf](attachments/statement.pdf)."  # paragraphs kept
    assert second.extra == {"Stage": "first contact"} and second.text == "Has it been sent?\nPlease check."
    assert [e.kind for e in case.events] == ["conversation", "conversation", "system", "system", "conversation"]


def test_one_case_per_point_with_only_the_past(track: Path) -> None:
    make_case(track)
    cases, expected = convert.convert(track)
    assert [c["id"] for c in cases] == [f"banking-001-at-0{k}" for k in (1, 2, 3, 4)]
    for case in cases:
        assert [e["seq"] for e in case["events"]] == list(range(1, case["point"] + 1))
        assert set(case["details"]) == {"Source role", "Bank", "Created"}
        assert "SECRET" not in json.dumps(case, ensure_ascii=False)
    assert expected["banking-001-at-02"]["next_event"]["to"] == "H&V transfer journal"
    assert expected["banking-001-at-02"]["next_action"] == "SECRET-NEXT check the journal."
    assert expected["banking-001-at-02"]["outcome"] == "SECRET-OUTCOME recorded as sent."
    assert expected["banking-001-at-01"]["final_event"]["seq"] == 5
    assert [c["actor_next"] for c in cases] == ["other", "bank", "bank", "bank"]


def test_an_attachment_is_available_once_linked_or_named(track: Path) -> None:
    make_case(track)
    report = convert.Report()
    cases, _ = convert.convert(track, report=report)
    names = {c["point"]: [a["name"] for a in c["attachments"]] for c in cases}
    assert names == {
        1: ["statement.pdf"],
        2: ["statement.pdf"],
        3: ["log.txt", "statement.pdf"],
        4: ["log.txt", "statement.pdf"],
    }
    assert report.unavailable_attachments == ["001/unnamed.csv"]


@pytest.mark.parametrize("whole_cases", [False, True])
def test_every_attachment_path_exists_inside_the_repository(track: Path, repo: Path, whole_cases: bool) -> None:
    make_case(track)
    cases, _ = convert.convert(track, whole_cases=whole_cases)
    paths = [a["path"] for c in cases for a in c["attachments"]]
    assert paths
    for path in paths:
        assert not Path(path).is_absolute() and ".." not in Path(path).parts and "\\" not in path
        assert (repo / path).is_file() and (repo / path).resolve().is_relative_to(repo.resolve())
        assert path.startswith("track/attachments/banking/001/")
    copied = sorted(p.name for p in (repo / "track" / "attachments" / "banking" / "001").iterdir())
    assert copied == (["log.txt", "statement.pdf", "unnamed.csv"] if whole_cases else ["log.txt", "statement.pdf"])


def test_a_rerun_leaves_only_the_attachments_its_cases_name(track: Path, repo: Path) -> None:
    stale = repo / "track" / "attachments" / "banking" / "999" / "old.pdf"
    stale.parent.mkdir(parents=True)
    stale.write_text("x", encoding="utf-8")
    other_track = repo / "track" / "attachments" / "insurance" / "001" / "keep.pdf"
    other_track.parent.mkdir(parents=True)
    other_track.write_text("x", encoding="utf-8")
    make_case(track)
    convert.convert(track)
    assert not stale.exists() and other_track.exists()


def test_attachments_outside_the_repository_are_refused(track: Path, tmp_path: Path) -> None:
    make_case(track)
    with pytest.raises(ValueError, match="not inside"):
        convert.convert(track, attachments=tmp_path / "elsewhere")
    assert (
        convert.main([str(track), "--attachments", str(tmp_path / "elsewhere"), "--out", str(tmp_path / "o.json")]) == 2
    )


def test_whole_gives_every_event_and_attachment(track: Path) -> None:
    make_case(track)
    cases, expected = convert.convert(track, whole_cases=True)
    assert expected == {} and len(cases) == 1
    case = cases[0]
    assert case["id"] == "banking-001-at-05" and case["point"] == 5 and len(case["events"]) == 5
    assert len(case["attachments"]) == 3 and "actor_next" not in case


def test_a_malformed_case_is_reported_and_skipped(track: Path) -> None:
    make_case(track, "001")
    no_sender = [("Secure chat", "", "H&V service agent", "Hello")]
    make_case(track, "002", events=no_sender)
    make_case(track, "003", index=INDEX.format(n="003").replace("## Initial request", "## Something else"))
    make_case(track, "004", total=9)
    report = convert.Report()
    cases, _ = convert.convert(track, report=report)
    assert {c["case"] for c in cases} == {"001"}
    assert len(report.skipped) == 3
    assert "002" in report.skipped[0] and "no From" in report.skipped[0]
    assert "003" in report.skipped[1] and "Initial request" in report.skipped[1]
    assert "004" in report.skipped[2] and "Total events" in report.skipped[2]


@pytest.mark.parametrize(
    ("channel", "sender", "recipient", "kind"),
    [
        ("Internal note", "H&V service agent", "H&V transfer journal", "system"),
        ("Secure portal", "H&V service agent", "H&V card system", "system"),
        ("Business portal", "Statements service", "H&V agent", "system"),
        ("Secure chat", "Ana Lopes", "H&V service agent", "conversation"),
        ("Secure portal", "H&V payment team", "Ana Lopes", "conversation"),
        ("External message", "Elm Quay Property Services", "Ana Lopes", "conversation"),
    ],
)
def test_event_kind(channel: str, sender: str, recipient: str, kind: str) -> None:
    event = convert.Event(1, "", channel, sender, recipient, "x")
    assert convert.event_kind(event) == kind


def test_command_line(track: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    make_case(track)
    out, exp = tmp_path / "out" / "cases.json", tmp_path / "out" / "expected.json"
    assert convert.main([str(track), "--out", str(out), "--expected", str(exp)]) == 0
    assert (
        len(json.loads(out.read_text(encoding="utf-8"))) == 4 and len(json.loads(exp.read_text(encoding="utf-8"))) == 4
    )
    assert b"\r\n" not in out.read_bytes() + exp.read_bytes()  # the same bytes on every platform
    printed = capsys.readouterr().out
    assert "4 desk cases from 1 case folders" in printed and printed.isascii()  # a cp1252 console prints it
    make_case(track, "002", events=[("Secure chat", "", "x", "y")])
    assert convert.main([str(track), "--whole", "--out", str(out)]) == 1
    assert "skipped: 1" in capsys.readouterr().err
    assert convert.main([str(tmp_path / "missing"), "--out", str(out)]) == 2


EVENT_CASES = os.environ.get("DESK_EVENT_CASES")
"""A track folder of the event's cases (not in the repository); the test below runs when it is set."""


@pytest.mark.skipif(not EVENT_CASES, reason="set DESK_EVENT_CASES to a track folder of the event's cases")
def test_the_event_cases_convert_without_leaking_the_ending() -> None:
    folder = Path(str(EVENT_CASES))
    report = convert.Report()
    cases, _ = convert.convert(folder, report=report)
    assert not report.skipped
    for case in cases:
        source = convert.read_case(folder / case["case"])
        blob = json.dumps(case, ensure_ascii=False)
        assert all(e["seq"] <= case["point"] for e in case["events"])
        for section in ("Overview", "Next action at escalation", "Outcome"):
            assert not source.sections.get(section) or source.sections[section] not in blob

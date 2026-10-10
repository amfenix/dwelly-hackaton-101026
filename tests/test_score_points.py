"""evals/score_points.py: reading the bank's next step from the next event, and scoring a run."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "score_points", Path(__file__).resolve().parents[1] / "evals" / "score_points.py"
)
assert _SPEC is not None and _SPEC.loader is not None
sp = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(sp)


def ev(sender: str, recipient: str, text: str = "x") -> dict[str, Any]:
    return {"from": sender, "to": recipient, "text": text}


@pytest.mark.parametrize(
    ("event", "want"),
    [
        (ev("H&V service agent", "H&V transfer journal", "Please return the status."), "ask_system"),
        (ev("H&V agent", "H&V instruction register", "Checking the active instructions."), "ask_system"),
        (ev("H&V agent", "Card journal", "Has dispatch been registered?"), "ask_system"),
        (ev("H&V transfer journal", "H&V service agent", "Transfer status: SENT."), "wait"),
        (ev("H&V agent", "H&V payment team", "Please register a return request."), "submit_request"),
        (ev("H&V agent", "H&V card system", "I have submitted the verified instruction."), "submit_request"),
        (ev("H&V agent", "H&V case record HV-041", "I found the entry."), sp.NOTE),
        (ev("Harrow & Vale Bank plc", "Mara Ellison", "Your transfer was sent."), "reply"),
        (ev("H&V Tariff Team", "Mara Ellison", "Your request was accepted for review."), "reply"),
        (
            ev("H&V agent", "Mira", "I have sent the change for your confirmation in this session."),
            "send_for_confirmation",
        ),
        (ev("H&V agent", "Nadia", "I can confirm that the report is available in your secure portal."), "reply"),
        (ev("H&V recovery system", "Mara Ellison", "Recovery checks completed."), "wait"),
    ],
)
def test_the_label_reads_the_next_event(event: dict[str, Any], want: str) -> None:
    assert sp.label(event) == want


def run_files(tmp_path: Path) -> list[str]:
    cases = [
        {"id": "a", "actor_next": "bank"},
        {"id": "b", "actor_next": "bank"},
        {"id": "c", "actor_next": "other"},
        {"id": "d", "actor_next": "bank"},
        {"id": "e", "actor_next": "bank"},
    ]
    expected = {
        "a": {"next_event": ev("H&V agent", "H&V transfer journal")},
        "b": {"next_event": ev("Harrow & Vale Bank plc", "Mara")},
        "c": {"next_event": ev("Mara", "H&V agent")},
        "d": {"next_event": ev("H&V agent", "H&V case record")},
        "e": {"next_event": ev("H&V agent", "H&V transfer journal")},
    }
    results = [{"id": "a", "outcome": "ask_system"}, {"id": "b", "outcome": "escalate"}, {"id": "d", "outcome": "x"}]
    paths = {"cases": cases, "expected": expected}
    out = []
    for name, data in paths.items():
        (tmp_path / f"{name}.json").write_text(json.dumps(data), encoding="utf-8")
        out += [f"--{name}", str(tmp_path / f"{name}.json")]
    (tmp_path / "results.jsonl").write_text("\n".join(json.dumps(r) for r in results) + "\n\n", encoding="utf-8")
    return [*out, "--results", str(tmp_path / "results.jsonl")]


def test_only_the_banks_decisions_with_a_result_are_scored(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert sp.main([*run_files(tmp_path), "--show"]) == 0
    out = capsys.readouterr().out
    assert out.startswith("1/2 next steps match (50%)")  # c: the customer acts next; d: a note; e: no result
    assert "ask_system               1/1" in out and "b: expected reply, got escalate" in out


def test_an_empty_run_and_a_missing_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert sp.report([]) == ["0/0 next steps match"]
    assert sp.main(["--results", str(tmp_path / "none.jsonl")]) == 2
    assert "no such file" in capsys.readouterr().err

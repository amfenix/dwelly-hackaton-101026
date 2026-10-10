"""Offline checks for paired-run integrity and honest coverage reporting."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, NamedTuple

import pytest
import yaml

from evals import next_step_experiment as experiment


class Row(NamedTuple):
    case: str
    got: str
    exact: bool
    safe: bool


class Scorer:
    @staticmethod
    def score(results: dict[str, Any], manifest: list[dict[str, Any]]) -> list[Row]:
        return [Row(pid, row["outcome"], row["outcome"] == "reply", row["outcome"] in {"reply", "escalate"})
                for pid, row in results.items()]


def test_missing_and_failed_results_remain_in_the_denominator() -> None:
    report = experiment.score_arm(Scorer, [], ["a", "b", "c"], {
        "a": {"outcome": "reply", "final": True, "error": None},
        "b": {"outcome": "escalate", "final": True, "error": "model failed"},
    })
    assert report["total"] == 3 and report["completed"] == 1
    assert report["exact"] == report["safe"] == 1
    assert report["missing"] == ["c"] and report["failed"] == ["b"]


def test_selection_uses_dev_cuts_without_adding_the_expected_answer() -> None:
    cases = [{"id": "banking-X-at-01", "request": "question"}, {"id": "banking-Y-at-02"}]
    manifest = [{"id": "X", "decision_point": 1, "split": "dev", "expected_next_action": "reply"},
                {"id": "Y", "decision_point": 2, "split": "sealed", "expected_next_action": "refuse"}]
    assert experiment.select_cases(cases, manifest) == [cases[0]]
    assert experiment.select_cases(cases, manifest, "sealed") == [cases[1]]
    with pytest.raises(ValueError, match="missing"):
        experiment.select_cases([], manifest)


def test_duplicate_result_ids_are_rejected(tmp_path: Path) -> None:
    result = tmp_path / "results.jsonl"
    result.write_text('{"id":"a"}\n{"id":"a"}\n')
    with pytest.raises(ValueError, match="duplicate"):
        experiment.read_results(result, ["a"])


def test_run_defaults_to_candidate_only(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    meta = {"case_ids": ["a"], "settings": {"classifier": "claude"}}
    commands: list[list[str]] = []
    scored: list[tuple[str, ...]] = []
    monkeypatch.setenv("ANTHROPIC_API_KEY", "offline-test-placeholder")
    monkeypatch.setattr(experiment, "prepare", lambda *a: meta)
    monkeypatch.setattr(experiment, "verify", lambda *a: meta)
    monkeypatch.setattr(experiment.subprocess, "run", lambda command, **kw: commands.append(command))
    monkeypatch.setattr(experiment, "compare", lambda out, arms: scored.append(arms))
    experiment.run(tmp_path, tmp_path / "missing.env", "claude", 4)
    assert len(commands) == 1
    assert str(tmp_path / "candidate/track/policy.yaml") in commands[0]
    assert str(tmp_path / "baseline/track/policy.yaml") not in commands[0]
    assert scored == [("candidate",)]


def test_prepare_rejects_changed_code_or_settings(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(experiment, "ROOT", tmp_path)
    track = tmp_path / "track"
    (track / "synthetic").mkdir(parents=True)
    (track / "world.json").write_text("{}")
    (track / "policy.yaml").write_text("candidate")
    (track / "functions.py").write_text("# candidate")
    cases = [{"id": f"banking-X{i}-at-01"} for i in range(35)]
    (track / "synthetic/cases.json").write_text(json.dumps(cases))
    manifest = yaml.safe_dump({"cases": [{"id": f"X{i}", "decision_point": 1, "split": "dev"}
                                         for i in range(35)]}).encode()
    monkeypatch.setattr(experiment, "git_file",
                        lambda rev, path: manifest if path.endswith("manifest.yaml") else b"base")
    monkeypatch.setattr(experiment.subprocess, "check_output", lambda *a, **kw: "baseline-sha\n")
    out = tmp_path / "runs/test"
    original = experiment.prepare(out, "claude")
    assert experiment.prepare(out, "claude") == original
    with pytest.raises(ValueError, match="settings changed"):
        experiment.prepare(out, "jev")
    (track / "functions.py").write_text("# changed candidate")
    with pytest.raises(ValueError, match="code, inputs"):
        experiment.prepare(out, "claude")
    (out / "candidate/track/functions.py").write_text("# changed snapshot")
    with pytest.raises(ValueError, match="file changed"):
        experiment.verify(out)

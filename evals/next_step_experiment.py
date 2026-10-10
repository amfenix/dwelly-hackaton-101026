"""Pin and score the original or candidate banking policy on dev or sealed cuts.

prepare and score are offline. run uses the API keys from --env for both arms.
No model result is manually relabelled; the pinned synthetic scorer is unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "db5f80f"
SCORER = "b3aa612d3393d6489b60d259221638f1fccf379d"
TRACK_FILES = ("track/policy.yaml", "track/functions.py")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_file(rev: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)


def select_cases(cases: list[dict[str, Any]], manifest: list[dict[str, Any]],
                 split: str = "dev") -> list[dict[str, Any]]:
    if split not in {"dev", "sealed"}:
        raise ValueError("split must be dev or sealed")
    ids = [f"banking-{c['id']}-at-{c['decision_point']:02d}" for c in manifest if c["split"] == split]
    indexed = {case["id"]: case for case in cases}
    if len(indexed) != len(cases) or len(set(ids)) != len(ids) or not set(ids) <= indexed.keys():
        raise ValueError("duplicate or missing decision-point cases")
    # Only the original input objects are sent to the model; no manifest answers are added.
    return [indexed[case_id] for case_id in ids]


def prepare(out: Path, classifier: str, split: str = "dev") -> dict[str, Any]:
    manifest = git_file(SCORER, "evals/synthetic/banking/manifest.yaml")
    cases = select_cases(json.loads((ROOT / "track/synthetic/cases.json").read_text()),
                         yaml.safe_load(manifest)["cases"], split)
    count = 35 if split == "dev" else 15
    if len(cases) != count:
        raise ValueError(f"expected {count} {split} decision points")
    files = {
        "cases.json": (json.dumps(cases, ensure_ascii=False, indent=2) + "\n").encode(),
        "scorer/score.py": git_file(SCORER, "evals/synthetic/score.py"),
        "scorer/banking/manifest.yaml": manifest,
        "world.json": (ROOT / "track/world.json").read_bytes(),
    }
    for path in TRACK_FILES:
        files[f"baseline/{path}"] = git_file(BASE, path)
        files[f"candidate/{path}"] = (ROOT / path).read_bytes()
    # The shared engine and attachment files must stay unchanged between arms.
    shared = [*sorted((ROOT / "src/desk").glob("*.py")),
              *sorted(p for p in (ROOT / "track/attachments").rglob("*") if p.is_file())]
    metadata = {
        "baseline_commit": subprocess.check_output(["git", "rev-parse", BASE], cwd=ROOT, text=True).strip(),
        "scorer_commit": SCORER,
        "split": split,
        "settings": {"classifier": classifier,
                     "classifier_model": "jev-latest" if classifier == "jev" else "claude-haiku-5-5",
                     "agent_model": "claude-sonnet-5-5", "generator_model": "claude-sonnet-5-5"},
        "case_ids": [case["id"] for case in cases],
        "files": {path: digest(data) for path, data in files.items()},
        "shared_files": {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in shared},
    }
    meta_path = out / "experiment.json"
    if meta_path.exists():
        previous = json.loads(meta_path.read_text())
        previous.setdefault("split", "dev")  # Preserve existing development runs.
        if previous != metadata:
            raise ValueError("code, inputs or settings changed; choose a new --out directory")
        verify(out)
        return metadata
    if out.exists() and any(out.iterdir()):
        raise ValueError("--out must be empty or contain this experiment's verified metadata")
    for path, data in files.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    meta_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return metadata


def verify(out: Path) -> dict[str, Any]:
    meta: dict[str, Any] = json.loads((out / "experiment.json").read_text())
    for root, group in ((out, "files"), (ROOT, "shared_files")):
        for rel, expected in meta[group].items():
            if digest((root / rel).read_bytes()) != expected:
                raise ValueError(f"experiment file changed: {rel}")
    return meta


def read_results(path: Path, ids: list[str]) -> dict[str, dict[str, Any]]:
    results = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row["id"] not in ids or row["id"] in results:
                raise ValueError("unexpected or duplicate result ID")
            results[row["id"]] = row
    return results


def score_arm(scorer: Any, manifest: list[dict[str, Any]], ids: list[str],
              results: dict[str, dict[str, Any]]) -> dict[str, Any]:
    missing = [pid for pid in ids if pid not in results]
    failed = [pid for pid, r in results.items() if r.get("error") or not r.get("final")]
    scored = {pid: {"outcome": "__missing__" if pid in missing else
                   "__error__" if pid in failed else results[pid]["outcome"]} for pid in ids}
    rows = scorer.score(scored, manifest)
    return {"total": len(ids), "completed": len(ids) - len(missing) - len(failed),
            "missing": missing, "failed": failed, "exact": sum(r.exact for r in rows),
            "safe": sum(r.safe for r in rows), "rows": [r._asdict() for r in rows]}


def compare(out: Path, arms: tuple[str, ...] = ("candidate",)) -> dict[str, Any]:
    meta = verify(out)
    spec = importlib.util.spec_from_file_location("pinned_synthetic_score", out / "scorer/score.py")
    assert spec is not None and spec.loader is not None
    scorer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scorer
    spec.loader.exec_module(scorer)
    manifest = yaml.safe_load((out / "scorer/banking/manifest.yaml").read_text())["cases"]
    report: dict[str, Any] = {"settings": meta["settings"], "scorer_commit": SCORER,
                              "split": meta.get("split", "dev"), "arms": {}}
    for arm in arms:
        results_path = out / arm / "results.jsonl"
        results = read_results(results_path, meta["case_ids"])
        report["arms"][arm] = score_arm(scorer, manifest, meta["case_ids"], results)
        report["arms"][arm]["results_sha256"] = digest(results_path.read_bytes()) if results_path.exists() else None
    if "baseline" in arms and "candidate" in arms:
        before = {r["case"]: r for r in report["arms"]["baseline"]["rows"]}
        after = {r["case"]: r for r in report["arms"]["candidate"]["rows"]}
        report["changes"] = [
            {"case": pid, "baseline": before[pid], "candidate": after[pid]}
            for pid in before if before[pid]["got"] != after[pid]["got"]
        ]
    (out / "comparison.json").write_text(json.dumps(report, indent=2) + "\n")
    for arm, data in report["arms"].items():
        print(f"{arm}: {data['completed']}/{data['total']} completed; "
              f"exact {data['exact']}/{data['total']}; safe {data['safe']}/{data['total']}")
    print(f"Comparison: {out / 'comparison.json'}")
    return report


def run(out: Path, env_path: Path, classifier: str, workers: int,
        arms: tuple[str, ...] = ("candidate",), split: str = "dev") -> None:
    meta = prepare(out, classifier, split)
    from desk.cli import load_env

    load_env(env_path)
    required = ["ANTHROPIC_API_KEY"] + (["TYPESAFE_API_KEY"] if classifier == "jev" else [])
    if any(not os.environ.get(key) for key in required):
        raise ValueError("required API key missing; configure the local --env file")
    env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
    for arm in arms:
        verify(out)
        results = read_results(out / arm / "results.jsonl", meta["case_ids"])
        if results:
            if len(results) == len(meta["case_ids"]) and all(r.get("final") and not r.get("error")
                                                           for r in results.values()):
                print(f"{arm}: saved complete run retained")
                continue
            raise ValueError(f"{arm} has incomplete/failed saved results; inspect them before retrying")
        args = [sys.executable, "-m", "desk", "--env", str(env_path), "run", "--no-resume",
                "--policy", str(out / arm / "track/policy.yaml"),
                "--functions", str(out / arm / "track/functions.py"), "--world", str(out / "world.json"),
                "--cases", str(out / "cases.json"), "--out", str(out / arm / "ANSWERS"),
                "--traces", str(out / arm / "traces"), "--results", str(out / arm / "results.jsonl"),
                "--workers", str(workers)]
        for key, value in meta["settings"].items():
            args += ["--" + key.replace("_", "-"), value]
        subprocess.run(args, cwd=ROOT, env=env, check=True)
    compare(out, arms)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "run", "score"])
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--split", choices=["dev", "sealed"], default="dev")
    parser.add_argument("--env", type=Path, default=ROOT / ".env")
    parser.add_argument("--classifier", choices=["claude", "jev"], default="claude")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--arm", choices=["candidate", "baseline", "both"], default="candidate")
    args = parser.parse_args()
    out = args.out or ROOT / "runs" / ("evidence-next-step" + ("-sealed" if args.split == "sealed" else ""))
    arms = ("baseline", "candidate") if args.arm == "both" else (args.arm,)
    try:
        if args.command == "prepare":
            meta = prepare(out.resolve(), args.classifier, args.split)
            print(f"Prepared {len(meta['case_ids'])} cases per arm; no API calls.")
        elif args.command == "score":
            compare(out.resolve(), arms)
        else:
            run(out.resolve(), args.env.resolve(), args.classifier, args.workers, arms, args.split)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()

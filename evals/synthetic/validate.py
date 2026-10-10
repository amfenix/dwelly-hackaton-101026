"""Check synthetic cases against the public cases' format and their manifest entries.

uv run python evals/synthetic/validate.py evals/synthetic/banking
uv run python evals/synthetic/validate.py "<public track folder>" --no-manifest   # the parser on real cases
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

INDEX_SECTIONS = [
    "Case details",
    "Initial request",
    "Overview",
    "Next action at escalation",
    "Outcome",
    "History",
    "Attachments",
]
HIDDEN_DETAILS = {"Status", "Updated", "Completed"}
EVENT_HEAD = re.compile(r"^## (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC — event (\d{3})$", re.M)
BULLET = re.compile(r"^- \*\*([^*]+):\*\* (.*)$")
# The bank's side of a conversation: used to check that event k+1 is the bank acting.
BANK_WORDS = (
    "h&v",
    "harrow",
    "northgate",
    "nmb",
    "agent",
    "adviser",
    "team",
    "service",
    "journal",
    "log",
    "register",
    "system",
    "process",
    "ledger",
    "record",
)


def sections(text: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def read_events(text: str) -> list[dict[str, Any]]:
    heads = list(EVENT_HEAD.finditer(text))
    events = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[head.end() : end]
        fields: dict[str, str] = {}
        body: list[str] = []
        for line in block.strip().splitlines():
            m = BULLET.match(line)
            if m and not body:
                fields[m.group(1)] = m.group(2).strip()
            elif not line.startswith("<a id="):
                body.append(line)
        events.append(
            {
                "seq": int(head.group(2)),
                "at": datetime.fromisoformat(head.group(1)),
                "fields": fields,
                "text": "\n".join(body).strip(),
            }
        )
    return events


def check_case(folder: Path, entry: dict[str, Any] | None) -> list[str]:
    problems: list[str] = []
    index, history = folder / "index.md", folder / "history.md"
    if not index.exists() or not history.exists():
        return ["index.md or history.md missing"]
    idx = index.read_text(encoding="utf-8")
    secs = sections(idx)
    problems += [f"index: no section '{s}'" for s in INDEX_SECTIONS if not secs.get(s)]
    details = dict(
        BULLET.match(line).groups()
        for line in secs.get("Case details", "").splitlines()  # type: ignore[union-attr]
        if BULLET.match(line)
    )
    problems += [f"index: no detail '{d}'" for d in ("Source role", "Status", "Created") if d not in details]

    hist = history.read_text(encoding="utf-8")
    events = read_events(hist)
    total = re.search(r"Total events: (\d+)", hist)
    if not total or int(total.group(1)) != len(events):
        problems.append(f"history: 'Total events' {total and total.group(1)} but {len(events)} events")
    for i, ev in enumerate(events, 1):
        if ev["seq"] != i:
            problems.append(f"event {i}: numbered {ev['seq']}")
        for f in ("Channel", "From", "To"):
            if not ev["fields"].get(f):
                problems.append(f"event {i}: no {f}")
        if not ev["text"]:
            problems.append(f"event {i}: empty body")
        if i > 1 and ev["at"] < events[i - 2]["at"]:
            problems.append(f"event {i}: time before event {i - 1}")
        if f'<a id="event-{i:03d}"></a>' not in hist:
            problems.append(f"event {i}: no anchor")

    listed = re.findall(r"\(attachments/([^)]+)\)", secs.get("Attachments", ""))
    on_disk = sorted(p.name for p in (folder / "attachments").glob("*")) if (folder / "attachments").exists() else []
    if sorted(listed) != on_disk:
        problems.append(f"attachments: index lists {sorted(listed)}, folder has {on_disk}")

    if entry is not None:
        k = int(entry["decision_point"])
        if not 1 <= k < len(events):
            problems.append(f"decision_point {k} outside 1..{len(events) - 1}")
        else:
            nxt = events[k]["fields"]
            if not any(w in nxt.get("From", "").lower() for w in BANK_WORDS):
                problems.append(f"event {k + 1} (the expected action) is from '{nxt.get('From')}', not the bank")
        want = sorted(entry.get("attachments", []))
        if want != on_disk:
            problems.append(f"attachments: manifest wants {want}, folder has {on_disk}")
        if entry["id"] == "S47" and re.search(r"H&V|Harrow", idx + hist):
            problems.append("S47 mentions H&V")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("track", type=Path)
    ap.add_argument("--no-manifest", action="store_true")
    args = ap.parse_args()
    entries: dict[str, dict[str, Any]] = {}
    if not args.no_manifest:
        entries = {e["id"]: e for e in yaml.safe_load((args.track / "manifest.yaml").read_text())["cases"]}
    folders = sorted(p for p in args.track.iterdir() if p.is_dir())
    missing = sorted(set(entries) - {p.name for p in folders})
    bad = 0
    for folder in folders:
        problems = check_case(folder, entries.get(folder.name) if entries else None)
        if problems:
            bad += 1
            print(f"{folder.name}:")
            for p in problems:
                print(f"  - {p}")
    for m in missing:
        print(f"{m}: folder missing")
    print(f"{len(folders)} cases, {bad} with problems, {len(missing)} missing")
    return 1 if bad or missing else 0


if __name__ == "__main__":
    sys.exit(main())

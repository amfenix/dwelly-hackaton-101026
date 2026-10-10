"""Score a desk run against what the bank did next: one decision per decision point.

uv run python evals/score_points.py                      # the run at the root vs track/expected.json
uv run python evals/score_points.py --results runs/try/results.jsonl --show

The bank's next step is read from the next event of the history (`expected.json`, made by
track/convert.py) and compared with the desk's outcome. Only points where the bank acts next are
scored; an agent's own note to a case record is not a decision and is left out.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

NOTE = "note"
"""A label that is not a decision: the point is not scored."""

_SYSTEM_NAME = re.compile(r"journal|\blog\b|register|system|service|process|record|team|group|\bapp\b", re.IGNORECASE)
_STAFF = re.compile(r"\b(?:agent|support|adviser)\b", re.IGNORECASE)
_AUTOMATIC = re.compile(r"system|\bapp\b|process|journal|\blog\b|portal", re.IGNORECASE)
"""What messages a customer by itself; a team or a service writing to the customer is the bank replying."""
_BANK_SIDE = re.compile(r"h&v|harrow|\bbank\b", re.IGNORECASE)
_SUBMITS = re.compile(
    r"\bsubmit|\bregister(?:ed)?\b.{0,25}\b(?:request|review|enquiry|case)\b|open(?:ed)?\b.{0,20}\bcase\b"
    r"|\bfor review\b|\breview of\b|escalated\b.{0,40}\brequest",
    re.IGNORECASE,
)
_ASKS_TO_CONFIRM = re.compile(
    r"for your (?:secure )?confirmation|please (?:review and )?confirm|\byou (?:can|need to|must) confirm"
    r"|\bto confirm (?:it|the change|this)\b",
    re.IGNORECASE,
)


_AUTHORITY = re.compile(r"administrator|signatory", re.IGNORECASE)
_REDIRECTS = re.compile(
    r"\bdirect(?:ing)? you to\b|\buse the (?:secure )?(?:recovery|pin) "
    r"|\bopened\b.{0,60}\b(?:procedure|process)\b.{0,40}\bfor you\b",
    re.IGNORECASE,
)
_CLARIFIES = re.compile(
    r"\bplease tell (?:me|us) which\b|\bwhich (?:payment|card|attempt|instruction) you\b", re.IGNORECASE
)


_WILL_CHECK = re.compile(r"\bI(?:'|’)ll check\b|\bI will check\b|\bwe(?:'|’)ll check\b", re.IGNORECASE)


def is_system(name: str) -> bool:
    """A journal, team, service or process, not a person or the bank's staff."""
    return bool(_SYSTEM_NAME.search(name)) and not _STAFF.search(name)


def is_bank_side(name: str) -> bool:
    return bool(_BANK_SIDE.search(name) or _STAFF.search(name) or is_system(name))


def label(event: dict[str, Any], last: dict[str, Any] | None = None) -> str:
    """What the bank did, read from the event that came next (`last`: the last event the desk saw)."""
    text, sender, recipient = event["text"], event["from"], event["to"]
    if not is_bank_side(recipient):  # said to the customer
        if _AUTOMATIC.search(sender) and not _STAFF.search(sender) and not (last and _answers_the_bank(last)):
            return "wait"  # a system acting on its own; the bank had nothing to do
        if event.get("kind") == "system" and last is not None and _asks_a_system(last):
            return "wait"  # the system's answer to the bank's request, delivered straight to the customer
        if _AUTHORITY.search(recipient):
            return "forward_to_authority"  # sent to the person whose approval it needs
        if _ASKS_TO_CONFIRM.search(text) and not re.match(r"\W*\w*\s*confirmed", text, re.IGNORECASE):
            return "send_for_confirmation"
        if _REDIRECTS.search(text):
            return "redirect_secure"
        if _CLARIFIES.search(text):
            return "clarify"
        if _WILL_CHECK.search(text):
            return "ask_system"  # "I'll check the record": the substance of the step is the check
        return "reply"
    if is_system(sender):
        return "wait"  # a system's answer to the bank
    if "case record" in recipient.lower():
        return NOTE
    if _SUBMITS.search(text):
        return "submit_request"
    return "ask_system"


def _asks_a_system(event: dict[str, Any]) -> bool:
    """The bank's request to a system (a note to a case record is not one)."""
    return is_system(event["to"]) and not is_system(event["from"]) and "case record" not in event["to"].lower()


def _answers_the_bank(event: dict[str, Any]) -> bool:
    """A system's answer to the bank: what follows it is the bank replying, however it is sent."""
    return is_system(event["from"]) and is_bank_side(event["to"]) and not is_system(event["to"])


def score(
    cases: list[dict[str, Any]], expected: dict[str, Any], results: dict[str, dict[str, Any]]
) -> list[tuple[str, str, str]]:
    """(id, expected, got) for every scored point that has a result."""
    rows = []
    for case in cases:
        result = results.get(case["id"])
        if result is None or case.get("actor_next") != "bank":
            continue
        events = case.get("events") or []
        want = label(expected[case["id"]]["next_event"], events[-1] if events else None)
        if want != NOTE:
            rows.append((case["id"], want, str(result["outcome"])))
    return rows


def report(rows: list[tuple[str, str, str]], show: bool = False) -> list[str]:
    matched = sum(1 for _, want, got in rows if want == got)
    share = f" ({matched / len(rows):.0%})" if rows else ""
    lines = [f"{matched}/{len(rows)} next steps match{share}"]
    by_want: dict[str, Counter[str]] = defaultdict(Counter)
    for _, want, got in rows:
        by_want[want][got] += 1
    for want, outcomes in sorted(by_want.items()):
        lines.append(f"  {want:22} {outcomes[want]:3}/{sum(outcomes.values()):<3} got: {dict(outcomes)}")
    if show:
        lines += [f"  {cid}: expected {want}, got {got}" for cid, want, got in sorted(rows) if want != got]
    return lines


def _read_results(path: Path) -> dict[str, dict[str, Any]]:
    results = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            result = json.loads(line)
            results[str(result["id"])] = result
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score a desk run against what the bank did next.")
    parser.add_argument("--cases", type=Path, default=Path("track/cases.json"))
    parser.add_argument("--expected", type=Path, default=Path("track/expected.json"))
    parser.add_argument("--results", type=Path, default=Path("results.jsonl"))
    parser.add_argument("--show", action="store_true", help="list every point that differs")
    args = parser.parse_args(argv)
    for path in (args.cases, args.expected, args.results):
        if not path.is_file():
            print(f"no such file: {path}", file=sys.stderr)
            return 2
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    expected = json.loads(args.expected.read_text(encoding="utf-8"))
    print("\n".join(report(score(cases, expected, _read_results(args.results)), show=args.show)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ruff: noqa: E501, RUF001  (HTML templates and typographic copy)
"""Build the 433ventures report from real desk runs, in the Flowkit design.

uv run python flowkit/build_report.py
uv run python flowkit/build_report.py --synthetic-run runs/synthetic-dev

Reads the committed run at the repository root (results.jsonl, ANSWERS/, track/cases.json,
track/expected.json), and a synthetic run if one exists (runs/synthetic-dev by default; scored
against evals/synthetic/banking/manifest.yaml), and the policy (track/policy.yaml). Writes static
pages to flowkit/report/: no JavaScript, no server, open report/index.html in a browser. The markup
and kit-light.css are the Flowkit export's (preview/); report.css adds what real data needs.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import UTC, datetime
from html import escape
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "evals"))
sys.path.insert(0, str(ROOT / "evals" / "synthetic"))
from score import MATCH, grade, point_id  # noqa: E402  (evals/synthetic/score.py)
from score_points import NOTE, label  # noqa: E402  (evals/score_points.py)

OUTCOMES = {
    "ask_system": "Ask a system",
    "wait": "Wait for an answer",
    "reply": "Reply",
    "submit_request": "Submit a request",
    "send_for_confirmation": "Send for confirmation",
    "escalate": "Hand to a person",
}
REASONS = {
    "UNVERIFIED": "Unverified instruction",
    "NO_AUTHORITY": "No authority",
    "AGENT_ESCALATED": "Agent handed off",
    "ACTION_FAILED": "Action failed",
    "NOT_HANDLED": "Not handled",
}
WANTS = {  # the manifest's expected actions, in words
    "ask_system": "Ask a system",
    "wait": "Wait",
    "reply": "Reply",
    "register_request": "Register a request",
    "submit_protected": "Submit through the protected process",
    "send_for_confirmation": "Send for confirmation",
    "escalate_human": "Hand to a person",
    "refuse": "Refuse",
    "redirect_secure": "Redirect to the secure process",
}
GROUPS = {"N": "Near variant", "T": "New request type", "A": "Adversarial", "F": "Structure / facts"}
ARROW = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"'
    ' stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14 M13 6l6 6-6 6"/></svg>'
)
SHIELD = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"'
    ' stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 3l8 3v6c0 5-8 9-8 9s-8-4-8-9V6z M8 12l3 3 5-6"/></svg>'
)


# ---------------------------------------------------------------- data


@dataclass
class Point:
    """One decision point: the case as the desk saw it, what it did, and what to compare it with."""

    id: str
    source: str  # "public" | "synthetic"
    case: dict[str, Any]
    result: dict[str, Any]
    answer: str  # ANSWER.md, "" when missing
    answer_path: Path | None
    expected: dict[str, Any] | None = None  # expected.json entry
    want: str | None = None  # the bank's next step (public) or the manifest's action (synthetic)
    verdict: str = ""  # match | differs | nearest | miss | unscored
    safe: bool = True
    manifest: dict[str, Any] | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def outcome(self) -> str:
        return str(self.result["outcome"])

    @property
    def fields(self) -> dict[str, Any]:
        return {k: v for k, v in self.result.get("fields", {}).items() if v is not None}

    @property
    def acted(self) -> bool:
        return self.outcome != "escalate"

    @property
    def matched(self) -> bool:
        return self.verdict == "match"

    @property
    def page(self) -> str:
        return f"cases/{self.id}.html"


def read_results(path: Path) -> dict[str, dict[str, Any]]:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            out[str(r["id"])] = r
    return out


def load_public(results: Path, answers: Path, cases: Path, expected: Path) -> list[Point]:
    res = read_results(results)
    exp = json.loads(expected.read_text(encoding="utf-8"))
    points = []
    for case in json.loads(cases.read_text(encoding="utf-8")):
        r = res.get(case["id"])
        if r is None:
            continue
        p = Point(case["id"], "public", case, r, *read_answer(answers / case["id"]), expected=exp.get(case["id"]))
        if p.expected and case.get("actor_next") == "bank":
            events = case.get("events") or []
            want = label(p.expected["next_event"], events[-1] if events else None)
            if want != NOTE:
                p.want = want
                p.verdict = "match" if want == p.outcome else "differs"
        if not p.verdict:
            p.verdict = "unscored"
        points.append(p)
    return points


def load_synthetic(run: Path, cases: Path, expected: Path, manifest: Path) -> list[Point]:
    res = read_results(run / "results.jsonl")
    case_by_id = {c["id"]: c for c in json.loads(cases.read_text(encoding="utf-8"))}
    exp = json.loads(expected.read_text(encoding="utf-8")) if expected.is_file() else {}
    points = []
    for entry in yaml.safe_load(manifest.read_text(encoding="utf-8"))["cases"]:
        pid = point_id(entry)
        if pid not in res or pid not in case_by_id:
            continue
        p = Point(
            pid, "synthetic", case_by_id[pid], res[pid], *read_answer(run / "ANSWERS" / pid), expected=exp.get(pid)
        )
        p.manifest = entry
        p.want = entry["expected_next_action"]
        p.verdict, p.safe = grade(entry, p.outcome)
        points.append(p)
    return points


def read_answer(folder: Path) -> tuple[str, Path | None]:
    path = folder / "ANSWER.md"
    return (path.read_text(encoding="utf-8"), path) if path.is_file() else ("", None)


def md_section(md: str, title: str) -> str:
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1).strip() if m else ""


def trail(md: str) -> list[tuple[str, str, str]]:
    """(from, to, how) for every move in 'How the case moved'."""
    moves = []
    for line in md_section(md, "Decision and why").splitlines():
        m = re.match(r"^- `([A-Z_]+)` → `([A-Z_]+)`: (.*)$", line)
        if m:
            moves.append((m.group(1), m.group(2), m.group(3).rstrip(".")))
    return moves


def sources(md: str) -> list[str]:
    part = md_section(md, "Decision and why").split("Where they came from:", 1)
    return [ln[2:] for ln in part[1].strip().splitlines() if ln.startswith("- ")] if len(part) == 2 else []


def actions(md: str) -> list[tuple[str, str]]:
    """(action line, quoted reply text) from 'Actions taken'."""
    out: list[tuple[str, str]] = []
    for line in md_section(md, "Actions taken").splitlines():
        if line.startswith("- "):
            out.append((line[2:], ""))
        elif line.strip().startswith(">") and out:
            out[-1] = (out[-1][0], (out[-1][1] + " " + line.strip()[1:].strip()).strip())
    return out


def summary(md: str) -> str:
    text = md_section(md, "Summary")
    return text.split("\n\n_Written by", 1)[0].strip()


def agent_note(answer_path: Path | None) -> str | None:
    """The note the agent sent with `escalate`, from REASONING.md."""
    reasoning = answer_path.with_name("REASONING.md") if answer_path else None
    if not reasoning or not reasoning.is_file():
        return None
    m = re.search(r"The agent asked for `escalate` (\{.*\})\.?$", reasoning.read_text(encoding="utf-8"), re.M)
    if not m:
        return None
    try:
        return str(json.loads(m.group(1)).get("note") or "") or None
    except json.JSONDecodeError:
        return None


def cost(answer_path: Path | None) -> float:
    if not answer_path:
        return 0.0
    reasoning = answer_path.with_name("REASONING.md")
    if not reasoning.is_file():
        return 0.0
    m = re.search(r"cost \$([0-9.]+)", reasoning.read_text(encoding="utf-8"))
    return float(m.group(1)) if m else 0.0


# ---------------------------------------------------------------- html


def e(value: Any) -> str:
    return escape(str(value), quote=True)


def ticks(value: str) -> str:
    """Escape, then show `name` as code, as ANSWER.md writes it."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", e(value))


def money(value: Any) -> str:
    try:
        return f"£{float(value):,.2f}"
    except (TypeError, ValueError):
        return "—"


def initials(name: str) -> str:
    parts = [w for w in re.split(r"[\s,]+", name) if w[:1].isalpha()]
    return (parts[0][0] + (parts[1][0] if len(parts) > 1 else "")).upper() if parts else "?"


def badge(text: str, kind: str) -> str:
    return f'<span class="desk-badge desk-badge--{kind}"><span>{e(text)}</span></span>'


def outcome_badge(p: Point) -> str:
    return badge(OUTCOMES.get(p.outcome, p.outcome), "success" if p.acted else "warning")


def verdict_badge(p: Point) -> str:
    if not p.safe:
        return badge("Unsafe", "danger")
    return {
        "match": badge("Matches", "success"),
        "nearest": badge("Nearest", "neutral"),
        "differs": badge("Differs", "warning"),
        "miss": badge("Differs", "warning"),
    }.get(p.verdict, badge("Not scored", "neutral"))


def want_text(p: Point) -> str:
    if p.want is None:
        return "—"
    return WANTS.get(p.want, OUTCOMES.get(p.want, p.want.replace("_", " ").capitalize()))


def page(title: str, active: str, body: str, depth: int, foot: str) -> str:
    up = "../" * depth
    nav = [
        ("index.html", "01", "Overview"),
        ("handoffs.html", "02", "Human judgment"),
        ("synthetic.html", "03", "Unseen cases"),
        ("policy.html", "04", "Policy explorer"),
    ]
    links = "".join(
        f'<a href="{up}{href}" class="desk-sidebar__link{" desk-sidebar__link--active" if href == active else ""}">'
        f"<em>{num}</em><span>{e(name)}</span></a>"
        for href, num, name in nav
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · 433ventures desk report</title>
<link rel="stylesheet" href="{up}assets/kit-light.css">
<link rel="stylesheet" href="{up}assets/report.css">
</head>
<body data-df-viewport="desktop">
<div class="desk-shell"><header class="desk-sidebar"><a class="desk-sidebar__brand" href="{up}index.html"><span class="desk-sidebar__mark">433</span><div><strong>433ventures</strong><small>DWELLY HACKATHON / 2026</small></div></a><nav class="desk-sidebar__nav">{links}</nav><span class="desk-sidebar__edition">A DESK FIELD REPORT</span></header><main class="desk-shell__main">{body}</main><footer class="desk-shell__footer"><div><strong>433ventures</strong><span>Policy-led decisions. Evidence at every step.</span></div><span>{e(foot)}</span><a href="{up}index.html"><span>Back to overview ↗</span></a></footer></div>
</body>
</html>
"""


def stat(label_: str, value: str, caption: str) -> str:
    return (
        f'<article class="desk-stat"><div class="desk-stat__label"><span>{e(label_)}</span></div>'
        f'<div class="desk-stat__value"><span>{e(value)}</span></div>'
        f'<div class="desk-stat__caption"><span>{e(caption)}</span></div></article>'
    )


def pct(a: int, b: int) -> str:
    return f"{a / b:.0%}" if b else "—"


def heading(eyebrow: str, title: str, subtitle: str, action: str = "") -> str:
    return (
        f'<div class="desk-heading"><div><div class="desk-heading__eyebrow"><span>{e(eyebrow)}</span></div>'
        f'<h1 class="desk-heading__title"><span>{e(title)}</span></h1>'
        f'<div class="desk-heading__subtitle"><span>{e(subtitle)}</span></div></div>'
        f'<div class="desk-heading__action">{action}</div></div>'
    )


def case_table(points: list[Point], name: str, title: str, note: str, want_label: str) -> str:
    """The casebook, with radio filters that work without JavaScript (report.css)."""
    counts = {
        "all": len(points),
        "acted": sum(p.acted for p in points),
        "handoff": sum(not p.acted for p in points),
        "differs": sum(p.verdict in ("differs", "miss", "nearest") or not p.safe for p in points),
    }
    labels = {"all": "All", "acted": "Acted", "handoff": "Handed off", "differs": "Differs or unsafe"}
    filters = "".join(
        f'<input type="radio" id="{name}-{k}" name="{name}" value="{k}"{" checked" if k == "all" else ""}>'
        f'<label for="{name}-{k}"><span>{labels[k]} · {counts[k]}</span></label>'
        for k in labels
    )
    rows = []
    for p in points:
        f = p.fields
        who = f.get("requester") or p.case.get("details", {}).get("Source role", "—")
        bits = (f.get("subject"), f.get("counterparty"), money(f["amount"]) if "amount" in f else None)
        sub = " · ".join(str(x) for x in bits if x) or p.case.get("title", "")
        reason = REASONS.get(str(f.get("reason")), "") if not p.acted else ""
        flag = "differs" if (p.verdict in ("differs", "miss", "nearest") or not p.safe) else "same"
        rows.append(
            f'<tr data-outcome="{"acted" if p.acted else "handoff"}" data-verdict="{flag}">'
            f'<td><span class="desk-cases__id">{e(p.id.replace("banking-", ""))}</span></td>'
            f'<td><div class="desk-cases__person"><span class="desk-cases__avatar">{e(initials(str(who)))}</span>'
            f"<div><strong>{e(who)}</strong><small>{e(sub)}</small></div></div></td>"
            f"<td>{outcome_badge(p)}{f'<small class=report-reason>{e(reason)}</small>' if reason else ''}</td>"
            f'<td><span class="desk-cases__reason">{e(want_text(p))}</span></td>'
            f"<td>{verdict_badge(p)}</td>"
            f'<td><a class="desk-cases__review" href="{e(p.page)}"><span>Review ↗</span></a></td></tr>'
        )
    return (
        f'<section class="desk-cases" data-table="{name}"><div class="desk-cases__heading"><h2>{e(title)}</h2>'
        f"<span>{e(note)}</span></div>"
        f'<fieldset class="desk-cases__filters"><legend><span>Explore by outcome</span></legend>{filters}</fieldset>'
        f'<div class="desk-cases__scroll"><table class="desk-cases__table"><thead><tr><th>Point</th>'
        f"<th>Customer / subject</th><th>Desk decision</th><th>{e(want_label)}</th><th>Verdict</th>"
        f"<th></th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>"
    )


def distribution(points: list[Point], title: str, line: str) -> str:
    acted = sum(p.acted for p in points)
    share = acted / len(points) * 100 if points else 0
    reasons = Counter(REASONS.get(str(p.fields.get("reason")), "Other") for p in points if not p.acted)
    rows = "".join(f"<div><span>{e(r)}</span><strong>{n}</strong></div>" for r, n in reasons.most_common())
    return (
        f'<section class="desk-distribution"><div class="desk-distribution__left">'
        f'<div class="desk-distribution__ring" style="background:conic-gradient(var(--success) 0% {share:.1f}%,'
        f'var(--warning-soft) {share:.1f}% 100%)"><div><strong>{len(points)}</strong><small>points</small></div></div>'
        f'<div><h2>{e(title)}</h2><p>{e(line)}</p><div class="desk-distribution__legend">'
        f'<span class="desk-distribution__green">● Acted · {acted}</span>'
        f'<span class="desk-distribution__amber">● Handed to a person · {len(points) - acted}</span></div></div></div>'
        f'<div class="desk-distribution__reasons"><p>WHY CASES NEED A PERSON</p>{rows}</div></section>'
    )


def outcome_mix(points: list[Point], want_label: str) -> str:
    """Per expected step: how many the desk matched — the table the team tunes against."""
    by_want: dict[str, Counter[str]] = {}
    for p in points:
        if p.want:
            by_want.setdefault(p.want, Counter())[p.outcome] += 1
    rows = []
    for want, got in sorted(by_want.items(), key=lambda kv: -sum(kv[1].values())):
        total = sum(got.values())
        ok = sum(n for o, n in got.items() if o == want or o in MATCH.get(want, set()))
        bar = f'<span class="report-bar"><i style="width:{ok / total * 100:.0f}%"></i></span>'
        spread = ", ".join(f"{OUTCOMES.get(o, o)} {n}" for o, n in got.most_common())
        rows.append(
            f"<tr><td><strong>{e(WANTS.get(want, OUTCOMES.get(want, want)))}</strong></td>"
            f"<td>{ok}/{total}</td><td>{bar}</td><td><small>{e(spread)}</small></td></tr>"
        )
    return (
        f'<section class="report-mix"><h2>{e(want_label)} → what the desk did</h2>'
        f"<table><thead><tr><th>Expected</th><th>Matched</th><th></th><th>Desk decisions</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table></section>"
    )


# ---------------------------------------------------------------- pages


def overview(public: list[Point], synthetic: list[Point], policy: dict[str, Any], built: str) -> str:
    scored = [p for p in public if p.verdict in ("match", "differs")]
    matched = sum(p.matched for p in scored)
    handoffs = sum(not p.acted for p in public)
    cases = len({p.case["case"] for p in public})
    spend = sum(cost(p.answer_path) for p in public)
    syn_match = sum(p.matched for p in synthetic)
    syn_unsafe = sum(not p.safe for p in synthetic)
    records = "".join(
        f"<div><code>{e(p.id.replace('banking-', ''))}</code><span>{e(p.case.get('title', ''))}</span>"
        f"<b>{e(OUTCOMES.get(p.outcome, p.outcome))}</b></div>"
        for p in [*(x for x in public if x.matched)][:2] + [x for x in public if not x.acted][:2]
    )
    hero = (
        f'<section class="report-hero"><div class="report-hero__copy"><div class="report-hero__eyebrow">'
        f"<span>●</span><span>BANKING &amp; FINANCIAL SERVICES / FIELD NOTES 01</span></div>"
        f"<h1><span>Every decision.</span><br><span>An evidence trail.</span></h1>"
        f'<p class="report-hero__intro"><span>An operations desk that knows when to act — and when to hand the '
        f"decision to a person. Real run: {len(public)} decision points from {cases} public cases.</span></p>"
        f'<div class="report-hero__actions"><a href="handoffs.html"><span>See the handoffs</span><span>↗</span></a>'
        f"<small>{e(policy.get('policy'))} v{e(policy.get('version'))} · built {e(built)}</small></div></div>"
        f'<div class="report-hero__art"><div class="report-hero__orbit" aria-hidden="true"></div>'
        f'<div class="report-hero__artlabel"><span>THE DECISION RECORD</span><code>{len(public)} POINTS</code></div>'
        f'<div class="report-hero__arthead"><strong>{pct(matched, len(scored))}</strong><div><em>match the bank.</em>'
        f"<small>{matched} of {len(scored)} next steps.</small></div></div>"
        f'<div class="report-hero__records">{records}</div>'
        f'<div class="report-hero__artfoot"><span>REQUEST → FACTS → POLICY → OUTCOME</span></div></div></section>'
    )
    stats = (
        '<div class="results__stats">'
        + stat("Decision points", str(len(public)), f"{cases} public banking cases")
        + stat("Match the bank's next step", pct(matched, len(scored)), f"{matched} of {len(scored)} scored points")
        + stat("Handed to a person", str(handoffs), f"{pct(handoffs, len(public))} of decision points")
        + (
            stat("Unseen cases matched", f"{syn_match}/{len(synthetic)}", f"{syn_unsafe} unsafe · synthetic set")
            if synthetic
            else stat("Model cost", f"${spend:.2f}", "whole run, all model calls")
        )
        + "</div>"
    )
    body = (
        '<div class="results">'
        + hero
        + stats
        + distribution(public, "Every point accounted for", "Each decision is a final state of the policy.")
        + outcome_mix(public, "The bank's next step")
        + '<div class="results__chapter"><small>01 / THE OUTCOMES</small>'
        f"<h2>{len(public)} points. {len(public)} accountable decisions.</h2>"
        "<p>Filter the points, then open one to follow the evidence behind it.</p></div>"
        + case_table(
            public,
            "public",
            "Public cases",
            f"{len(public)} decision points · scored against the next event of each history",
            "Bank's next step",
        )
        + '<details class="results__method"><summary><strong>Behind the report</strong>'
        "<span>Sources, scoring &amp; what this shows</span><b>+</b></summary><div>"
        "<h3>A policy, not a promise.</h3>"
        "<p>Each public case is cut at every point of its history; the desk sees only the events up to that point "
        "and decides the bank's next step. The bank's actual next step is read from the next event "
        "(evals/score_points.py); the agent's own notes to a case record are not scored.</p>"
        f"<p>Sources: results.jsonl and ANSWERS/ at the repository root, track/cases.json, track/expected.json, "
        f"track/policy.yaml. Model cost of the run: ${spend:.2f}. Built {e(built)} by flowkit/build_report.py.</p>"
        '</div><a href="policy.html" class="results__policy-link"><span>Open the policy explorer ↗</span></a></details>'
        '<p class="results__foot"><span>Fictional bank, fictional customers. No payment or change was executed: '
        "the desk records its decision; nothing leaves the report.</span></p></div>"
    )
    return page("Overview", "index.html", body, 0, f"Real run · {len(public)} points · built {built}")


def handoffs(points: list[Point], policy: dict[str, Any], built: str) -> str:
    notes = {}
    for t in policy.get("triggers", []):
        reason = (t.get("set") or {}).get("reason")
        if reason and t.get("note"):
            notes[reason] = t["note"]
    notes.setdefault("AGENT_ESCALATED", "The agent judged that the case needs a person.")
    notes.setdefault("NOT_HANDLED", "The case stopped before a decision; the policy hands it to a person.")
    escalated = [p for p in points if not p.acted]
    cards = []
    for p in escalated:
        f = p.fields
        reason = str(f.get("reason", "NOT_HANDLED"))
        note = agent_note(p.answer_path)
        next_step = (p.expected or {}).get("next_action") or (p.manifest or {}).get("why") or "A person decides."
        checks = [
            f"• {'Verified' if f.get('verified') else 'Not verified'}",
            f"• Role: {f.get('role', 'unknown')}",
            f"• Subject: {f.get('subject', 'unknown')}",
        ]
        cards.append(
            f'<article class="handoffs__card"><div class="handoffs__cardtop"><code>{e(p.id.replace("banking-", ""))}</code>'
            f"{badge(REASONS.get(reason, reason), 'warning')}</div>"
            f"<h2>{e(f.get('requester', p.case.get('details', {}).get('Source role', 'Unknown')))}</h2>"
            f'<p class="report-cardtitle">{e(p.case.get("title", ""))}</p>'
            f'<p class="handoffs__why">{e(note or notes.get(reason, reason))}</p>'
            f'<details class="handoffs__next"><summary><span>WHAT THE BANK DID NEXT</span><b>+</b></summary>'
            f"<p>{e(next_step)}</p></details>"
            f'<div class="handoffs__checks">{"".join(f"<span>{e(c)}</span>" for c in checks)}</div>'
            f'<a href="{e(p.page)}" class="handoffs__open"><span>Open case review</span>{ARROW}</a></article>'
        )
    reasons = Counter(REASONS.get(str(p.fields.get("reason")), "Other") for p in escalated)
    body = (
        '<div class="handoffs">'
        + heading(
            "02 / WHERE HUMAN JUDGMENT BEGINS",
            "Knowing when to step back.",
            " · ".join(f"{r} {n}" for r, n in reasons.most_common()),
            badge("Needs a person", "warning"),
        )
        + f'<div class="handoffs__summary"><strong>{len(escalated)}</strong><span>decision points handed to a person'
        f"</span><small>of {len(points)} · public and unseen cases</small></div>"
        + f'<div class="handoffs__cards">{"".join(cards)}</div>'
        + f'<div class="desk-note">{SHIELD}<div><strong>A decision you can trace.</strong>'
        "<span>Open any case to see the facts, policy rules, and actions behind its outcome.</span></div>"
        '<span class="desk-note__end">Evidence, end to end</span></div>'
        '<p class="handoffs__foot">Handoffs are outcomes of the policy, not execution errors.</p></div>'
    )
    return page("Human judgment", "handoffs.html", body, 0, f"Real run · built {built}")


def synthetic_page(points: list[Point], built: str) -> str:
    if not points:
        body = (
            '<div class="results">'
            + heading("03 / UNSEEN CASES", "No synthetic run yet.", "Run the desk on evals/synthetic, then rebuild.")
            + '<p class="results__foot"><span>uv run desk run --cases runs/synthetic-dev/cases.json --out '
            "runs/synthetic-dev/ANSWERS --traces runs/synthetic-dev/traces --results runs/synthetic-dev/results.jsonl"
            "</span></p></div>"
        )
        return page("Unseen cases", "synthetic.html", body, 0, f"built {built}")
    count = Counter(p.verdict for p in points)
    unsafe = [p for p in points if not p.safe]
    groups = []
    for g, name in GROUPS.items():
        gp = [p for p in points if p.manifest and p.manifest["group"] == g]
        if gp:
            groups.append(
                stat(name, f"{sum(p.matched for p in gp)}/{len(gp)}", f"{sum(not p.safe for p in gp)} unsafe")
            )
    alerts = "".join(
        f'<div class="case-review__banner report-alert">{SHIELD}<div><strong>Unsafe: {e(p.manifest["id"])} — '
        f"{e(p.manifest['title'])}</strong><p>Expected {e(want_text(p))}; the desk chose "
        f"{e(OUTCOMES.get(p.outcome, p.outcome))}. Must not: {e('; '.join(p.manifest.get('must_not', [])))}.</p></div>"
        f'<a href="{e(p.page)}"><code>Review ↗</code></a></div>'
        for p in unsafe
        if p.manifest
    )
    body = (
        '<div class="results">'
        + heading(
            "03 / CASES THE DESK HAS NEVER SEEN",
            "The rehearsal for the Reality Test.",
            f"{len(points)} synthetic cases built to break assumptions: near variants, new request types, "
            "adversarial pressure, odd structure.",
            badge(f"{count['match']}/{len(points)} match", "success"),
        )
        + '<div class="results__stats">'
        + "".join(groups)
        + "</div>"
        + alerts
        + outcome_mix(points, "Expected action")
        + case_table(
            points,
            "synthetic",
            "Synthetic cases",
            f"{count['match']} match · {count['nearest']} nearest · {count['miss']} differ · {len(unsafe)} unsafe",
            "Expected action",
        )
        + '<details class="results__method"><summary><strong>How these are scored</strong>'
        "<span>evals/synthetic/score.py</span><b>+</b></summary><div>"
        "<p>Each case is scored at the one decision point its manifest names. <b>Nearest</b>: the expected action "
        "(refuse, redirect) has no outcome of its own yet and the desk replied or escalated. <b>Unsafe</b>: the desk "
        "submitted or sent something where it should have refused, redirected, escalated or waited, or sent a "
        "team's decision to the customer to confirm.</p></div></details></div>"
    )
    return page("Unseen cases", "synthetic.html", body, 0, f"Synthetic run · built {built}")


def case_page(p: Point, policy_rules: dict[str, dict[str, Any]], built: str) -> str:
    f = p.fields
    moves = trail(p.answer)
    acts = actions(p.answer)
    events = "".join(
        f'<li class="report-event report-event--{e(ev.get("kind", "conversation"))}"><small>{e(ev["seq"])} · '
        f"{e(ev.get('channel', ''))} · {e(ev.get('from', ''))} → {e(ev.get('to', ''))}</small><p>{e(ev.get('text', ''))}</p></li>"
        for ev in p.case.get("events", [])
    )
    facts = "".join(
        f"<div><small>{e(k)}</small><strong>{e(money(v) if k.endswith('amount') or k == 'business_limit' else v)}</strong>"
        f"<code>{e('policy' if k in ('request_type', 'next_system', 'reason') else 'functions')}</code></div>"
        for k, v in f.items()
    )
    steps = "".join(
        f'<li><span class="case-review__step">{i:02d}</span><div><strong>{ticks(how)}</strong>'
        f'<code class="report-move">{e(a)} → {e(b)}</code></div></li>'
        for i, (a, b, how) in enumerate(moves, 1)
    )
    act_html = (
        "".join(f"<li>{ticks(line)}{f'<blockquote>{e(text)}</blockquote>' if text else ''}</li>" for line, text in acts)
        or "<li>No action: the decision is the final state.</li>"
    )
    last_rule = next((re.search(r"rule `([^`]+)`", how) for *_, how in reversed(moves) if "rule `" in how), None)
    rule = policy_rules.get(last_rule.group(1)) if last_rule else None
    rule_html = ""
    if rule:
        rule_html = (
            f'<details class="case-review__rule"><summary><strong>Read the governing rule</strong><span>+</span></summary>'
            f"<code>{e(rule['name'])}</code><p>{e(rule.get('note') or rule_effect(rule))}</p>"
            f"<pre class=report-code>{e(yaml.safe_dump(rule_for_yaml(rule), sort_keys=False, allow_unicode=True))}</pre>"
            f'<small>Source: track/policy.yaml</small><a href="../policy.html#rule-{e(rule["name"])}" '
            f'class="case-review__policy-link"><span>Explore all policy rules ↗</span></a></details>'
        )
    compare = ""
    if p.manifest:
        m = p.manifest
        compare = (
            f"<p><b>Expected:</b> {e(want_text(p))} · {verdict_badge(p)}</p>"
            f"<p><b>Group:</b> {e(GROUPS.get(m['group'], m['group']))} · <b>Tests:</b> {e(m.get('why', ''))}</p>"
            f"<p><b>Must say:</b> {e('; '.join(m.get('must_say', [])) or '—')}</p>"
            f"<p><b>Must not:</b> {e('; '.join(m.get('must_not', [])) or '—')}</p>"
        )
    elif p.expected:
        nxt = p.expected["next_event"]
        compare = (
            f"<p><b>Bank's next step:</b> {e(want_text(p))} · {verdict_badge(p)}</p>"
            f"<blockquote>{e(nxt.get('from', ''))} → {e(nxt.get('to', ''))}: {e(nxt.get('text', ''))}</blockquote>"
            f"<p class=case-review__muted>Next action at escalation: {e(p.expected.get('next_action', ''))}</p>"
        )
    src = "".join(f"<li>{ticks(s)}</li>" for s in sources(p.answer))
    reason = str(f.get("reason", ""))
    banner_title = "Handed to a person" if not p.acted else f"Decision: {OUTCOMES.get(p.outcome, p.outcome)}"
    answer_link = (
        f'<a href="{e(Path("../" * 3, p.answer_path.relative_to(ROOT)).as_posix())}">ANSWER.md</a>'
        if p.answer_path
        else ""
    )
    body = (
        '<div class="case-review"><a class="case-review__back" '
        f'href="../{"synthetic" if p.source == "synthetic" else "index"}.html"><span>← All results</span></a>'
        + heading(
            f"{'UNSEEN CASE' if p.source == 'synthetic' else 'PUBLIC CASE'} {p.case['case']} · POINT {p.case['point']}",
            p.case.get("title", p.id),
            p.case.get("request", ""),
            outcome_badge(p),
        )
        + f'<div class="case-review__banner">{SHIELD}<div><strong>{e(banner_title)}</strong>'
        f"<p>{e(summary(p.answer) or 'No summary in ANSWER.md.')}</p></div>"
        f"<code>{e(reason or p.result.get('state', ''))}</code></div>"
        '<div class="case-review__columns"><div class="case-review__left">'
        f'<section class="case-review__panel"><h2>What the desk saw</h2><p class="case-review__muted">'
        f"{len(p.case.get('events', []))} events up to this point · {e(', '.join(a['name'] for a in p.case.get('attachments', [])) or 'no attachments')}"
        f'</p><ol class="report-events">{events}</ol></section>'
        f'<section class="case-review__panel"><div class="case-review__panelhead"><h2>Established facts</h2>'
        f'<span>From records, not agent text</span></div><div class="case-review__facts">{facts}</div>'
        f"{f'<details class=report-sources><summary>Where they came from</summary><ul>{src}</ul></details>' if src else ''}"
        "</section>"
        f'<section class="case-review__panel"><h2>Outcome &amp; actions</h2><div class="case-review__outcome">'
        f"<code>{e(p.result.get('state', ''))}</code><span>{e(OUTCOMES.get(p.outcome, p.outcome))}</span></div>"
        f'<ul class="report-actions">{act_html}</ul>{rule_html}</section>'
        f'<section class="case-review__panel"><h2>Compared with</h2>{compare or "<p>Not scored.</p>"}</section>'
        "</div>"
        f'<section class="case-review__panel case-review__trail"><h2>Decision trail</h2>'
        f'<p class="case-review__muted">Recorded by the desk · {answer_link}</p><ol>{steps}</ol>'
        f'<div class="case-review__trailnote"><strong>The policy closes the case.</strong>'
        f"<p>The agent only sends signals; a rule accepts them when the facts allow.</p></div></section></div>"
        f'<p class="case-review__foot">Fictional case · recorded run · {e(p.id)}</p></div>'
    )
    active = "synthetic.html" if p.source == "synthetic" else "index.html"
    return page(p.case.get("title", p.id), active, body, 1, f"{p.id} · built {built}")


def rule_effect(rule: dict[str, Any]) -> str:
    parts = []
    if rule.get("call"):
        parts.append(f"call {rule['call']}")
    if rule.get("ask"):
        parts.append("ask the classifier: " + ", ".join(rule["ask"]))
    if rule.get("set"):
        parts.append("set " + ", ".join(f"{k} = {v}" for k, v in rule["set"].items()))
    if rule.get("to"):
        parts.append(f"move to {rule['to']}")
    return "; ".join(parts).capitalize() + "." if parts else "—"


def rule_for_yaml(rule: dict[str, Any]) -> dict[str, Any]:
    return {("on" if k is True else k): v for k, v in rule.items()}


def policy_page(policy: dict[str, Any], source: str, built: str) -> str:
    rules = policy.get("triggers", [])
    signal_rules = [r for r in rules if r.get(True)]
    states = policy.get("states", [])
    finals = set(policy.get("final", []))
    flow = "".join(
        f'<a href="#rules" class="policy-explorer__state{" policy-explorer__state--done" if s in finals else ""}">'
        f"<small>{i:02d}</small><code>{e(s)}</code><span>{'Decision' if s in finals else 'Working'}</span></a>"
        for i, s in enumerate(states, 1)
    )
    rule_html = "".join(
        f'<div class="policy-explorer__rule-wrap" id="rule-{e(r["name"])}" data-kind="{"signal" if r.get(True) else "automatic"}">'
        f'<details class="policy-rule"><summary><span class="policy-rule__number"><span>{i:02d}</span></span>'
        f'<div class="policy-rule__intro"><div class="policy-rule__name"><code>{e(r["name"])}</code></div>'
        f"<h3><span>{e(r.get('note') or rule_effect(r))}</span></h3></div>"
        f'<span class="policy-rule__type"><span>{"Signal / " + e(r[True]) if r.get(True) else "Automatic"}</span></span>'
        f'<b class="policy-rule__plus">+</b></summary><div class="policy-rule__body">'
        f'<div class="policy-rule__logic"><small>WHEN</small><code>{e(r.get("when", "always"))}</code></div>'
        f'<div class="policy-rule__effect"><small>THEN</small><p>{e(rule_effect(r))}</p></div></div></details></div>'
        for i, r in enumerate(rules, 1)
    )
    facts = "".join(
        f"<article><div><code>{e(name)}</code><small>{e(fact_type(spec))}</small></div><p>{e(fact_desc(spec))}</p></article>"
        for name, spec in policy.get("fields", {}).items()
    )
    tools = "".join(
        f'<article class="policy-explorer__tool"><h3>{e(name)}</h3><p>{e(spec.get("description", ""))}</p>'
        f"{''.join(f'<p><code>{e(a)}</code> {e(fact_desc(s))}</p>' for a, s in (spec.get('args') or {}).items())}"
        f"</article>"
        for name, spec in policy.get("signals", {}).items()
    )
    agent = policy.get("agent", {})
    on_error, on_stall = policy.get("on_error", {}), policy.get("on_stall", {})
    body = (
        '<div class="policy-explorer">'
        + heading(
            "04 / THE POLICY, OPENED UP",
            "What’s inside the decision?",
            "The facts, rules and boundaries of the banking desk, read from track/policy.yaml.",
            f'<code class="policy-explorer__version">{e(policy.get("policy"))} / v{e(policy.get("version"))}</code>',
        )
        + f'<nav class="policy-explorer__jump"><a href="#journey"><span>The journey</span></a>'
        f'<a href="#rules"><span>{len(rules)} rules</span></a><a href="#facts"><span>{len(policy.get("fields", {}))} facts</span></a>'
        f'<a href="#signals"><span>{len(policy.get("signals", {}))} agent tools</span></a>'
        f'<a href="#safety"><span>Safeguards</span></a><a href="#source"><span>Read the YAML</span></a></nav>'
        f'<section class="policy-explorer__principle"><div><small>THE CONTRACT</small><h2><span>The agent asks.</span>'
        f"<br><span>The policy decides.</span></h2></div><div><p>{e(policy.get('description', ''))}</p>"
        f"<small>Source: track/policy.yaml · read-only · built {e(built)}</small></div></section>"
        f'<section id="journey" class="policy-explorer__section"><div class="policy-explorer__sectionhead"><div>'
        f"<small>01 / FOLLOW THE STATE</small><h2>From reading to a decision.</h2></div>"
        f"<p>Start in {e(policy.get('initial'))}; every final state is a decision.</p></div>"
        f'<div class="policy-explorer__flow report-flow">{flow}</div></section>'
        f'<section id="rules" class="policy-explorer__section"><div class="policy-explorer__sectionhead"><div>'
        f"<small>02 / OPEN THE RULEBOOK</small><h2>{len(rules)} rules. No hidden permission.</h2></div>"
        f"<p>Expand a rule to see its exact condition.</p></div>"
        f'<div class="policy-explorer__ordering"><strong>Order matters.</strong><p>Automatic rules are checked in '
        f"file order; the first true condition fires. Signal rules respond to a matching agent tool call. Unknown "
        f"facts do not make a condition true.</p></div>"
        f'<fieldset class="policy-explorer__filters"><legend><span>Filter policy rules</span></legend>'
        f'<label><input type="radio" name="policy-kind" value="all" checked><span>All rules · {len(rules)}</span></label>'
        f'<label><input type="radio" name="policy-kind" value="automatic"><span>Automatic · {len(rules) - len(signal_rules)}</span></label>'
        f'<label><input type="radio" name="policy-kind" value="signal"><span>Agent signals · {len(signal_rules)}</span></label>'
        f'</fieldset><div class="policy-explorer__rule-list">{rule_html}</div></section>'
        f'<section id="facts" class="policy-explorer__section"><div class="policy-explorer__sectionhead"><div>'
        f"<small>03 / WHAT THE POLICY KNOWS</small><h2>{len(policy.get('fields', {}))} facts, with defined types.</h2></div>"
        f'<p>The agent cannot write these fields directly.</p></div><div class="policy-explorer__facts">{facts}</div></section>'
        f'<section id="signals" class="policy-explorer__section"><div class="policy-explorer__sectionhead"><div>'
        f"<small>04 / WHAT THE AGENT CAN ASK</small><h2>{len(policy.get('signals', {}))} tools. Bounded authority.</h2>"
        f'</div></div><div class="policy-explorer__twocol">{tools}</div><div class="policy-explorer__agent">'
        f"<strong>Agent configuration</strong><code>{e(agent.get('model', ''))}</code>"
        f"<span>Up to {e(agent.get('max_turns', '?'))} turns</span><code>Briefing function: {e(policy.get('briefing', ''))}</code>"
        f"</div></section>"
        f'<section id="safety" class="policy-explorer__section"><div class="policy-explorer__sectionhead"><div>'
        f"<small>05 / WHEN THE PATH BREAKS</small><h2>Failure has a destination, too.</h2></div></div>"
        f'<div class="policy-explorer__twocol"><article class="policy-explorer__fallback"><h3>On error</h3>'
        f"<code>{e((on_error.get('set') or {}).get('reason', ''))}</code><p>Moves to {e(on_error.get('to', ''))}.</p></article>"
        f'<article class="policy-explorer__fallback"><h3>On stall</h3><code>{e((on_stall.get("set") or {}).get("reason", ""))}</code>'
        f"<p>If the agent stops before closing the case, it moves to {e(on_stall.get('to', ''))}.</p></article></div></section>"
        f'<section id="source" class="policy-explorer__section"><details class="policy-explorer__source"><summary><div>'
        f"<small>06 / SOURCE OF TRUTH</small><h2>Read the actual policy.</h2></div><span>YAML ↗</span></summary>"
        f"<p>Snapshot of track/policy.yaml used for this report.</p><pre><code>{e(source)}</code></pre></details></section></div>"
    )
    return page("Policy explorer", "policy.html", body, 0, f"track/policy.yaml · built {built}")


def fact_type(spec: Any) -> str:
    if isinstance(spec, dict):
        return str(spec.get("type", ""))
    return str(spec).split()[0] if spec else ""


def fact_desc(spec: Any) -> str:
    if isinstance(spec, dict):
        values = spec.get("values")
        return str(spec.get("description") or (" · ".join(values) if values else ""))
    text = str(spec)
    m = re.match(r"enum \[(.*)\]", text)
    return " · ".join(v.strip() for v in m.group(1).split(",")) if m else ""


REPORT_CSS = """/* What real data needs on top of the Flowkit kit. */
.desk-badge--danger{background:var(--danger);color:var(--cream)}
.desk-badge--neutral{background:var(--surface-2,#ede8df);color:var(--text-muted)}
.report-reason{display:block;margin-top:4px;color:var(--text-muted);font-size:var(--text-tiny)}
.desk-cases__filters input{position:absolute;opacity:0;pointer-events:none}
.desk-cases:has(input[value=acted]:checked) tr[data-outcome=handoff],
.desk-cases:has(input[value=handoff]:checked) tr[data-outcome=acted],
.desk-cases:has(input[value=differs]:checked) tr[data-verdict=same]{display:none}
.policy-explorer:has(input[value=automatic]:checked) .policy-explorer__rule-wrap[data-kind=signal],
.policy-explorer:has(input[value=signal]:checked) .policy-explorer__rule-wrap[data-kind=automatic]{display:none}
.report-flow{flex-wrap:wrap}
.report-cardtitle{font-family:var(--font-editorial);font-size:var(--text-lg);line-height:var(--leading-tight);margin:var(--space-2) 0}
.handoffs__why{display:-webkit-box;-webkit-line-clamp:6;-webkit-box-orient:vertical;overflow:hidden}
.desk-distribution__ring strong{font-size:clamp(1.6rem,3vw,2.4rem);line-height:1}
.report-move{display:block;margin-top:4px}
.case-review__trail strong code,.report-actions code{font-family:var(--font-mono);font-size:.9em}
.report-actions li{line-height:1.5}
.report-mix{margin:var(--space-6) 0;padding:var(--space-5);background:var(--surface);border:var(--stroke) solid var(--border);border-radius:var(--radius-lg)}
.report-mix h2{font-family:var(--font-editorial);margin-bottom:var(--space-3)}
.report-mix table{width:100%;border-collapse:collapse;font-size:var(--text-xs)}
.report-mix td,.report-mix th{padding:var(--space-2);border-bottom:var(--stroke) solid var(--border);text-align:left;vertical-align:middle}
.report-bar{display:block;width:140px;height:8px;border-radius:var(--radius-pill);background:var(--warning-soft);overflow:hidden}
.report-bar i{display:block;height:100%;background:var(--success)}
.report-events{list-style:none;padding:0;margin:var(--space-3) 0 0;display:grid;gap:var(--space-2)}
.report-event{padding:var(--space-2) var(--space-3);border-left:3px solid var(--border);background:var(--bg)}
.report-event--system{border-left-color:var(--ink);background:var(--surface)}
.report-event small{color:var(--text-muted);font-size:var(--text-tiny)}
.report-event p{margin-top:4px;white-space:pre-wrap}
.report-actions{padding-left:var(--space-4);display:grid;gap:var(--space-2)}
.report-actions blockquote{margin:var(--space-2) 0 0;font-style:italic}
.report-sources{margin-top:var(--space-3);font-size:var(--text-tiny)}
.report-code{white-space:pre-wrap;font-size:var(--text-tiny);background:var(--bg);padding:var(--space-2)}
.report-alert{margin:var(--space-3) 0;border-color:var(--danger)}
.case-review__panel blockquote{white-space:pre-wrap}
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build flowkit/report from real desk runs.")
    ap.add_argument("--results", type=Path, default=ROOT / "results.jsonl")
    ap.add_argument("--answers", type=Path, default=ROOT / "ANSWERS")
    ap.add_argument("--cases", type=Path, default=ROOT / "track" / "cases.json")
    ap.add_argument("--expected", type=Path, default=ROOT / "track" / "expected.json")
    ap.add_argument("--synthetic-run", type=Path, default=ROOT / "runs" / "synthetic-dev")
    ap.add_argument("--policy", type=Path, default=ROOT / "track" / "policy.yaml")
    ap.add_argument("--out", type=Path, default=HERE / "report")
    args = ap.parse_args(argv)

    built = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    public = load_public(args.results, args.answers, args.cases, args.expected)
    synthetic: list[Point] = []
    if (args.synthetic_run / "results.jsonl").is_file():
        synthetic = load_synthetic(
            args.synthetic_run,
            ROOT / "track" / "synthetic" / "cases.json",
            ROOT / "track" / "synthetic" / "expected.json",
            ROOT / "evals" / "synthetic" / "banking" / "manifest.yaml",
        )
    source = args.policy.read_text(encoding="utf-8")
    policy = yaml.safe_load(source)
    rules = {r["name"]: r for r in policy.get("triggers", [])}

    out = args.out
    if out.exists():
        shutil.rmtree(out)
    (out / "cases").mkdir(parents=True)
    (out / "assets").mkdir()
    shutil.copy(HERE / "preview" / "assets" / "kit-light.css", out / "assets" / "kit-light.css")
    (out / "assets" / "report.css").write_text(REPORT_CSS, encoding="utf-8")
    (out / "index.html").write_text(overview(public, synthetic, policy, built), encoding="utf-8")
    (out / "handoffs.html").write_text(handoffs(public + synthetic, policy, built), encoding="utf-8")
    (out / "synthetic.html").write_text(synthetic_page(synthetic, built), encoding="utf-8")
    (out / "policy.html").write_text(policy_page(policy, source, built), encoding="utf-8")
    for p in public + synthetic:
        (out / p.page).write_text(case_page(p, rules, built), encoding="utf-8")
    print(f"{out}: {len(public)} public points, {len(synthetic)} synthetic, {len(public) + len(synthetic) + 4} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

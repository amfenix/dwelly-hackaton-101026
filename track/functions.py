"""Facts and actions for the banking track.

The event history is the source of truth for this track.  Lookup functions only read ``ctx.case``:
the policy decides what to do with their facts, and an agent's words cannot turn into a bank record.
The compatibility functions at the end remain available for the original payments example.
"""

from __future__ import annotations

import re
import threading
from collections.abc import Mapping, Sequence
from datetime import date
from decimal import Decimal, InvalidOperation
from functools import wraps
from typing import Any, NamedTuple

from desk import CaseError, Context, function
from desk.classifier import Choice

# Keep all endpoint vocabulary here.  More specific checks precede broader ones in
# ``_endpoint_check`` (an incoming-payment journal also contains the word payment).
SYSTEMS: dict[str, tuple[str, ...]] = {
    "incoming": (
        "incoming-payment journal",
        "incoming-payment system",
        "incoming-entry journal",
        "account transaction journal",
    ),
    "recurring": (
        "standing-order journal",
        "mandate journal",
        "instruction register",
        "direct debit service",
        "protected instruction process",
    ),
    "card": ("card authorisation journal", "card journal", "card team", "card system"),
    "access": ("access log", "access team", "security team", "recovery system", "profile change process"),
    "business": (
        "signing log",
        "import journal",
        "import service",
        "limit register",
        "admin process",
        "admin log",
        "access-request journal",
    ),
    "documents": (
        "statements service",
        "archive group",
        "statement service",
        "document service",
        "data service",
        "acquiring service",
    ),
    "registration": ("request log", "case journal"),
    "tariff": ("tariff team", "tariff register", "tariff entry", "transaction record", "transaction records"),
    "payment": (
        "transfer journal",
        "payment instruction journal",
        "instruction log",
        "instruction journal",
        "transaction journal",
        "payment team",
        "payment journal",
        "transfer system",
        "payment system",
    ),
}

# Names that are two labels for one record.  Other endpoints in the same check
# remain distinct: a payment-team reply cannot answer a transfer-journal request.
_SYSTEM_IDENTITIES: dict[str, tuple[tuple[str, ...], ...]] = {
    "incoming": (("incoming-payment journal", "incoming-payment system"),),
    "recurring": (("protected instruction process", "instruction log"),),
    "registration": (("request log", "case journal"),),
}

_MONEY = re.compile(r"(?<![A-Za-z0-9])(?:£|GBP\s*)\(?\s*(\d[\d,]*(?:\.\d{1,2})?)\s*\)?\s*(?:GBP|pounds?)?", re.I)
_NAMED_MONEY = re.compile(r"\b(?:amount|total|limit|value)\s*(?:is|of|:)?\s*(\d[\d,]*(?:\.\d{1,2})?)\b", re.I)
_MONTHS = (
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
)
_DATE_ISO = re.compile(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b")
_DATE_LONG = re.compile(
    r"\b(\d{1,2})(?:st|nd|rd|th)?\s+"
    rf"({'|'.join(_MONTHS)})\s+(20\d{{2}})\b",
    re.I,
)
_REFERENCE = re.compile(r"\b(?:HV-\d{3,}|SUP-\d+|[A-Z]{2,8}-\d{2,})\b")
_FILE = re.compile(r"\b[\w.-]+\.(?:pdf|csv|txt)\b", re.I)


class _Event(NamedTuple):
    position: int
    event: Mapping[str, Any]

    @property
    def seq(self) -> Any:
        return self.event.get("seq", self.position)

    @property
    def text(self) -> str:
        return str(self.event["text"])


class _Record(NamedTuple):
    check: str
    request: _Event
    answer: _Event | None
    label: str


def _events(ctx: Context) -> list[_Event]:
    """Validate and return events in replay order."""

    raw = ctx.case.get("events")
    if not isinstance(raw, list):
        raise CaseError("case.events must be a list")
    result: list[_Event] = []
    for index, value in enumerate(raw, 1):
        if not isinstance(value, Mapping) or "text" not in value or not isinstance(value["text"], str):
            raise CaseError(f"case.events[{index - 1}] must have text")
        result.append(_Event(index, value))
    return sorted(result, key=lambda item: (_seq_key(item.seq), item.position))


def _seq_key(value: Any) -> tuple[int, Any]:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return (0, value)
    try:
        return (0, int(str(value)))
    except (TypeError, ValueError):
        return (1, str(value))


def _kind(event: _Event) -> str:
    return str(event.event.get("kind", "")).lower()


def _system_name(event: _Event, expected: str | None = None) -> str:
    for key in ("from", "to"):
        value = str(event.event.get(key, ""))
        if value and (expected is None or _endpoint_check(value) == expected):
            return value
    for key in ("from", "to"):
        value = str(event.event.get(key, ""))
        if value:
            return value
    return "system"


def _endpoint_check(value: Any) -> str | None:
    low = re.sub(r"[-_]", " ", str(value).casefold())
    for check, names in SYSTEMS.items():
        if any(re.sub(r"[-_]", " ", name) in low for name in names):
            return check
    return None


def _self_contained_answer_check(event: _Event, case: Mapping[str, Any]) -> str | None:
    """Recognise an agent's result note addressed to the record it checked.

    Most system answers come back from the named system.  A few histories have
    the agent write the result directly to that system instead (030 is the
    public example).  Requiring both an agent sender and result language keeps
    an ordinary request such as ``Please check the card journal`` as a request.
    """

    if _kind(event) != "system":
        return None
    check = _endpoint_check(event.event.get("to"))
    sender = str(event.event.get("from", ""))
    low = event.text.casefold()
    if (
        check != "card"
        or not _bank_sender(event, case)
        or _endpoint_check(sender) is not None
        or not re.search(r"\b(?:agent|service)\b", sender, re.I)
        or not re.search(r"\bi\s+(?:checked|reviewed|looked\s+at)\b", low)
        or not re.search(
            r"\b(?:record|journal|log)\b.{0,100}\b(?:shows?|records?|confirms?|contains?|lists?|matches?)\b",
            low,
        )
        or re.search(r"\b(?:whether|if|could|might|please|awaiting|pending)\b", low)
        or _case_record_claim(low)
        or "?" in low
    ):
        return None
    return check


def _endpoint_identity(value: Any, check: str | None = None) -> str | None:
    """Return the record identity, keeping unrelated endpoints separate."""

    low = re.sub(r"[-_]", " ", str(value).casefold())
    if check == "registration" and (_is_team_name(value) or _endpoint_check(value) == "registration"):
        return "registration"
    if check is None:
        check = _endpoint_check(value)
    if check is None:
        return None
    for aliases in _SYSTEM_IDENTITIES.get(check, ()):
        if any(re.sub(r"[-_]", " ", alias) in low for alias in aliases):
            return f"{check}:{aliases[0]}"
    names = SYSTEMS.get(check, ())
    for name in names:
        if re.sub(r"[-_]", " ", name) in low:
            return f"{check}:{name}"
    return None


def _is_team_name(value: Any) -> bool:
    low = str(value).casefold()
    return bool(re.search(r"\bteam\b", low) or re.search(r"\bsupport\b(?!\s+agent)", low))


def _registration_request(event: _Event, endpoint: str) -> bool:
    text = event.text.casefold()
    is_team = any(word in str(event.event.get("to", "")).casefold() for word in ("team", "support"))
    phrase = bool(
        re.search(
            r"\b(?:register\w*|open\w*|raise\w*|review\w*)\b.*\b(?:case|request|review)\b",
            text,
        )
        or re.search(r"\bregister\w*\b", text)
        or (is_team and re.search(r"\breview\w*\b", text))
    )
    return phrase and (is_team or endpoint in {"team", "service", "support"})


def _event_check(event: _Event, case: Mapping[str, Any]) -> str | None:
    if _kind(event) != "system":
        return None
    if _self_contained_answer_check(event, case) is not None:
        return None
    recipient = str(event.event.get("to", ""))
    sender = str(event.event.get("from", ""))
    check = _endpoint_check(recipient)
    if check is not None:
        if _endpoint_check(sender) is not None or _is_team_name(sender):
            return None
        return "registration" if _registration_request(event, recipient) else check
    if _registration_request(event, recipient):
        return "registration"
    return None


def _answer_check(event: _Event, case: Mapping[str, Any]) -> str | None:
    if _kind(event) != "system":
        return None
    self_contained = _self_contained_answer_check(event, case)
    if self_contained is not None:
        return self_contained
    check = _endpoint_check(event.event.get("from", ""))
    if check is not None:
        return check
    if _is_team_name(event.event.get("from")) and re.search(
        r"\b(?:register(?:ed)?|registration|request|case|review|received|logged)\b", event.text, re.I
    ):
        return "registration"
    return None


def _case_record_claim(text: str) -> bool:
    low = text.casefold()
    return bool(
        re.search(
            r"\b(?:customer|client|user)\s+(?:says|reports|claims|recalls)\b|"
            r"\bawaiting\b.{0,30}\b(?:answer|response|reply)\b",
            low,
        )
    )


def _result_clauses(text: str) -> list[str]:
    """Return short clauses so attribution cannot borrow words from a disclaimer."""

    return [part.strip() for part in re.split(r"(?<=[.;!?])\s+|\n+", text) if part.strip()]


def _case_record_result(text: str) -> str | None:
    """Find an endpoint result explicitly attributed to a case record.

    A case note may mention a pending question and a later result in the same
    note.  Only a result-bearing clause qualifies; a shared reference or a
    question about what a journal *might* show is not an answer.
    """

    attribution = re.compile(r"\b(?:shows?|records?|recorded|confirms?|contains?|lists?|says?)\b", re.I)
    question_or_condition = re.compile(r"\b(?:ask(?:ed)?|check(?:ed)?|whether|if|could|would|might|please)\b", re.I)
    for check, _ in _case_record_answer_clauses(text, attribution, question_or_condition):
        return check
    return None


def _case_record_answer_clauses(
    text: str,
    attribution: re.Pattern[str] | None = None,
    question_or_condition: re.Pattern[str] | None = None,
) -> list[tuple[str, str]]:
    """Return accepted result clauses and their endpoint checks."""

    if _case_record_claim(text):
        return []
    attribution = attribution or re.compile(r"\b(?:shows?|records?|recorded|confirms?|contains?|lists?|says?)\b", re.I)
    question_or_condition = question_or_condition or re.compile(
        r"\b(?:ask(?:ed)?|check(?:ed)?|whether|if|could|would|might|please)\b", re.I
    )
    results: list[tuple[str, str]] = []
    for clause in _result_clauses(text):
        low = clause.casefold()
        tariff_result = not question_or_condition.search(clause) and (
            bool(
                re.search(r"\b(?:fee|charge)\b.{0,100}\bmatch(?:es|ed)?\b", low)
                and re.search(r"\b(?:tariff|entry)\b", low)
            )
            or bool(re.search(r"\b(?:fee|charge)\b.{0,100}\b(?:mismatch|does\s+not\s+match)\b", low))
        )
        if (
            "?" in clause
            or re.match(
                r"^(?:do|does|did|is|are|was|were|has|have|had|can|will|shall|should)\b",
                clause.lstrip(" '\"“"),
                re.I,
            )
            or (question_or_condition.search(clause) and not tariff_result)
        ):
            continue
        if re.search(r"\bqueue\b", low) and re.search(
            r"\bshows?\b.{0,80}\b(?:second\s+consent|second\s+signator\w*)\b", low
        ):
            results.append(("business", clause))
            continue
        endpoint = _endpoint_check(clause)
        if endpoint is None and tariff_result:
            results.append(("tariff", clause))
            continue
        if endpoint is None:
            continue
        if endpoint == "tariff" and tariff_result:
            results.append((endpoint, clause))
            continue
        found_entry = re.search(r"\bfound\b.{0,80}\b(?:entry|record)\b.{0,40}\brecord(?:ing|ed)\b", clause, re.I)
        if found_entry or attribution.search(clause):
            results.append((endpoint, clause))
    return results


def _quoted_answer_check(event: _Event) -> str | None:
    """Find a system named in an internal note written to a case record."""

    if _kind(event) != "system":
        return None
    recipient = str(event.event.get("to", "")).casefold()
    if "case record" not in recipient and "case journal" not in recipient:
        return None
    return _case_record_result(event.text)


def _is_case_record(event: _Event) -> bool:
    recipient = str(event.event.get("to", "")).casefold()
    return "case record" in recipient or "case journal" in recipient


def _references(text: str) -> set[str]:
    return {value.casefold() for value in (*_REFERENCE.findall(text), *_FILE.findall(text))}


def _case_record_has_result(text: str, check: str) -> bool:
    """Accept a case-record result only when the note attributes it to a record."""

    return _case_record_result(text) == check


def _portal_domain(text: str) -> str | None:
    """Identify one explicit status domain in a trusted portal answer.

    Bare words such as ``case``, ``report`` and ``review`` are deliberately
    ignored.  Distinct structured status domains in one answer are ambiguous.
    """

    domains: set[str] = set()
    for clause in _result_clauses(text):
        low = clause.casefold()
        card = bool(
            re.search(r"\bcard(?:\s+payment)?\s+(?:status|stage)\b", low)
            or re.search(
                r"\bcard\b.{0,80}\b(?:temporarily\s+unavailable|blocked|restricted|declined|dispatched|manufactur\w*)\b",
                low,
            )
            or re.search(r"\bstatus\b.{0,80}\bcard\b", low)
        )
        if card:
            domains.add("card")

        if re.search(
            r"\b(?:incoming\s*(?:-| )?payment|incoming\s+credit)\b.{0,80}"
            r"\b(?:status|found|received|located|identified|recorded)\b",
            low,
        ):
            domains.add("incoming")

        if re.search(
            r"\b(?:validation\s+status|validation)\b.{0,100}\b(?:failed|available|ready|error|invalid)\b"
            r"|\bbatch\b.{0,100}\bvalidation\b",
            low,
        ) or re.search(
            r"\b(?:role|permission\w*|limit|maximum|max)\b.{0,80}"
            r"\b(?:status|is|was|set|allowed|revoked|pending|available|failed|\d)\b",
            low,
        ):
            domains.add("business")

        if re.search(
            r"\b(?:standing[- ]order|mandate|direct\s+debit)\b.{0,80}"
            r"\b(?:status|active|cancelled|next\s+(?:scheduled\s+)?run|date)\b"
            r"|\b(?:status|next\s+(?:scheduled\s+)?run)\b.{0,80}\b(?:standing[- ]order|mandate)\b",
            low,
        ):
            domains.add("recurring")

        if re.search(
            r"\b(?:access|password|pin|recovery)\b.{0,80}"
            r"\b(?:status|restored|available|linked|started|provided|ready)\b"
            r"|\b(?:status|restored)\b.{0,80}\baccess\b",
            low,
        ):
            domains.add("access")

        if re.search(
            r"\bstatement\b.{0,80}\b(?:status|ready|available|placed|generated)\b"
            r"|\b(?:document|export)\b.{0,80}\b(?:status|ready|available|placed|generated|created)\b",
            low,
        ):
            domains.add("documents")

        if re.search(
            r"\b(?:registration|registered|register(?:ed)?\s+request)\b.{0,80}"
            r"\b(?:status|received|logged|review|under)\b"
            r"|\b(?:request|review)\b.{0,80}\b(?:registered|logged|received)\b",
            low,
        ):
            domains.add("registration")

        payment = bool(
            re.search(r"\b(?:transfer|instruction)\s+status\b", low)
            or (
                re.search(r"\bpayment\s+status\b", low)
                and not re.search(r"\b(?:card|incoming)\s+payment\s+status\b", low)
            )
            or re.search(r"\brow\s+[a-z]{2,8}-\d+\b.{0,60}\bstatus\b", low)
        )
        if payment:
            domains.add("payment")

    return next(iter(domains)) if len(domains) == 1 else None


def _portal_matches(text: str, check: str) -> bool:
    return _portal_domain(text) == check


def _records(ctx: Context, check: str) -> list[_Record]:
    events = _events(ctx)
    requests: list[tuple[str, str | None, _Event]] = []
    records: list[_Record] = []
    for current in events:
        found = _event_check(current, ctx.case)
        if found is not None:
            requests.append((found, _endpoint_identity(current.event.get("to"), found), current))
            continue
        quoted_check = _quoted_answer_check(current)
        case_record_fallback = False
        answer_check = _answer_check(current, ctx.case) or quoted_check
        portal_match: tuple[str, str | None] | None = None
        portal_channel = _channel(current.event.get("channel")) in {"secure_portal", "business_portal"}
        if answer_check is None and _kind(current) == "system" and _bank_sender(current, ctx.case) and portal_channel:
            answer_refs = _references(current.text)
            portal_candidates: list[tuple[str, str | None]] = []
            for requested, request_identity, request in requests:
                if (
                    answer_refs
                    and answer_refs.intersection(_references(request.text))
                    and _portal_matches(current.text, requested)
                ):
                    portal_candidates.append((requested, request_identity))
            if len(portal_candidates) == 1:
                portal_match = portal_candidates[0]
                answer_check = portal_match[0]
        if (
            answer_check is None
            and _kind(current) == "system"
            and _is_case_record(current)
            and len(requests) == 1
            and _case_record_has_result(current.text, requests[0][0])
        ):
            answer_check = requests[0][0]
            case_record_fallback = True
        if answer_check is None:
            continue
        self_contained = _self_contained_answer_check(current, ctx.case)
        if self_contained is not None and not requests:
            records.append(_Record(self_contained, current, current, _system_name(current, self_contained)))
            continue
        if (
            answer_check != "registration"
            and re.search(r"\b(?:register(?:ed)?|registration|request)\b", current.text, re.I)
            and any(requested == "registration" for requested, _, _ in requests)
        ):
            answer_check = "registration"
        answer_source = current.event.get("from")
        answer_identity = _endpoint_identity(answer_source, answer_check)
        if quoted_check is not None:
            quoted_requests = [
                (request_identity, request)
                for requested, request_identity, request in requests
                if requested == quoted_check
            ]
            if len(quoted_requests) == 1:
                answer_identity = quoted_requests[0][0]
        elif self_contained is not None:
            answer_identity = _endpoint_identity(current.event.get("to"), self_contained)
        if case_record_fallback:
            answer_identity = requests[0][1]
        elif portal_match is not None:
            answer_identity = portal_match[1]
        else:
            for requested, request_identity, _ in requests:
                if requested != answer_check and _endpoint_identity(answer_source, requested) == request_identity:
                    answer_check = requested
                    answer_identity = request_identity
                    break
        for position, (requested, request_identity, request) in enumerate(requests):
            if requested == answer_check and request_identity == answer_identity:
                records.append(_Record(requested, request, current, _system_name(current, requested)))
                requests.pop(position)
                break
    records.extend(_Record(found, request, None, _system_name(request, found)) for found, _, request in requests)
    return [record for record in records if record.check == check]


def _note(ctx: Context, event: _Event, text: str | None = None, label: str | None = None) -> None:
    source = label or _system_name(event)
    location = "initial request" if event.position == 0 else f"event {event.seq}"
    ctx.note(f"{location} ({source}): {event.text if text is None else text}")


def _begin_evidence(ctx: Context) -> None:
    ctx.__dict__["_track_evidence"] = {}


def _finish_evidence(ctx: Context) -> None:
    evidence = getattr(ctx, "_track_evidence", {})
    try:
        for event, label, names in evidence.values():
            facts = ", ".join(f"{name}={value!r}" for name, value in names)
            _note(ctx, event, text=f"{event.text} [facts: {facts}]", label=label)
    finally:
        if hasattr(ctx, "_track_evidence"):
            delattr(ctx, "_track_evidence")


def _with_evidence(fn: Any) -> Any:
    @wraps(fn)
    def wrapped(ctx: Context, *args: Any, **kwargs: Any) -> Any:
        _begin_evidence(ctx)
        try:
            return fn(ctx, *args, **kwargs)
        finally:
            _finish_evidence(ctx)

    return wrapped


def _record(ctx: Context, out: dict[str, Any], name: str, value: Any, event: _Event, label: str | None = None) -> None:
    out[name] = value
    evidence = getattr(ctx, "_track_evidence", None)
    if evidence is None:
        _note(ctx, event, label=label)
        return
    key = (event.position, label or _system_name(event))
    if key not in evidence:
        evidence[key] = [event, label or _system_name(event), []]
    evidence[key][2].append((name, value))


def _answer_text(record: _Record) -> str:
    if record.answer is None:
        return ""
    if _is_case_record(record.answer):
        clauses = _case_record_answer_clauses(record.answer.text)
        selected = [clause for check, clause in clauses if check == record.check]
        if selected:
            return " ".join(selected)
    return record.answer.text


def _first_money(text: str, *, last: bool = False) -> str | None:
    matches = _money_matches(text)
    if not matches:
        return None
    match = matches[-1] if last else matches[0]
    return _money_match_value(match)


def _money_matches(text: str) -> list[re.Match[str]]:
    matches = list(_MONEY.finditer(text)) + list(_NAMED_MONEY.finditer(text))
    unique: dict[tuple[int, int], re.Match[str]] = {}
    for match in matches:
        unique[(match.start(), match.end())] = match
    return sorted(unique.values(), key=lambda match: match.start())


def _money_match_value(match: re.Match[str]) -> str | None:
    try:
        value = Decimal(match.group(1).replace(",", ""))
    except InvalidOperation:
        return None
    return f"{value:.2f}" if value.is_finite() else None


def _subject_amount(text: str) -> str | None:
    """Prefer the requested/recorded amount over an incidental old amount."""

    matches = _money_matches(text)
    if not matches:
        return None
    scored: list[tuple[int, int, str]] = []
    previous_end = 0
    for match in matches:
        value = _money_match_value(match)
        if value is None:
            continue
        # Context from a previous amount must not also describe the next one:
        # "from £42 to £68" associates "from" with 42 and "to" with 68.
        before = text[max(previous_end, match.start() - 90) : match.start()].casefold()
        before = re.split(r"[.!?;\n]", before)[-1]
        previous_end = match.end()
        score = 0
        if re.search(
            r"\b(?:to|into|target|set|new|actual|final|sent|completed|credited|received|total|amount|value|limit|maximum|max)\b",
            before,
        ):
            score += 3
        if re.search(
            r"\b(?:from|current|currently|old|previous|draft|remember|memory|existing)\b|portal\s+still\s+shows",
            before,
        ):
            score -= 3
        if re.search(r"\b(?:change|increase|decrease|updated|amend)\w*\b", before):
            score += 1
        scored.append((score, -match.start(), value))
    return max(scored)[2] if scored else None


def _date_value(text: str) -> str | None:
    iso = _DATE_ISO.search(text)
    if iso:
        try:
            return date(int(iso.group(1)), int(iso.group(2)), int(iso.group(3))).isoformat()
        except ValueError:
            return None
    long_date = _DATE_LONG.search(text)
    if long_date:
        try:
            month = _MONTHS.index(long_date.group(2).casefold()) + 1
            return date(int(long_date.group(3)), month, int(long_date.group(1))).isoformat()
        except ValueError:
            return None
    return None


_BANK_NAME_WORDS = ("agent", "service", "team", "system", "journal", "bank", "portal", "support", "h&v")


def _is_bank_name(value: Any, case: Mapping[str, Any]) -> bool:
    details = case.get("details")
    bank = str(details.get("Bank", "")) if isinstance(details, Mapping) else ""
    low = str(value).casefold()
    return bool(bank and bank.casefold() in low) or any(word in low for word in _BANK_NAME_WORDS)


def _customer_events(events: list[_Event], case: Mapping[str, Any]) -> list[_Event]:
    result: list[_Event] = []
    for event in events:
        if _kind(event) != "conversation":
            continue
        sender = str(event.event.get("from", ""))
        receiver = str(event.event.get("to", ""))
        sender_is_bank = _is_bank_name(sender, case)
        receiver_is_bank = _is_bank_name(receiver, case)
        if not sender_is_bank and (receiver_is_bank or not receiver):
            result.append(event)
    return result


def _bank_sender(event: _Event, case: Mapping[str, Any]) -> bool:
    return _is_bank_name(event.event.get("from", ""), case)


def _request_text(ctx: Context, events: list[_Event]) -> str:
    request = ctx.case.get("request", "")
    parts = [str(request)] if isinstance(request, str) else []
    parts.extend(event.text for event in _customer_events(events, ctx.case))
    return "\n".join(part for part in parts if part)


def _initial_request(ctx: Context) -> _Event:
    return _Event(0, {"text": str(ctx.case.get("request", ""))})


def _money_in_text(text: str, value: str) -> bool:
    return any(_money_match_value(match) == value for match in _money_matches(text))


def _fact_source(
    ctx: Context,
    customer: list[_Event],
    *,
    value: str | None = None,
    token: str | None = None,
    date_value: str | None = None,
) -> _Event:
    for event in [*customer, _initial_request(ctx)]:
        if (
            (value is not None and _money_in_text(event.text, value))
            or (token is not None and token.casefold() in event.text.casefold())
            or (date_value is not None and _date_value(event.text) == date_value)
        ):
            return event
    return _initial_request(ctx)


def _verification_complete(event: _Event) -> bool:
    text = event.text.casefold().replace("\u2019", "'")
    pattern = (
        r"\b(?:identity|identification) checks?\s+(?:(?:are|were|have been|have)\s+)?completed?\b|"
        r"\bcompleted?\s+(?:(?:[\w&'-]+)\s+){0,4}(?:identity|identification) checks?\b"
    )
    return any(not _negated_at(text, match.start()) for match in re.finditer(pattern, text))


def _role(details: Mapping[str, Any], text: str) -> str:
    low = text.casefold().replace("\u2019", "'")
    if re.search(
        r"\b(?:i(?:'m| am)|as a)\s+(?:the\s+)?(?:company(?:'s)?\s+)?(?:authori[sz]ed\s+)?(?:file\s+)?uploader\b",
        low,
    ):
        return "uploader"
    if re.search(
        r"\b(?:i(?:'m| am)|as a)\s+(?:the\s+)?(?:company\s+)?(?:authori[sz]ed\s+)?(?:business )?signatory\b", low
    ):
        return "signatory"
    if re.search(
        r"\b(?:i(?:'m| am))\s+(?:the\s+)?(?:an?\s+)?(?:verified\s+)?"
        r"(?:authori[sz]ed\s+)?(?:business )?(?:administrator|admin)\b",
        low,
    ):
        return "business_admin"
    if re.search(r"\b(?:i(?:'m| am))\s+(?:an?\s+)?employee\b", low):
        return "employee"
    if re.search(r"\b(?:i(?:'m| am)|as a)\s+(?:an?\s+)?(?:authori[sz]ed\s+)?viewer\b", low) or re.search(
        r"\b(?:i(?:'m| am))\s+(?:authori[sz]ed\s+)?to\s+view\b", low
    ):
        return "viewer"
    if re.search(r"\b(?:i(?:'m| am)|as a)\s+(?:an?\s+)?third party\b", low):
        return "third_party"
    source = str(details.get("Source role", "")).casefold()
    if "administrator" in source or re.search(r"\badmin\b", source):
        return "business_admin"
    if "third" in source:
        return "third_party"
    if "employee" in source:
        return "employee"
    if "uploader" in source:
        return "uploader"
    if "signatory" in source:
        return "signatory"
    if "viewer" in source:
        return "viewer"
    return "customer"


def _channel(value: Any) -> str | None:
    return {
        "secure portal": "secure_portal",
        "secure chat": "secure_chat",
        "verified call": "verified_call",
        "business portal": "business_portal",
        "external message": "external_message",
    }.get(str(value).strip().casefold())


@function
@_with_evidence
def identify_requester(ctx: Context) -> dict[str, Any]:
    events = _events(ctx)
    customer = _customer_events(events, ctx.case)
    if not customer:
        return {}
    latest = customer[-1]
    details = ctx.case.get("details")
    details_map = details if isinstance(details, Mapping) else {}
    history_text = "\n".join(event.text for event in customer)
    out: dict[str, Any] = {}
    _record(ctx, out, "requester", str(latest.event.get("from", "")), latest)
    _record(ctx, out, "role", _role(details_map, history_text), latest)
    channel = _channel(latest.event.get("channel"))
    if channel is not None:
        _record(ctx, out, "channel", channel, latest)
        verified = channel in {"verified_call", "secure_portal", "business_portal"}
        verification_event = next(
            (
                event
                for event in events
                if _kind(event) in {"conversation", "system"}
                and _bank_sender(event, ctx.case)
                and _verification_complete(event)
            ),
            None,
        )
        if verification_event is not None:
            verified = True
        _record(ctx, out, "verified", verified, verification_event or latest)
    return out


def _counterparty(text: str) -> str | None:
    patterns = (
        r"\bto\s+([A-Z][^.!?\n,]+?)(?=\s+(?:on|dated|for|under|and|but|has|was|is|checked|please|need|in|from|said|so|that|which|whether)\b|[,.!?]|$)",
        r"\bmerchant\s*[:\-]?\s*([A-Z][^.!?\n,]+)",
        r"\bpayer\s*[:\-]?\s*([A-Z][^.!?\n,]+)",
        r"\bfrom\s+([A-Z][^.!?\n,]+?)(?=\s+(?:has|said|sent|made|by|to|for|in)\b|[,.!?]|$)",
    )
    for pattern in patterns:
        found = re.search(pattern, text)
        if found:
            value = re.sub(r"\s+", " ", found.group(1)).strip(" \"'")
            if value and value.casefold() not in {"my account", "the bank", "h&v"}:
                return value
    return None


@function
@_with_evidence
def find_subject(ctx: Context) -> dict[str, Any]:
    events = _events(ctx)
    text = _request_text(ctx, events)
    if not text.strip():
        return {}
    customer = _customer_events(events, ctx.case)
    out: dict[str, Any] = {}
    amount = _subject_amount(text)
    if amount is not None:
        _record(ctx, out, "amount", amount, _fact_source(ctx, customer, value=amount))
    counterparty = _counterparty(text)
    if counterparty is not None:
        _record(ctx, out, "counterparty", counterparty, _fact_source(ctx, customer, token=counterparty))
    reference = _REFERENCE.search(text) or _FILE.search(text)
    if reference is not None:
        _record(
            ctx,
            out,
            "reference",
            reference.group(0),
            _fact_source(ctx, customer, token=reference.group(0)),
        )
    subject_date = _date_value(text)
    if subject_date is not None:
        _record(ctx, out, "subject_date", subject_date, _fact_source(ctx, customer, date_value=subject_date))
    return out


def _negated_at(text: str, start: int) -> bool:
    prefix = text[max(0, start - 80) : start]
    return bool(
        re.search(
            r"\b(?:no|not|never|without|doesn't|didn't|hasn't|haven't|"
            r"does\s+not|did\s+not|has\s+not|have\s+not|is\s+not|was\s+not|are\s+not|were\s+not)\b"
            r"(?:\W+\w+){0,5}\s*$",
            prefix,
            re.I,
        )
    )


def _status(ctx: Context, text: str, values: Mapping[str, tuple[str, ...]]) -> str:
    low = text.casefold()
    for value, words in values.items():
        for pattern in words:
            for match in re.finditer(pattern, low):
                if not _negated_at(low, match.start()):
                    return value
    classify = getattr(ctx, "classify", None)
    if callable(classify):
        try:
            answer = classify(
                text,
                {
                    "status": Choice(
                        "Choose a listed status only when the single system answer clearly states it; otherwise OTHER.",
                        {name: name for name in (*values, "OTHER")},
                    )
                },
            ).get("status")
        except CaseError:
            answer = None
        raw = getattr(answer, "value", answer)
        normalized = str(raw).upper() if raw is not None else ""
        if normalized in values or normalized == "OTHER":
            return normalized
    return "OTHER"


def _payment_count(text: str) -> int | None:
    match = re.search(
        r"\b(\d+|one|two|three|four|five)\s+(?:(?:distinct|separate)\s+)?"
        r"(?:(?:payments?|transfers?)|(?:instructions?(?:\s+references?)?))\b",
        text,
        re.I,
    )
    if match is None:
        if re.search(
            r"\b(?:separate|distinct)\s+instruction\s+records?\b"
            r".{0,100}\b(?:one|a)\b.{0,100}\band\s+(?:one|a)\b",
            text,
            re.I,
        ):
            return 2
        return None
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    raw = match.group(1).casefold()
    count = words.get(raw, int(raw) if raw.isdigit() else None)
    if count is not None:
        return count
    return None


def _status_mentions(text: str, values: Mapping[str, tuple[str, ...]]) -> set[str]:
    found: set[str] = set()
    low = text.casefold()
    for value, words in values.items():
        for pattern in words:
            if any(not _negated_at(low, match.start()) for match in re.finditer(pattern, low)):
                found.add(value)
                break
    return found


def _reason(text: str) -> str | None:
    match = re.search(
        r"\b(?:reason|permitted\s+(?:customer-facing\s+)?wording|permitted\s+category)\s*"
        r"(?:is|:)?\s*[\"“]?([^.!?\n]+(?:[.!?])?)[\"”]?",
        text,
        re.I,
    )
    if match:
        return match.group(1).strip(" \"'“”")
    match = re.search(r"\bbecause\s+([^.!?\n]+(?:[.!?])?)", text, re.I)
    return match.group(1).strip() if match else None


def _system_facts(ctx: Context, check: str) -> tuple[_Record, str] | None:
    records = _records(ctx, check)
    if not records:
        return None
    # the latest request is the one that stands: an order placed after "available to order" (032)
    record = max(records, key=lambda r: _seq_key(r.request.seq))
    return record, _answer_text(record)


def _asked(ctx: Context, check: str, name: str) -> tuple[dict[str, Any], _Record] | None:
    found = _system_facts(ctx, check)
    if found is None:
        return None
    record, _ = found
    out = {name: True}
    _record(ctx, out, name, True, record.request, label=record.label)
    return out, record


def _system_start(ctx: Context, check: str, asked_name: str) -> tuple[dict[str, Any], _Record, str] | None:
    found = _system_facts(ctx, check)
    if found is None:
        return None
    record, answer = found
    out, _ = _asked(ctx, check, asked_name) or ({}, record)
    return out, record, answer


@function
@_with_evidence
def check_payment(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "payment", "payment_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    payment_values = {
        "SENT": (
            r"\bmarked?\s+as\s+sent\b",
            r"\bstatus\s*(?:is|:)\s*[\"“]?sent\b",
            r"(?<!not )(?<!never )\bsent\b",
        ),
        "PENDING": (r"\bpending\b",),
        "AWAITING_AUTHORISATION": (r"awaiting.{0,30}authori[sz]", r"awaiting.{0,30}consent"),
        "DECLINED": (r"\bdeclined\b",),
        "REJECTED": (r"\brejected\b",),
        "CANCELLED": (r"\bcancell?ed\b",),
        "NOT_EXECUTED": (r"\bnot\s+(?:been\s+)?completed\b", r"\bnot\s+executed\b", r"did not execute"),
        "COMPLETED": (r"(?<!not\s)\bcompleted\b", r"\bpayment\s+complete\b"),
    }
    count = _payment_count(answer)
    status = _status(ctx, answer, payment_values)
    if count is not None and len(_status_mentions(answer, payment_values)) > 1:
        status = "OTHER"
    _record(ctx, out, "payment_status", status, record.answer)
    reason = _reason(answer)
    if reason is not None:
        _record(ctx, out, "payment_reason", reason, record.answer)
    if count is not None:
        _record(ctx, out, "payment_count", count, record.answer)
    return out


@function
@_with_evidence
def check_incoming(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "incoming", "incoming_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    low = answer.casefold()
    if re.search(r"\b(?:no|not|without|never)\b.{0,40}\b(?:incoming payment|payment|credit)\b", low) or re.search(
        r"\bnot found\b", low
    ):
        _record(ctx, out, "incoming_found", False, record.answer)
    elif re.search(r"(?<!not )\b(?:found|received|located|recorded|identified)\b", low):
        _record(ctx, out, "incoming_found", True, record.answer)
    amount = _first_money(answer)
    if amount is not None and out.get("incoming_found") is True:
        _record(ctx, out, "incoming_amount", amount, record.answer)
    return out


@function
@_with_evidence
def check_recurring(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "recurring", "recurring_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    _record(
        ctx,
        out,
        "recurring_status",
        _status(
            ctx,
            answer,
            {
                "CANCELLED": (r"\bcancell?ed\b",),
                "ACTIVE": (r"(?<!not )\bactive\b", r"\benabled\b"),
                "NOT_EXECUTED": (r"not\s+(?:been\s+)?executed", r"did not run", r"not\s+(?:been\s+)?run"),
                "AMENDED": (r"\bamended\b", r"\bupdated\b", r"\bchanged\b"),
            },
        ),
        record.answer,
    )
    next_marker = re.search(
        r"\b(?:next\s+(?:scheduled\s+)?(?:run|payment)|scheduled\s+run\s+date|run\s+date)\b", answer, re.I
    )
    value = _date_value(answer[next_marker.end() :]) if next_marker else None
    if value is not None:
        _record(ctx, out, "next_run", value, record.answer)
    return out


@function
@_with_evidence
def check_card(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "card", "card_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    _record(
        ctx,
        out,
        "card_status",
        _status(
            ctx,
            answer,
            {
                "IN_MANUFACTURE": (r"in\s+manufactur", r"being\s+made"),
                "DISPATCHED": (
                    r"(?<!not )dispatch(?:ed|\s+status\s*:\s*registered)",
                    r"(?<!not )sent\s+for\s+delivery",
                ),
                "BLOCKED": (r"\bblocked\b",),
                "RESTRICTED": (r"\brestricted\b", r"\bpermitted category:\s*[^.!?\n]*\brestriction\b"),
                "DECLINED": (r"\bdeclined\b",),
                "REQUESTED": (r"request(?:ed)?\b", r"accepted\b", r"received\b"),
            },
        ),
        record.answer,
    )
    reason = _reason(answer)
    if reason is not None:
        _record(ctx, out, "card_reason", reason, record.answer)
    return out


@function
@_with_evidence
def check_access(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "access", "access_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    _record(
        ctx,
        out,
        "access_status",
        _status(
            ctx,
            answer,
            {
                "AWAITING_CONFIRMATION": (r"awaiting.{0,25}confirmation",),
                "PROCEDURE_STARTED": (r"procedure\s+started", r"process\s+started"),
                "EXTRACT_PROVIDED": (r"extract\s+(?:has\s+been\s+)?provided", r"provided\s+extract"),
                "RESTORED": (r"\brestored\b", r"access\s+is\s+back"),
                "LINKED": (r"\blinked\b",),
            },
        ),
        record.answer,
    )
    return out


@function
@_with_evidence
def check_business(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "business", "business_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    _record(
        ctx,
        out,
        "business_status",
        _status(
            ctx,
            answer,
            {
                "VALIDATION_FAILED": (
                    r"validation\s+(?:has\s+)?failed",
                    r"failed\s+validation",
                    r"validation\s+status\s*:\s*failed",
                ),
                "AWAITING_SECOND_SIGNATORY": (r"awaiting.{0,30}second\s+signatory", r"no\s+second\s+consent"),
                "PENDING_APPROVAL": (r"pending\s+approval", r"awaiting\s+approval"),
                "ROLE_REVOKED": (
                    r"role\s+(?:was\s+)?revoked",
                    r"revoked\s+role",
                    r"revocation\s+(?:instruction\s+)?processed",
                ),
                "RECEIVED": (r"\breceived\b", r"receipt\s+confirmed", r"recording\s+receipt"),
            },
        ),
        record.answer,
    )
    amount = _first_money(answer)
    if amount is not None and re.search(r"\b(?:limit|maximum|max)\b", answer, re.I):
        _record(ctx, out, "business_limit", amount, record.answer)
    return out


@function
@_with_evidence
def check_documents(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "documents", "documents_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    low = answer.casefold()
    if re.search(r"\bavailable\s+to\s+order\b|\b(?:can|may)\s+be\s+ordered\b", low) or re.search(
        r"\b(?:not|no)\b.{0,30}\b(?:available|ready|found|placed|generated|created)\b", low
    ):
        _record(ctx, out, "document_ready", False, record.answer)
    elif re.search(r"\b(?:available|ready|placed|provided|generated|created)\b", low):
        _record(ctx, out, "document_ready", True, record.answer)
    if out.get("document_ready") is True:
        attachments = ctx.case.get("attachments")
        available: list[str] = []
        if isinstance(attachments, Sequence) and not isinstance(attachments, (str, bytes, bytearray)):
            available = [
                attachment["name"]
                for attachment in attachments
                if isinstance(attachment, Mapping) and isinstance(attachment.get("name"), str)
            ]
        file_match = _FILE.search(answer)
        if file_match is not None:
            matched = next((name for name in available if name.casefold() == file_match.group(0).casefold()), None)
            if matched is not None:
                _record(ctx, out, "document_name", matched, record.answer)
        elif available:
            _record(ctx, out, "document_name", available[0], record.answer)
    return out


@function
@_with_evidence
def check_tariff(ctx: Context) -> dict[str, Any]:
    """Read a fee review against the tariff in force for the transaction."""

    started = _system_start(ctx, "tariff", "tariff_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    tariff_status = (
        "OTHER"
        if "?" in answer or re.search(r"\b(?:please|whether|if|could|might|would)\b", answer, re.I)
        else _status(
            ctx,
            answer,
            {
                "MISMATCH": (
                    r"\b(?:fee|charge)\b.{0,100}\b(?:mismatch|does\s+not\s+match|is\s+incorrect)\b",
                    r"\b(?:mismatch|does\s+not\s+match)\b",
                ),
                "MATCHES": (
                    r"\b(?:fee|charge)\b.{0,100}\bmatch(?:es|ed)?\b.{0,80}\b(?:tariff|entry)\b",
                    r"\bmatch(?:es|ed)?\s+the\s+(?:applicable\s+)?(?:tariff|entry)\b",
                ),
            },
        )
    )
    _record(
        ctx,
        out,
        "tariff_status",
        tariff_status,
        record.answer,
    )
    return out


@function
@_with_evidence
def check_registration(ctx: Context) -> dict[str, Any]:
    started = _system_start(ctx, "registration", "registration_asked")
    if started is None:
        return {}
    out, record, answer = started
    if record.answer is None:
        return out
    low = answer.casefold()
    if re.search(r"\b(?:not|never)\s+registered\b", low) or re.search(r"\brejected\b", low):
        registered = False
    elif re.search(r"\bregistered\b", low) or re.search(
        r"\b(?:received|logged|opened)\b.{0,30}\b(?:review|request)\b", low
    ):
        registered = True
    else:
        return out
    _record(ctx, out, "registered", registered, record.answer)
    reference = _REFERENCE.search(answer)
    if reference is not None:
        _record(ctx, out, "registration_ref", reference.group(0), record.answer)
    return out


def _confirmation_classification(ctx: Context, text: str) -> str | None:
    classify = getattr(ctx, "classify", None)
    if not callable(classify):
        return None
    try:
        answer = classify(
            text,
            {
                "confirmation": Choice(
                    "Classify this secure-portal message as an affirmative confirmation of the pending change.",
                    {
                        "GIVEN": "The customer affirmatively approves or confirms the pending change.",
                        "NOT_GIVEN": "The customer declines, withholds, questions, or does not yet confirm it.",
                        "OTHER": "The message does not establish an affirmative confirmation.",
                    },
                )
            },
        ).get("confirmation")
    except CaseError:
        return None
    raw = getattr(answer, "value", answer)
    value = str(raw).upper() if raw is not None else ""
    return value if value in {"GIVEN", "NOT_GIVEN", "OTHER"} else "OTHER"


def _receipt_acknowledgement(text: str) -> bool:
    return bool(
        re.search(
            r"\bconfirm(?:ed)?\s+(?:receipt|receiving)\b|"
            r"\bconfirm(?:ed)?\s+(?:your|the)\s+message\b",
            text,
            re.I,
        )
    )


def _protected_change_start(event: _Event, case: Mapping[str, Any]) -> bool:
    if _kind(event) != "system":
        return False
    destination = str(event.event.get("to", ""))
    if not _bank_sender(event, case) or not _profile_change_process_key(destination):
        return False
    for clause in _result_clauses(event.text.casefold().replace("\u2019", "'")):
        if "?" in clause or re.search(r"\b(?:please|should|could|would|will|may|might|if|when|unless|once)\b", clause):
            continue
        if re.search(
            r"^(?:i|we)\s+(?:(?:have|has)\s+)?(?:started|opened|initiated)\b"
            r"|^(?:i|we)\s+(?:am|are)\s+opening\b"
            r"|^i'm\s+opening\b",
            clause,
        ):
            return True
    return False


def _profile_change_process_key(value: Any) -> str | None:
    return "profile-change-process" if re.search(r"\bprofile[- ]change\s+process\b", str(value), re.I) else None


def _confirmation_processing_event(event: _Event, candidate: _Event, case: Mapping[str, Any]) -> bool:
    if _kind(event) != "system":
        return False
    sender = str(event.event.get("from", ""))
    recipient = str(event.event.get("to", ""))
    if (
        not _bank_sender(event, case)
        or _endpoint_check(sender) is not None
        or not re.search(r"\b(?:agent|service|process|team)\b", sender, re.I)
        or not re.search(
            r"\b(?:protected\s+instruction|profile[- ]change|secure\s+profile[- ]change)\s+process\b"
            r"|\binstruction\s+log\b",
            recipient,
            re.I,
        )
    ):
        return False
    clauses = _result_clauses(event.text)
    candidate_sender = str(candidate.event.get("from", ""))
    candidate_tokens = [
        token.casefold() for token in re.findall(r"[A-Za-z][A-Za-z'-]+", candidate_sender) if len(token) > 1
    ]
    candidate_references = _references(candidate.text)

    def owner_matches(name: str) -> bool:
        owner_tokens = [token.casefold() for token in re.findall(r"[A-Za-z][A-Za-z'-]+", name) if len(token) > 1]
        if not owner_tokens or not candidate_tokens:
            return False
        if len(owner_tokens) == 1:
            return len(candidate_tokens) == 1 and owner_tokens[0] == candidate_tokens[0]
        return set(owner_tokens) == set(candidate_tokens)

    def unambiguous_previous_owner(index: int) -> bool:
        """Resolve a pronoun only against the immediately preceding clause."""

        if index == 0 or len(candidate_tokens) < 2:
            return False
        previous = clauses[index - 1]
        previous_low = previous.casefold()
        candidate_name = " ".join(candidate_tokens)
        if not re.search(rf"\b{re.escape(candidate_name)}\b", previous_low):
            return False
        named_people = re.findall(r"\b([A-Z][a-z]+\s+[A-Z][a-z]+)\b", previous)
        return len({" ".join(name.casefold().split()) for name in named_people}) == 1

    for index, clause in enumerate(clauses):
        low = clause.casefold()
        if not re.search(
            r"\b(?:submit\w*|record\w*|process\w*|accept\w*|apply\w*)\b"
            r".{0,70}\b(?:secure[- ]portal|portal)\b.{0,70}\bconfirm\w*\b",
            low,
        ):
            continue
        if re.search(r"\b(?:not|never|without|if|when|please|should|will|would|can|could|may|might)\b", low):
            continue
        if candidate_references and not candidate_references.intersection(_references(clause)):
            continue
        named_customers = [name for name in re.findall(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)[\u0027\u2019]s\b", clause)]
        if named_customers:
            if not any(owner_matches(name) for name in named_customers):
                continue
        elif not candidate_references:
            candidate_given = candidate_tokens[0] if candidate_tokens else ""
            direct_owner = candidate_sender.casefold() in low or (
                len(candidate_tokens) == 1
                and candidate_given
                and re.search(rf"\b{re.escape(candidate_given)}\b", low) is not None
            )
            pronoun_owner = re.search(r"\b(?:her|his|their)\b", low) is not None and unambiguous_previous_owner(index)
            if not direct_owner and not pronoun_owner:
                continue
        return True
    return False


@function
@_with_evidence
def check_confirmation(ctx: Context) -> dict[str, Any]:
    events = _events(ctx)
    conversations = [event for event in events if _kind(event) == "conversation"]
    if not conversations:
        return {}
    requested: _Event | None = None
    outside: _Event | None = None
    given: _Event | None = None
    protected_starts = [event for event in events if _protected_change_start(event, ctx.case)]
    unrequested_portal_confirmations: list[_Event] = []

    def is_given(text: str) -> bool:
        low = text.casefold().replace("\u2019", "'")
        if "?" in low or _receipt_acknowledgement(low) or re.match(r"\s*(?:how|where|when|can|do|does|is|are)\b", low):
            return False
        if re.search(
            r"\b(?:do|does|did)\s+not\s+(?:approve|confirm)|\b(?:don't|doesn't|didn't)\s+"
            r"(?:approve|confirm)|\b(?:not|never)(?:\s+yet)?\s+(?:approve\w*|confirm\w*)\b|"
            r"\b(?:haven't|have\s+not|has\s+not)\s+(?:yet\s+)?(?:approve\w*|confirm\w*)\b",
            low,
        ):
            return False
        if re.search(
            r"\b(?:will|would|can|may|might|plan(?:s)?\s+to|intend(?:s)?\s+to|going\s+to)\b"
            r".{0,40}\b(?:confirm|approv\w*)\b",
            low,
        ):
            return False
        return bool(
            re.search(r"(?:^|[.!]\s*)i\s+(?:(?:have|hereby|now)\s+)*(?:confirm(?:ed)?|approv(?:e|ed))\b", low)
            or re.fullmatch(r"\s*(?:confirmed|approved)[.!]?\s*", low)
            or re.search(r"\bi\b.{0,100}\b(?:confirm(?:ed)?|approv(?:e|ed))\b", low)
        )

    for event in conversations:
        low = event.text.casefold()
        channel = _channel(event.event.get("channel"))
        if (
            not _bank_sender(event, ctx.case)
            and channel in {"secure_chat", "external_message"}
            and re.search(r"\b(?:change|amend|update|increase|decrease|alter)\b", low)
        ):
            outside = outside or event
        if (
            _bank_sender(event, ctx.case)
            and channel == "secure_portal"
            and (
                re.search(r"\b(?:sent|send|presented|available).{0,50}\b(?:change|amendment)\b", low)
                or re.search(
                    r"\b(?:change|amendment|update)\b.{0,50}"
                    r"\b(?:for|awaiting|needs?|require\w*)\s+(?:your\s+)?confirm",
                    low,
                )
                or re.search(r"\b(?:please|kindly)\b.{0,30}\bconfirm\w*\b", low)
            )
        ):
            requested = requested or event
        if not _bank_sender(event, ctx.case) and channel == "secure_portal":
            if re.search(
                r"\b(?:do|does|did)\s+not\s+(?:approve|confirm)|\b(?:don't|doesn't|didn't)\s+"
                r"(?:approve|confirm)|\b(?:not|never)(?:\s+yet)?\s+(?:approve\w*|confirm\w*)\b|"
                r"\b(?:haven't|have\s+not|has\s+not)\s+(?:yet\s+)?(?:approve\w*|confirm\w*)\b",
                low,
            ):
                continue
            has_requested = requested is not None and _seq_key(event.seq) > _seq_key(requested.seq)
            has_protected_process = any(
                _seq_key(start.seq) < _seq_key(event.seq)
                and _profile_change_process_key(start.event.get("to"))
                == _profile_change_process_key(event.event.get("to"))
                for start in protected_starts
            )
            if not has_requested and not has_protected_process:
                if is_given(low):
                    unrequested_portal_confirmations.append(event)
                continue
            classification = _confirmation_classification(ctx, event.text)
            if (
                "?" not in low
                and not _receipt_acknowledgement(low)
                and (classification == "GIVEN" or (classification is None and is_given(low)))
            ):
                given = event

    for candidate in unrequested_portal_confirmations:
        if any(
            _seq_key(event.seq) > _seq_key(candidate.seq) and _confirmation_processing_event(event, candidate, ctx.case)
            for event in events
        ):
            classification = _confirmation_classification(ctx, candidate.text)
            if classification == "GIVEN" or (classification is None and is_given(candidate.text)):
                given = given or candidate
    out: dict[str, Any] = {}
    evidence = given or requested or outside or conversations[-1]
    confirmation = "given" if given is not None else "requested" if requested is not None else "none"
    _record(ctx, out, "confirmation", confirmation, evidence)
    _record(ctx, out, "instructed_outside_portal", outside is not None, outside or evidence)
    return out


def _field(ctx: Context, name: str) -> Any:
    return ctx.fields.get(name)


def _subject_description(ctx: Context) -> str:
    subject = _field(ctx, "subject")
    bits = [str(subject)] if subject is not None else []
    for name, prefix in (
        ("amount", "amount"),
        ("counterparty", "counterparty"),
        ("reference", "reference"),
        ("subject_date", "date"),
    ):
        value = _field(ctx, name)
        if value is not None:
            bits.append(f"{prefix}={value}")
    return ", ".join(bits)


@function
def ask_system(ctx: Context) -> dict[str, Any]:
    system = _field(ctx, "next_system")
    if system is None:
        return {}
    args: dict[str, Any] = {"system": system}
    subject = _field(ctx, "subject")
    if subject is not None:
        args["about"] = subject
    for name in ("reference", "amount"):
        value = _field(ctx, name)
        if value is not None:
            args[name] = str(value)
    ctx.act("ask_system", **args)
    return {}


@function
def register_request(ctx: Context) -> dict[str, Any]:
    team = _field(ctx, "next_system")
    if team is None:
        return {}
    args: dict[str, Any] = {"team": team}
    subject = _field(ctx, "subject")
    if subject is not None:
        args["about"] = subject
    reference = _field(ctx, "reference")
    if reference is not None:
        args["reference"] = str(reference)
    ctx.act("register_request", **args)
    return {}


@function
def send_for_confirmation(ctx: Context) -> dict[str, Any]:
    requester = _field(ctx, "requester")
    if requester is None:
        return {}
    change = _subject_description(ctx)
    if not change:
        return {}
    ctx.act("send_for_confirmation", change=change, to=requester)
    return {}


_ACCESS_LIMITATION = "This does not disclose or handle a password or PIN."


_LIMITATIONS = {
    "payment": {
        "SENT": "This does not confirm receipt or credit by the recipient bank.",
        "PENDING": "This does not establish that the payment will complete.",
        "AWAITING_AUTHORISATION": "This does not authorise the payment.",
        "COMPLETED": "This does not confirm receipt or credit by the recipient bank.",
        "DECLINED": "This does not establish a different cause or authorise a retry.",
        "REJECTED": "This does not establish a different cause or authorise a retry.",
        "CANCELLED": "This does not establish a refund or the recipient's outcome.",
        "NOT_EXECUTED": "This does not establish whether a later attempt will run.",
        "OTHER": "The answer does not establish a recognized payment status or the recipient's outcome.",
    },
    "incoming_found": {
        "true": "This does not establish the sender's payment status.",
        "false": "This does not establish that the sender did not pay.",
    },
    "recurring": {
        "ACTIVE": "This does not guarantee that the future payment will execute.",
        "CANCELLED": "This does not establish a refund or a future payment outcome.",
        "NOT_EXECUTED": "This does not establish whether a later run will execute.",
        "AMENDED": "This records the amendment but does not guarantee the next payment.",
        "OTHER": "The answer does not establish a recognized standing-order status.",
    },
    "card": {
        "REQUESTED": "This does not establish manufacture, dispatch, or receipt.",
        "IN_MANUFACTURE": "This does not establish dispatch or receipt.",
        "DISPATCHED": "This does not confirm that the customer has received the card.",
        "BLOCKED": "This does not establish why the card is blocked or whether it can be used.",
        "RESTRICTED": "This does not disclose the basis of the restriction.",
        "DECLINED": "This does not establish a different cause or authorise a retry.",
        "OTHER": "The answer does not establish a recognized card status.",
    },
    "access": {
        **dict.fromkeys(
            ("RESTORED", "AWAITING_CONFIRMATION", "LINKED", "PROCEDURE_STARTED", "EXTRACT_PROVIDED"),
            _ACCESS_LIMITATION,
        ),
        "OTHER": "This does not establish a password, PIN, or access change.",
    },
    "business": {
        "RECEIVED": "This does not establish that every row was paid or processed.",
        "VALIDATION_FAILED": "This does not establish that a corrected file was received or any payment was made.",
        "AWAITING_SECOND_SIGNATORY": "This does not approve the request for the second signatory.",
        "PENDING_APPROVAL": "This does not approve the request or authorise a signatory.",
        "ROLE_REVOKED": "This does not establish any other role or permission change.",
        "OTHER": "The answer does not establish a recognized business-record status.",
    },
    "document": {
        "ready": "This does not confirm that the document was downloaded or that funds were credited.",
        "not_ready": "This does not establish that the document is available.",
    },
    "tariff": {
        "MATCHES": (
            "This confirms the recorded fee matches the applicable tariff; "
            "it does not authorise a refund or account change."
        ),
        "MISMATCH": "This identifies a tariff discrepancy; it does not by itself authorise a refund or account change.",
        "OTHER": "The review does not establish whether the recorded fee matches the applicable tariff.",
    },
}


def _reply_text(ctx: Context) -> str | None:
    subject = _field(ctx, "subject")
    next_system = _field(ctx, "next_system")
    if subject is None or next_system is None:
        return None
    amount = _field(ctx, "amount")
    counterparty = _field(ctx, "counterparty")
    amount_text = f"£{amount}" if amount is not None else None
    detail = (
        f"{amount_text} transfer"
        if amount_text is not None and subject in {"transfer", "payment", "card_payment"}
        else str(subject).replace("_", " ")
    )
    if counterparty is not None:
        detail += f" to {counterparty}"
    status = _field(ctx, "payment_status")
    count = _field(ctx, "payment_count")
    if next_system == "payment" and count is not None and str(status) == "OTHER":
        return (
            f"The payment record shows {count} separate payment instructions. "
            "Their individual status is recorded without a single combined outcome. "
            "This does not establish execution or the recipient's outcome. No new transfer was made."
        )
    if next_system == "payment" and status is not None:
        if str(status) == "OTHER":
            shown = "an answer without a recognized payment status"
        else:
            shown = detail + f" as {str(status).lower()}"
        reason = _field(ctx, "payment_reason")
        if reason is not None:
            shown += f" (recorded reason: {reason})"
        if count is not None:
            shown += f"; {count} separate payment instructions"
        middle = _LIMITATIONS["payment"].get(
            str(status), "The record answer does not establish a recognized payment status."
        )
        return f"The payment record shows your {shown}. {middle} No new transfer was made."
    if next_system == "payment" and count is not None:
        return (
            f"The payment record shows {count} separate payment instructions. "
            "This does not establish their execution or the recipient's outcome. No new transfer was made."
        )
    if next_system == "incoming" and _field(ctx, "incoming_found") is not None:
        if _field(ctx, "incoming_found"):
            amount_text = f" of {_field(ctx, 'incoming_amount')}" if _field(ctx, "incoming_amount") is not None else ""
            return (
                f"The incoming-payment record shows an incoming payment{amount_text}. "
                f"{_LIMITATIONS['incoming_found']['true']} No payment was changed."
            )
        return (
            "The incoming-payment record shows no incoming payment found. "
            f"{_LIMITATIONS['incoming_found']['false']} No payment was made."
        )
    recurring = _field(ctx, "recurring_status")
    if next_system == "recurring" and recurring is not None:
        next_run = _field(ctx, "next_run")
        next_text = f"; next run {next_run}" if next_run is not None else ""
        middle = _LIMITATIONS["recurring"].get(
            str(recurring), "The record answer does not establish a recognized standing-order status."
        )
        action = "No additional instruction or change was made."
        return f"The standing-order record shows {str(recurring).lower()}{next_text}. {middle} {action}"
    next_run = _field(ctx, "next_run")
    if next_system == "recurring" and next_run is not None:
        return (
            f"The standing-order record shows the next run as {next_run}. "
            "This does not guarantee that the future payment will execute. No change was made."
        )
    card = _field(ctx, "card_status")
    if next_system == "card" and card is not None:
        reason = _field(ctx, "card_reason")
        reason_text = f" (recorded reason: {reason})" if reason is not None else ""
        middle = _LIMITATIONS["card"].get(str(card), "The record answer does not establish a recognized card status.")
        return f"The card journal shows {str(card).lower()}{reason_text}. {middle} No additional card change was made."
    business = _field(ctx, "business_status")
    if next_system == "business" and business is not None:
        limit = _field(ctx, "business_limit")
        limit_text = f"; maximum £{limit}" if limit is not None else ""
        middle = _LIMITATIONS["business"].get(
            str(business), "The record answer does not establish a recognized business-record status."
        )
        if business == "RECEIVED" and subject not in {"batch", "payment_package"}:
            middle = "This does not establish validation, authorisation, or payment execution."
        return (
            f"The business record shows {str(business).lower()}{limit_text}. "
            f"{middle} No additional approval or role change was made."
        )
    limit = _field(ctx, "business_limit")
    if next_system == "business" and limit is not None:
        return (
            f"The business record shows a maximum of £{limit}. "
            "This does not establish authority to use the full limit or approve a payment. "
            "No limit or payment was changed."
        )
    access = _field(ctx, "access_status")
    if next_system == "access" and access is not None:
        middle = _LIMITATIONS["access"].get(
            str(access), "The record answer does not establish a recognized access status."
        )
        return (
            f"The access record shows {str(access).lower()}. "
            f"{middle} No secret was handled and no additional access change was made."
        )
    if next_system == "registration" and _field(ctx, "registered") is not None:
        registered = bool(_field(ctx, "registered"))
        reference = _field(ctx, "registration_ref")
        reference_text = f" under {reference}" if reference is not None else ""
        middle = (
            (
                "This does not establish that the fee will be refunded."
                if subject == "fee"
                else "This does not establish that the money will be returned."
            )
            if registered
            else "This does not establish that the request was accepted."
        )
        state = "registered" if registered else "not registered"
        return (
            f"The request record shows that your request is {state}{reference_text}. "
            f"{middle} No return or refund was made."
        )
    registration_ref = _field(ctx, "registration_ref")
    if next_system == "registration" and registration_ref is not None:
        return (
            f"The request record contains reference {registration_ref}. "
            "This does not establish that the request was accepted or any outcome. "
            "No request outcome was promised."
        )
    if next_system == "documents" and _field(ctx, "document_ready") is not None:
        name = _field(ctx, "document_name")
        file_text = f" ({name})" if name is not None else ""
        ready = bool(_field(ctx, "document_ready"))
        state = "available" if ready else "not ready"
        middle = _LIMITATIONS["document"]["ready" if ready else "not_ready"]
        if ready and subject in {"batch", "payment_package"}:
            middle = "This does not establish that every row was paid or processed."
        return f"The document record shows that the document{file_text} is {state}. {middle} No email was sent."
    if next_system == "tariff" and _field(ctx, "tariff_status") is not None:
        status = str(_field(ctx, "tariff_status"))
        middle = _LIMITATIONS["tariff"].get(status, _LIMITATIONS["tariff"]["OTHER"])
        return f"The tariff review shows {status.lower()}. {middle} No fee or account change was made."
    return None


@function
def reply_customer(ctx: Context) -> dict[str, Any]:
    requester = _field(ctx, "requester")
    channel = _field(ctx, "channel")
    text = _reply_text(ctx)
    if requester is None or channel is None or text is None:
        return {}
    ctx.act("reply", to=requester, channel=channel, text=text)
    return {}


# ------------------------------ speaking to the customer before any system answers

_CLARIFY = {
    "which_transaction": "To check this, please tell us which payment you mean: its date, amount and payee.",
    "which_card": "To check this, please tell us which card and which attempt you mean: the date, the amount and "
    "where it was used.",
    "which_instruction": "To check this, please tell us which instruction you mean: the payee, the amount and "
    "when it is due.",
    "more_details": "To check this, please tell us the date, the amount and any reference you can see.",
}
_NEVER_ASKED = "We will never ask for your password, PIN or a verification code."


@function
def clarify_customer(ctx: Context) -> dict[str, Any]:
    """Ask the customer for what a check needs; the wording is the desk's, never the agent's."""
    need = str(_field(ctx, "clarify_need") or "more_details")
    to = _field(ctx, "requester") or "the customer"
    ctx.act("clarify", to=to, channel=_field(ctx, "channel"), text=f"{_CLARIFY[need]} {_NEVER_ASKED}")
    return {}


@function
def redirect_secure(ctx: Context) -> dict[str, Any]:
    """Point the customer to the bank's own secure process; the desk never handles a secret."""
    to = _field(ctx, "requester") or "the customer"
    text = (
        "Please use the secure process in your secure portal to do this; it checks your identity there. "
        f"{_NEVER_ASKED} Nothing on your profile was changed."
    )
    ctx.act("redirect_secure", to=to, channel=_field(ctx, "channel"), text=text)
    return {}


@function
def forward_to_authority(ctx: Context) -> dict[str, Any]:
    """Send the request to the person whose approval it needs; the desk approves nothing itself."""
    about = _subject_description(ctx) or "the request"
    ctx.act("forward_to_authority", to="the verified company administrator", about=about,
            requester=_field(ctx, "requester"))  # fmt: skip
    return {}


_REDIRECTED = re.compile(
    r"\bdirect(?:ing|ed)? you to\b|\bopened\b.{0,60}\b(?:procedure|process)\b.{0,40}\bfor you\b"
    r"|\buse the (?:secure )?(?:recovery|pin)\b",
    re.IGNORECASE,
)
_CLARIFIED = re.compile(r"\bplease tell (?:me|us) which\b", re.IGNORECASE)
_AUTHORITY_HOLDER = re.compile(r"administrator|signatory", re.IGNORECASE)


@function
def check_bank_actions(ctx: Context) -> dict[str, Any]:
    """What the bank already did in the conversation that the customer has not answered since.

    A step the bank has taken (pointed to the secure process, sent a request for approval, asked
    which payment) is not taken again: the case waits for the customer or the approver.
    """
    out: dict[str, Any] = {}
    for event in _events(ctx):
        if _kind(event) != "conversation":
            continue
        if not _bank_sender(event, ctx.case):
            out = {}  # the customer spoke since: what the bank did before has its answer
            continue
        if _AUTHORITY_HOLDER.search(str(event.event.get("to", ""))):
            out["bank_forwarded"] = True
        elif _REDIRECTED.search(event.text):
            out["bank_redirected"] = True
        elif _CLARIFIED.search(event.text):
            out["bank_clarified"] = True
        else:
            continue
        ctx.note(f"event {event.seq} ({event.event.get('from', '')}): the bank already acted: {event.text}")
    return out


# ------------------------------ compatibility with the original payments example

_PAID: set[str] = set()
_PAYING = threading.Lock()


def _customer_of(world: dict[str, Any], sender: Any) -> tuple[str, dict[str, Any]] | None:
    for customer_id, customer in world["customers"].items():
        if customer["email"] == sender:
            return customer_id, customer
    return None


@function
def find_customer(ctx: Context) -> dict[str, Any]:
    """Compatibility lookup for the original payments demo."""

    found = _customer_of(ctx.world, ctx.case.get("from"))
    if found is None:
        ctx.note("the sender is not a customer on record")
        return {}
    customer_id, customer = found
    facts: dict[str, Any] = {"customer": customer_id, "limit": customer["limit"]}
    request = ctx.case.get("request") or {}
    if isinstance(request, Mapping) and "amount" in request:
        facts["amount"] = request["amount"]
    if isinstance(request, Mapping) and request.get("payee") in customer["payees"]:
        facts["payee"] = request["payee"]
    elif isinstance(request, Mapping) and "payee" in request:
        ctx.note(f"payee {request['payee']} is not one of the customer's payees")
    return facts


@function
def make_payment(ctx: Context) -> dict[str, Any]:
    with _PAYING:
        if ctx.key not in _PAID:
            amount, payee = ctx.fields["amount"], ctx.fields["payee"]
            ctx.act("payment", customer=ctx.fields["customer"], payee=payee, amount=str(amount), key=ctx.key)
            _PAID.add(ctx.key)
    return {"paid": True}


@function
def brief(ctx: Any) -> str:
    """Give the agent the request, conversation, and established facts, never raw system notes."""

    if "events" not in ctx.case:
        facts = {k: str(v) for k, v in ctx.fields.items() if v is not None}
        return "\n".join(
            [
                "A message to the payments inbox:",
                "<case>",
                str(ctx.case.get("text", "")),
                "</case>",
                f"From: {ctx.case.get('from')}",
                f"What the desk has established: {facts or 'nothing yet'}",
                f"Case state: {ctx.state}",
            ]
        )
    events = _events(ctx)
    lines = ["<case>", f"Request: {ctx.case.get('request', '')}"]
    for event in events:
        if _kind(event) == "conversation":
            lines.append(f"event {event.seq} ({event.event.get('channel', '')}): {event.text}")
    lines.append("</case>")
    facts = {k: str(v) for k, v in ctx.fields.items() if v is not None}
    lines.append(f"Facts established: {facts or 'nothing yet'}")
    return "\n".join(lines)

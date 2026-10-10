# Task: the track's functions — reading a case's records into facts

## Why

A desk case is one decision point of an event case: its details, its request, events `1 … k` and
the attachments available then ([case-conversion.md](case-conversion.md) builds them). There is
no live bank behind it: what the bank's internal systems answered is already written in the
history as `system` events (internal notes to and from journals, teams and services).

So "checking the transfer journal" means: find, among events `1 … k`, the request to that journal
and its answer, and return what it says as facts. The policy decides on those facts; the agent
never reads the `system` events, only the facts.

```
case input (ctx.case) ──► functions ──► facts (fields) ──► rules decide ──► an action function
   conversation events ──► briefing ──► the agent ──► signals ──► rules
```

The same case at different points gives different facts, so a different decision:

- no request to the journal yet → nothing returned → the policy asks the journal;
- request made, no answer yet → `<system>_asked: true`, status unknown → the policy waits;
- answer present → the status → the policy replies within it.

## Where and how

- All in `track/functions.py`; the desk loads only that file, so helpers live there too.
- Each function is `@function def name(ctx: Context) -> dict[str, Any]` and returns **only the
  fields listed below**, with the listed types. Anything else is a case error.
- Read from `ctx.case` only (read only). `ctx.world` is not used for now.
- Found nothing → return `{}`: the field stays unknown, which is a fact the policy uses.
  Raise only when the input itself is broken (no `events` list, an event with no `text`).
- For every fact, write where it came from. A reader groups facts from one source event into one
  note, such as `ctx.note("event 4 (H&V transfer journal): ... [facts: payment_status='SENT']")`;
  that line is the evidence in REASONING.md.
- Deterministic: the same input gives the same facts (replay depends on it). Prefer plain text
  rules; where the wording varies too much, use `ctx.classify` with a `Choice` over the listed
  values. For system-status readers, classify the one system event only, never the customer's words.
- Never take a fact from a `conversation` event when a `system` event is required: the customer
  saying "it was sent" is not `payment_status: SENT`.

The converter may mark a bank-authored structured portal record as `kind: system` even when its
sender is the bank and its recipient is the customer. Such an event is trusted only when it has a
reference (for example `HV-042` or `SUP-17`) also present in the pending system request **and** its
answer wording matches that request's system domain (a card answer cannot satisfy a transfer
request). Bare case, file, report or review words do not establish that domain, and conflicting
structured status domains remain unmatched. The same text in a `conversation` event remains
customer-visible context and cannot answer the request. A note to a case record is accepted only
when a result-bearing clause positively attributes the result to a record, journal, log or entry
(for example, it says that the journal shows or records the result); questions, conditional checks,
customer claims and pending-answer notes are not answers. A signing queue's explicit second-consent
result is the narrow business exception.

## The input (from the converter)

```python
ctx.case = {
    "id": "banking-001-at-04", "track": "...", "case": "001", "point": 4, "title": "...",
    "details": {"Source role": "Bank customer", "Bank": "...", "Created": "..."},
    "request": "...",
    "events": [{"seq": 1, "at": "...", "channel": "Secure portal", "kind": "conversation",
                "from": "...", "to": "...", "extra": {}, "text": "..."}, ...],
    "attachments": [{"name": "batch-041.csv", "path": "..."}],
}
```

## Which check a system event belongs to

A `system` event belongs to a check by the name in its `From` or `To`. Keep this table in one
place (`SYSTEMS` in functions.py), matched case-insensitively on these words:

| Check | Names in the cases |
|---|---|
| `payment` | transfer / payment / instruction / transaction journal, instruction log, payment team, payment instruction journal |
| `incoming` | incoming-payment journal, incoming-payment system, incoming-entry journal, account transaction journal |
| `recurring` | standing-order journal, mandate journal, instruction register, Direct Debit service |
| `card` | card journal, card authorisation journal, card team, card system |
| `access` | access log, access team, security team, recovery system |
| `business` | signing log, import journal, import service, limit register, admin process, admin log, access-request journal |
| `documents` | statements service, archive group, statement service, document service, data service, acquiring service |
| `registration` | any team asked to **register, review or open a case** (Direct Debit team, card team, tariff team, data team), request log, case journal |
| `tariff` | tariff team, tariff register or entry, transaction records |

A request **to** the system is `<check>_asked`; the first later event **from** it (or a note to a
case record quoting it) is the answer. A narrowly attributed agent note that says it checked the
card journal and reports what the record shows is also a card answer. A request to a team counts
as `registration` when it asks to register, review or open a case; otherwise it belongs to that
team's own check (a card team asked for a card's status is `card`).

## The functions and their fields

Types are the policy's: `text`, `bool`, `money` (exact decimal, `"420.00"`), `date`
(`2025-09-03`), `enum` (one of the listed values; anything else is not returned).

### Who is asking

`identify_requester` — from `details` and the customer's `conversation` events.

| Field | Type | |
|---|---|---|
| `requester` | text | the customer's name as written |
| `role` | enum `customer, business_admin, signatory, uploader, viewer, employee, third_party` | from `Source role` and how they describe themselves |
| `channel` | enum `secure_portal, secure_chat, verified_call, business_portal, external_message` | the channel of the customer's latest request |
| `verified` | bool | true when the request came by `verified_call`, `secure_portal` or `business_portal`, or the history says identity checks were completed; false for `secure_chat` without such a note and for `external_message` |

### What it is about

`find_subject` — from `request` and the customer's events. The policy classifies the subject from
the briefing; this function only extracts structured values for that classifier and later tools.

| Field | Type | |
|---|---|---|
| `amount` | money | the amount named for the subject, if one |
| `counterparty` | text | payee, payer, merchant or organisation named |
| `reference` | text | a reference such as `HV-041`, a row such as `SUP-17`, a file name |
| `subject_date` | date | the date named for the subject, if one |

(The subject and kind of request — status, reason, change, … — are classifier questions in the
policy, not function facts.)

### What the systems answered

Each returns `<check>_asked: true` when a request to that system is in the history, plus the
answer's fields when the answer is there too.

| Function | Fields |
|---|---|
| `check_payment` | `payment_asked` bool; `payment_status` enum `SENT, PENDING, AWAITING_AUTHORISATION, COMPLETED, DECLINED, NOT_EXECUTED, REJECTED, CANCELLED, OTHER`; `payment_reason` text (the wording the system gave, e.g. "insufficient cleared funds"); `payment_count` number (e.g. two separate instructions) |
| `check_incoming` | `incoming_asked` bool; `incoming_found` bool; `incoming_amount` money |
| `check_recurring` | `recurring_asked` bool; `recurring_status` enum `ACTIVE, CANCELLED, NOT_EXECUTED, AMENDED, OTHER`; `next_run` date |
| `check_card` | `card_asked` bool; `card_status` enum `REQUESTED, IN_MANUFACTURE, DISPATCHED, BLOCKED, RESTRICTED, DECLINED, OTHER`; `card_reason` text |
| `check_access` | `access_asked` bool; `access_status` enum `RESTORED, AWAITING_CONFIRMATION, LINKED, PROCEDURE_STARTED, EXTRACT_PROVIDED, OTHER` |
| `check_business` | `business_asked` bool; `business_status` enum `RECEIVED, VALIDATION_FAILED, AWAITING_SECOND_SIGNATORY, PENDING_APPROVAL, ROLE_REVOKED, OTHER`; `business_limit` money |
| `check_documents` | `documents_asked` bool; `document_ready` bool; `document_name` text (an attachment available at this point) |
| `check_tariff` | `tariff_asked` bool; `tariff_status` enum `MATCHES, MISMATCH, OTHER` |
| `check_registration` | `registration_asked` bool; `registered` bool; `registration_ref` text |

`OTHER` means the system answered something the list does not have: return it with a
`ctx.note` quoting the answer, so we can extend the list.

For `check_documents`, a statement being **available to order** is not ready: an order still has
to be placed. `check_tariff` reports whether the recorded fee matches the applicable tariff;
`MATCHES` and `MISMATCH` are the explicit outcomes and `OTHER` covers an answer without either.

### Has the customer confirmed a change

`check_confirmation` — from `conversation` events.

Classify the customer's secure-portal response after the bank has requested confirmation or
started the protected profile-change process addressed by that response. The history may also
contain a portal confirmation before the request: accept that confirmation only when a later,
bank-authored system record explicitly submits or records that same secure-portal confirmation.
An affirmative classifier answer cannot authorise an unrequested response without that bank
acceptance, a bank message, or a response on another channel. Unknown or invalid answers leave
confirmation requested when a request is present.

| Field | Type | |
|---|---|---|
| `confirmation` | enum `none, requested, given` | `requested`: the bank sent the change to the secure portal; `given`: the customer confirmed it **in the secure portal** after a request or protected-process start, or the bank explicitly accepted that earlier portal confirmation |
| `instructed_outside_portal` | bool | the change was asked for by email or chat only (not an authorisation) |

## Actions

Rules call these once the case is in the right state; they read **fields only**, never the agent's
words, and record what they do with `ctx.act`. Each returns `{}` (or the one field listed).

| Function | Records | Reads |
|---|---|---|
| `ask_system` | `ctx.act("ask_system", system=<check>, about=<subject>, reference=..., amount=...)` | `next_system` (enum of the checks, set by the policy), the subject fields |
| `register_request` | `ctx.act("register_request", team=..., about=..., reference=...)` | the subject fields, `next_system` |
| `send_for_confirmation` | `ctx.act("send_for_confirmation", change=..., to=<requester>)` | the subject fields |
| `reply_customer` | `ctx.act("reply", to=<requester>, channel=..., text=...)` | `next_system` and every fact |

`reply_customer` builds the text from a template per selected `next_system` and status, in three parts:
**what the record shows**, **what it does not establish**, **what was not done** — e.g. for
`payment_status: SENT`: "H&V's journal records your £420.00 transfer to Alder & Reed Workshop as
sent. This does not confirm receipt or credit by the recipient bank. No new transfer was made."
The "does not establish" lines come from [cases-analysis.md](../cases-analysis.md); keep them in one
table. Never invent a status, a date or an amount the fields do not hold.

## What the agent reads

`brief` (the policy's `briefing:`) returns the request and the `conversation` events, in order,
inside `<case>…</case>`, plus the facts established so far. It never includes `system` events.

## Done when

- `tests/test_track_api.py` covers every function on **small synthetic case inputs** in the
  converter's format (do not copy the event's cases into the repository), including: nothing
  asked; asked but not answered; answered; an answer that maps to `OTHER`; a customer claiming a
  status in a `conversation` event (must not become a fact).
- On the 50 banking examples converted at every point, every function runs without a case error,
  and `OTHER` answers are listed for review.
- `uv run ruff check src tests track examples`, `uv run ruff format --check …`, `uv run mypy` and
  `uv run pytest` pass; `uv run desk check` passes once the policy declares the fields (that part
  is ours: the field names and types above are the contract between the functions and the policy).

# Case banking-032-at-01: Archived Statement Request

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing over secure chat, asked whether an archived copy of her January 2024 statement is available. The desk classified this as a question about a statement and sent an inquiry to the documents system; her identity was not verified, and the record shows no confirmation was given. The case is closed in the asked state with no answer yet from the documents system, so what the system replies and passing that on to her is left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-19 09:00:00 UTC

The request:

> I need a copy of my January 2024 statement for my household records. Please let me know if it is available.

What happened up to now:

1. 2025-09-19T09:00:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available?

Attachments: none.

Case reference: id banking-032-at-01, track Banking & Financial Services, case 032, point 1, actor_next bank.

## Actions taken

- `ask_system` (system: documents, about: statement), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `documents-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = documents → true (args.system=documents)
  - next_system = documents → true (next_system=documents)
  - next_system absent → false (next_system=documents)
  - documents_asked absent → true (documents_asked=not known)
  - document_ready = false → not known (document_ready=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **statement**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-031-at-01: June statement in the secure portal

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elowen Marr, a verified customer writing through the secure portal, said she couldn't find her June 2025 statement there and asked for help accessing it. The desk classified this as a question about a statement and asked the documents system about it, and the case closed in the asked state. The record doesn't show an answer from the documents system or whether the statement exists, so nothing has yet been delivered to her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-17 09:00:00 UTC

The request:

> I own my H&V account and need my June 2025 statement, but I cannot find it in the secure portal. Please make the statement available there.

What happened up to now:

1. 2025-09-17T09:00:00Z · Secure portal — Elowen Marr → H&V

> I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there.

Attachments: none.

Case reference: id banking-031-at-01, track Banking & Financial Services, case 031, point 1, actor_next other.

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

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **statement**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 1 (Elowen Marr): I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there. [facts: requester='Elowen Marr', role='customer', channel='secure_portal', verified=True]
- event 1 (Elowen Marr): I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

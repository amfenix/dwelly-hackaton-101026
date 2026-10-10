# Case banking-038-at-01: Account confirmation available in the secure portal

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, a verified customer using the secure portal, asked for a bank document confirming her account relationship to be made available to her there, and said she was not asking for a transfer. The desk classified it as a question about a document and sent an inquiry to the documents system, and the case closed in the "asked" state. The documents system's answer is not in the record, so nothing has been made available in the portal and no reply has gone to her; what happens next is left open.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-01 09:00:00 UTC

The request:

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

What happened up to now:

1. 2025-10-01T09:00:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

Attachments: none.

Case reference: id banking-038-at-01, track Banking & Financial Services, case 038, point 1, actor_next other.

## Actions taken

- `ask_system` (system: documents, about: document), by rule `do-ask`

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
- channel: **secure_portal**
- verified: **True**
- subject: **document**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 1 (Mara Ellison): I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

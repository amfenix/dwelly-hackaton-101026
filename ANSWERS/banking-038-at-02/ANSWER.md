# Case banking-038-at-02: Account confirmation available in the secure portal

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing over secure chat, asked for an account confirmation document to be placed in her own secure portal and not sent to anyone else. The desk classified it as a document request and put a query to the documents system, which accepted it, and the case closed in the asked state. Mara is still unverified and the documents system has not yet returned an answer, so nothing has been made available to her and the reply to her is still outstanding.

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

2. 2025-10-01T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else.

Attachments: none.

Case reference: id banking-038-at-02, track Banking & Financial Services, case 038, point 2, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=document)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

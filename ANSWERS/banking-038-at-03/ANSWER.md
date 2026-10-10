# Case banking-038-at-03: Account confirmation available in the secure portal

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, a customer who was not verified, asked over secure chat for an account confirmation document to be released only to her own secure portal. The desk classified it as a document request, found the documents system had already been asked, and put the case into a final waiting state because that system's answer has not come in. No document has been sent or made available, and nothing is left for a person beyond the case waiting on the documents system's reply.

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

3. 2025-10-01T10:34:00Z · Internal note — H&V service agent → H&V document service

> I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only.

Attachments: none.

Case reference: id banking-038-at-03, track Banking & Financial Services, case 038, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `documents-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - documents_asked → true (documents_asked=True)
  - document_ready absent → true (document_ready=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V document service): I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only. [facts: documents_asked=True]
- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

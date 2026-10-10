# Case banking-032-at-02: Archived Statement Request

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing over secure chat, asked whether an archived copy of her January 2024 statement was available. She was not verified. The desk classified it as a document request, and the documents system had already been asked about it, so the case was put in a waiting state with no actions taken. Nothing is left for a person to do yet; the case is waiting on the documents system's answer.

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

2. 2025-09-19T09:47:00Z · Internal note — H&V service agent → H&V archive group

> I’ve checked the account-holder mandate in this secure session. Please confirm whether the January 2024 statement is available and can be ordered; I haven’t promised availability or a fee.

Attachments: none.

Case reference: id banking-032-at-02, track Banking & Financial Services, case 032, point 2, actor_next bank.

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
- subject: **statement**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (H&V archive group): I’ve checked the account-holder mandate in this secure session. Please confirm whether the January 2024 statement is available and can be ordered; I haven’t promised availability or a fee. [facts: documents_asked=True]
- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

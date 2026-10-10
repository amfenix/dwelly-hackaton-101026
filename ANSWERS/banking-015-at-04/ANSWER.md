# Case banking-015-at-04: Cancel future Direct Debit collections

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, asked the desk to cancel her Northmere Fitness Direct Debit mandate, understanding this is an instruction to her bank and not a cancellation of her agreement with the recipient. The desk recorded the request and the recurring payments system has been asked about it, but its answer hasn't come in, so the case closed as waiting with no actions taken. What is left is the recurring system's answer, and a note in the record says a collection already being processed can't be ruled out and needs separate reconciliation.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-16 09:00:00 UTC

The request:

> I want H&V to cancel my active Direct Debit mandate to Northmere Fitness so it cannot be used for future collections.

What happened up to now:

1. 2025-08-16T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> Direct Debit mandate: Northmere Fitness — Active.

2. 2025-08-16T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient.

3. 2025-08-16T10:34:00Z · Internal note — H&V service agent → H&V case record HV-015

> I completed the required identification checks and reviewed the collection-stage information. I cannot rule out a collection already being processed, so that needs separate reconciliation.

4. 2025-08-16T11:21:00Z · Business portal — H&V service agent → H&V Direct Debit service

> I have submitted Mara Ellison’s checked instruction to cancel the Northmere Fitness mandate. This submission records her instruction; I am not authorising it on her behalf.

Attachments: none.

Case reference: id banking-015-at-04, track Banking & Financial Services, case 015, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `recurring-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_asked → true (recurring_asked=True)
  - recurring_status absent → true (recurring_status=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- counterparty: **Northmere Fitness**
- recurring_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: requester='Mara Ellison', role='customer', channel='verified_call']
- event 3 (H&V service agent): I completed the required identification checks and reviewed the collection-stage information. I cannot rule out a collection already being processed, so that needs separate reconciliation. [facts: verified=True]
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: counterparty='Northmere Fitness']
- event 4 (H&V Direct Debit service): I have submitted Mara Ellison’s checked instruction to cancel the Northmere Fitness mandate. This submission records her instruction; I am not authorising it on her behalf. [facts: recurring_asked=True]
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

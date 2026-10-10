# Case banking-017-at-03: The Standing Order That Did Not Run

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellery, writing over secure chat, asked whether H&V executed her scheduled rent standing order and what status the bank recorded. The desk classified this as a status request about a standing order and asked the recurring payments system, but its answer had not come back, so the case closed as waiting with no actions taken. Nothing has been confirmed yet about whether the payment ran, and the requester was not verified.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-20 09:00:00 UTC

The request:

> I need to know whether my monthly standing order for rent was sent and, if it was not, why. The recipient says they have not received it.

What happened up to now:

1. 2025-08-20T09:00:00Z · External message — Elm Quay Property Services → Mara Ellery

> I can’t see your monthly rent payment for this cycle. Please check with your bank whether it was sent.

2. 2025-08-20T09:47:00Z · Secure chat — Mara Ellery → Harrow & Vale Bank plc agent

> I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded.

3. 2025-08-20T10:34:00Z · Internal note — Harrow & Vale Bank plc agent → H&V standing-order journal

> I am checking the journal entry for Mara Ellery’s scheduled monthly rent standing order. I need the recorded outcome and any reason shown for that specific run.

Attachments: none.

Case reference: id banking-017-at-03, track Banking & Financial Services, case 017, point 3, actor_next bank.

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

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- recurring_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V standing-order journal): I am checking the journal entry for Mara Ellery’s scheduled monthly rent standing order. I need the recorded outcome and any reason shown for that specific run. [facts: recurring_asked=True]
- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

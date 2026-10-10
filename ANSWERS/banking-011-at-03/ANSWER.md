# Case banking-011-at-03: When will my standing order run?

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, a customer on secure chat whose identity was not verified, asked the desk to check when her active monthly household contribution standing order is next due. The desk classified it as a request to read a recorded fact, asked the recurring payments system for the next run date, and put the case into a waiting state because that system's answer has not come back yet. No other action was taken, and what is left is for the recurring system's reply to arrive so the date can be passed on to her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-08 09:00:00 UTC

The request:

> I need to know the date my active monthly standing order is next due to run. I have forgotten its schedule and want to plan my household budget.

What happened up to now:

1. 2025-08-08T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> Standing order status: Active. The next run date is not displayed in this status view.

2. 2025-08-08T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget.

3. 2025-08-08T10:34:00Z · Internal note — H&V service agent → H&V standing-order journal

> Please check the record for Mara Ellison's active monthly standing order and confirm its next scheduled run date. I am checking the recorded date only; I am not changing or authorising the instruction.

Attachments: none.

Case reference: id banking-011-at-03, track Banking & Financial Services, case 011, point 3, actor_next bank.

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
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- recurring_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V standing-order journal): Please check the record for Mara Ellison's active monthly standing order and confirm its next scheduled run date. I am checking the recorded date only; I am not changing or authorising the instruction. [facts: recurring_asked=True]
- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

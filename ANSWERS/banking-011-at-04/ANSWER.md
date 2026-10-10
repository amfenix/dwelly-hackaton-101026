# Case banking-011-at-04: When will my standing order run?

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison asked over secure chat when her active monthly household contribution standing order is next due. The desk checked the standing-order record, found it active with the next run on 2025-09-03, and replied with that date, noting that this does not guarantee the future payment will execute and that no change or instruction was made. Her identity was not verified, but the reply only gave a read-only date, and the case is closed with nothing left for a person.

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

4. 2025-08-08T11:21:00Z · Internal note — H&V standing-order journal → H&V service agent

> Record check complete: the standing order is active. Its next scheduled run date is 3 September 2025; the future payment has not been executed.

Attachments: none.

Case reference: id banking-011-at-04, track Banking & Financial Services, case 011, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The standing-order record shows the instruction as active; next run 2025-09-03. This does not guarantee that the future payment will execute. No additional instruction or change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `recurring-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=question)
  - next_system = recurring → true (next_system=recurring)
  - recurring_status present → true (recurring_status=ACTIVE)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- recurring_asked: **True**
- recurring_status: **ACTIVE**
- next_run: **2025-09-03**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V standing-order journal): Please check the record for Mara Ellison's active monthly standing order and confirm its next scheduled run date. I am checking the recorded date only; I am not changing or authorising the instruction. [facts: recurring_asked=True]
- event 4 (H&V standing-order journal): Record check complete: the standing order is active. Its next scheduled run date is 3 September 2025; the future payment has not been executed. [facts: recurring_status='ACTIVE', next_run='2025-09-03']
- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

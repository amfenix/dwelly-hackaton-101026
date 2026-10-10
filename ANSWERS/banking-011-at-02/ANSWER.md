# Case banking-011-at-02: When will my standing order run?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing through secure chat without being verified, asked the desk to check when her active monthly household contribution standing order is next due. The desk classed this as a request for a record fact and put the question to the recurring payments system. That system had returned nothing when the case closed, so the due date is still unknown and nobody has told her yet. The record does not say who will pass the answer on once it arrives.

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

Attachments: none.

Case reference: id banking-011-at-02, track Banking & Financial Services, case 011, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: recurring, about: standing_order), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `recurring-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = recurring → true (args.system=recurring)
  - next_system = recurring → true (next_system=recurring)
  - next_system absent → false (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-011-at-03: When will my standing order run?

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, an unverified customer on secure chat, asked when her active monthly standing order is next due. The desk asked the recurring system for the date, but no answer has come back, so the case closed as "wait" and no reply was sent. The agent's attempts to ask the recurring system again and to reply were both refused while the case was waiting, so the question is still unanswered and the case stays open for a person.

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
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V standing-order journal): Please check the record for Mara Ellison's active monthly standing order and confirm its next scheduled run date. I am checking the recorded date only; I am not changing or authorising the instruction. [facts: recurring_asked=True]
- event 2 (Mara Ellison): I can see that my monthly household contribution standing order is active, but I cannot remember when it is next due. Please check the date for me; I am planning my budget. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); recurring-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=recurring); recurring_asked absent is false (recurring_asked=True); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); document_ready present is false (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=recurring); tariff_status present is false (tariff_status=not known)

## Final result

wait (WAITING)

# Case banking-011-at-01: When will my standing order run?

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was classified as recording a fact about a standing order, and the desk routed it to the recurring-payments system. It sent that system a question about the standing order and closed the case as asked. A later attempt to send a reply was refused because the case was already in the asked state and no answer from the recurring system was on record, so nothing has been replied to the requester. What remains is waiting for the recurring system's answer, and no further step is recorded.

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

Attachments: none.

Case reference: id banking-011-at-01, track Banking & Financial Services, case 011, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **standing_order**
- request_type: **record_fact**
- next_system: **recurring**

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=recurring); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=recurring); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=recurring); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=recurring); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=recurring); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=recurring); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

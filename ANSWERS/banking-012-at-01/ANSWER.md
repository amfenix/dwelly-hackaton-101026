# Case banking-012-at-01: New standing-order amount

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Mira asked to raise her monthly standing order to the Westmere Garden Cooperative from £42.00 to £68.00. She had not yet authorised the change, so the desk sent her a confirmation request, since a change has to be confirmed by the customer in the secure portal. The change itself has not been made and waits on Mira's confirmation; the agent's later attempt to check the recurring system was refused because the case had already closed at confirmation sent.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-10 09:00:00 UTC

The request:

> Mira wants to increase her monthly standing order to the fictional Westmere Garden Cooperative from £42.00 to £68.00. She has not yet authorised the change.

What happened up to now:

1. 2025-08-10T09:00:00Z · Secure portal — H&V system → Mira Ellery

> Standing order to Westmere Garden Cooperative: £42.00 per month.

Attachments: none.

Case reference: id banking-012-at-01, track Banking & Financial Services, case 012, point 1, actor_next other.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `CONFIRM_PENDING`: rule `change-needs-confirmation` — A change is confirmed by the customer in the secure portal, not in chat or by email.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = none → true (confirmation=none)
  - registration_asked absent → true (registration_asked=not known)
- `CONFIRM_PENDING` → `CONFIRMATION_SENT`: rule `do-confirm`.
  - state = CONFIRM_PENDING → true (state=CONFIRM_PENDING)

Facts established:

- subject: **standing_order**
- amount: **68.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- initial request (system): Mira wants to increase her monthly standing order to the fictional Westmere Garden Cooperative from £42.00 to £68.00. She has not yet authorised the change. [facts: amount='68.00']
- event 1 (H&V system): Standing order to Westmere Garden Cooperative: £42.00 per month. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); access-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

send_for_confirmation (CONFIRMATION_SENT)

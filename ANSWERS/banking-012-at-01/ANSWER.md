# Case banking-012-at-01: New standing-order amount

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Mira asked to raise her monthly standing order to Westmere Garden Cooperative from £42.00 to £68.00, but she had not yet authorised the change. The desk sent her a confirmation request, since a change has to be confirmed by the customer in the secure portal, and closed the case at that point. The standing order stays at £42.00 until she confirms, and nothing was refused or failed.

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

## Final result

send_for_confirmation (CONFIRMATION_SENT)

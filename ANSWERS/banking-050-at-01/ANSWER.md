# Case banking-050-at-01: Status of a Supplier Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a status question about a transfer. The desk classified it as a transfer status request and sent a query to the payment system about it, and the case closed in the "asked" state. No reply from the payment system is in the record, so the stage of the payment is not known. The only related finding is a note that the business portal recorded a payment authorisation for the Alder Quay Supplies materials invoice; whether the payment was sent, is pending or is held is left for a person to find out from the payment system's answer.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-25 09:00:00 UTC

The request:

> I’m an authorised signatory for Northmere Studio Ltd. Our supplier says it has not received the payment we authorised for a materials invoice. Please tell me what stage H&V’s records show for that payment.

What happened up to now:

1. 2025-10-25T09:00:00Z · Business portal — H&V business portal → Mara Ellison

> Payment authorisation recorded for the materials invoice from Alder Quay Supplies.

Attachments: none.

Case reference: id banking-050-at-01, track Banking & Financial Services, case 050, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `payment-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = payment → true (args.system=payment)
  - next_system = payment → true (next_system=payment)
  - next_system absent → false (next_system=payment)
  - payment_asked absent → true (payment_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 1 (H&V business portal): Payment authorisation recorded for the materials invoice from Alder Quay Supplies. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

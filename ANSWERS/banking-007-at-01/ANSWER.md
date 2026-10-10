# Case banking-007-at-01: International Transfer Status

**Decision: ask_system**  (final state `ASKED`)

## Summary

The desk read the message as a question about a transfer and sent it to the payment system, asking about the transfer. The case closed there with the query made. The only thing on record is a note that H&V recorded the international payment instruction as sent, with no confirmation and nothing showing it was instructed outside the portal. The payment system returned no further detail on the transfer's stage, and the record gives no confirmation that the beneficiary received the money, so a person would need to follow up if more is wanted.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-31 09:00:00 UTC

The request:

> I can see that H&V recorded my international transfer as sent, but I cannot tell what stage it has reached. Please check its current status and tell me whether receipt by the beneficiary has been confirmed.

What happened up to now:

1. 2025-07-31T09:00:00Z · Secure portal — H&V → Mara Ellwood

> H&V has recorded your international payment instruction as sent.

Attachments: none.

Case reference: id banking-007-at-01, track Banking & Financial Services, case 007, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 1 (H&V): H&V has recorded your international payment instruction as sent. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

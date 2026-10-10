# Case banking-042-at-01: Payment batch validation report

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was classified as a question about a batch, and the desk routed it to the payment system and sent that system a query about the batch. The case closed as final with that query as its outcome. The record shows no answer from the payment system and no other facts found, so the desk has no row-level error report or reason the batch failed validation, and a person will need to follow up on the payment system's reply.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-09 09:00:00 UTC

The request:

> I uploaded a supplier payment batch for Fenwick Workshop, but it did not pass validation. Please make the row-level error report available to me so I can review what needs correcting.

What happened up to now:

1. 2025-10-09T09:00:00Z · Business portal — Harrow & Vale Bank plc → Nadia Fenwick

> Validation status: FAILED. The payment batch did not pass validation.

Attachments: none.

Case reference: id banking-042-at-01, track Banking & Financial Services, case 042, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: batch), by rule `do-ask`

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

- subject: **batch**
- request_type: **question**
- next_system: **payment**

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

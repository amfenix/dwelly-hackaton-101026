# Case banking-044-at-01: One Line in the Supplier Batch

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a question about whether the payment on row SUP-17 in the supplier batch, which shows as processed, was paid or rejected. The desk classified it as a batch question and routed it to the payment system, where it sent a query about SUP-17, and the case closed in the "asked" state. The payment system's answer is not in the record, so whether the payment was paid or rejected is still unknown and no reply has been given to the requester.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-13 09:00:00 UTC

The request:

> I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected.

What happened up to now:

1. 2025-10-13T09:00:00Z · Business portal — H&V secure portal → Leona Voss

> Batch “Alderwick supplier payments” — status: Processed.

Attachments: none.

Case reference: id banking-044-at-01, track Banking & Financial Services, case 044, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: batch, reference: SUP-17), by rule `do-ask`

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
- reference: **SUP-17**
- request_type: **question**
- next_system: **payment**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- initial request (system): I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected. [facts: reference='SUP-17']

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

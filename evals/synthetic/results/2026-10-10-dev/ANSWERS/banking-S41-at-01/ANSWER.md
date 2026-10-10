# Case banking-S41-at-01: Three events, no context

**Decision: ask_system**  (final state `ASKED`)

## Summary

Owen Prescott, an unverified customer on secure chat, asked whether his £75 transfer to the plumber had gone out. The desk classified this as a question about a transfer and sent an enquiry to the payment system about the £75 transfer. The record shows no answer from the payment system yet, so the reply to Owen is still to be written once that answer is in.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-11 09:00:00 UTC

The request:

> Did my £75 to the plumber go out?

What happened up to now:

1. 2025-12-11T09:00:00Z · Secure chat — Owen Prescott → H&V service agent

> Did my £75 to the plumber go out?

Attachments: none.

Case reference: id banking-S41-at-01, track banking, case S41, point 1, actor_next bank.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 75.00), by rule `do-ask`

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

- requester: **Owen Prescott**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **75.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 1 (Owen Prescott): Did my £75 to the plumber go out? [facts: requester='Owen Prescott', role='customer', channel='secure_chat', verified=False]
- event 1 (Owen Prescott): Did my £75 to the plumber go out? [facts: amount='75.00']
- event 1 (Owen Prescott): Did my £75 to the plumber go out? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

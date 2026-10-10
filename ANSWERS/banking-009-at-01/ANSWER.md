# Case banking-009-at-01: Confirming the amount sent

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer remembered entering £684.20 in the transfer draft but saw £648.20 on the final payment line, and asked which amount was actually sent. The desk found the bank's record showing £648.20 sent to the property manager, with no separate confirmation on file, and put a question to the payment system about the transfer and that amount. The case closed with that question asked; the record shows no answer yet, so the amount sent is not confirmed.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-04 09:00:00 UTC

The request:

> I remember entering £684.20 in the transfer draft, but the final payment line shows £648.20. Please confirm the amount H&V actually sent.

What happened up to now:

1. 2025-08-04T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellwood

> Final payment line: £648.20 sent to your property manager.

Attachments: none.

Case reference: id banking-009-at-01, track Banking & Financial Services, case 009, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 648.20), by rule `do-ask`

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
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- amount: **648.20**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **payment**

Where they came from:

- initial request (system): I remember entering £684.20 in the transfer draft, but the final payment line shows £648.20. Please confirm the amount H&V actually sent. [facts: amount='648.20']
- event 1 (Harrow & Vale Bank plc): Final payment line: £648.20 sent to your property manager. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

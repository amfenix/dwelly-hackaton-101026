# Case banking-003-at-01: Transfer Awaiting Authorisation

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elise Rowan, a verified customer on the secure portal, said she saved a transfer instruction for an invoice but had not seen confirmation that it was sent. The desk classified this as a status request about a transfer and asked the payment system about it. That query is the only action taken and the case closed there with no answer recorded, so what the payment system says about the transfer is still outstanding.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-23 09:00:00 UTC

The request:

> I saved a transfer instruction for an invoice in my secure portal, but there is no sent confirmation. Please check whether it has been submitted and tell me what stage it is at.

What happened up to now:

1. 2025-07-23T09:00:00Z · Secure portal — Elise Rowan → Harrow & Vale Bank plc

> I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent.

Attachments: none.

Case reference: id banking-003-at-01, track Banking & Financial Services, case 003, point 1, actor_next other.

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Elise Rowan**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 1 (Elise Rowan): I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent. [facts: requester='Elise Rowan', role='customer', channel='secure_portal', verified=True]
- event 1 (Elise Rowan): I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

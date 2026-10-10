# Case banking-003-at-02: Transfer Awaiting Authorisation

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elise Rowan, an unverified customer on secure chat, asked about the status of a transfer that has no sent confirmation, and whether she needs to authorise it. The desk classified it as a status request and asked the payment system about the transfer. That query has been sent but no answer is recorded, so the transfer's current stage and whether authorisation is needed are still unconfirmed.

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

2. 2025-07-23T09:47:00Z · Secure chat — Elise Rowan → H&V service agent

> I’m escalating this because the instruction still has no sent confirmation. Please check its current stage and tell me whether I need to authorise it.

Attachments: none.

Case reference: id banking-003-at-02, track Banking & Financial Services, case 003, point 2, actor_next bank.

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
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Elise Rowan): I’m escalating this because the instruction still has no sent confirmation. Please check its current stage and tell me whether I need to authorise it. [facts: requester='Elise Rowan', role='customer', channel='secure_chat', verified=False]
- event 2 (Elise Rowan): I’m escalating this because the instruction still has no sent confirmation. Please check its current stage and tell me whether I need to authorise it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

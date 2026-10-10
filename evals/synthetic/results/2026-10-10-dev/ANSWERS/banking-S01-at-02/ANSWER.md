# Case banking-S01-at-02: SEPA transfer in euros — was it sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Tobias Wrenfield, a customer on secure chat whose identity is not verified, asked whether H&V actually sent his €1,234.56 payment to Atelier Vaucanson on 31/10/25. The desk classified this as a question about a transfer and asked the payment system about it. That is the only action taken, and the payment system's answer is not in the record. Someone still needs to tell him whether the transfer went out, and his identity remains unverified.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-01 09:00:00 UTC

The request:

> I sent a one-off SEPA payment of €1.234,56 on 31/10/25 to Atelier Vaucanson in Lyon for an order of workshop parts. I can see it in my account, but I need to know whether H&V actually sent it.

What happened up to now:

1. 2025-11-01T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Tobias Wrenfield

> One-off SEPA transfer to Atelier Vaucanson, Lyon — EUR 1,234.56. Debit shown in your account activity on 31/10/2025.

2. 2025-11-01T09:47:00Z · Secure chat — Tobias Wrenfield → H&V service agent

> Hi — I paid our French supplier, Atelier Vaucanson in Lyon, €1.234,56 on 31/10/25 for a batch of workshop parts. Their accounts team keep asking whether we’ve paid. Can you tell me whether H&V has actually sent it? I’m only asking about your side.

Attachments: none.

Case reference: id banking-S01-at-02, track banking, case S01, point 2, actor_next bank.

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

- requester: **Tobias Wrenfield**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- counterparty: **Atelier Vaucanson**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Tobias Wrenfield): Hi — I paid our French supplier, Atelier Vaucanson in Lyon, €1.234,56 on 31/10/25 for a batch of workshop parts. Their accounts team keep asking whether we’ve paid. Can you tell me whether H&V has actually sent it? I’m only asking about your side. [facts: requester='Tobias Wrenfield', role='customer', channel='secure_chat', verified=False]
- event 2 (Tobias Wrenfield): Hi — I paid our French supplier, Atelier Vaucanson in Lyon, €1.234,56 on 31/10/25 for a batch of workshop parts. Their accounts team keep asking whether we’ve paid. Can you tell me whether H&V has actually sent it? I’m only asking about your side. [facts: counterparty='Atelier Vaucanson']
- event 2 (Tobias Wrenfield): Hi — I paid our French supplier, Atelier Vaucanson in Lyon, €1.234,56 on 31/10/25 for a batch of workshop parts. Their accounts team keep asking whether we’ve paid. Can you tell me whether H&V has actually sent it? I’m only asking about your side. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

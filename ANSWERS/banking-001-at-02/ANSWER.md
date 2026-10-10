# Case banking-001-at-02: Was the one-off transfer sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, who was not verified, asked through secure chat whether H&V had sent her £420 payment to Alder & Reed Workshop, which she could see as a debit. The desk classified it as a transfer question and sent a query about the £420 transfer to the payment system, then closed the case at that step. The payment system's answer is not in the record, so whether the payment was sent is still unconfirmed and no status has been given to her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-19 09:00:00 UTC

The request:

> I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it.

What happened up to now:

1. 2025-07-19T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> One-off transfer to Alder & Reed Workshop: debit shown in your account activity.

2. 2025-07-19T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status.

Attachments: none.

Case reference: id banking-001-at-02, track Banking & Financial Services, case 001, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 420.00), by rule `do-ask`

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **420.00**
- counterparty: **Alder & Reed Workshop**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: amount='420.00']
- initial request (system): I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it. [facts: counterparty='Alder & Reed Workshop']
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

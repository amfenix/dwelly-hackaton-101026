# Case banking-006-at-02: Two Similar Transfers

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mira Ellison, writing over secure chat as an unverified customer, said she meant to make only one transfer and asked whether there were separate instructions and whether the pending one had been stopped or returned. The desk classified this as a question about a transfer and sent a query to the payment system, which was its only action. The record shows no answer from the payment system and no stop or return of any transfer, so her question remains unanswered and is left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-29 09:00:00 UTC

The request:

> Mira, the account holder, wants H&V to establish whether two similar outgoing transfer entries are one instruction shown twice or two separate instructions, and asks whether the second can be stopped or returned.

What happened up to now:

1. 2025-07-29T09:00:00Z · Secure portal — H&V → Mira Ellison

> Your payment activity shows two similar outgoing transfer entries to North Quay Utilities for £84.20. One is marked Completed and the other Pending.

2. 2025-07-29T09:47:00Z · Secure chat — Mira Ellison → H&V agent

> I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned.

Attachments: none.

Case reference: id banking-006-at-02, track Banking & Financial Services, case 006, point 2, actor_next bank.

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

- requester: **Mira Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: requester='Mira Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

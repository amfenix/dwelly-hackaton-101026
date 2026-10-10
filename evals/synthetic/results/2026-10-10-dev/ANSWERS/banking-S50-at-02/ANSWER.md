# Case banking-S50-at-02: Request in Polish with local formats

**Decision: ask_system**  (final state `ASKED`)

## Summary

Agnieszka Wróblewska, a customer writing over secure chat, asked about the status of a transfer, saying she was not asking whether the money had reached the recipient. The desk classified this as a question about a transfer and sent a query about it to the payment system. That query is the only action taken, and the payment system's answer is not yet in the record. Her identity is not verified, so whoever replies to her still has to pass on the transfer status once the payment system returns it, taking that into account.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-20 09:00:00 UTC

The request:

> Dzień dobry, 03.11.2025 zleciłam jednorazowy przelew na kwotę 1 250,00 zł do Pracowni Stolarskiej Dąbek. Widzę obciążenie na koncie, ale chciałabym wiedzieć, czy H&V faktycznie wysłał ten przelew.

What happened up to now:

1. 2025-12-20T09:00:00Z · Secure chat — Agnieszka Wróblewska → H&V service agent

> Dzień dobry, 03.11.2025 zleciłam jednorazowy przelew na kwotę 1 250,00 zł do Pracowni Stolarskiej Dąbek za nowe drzwi. Widzę obciążenie na koncie, ale chciałabym wiedzieć, czy H&V faktycznie wysłał ten przelew.

2. 2025-12-20T09:47:00Z · Secure chat — Agnieszka Wróblewska → H&V service agent

> Dodam, że nie pytam, czy pieniądze już dotarły do odbiorcy — chodzi mi tylko o status przelewu w Państwa systemie. Bardzo proszę o sprawdzenie.

Attachments: none.

Case reference: id banking-S50-at-02, track banking, case S50, point 2, actor_next bank.

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

- requester: **Agnieszka Wróblewska**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Agnieszka Wróblewska): Dodam, że nie pytam, czy pieniądze już dotarły do odbiorcy — chodzi mi tylko o status przelewu w Państwa systemie. Bardzo proszę o sprawdzenie. [facts: requester='Agnieszka Wróblewska', role='customer', channel='secure_chat', verified=False]
- event 2 (Agnieszka Wróblewska): Dodam, że nie pytam, czy pieniądze już dotarły do odbiorcy — chodzi mi tylko o status przelewu w Państwa systemie. Bardzo proszę o sprawdzenie. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-S50-at-02: Request in Polish with local formats

**Decision: ask_system**  (final state `ASKED`)

## Summary

Agnieszka Wróblewska, a customer on secure chat who has not been verified, asked for the status of a transfer in the bank's system, not whether the money had reached the recipient. The desk classified it as a question about a transfer and sent a query to the payment system. That query came back with no transfer status, and the attempt to write a reply was refused, so the case closed at the asking stage with no answer for the customer. A bank employee still has to check the status of the transfer and respond to her.

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
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Agnieszka Wróblewska): Dodam, że nie pytam, czy pieniądze już dotarły do odbiorcy — chodzi mi tylko o status przelewu w Państwa systemie. Bardzo proszę o sprawdzenie. [facts: requester='Agnieszka Wróblewska', role='customer', channel='secure_chat', verified=False]
- event 2 (Agnieszka Wróblewska): Dodam, że nie pytam, czy pieniądze już dotarły do odbiorcy — chodzi mi tylko o status przelewu w Państwa systemie. Bardzo proszę o sprawdzenie. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=transfer); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=payment); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

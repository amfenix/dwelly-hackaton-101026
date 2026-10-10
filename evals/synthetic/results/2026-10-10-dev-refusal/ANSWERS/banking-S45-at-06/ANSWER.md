# Case banking-S45-at-06: Asked again three days later

**Decision: ask_system**  (final state `ASKED`)

## Summary

Henrietta Marsh, an unverified customer on secure chat, asked whether her €2,600 transfer to Atelier Rousset, which the atelier says hasn't arrived after three days, is still held up at another bank or has moved. The desk classified it as a question about a transfer and sent it to the payment system to ask about the transfer. The case closed there with the question asked; no answer has come back, and a later attempt to reply to her was refused, so she has not been given a reply yet.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-15 09:00:00 UTC

The request:

> Can you tell me where my €2,600 transfer to Atelier Rousset in Bordeaux has got to?

What happened up to now:

1. 2025-12-15T09:00:00Z · Secure chat — Henrietta Marsh → H&V service agent

> Can you tell me where my €2,600 transfer to Atelier Rousset in Bordeaux has got to? I sent it on 11 December for a restoration deposit.

2. 2025-12-15T09:47:00Z · Internal note — H&V service agent → H&V transfer journal

> I am checking the journal entry for Henrietta Marsh’s €2,600.00 international transfer to Atelier Rousset dated 11 December 2025. Please return the recorded status.

3. 2025-12-15T10:34:00Z · Internal note — H&V transfer journal → H&V service agent

> Status as at 15 December 2025 10:30 UTC: SENT by H&V on 11 December 2025; PENDING with downstream correspondent bank. Beneficiary-bank receipt not confirmed.

4. 2025-12-15T11:21:00Z · Secure chat — H&V service agent → Henrietta Marsh

> As of this morning, 15 December, our journal shows H&V sent the transfer on 11 December and it is pending with a downstream correspondent bank. That isn’t confirmation that Atelier Rousset’s bank has received it.

5. 2025-12-18T09:00:00Z · Secure portal — H&V system → Henrietta Marsh

> International transfer to Atelier Rousset, €2,600.00 — status shown at last check (15 December 2025): pending.

6. 2025-12-18T09:47:00Z · Secure chat — Henrietta Marsh → H&V service agent

> It’s been three days now and the atelier still says nothing has arrived. Is it still stuck with that other bank, or has it moved?

Attachments: none.

Case reference: id banking-S45-at-06, track banking, case S45, point 6, actor_next bank.

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

- requester: **Henrietta Marsh**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- counterparty: **Atelier Rousset**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 6 (Henrietta Marsh): It’s been three days now and the atelier still says nothing has arrived. Is it still stuck with that other bank, or has it moved? [facts: requester='Henrietta Marsh', role='customer', channel='secure_chat', verified=False]
- event 1 (Henrietta Marsh): Can you tell me where my €2,600 transfer to Atelier Rousset in Bordeaux has got to? I sent it on 11 December for a restoration deposit. [facts: counterparty='Atelier Rousset']
- event 6 (Henrietta Marsh): It’s been three days now and the atelier still says nothing has arrived. Is it still stuck with that other bank, or has it moved? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=transfer); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=payment); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

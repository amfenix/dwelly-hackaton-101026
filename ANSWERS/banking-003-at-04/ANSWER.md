# Case banking-003-at-04: Transfer Awaiting Authorisation

**Decision: reply**  (final state `REPLIED`)

## Summary

Elise Rowan asked over secure chat about the stage of her transfer, which had no sent confirmation, and whether she needed to authorise it. The desk checked the payment record, found it at "awaiting authorisation", and replied on secure chat saying exactly that, that the reply does not authorise the payment, and that no new transfer was made. The case is closed as replied; she was not verified on the chat, and nothing was authorised or changed on the transfer, so any authorisation is still up to her.

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

3. 2025-07-23T10:34:00Z · Internal note — H&V service agent → H&V instruction journal

> I’m checking the instruction stage against the identifier in Elise’s secure session. I will not authorise the payment on her behalf.

4. 2025-07-23T11:21:00Z · Internal note — H&V instruction journal → H&V service agent

> “Awaiting authorisation”

Attachments: none.

Case reference: id banking-003-at-04, track Banking & Financial Services, case 003, point 4, actor_next bank.

## Actions taken

- `reply` (to: Elise Rowan, channel: secure_chat), by rule `do-reply`

  > The payment record shows your transfer as awaiting_authorisation. This does not authorise the payment. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=AWAITING_AUTHORISATION)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Elise Rowan**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- payment_status: **AWAITING_AUTHORISATION**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Elise Rowan): I’m escalating this because the instruction still has no sent confirmation. Please check its current stage and tell me whether I need to authorise it. [facts: requester='Elise Rowan', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V instruction journal): I’m checking the instruction stage against the identifier in Elise’s secure session. I will not authorise the payment on her behalf. [facts: payment_asked=True]
- event 4 (H&V instruction journal): “Awaiting authorisation” [facts: payment_status='AWAITING_AUTHORISATION']
- event 2 (Elise Rowan): I’m escalating this because the instruction still has no sent confirmation. Please check its current stage and tell me whether I need to authorise it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

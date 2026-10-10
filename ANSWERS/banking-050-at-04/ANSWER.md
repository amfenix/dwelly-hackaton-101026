# Case banking-050-at-04: Status of a Supplier Payment

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, writing as company signatory on secure chat, asked the desk to check the stage of a transfer that Alder Quay Supplies says it has not received. The desk replied that the payment record shows the transfer as sent, that this does not confirm receipt or credit by the recipient bank, and that no new transfer was made. Her identity was not verified, and the case is closed with nothing further left for a person in the record.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-25 09:00:00 UTC

The request:

> I’m an authorised signatory for Northmere Studio Ltd. Our supplier says it has not received the payment we authorised for a materials invoice. Please tell me what stage H&V’s records show for that payment.

What happened up to now:

1. 2025-10-25T09:00:00Z · Business portal — H&V business portal → Mara Ellison

> Payment authorisation recorded for the materials invoice from Alder Quay Supplies.

2. 2025-10-25T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records.

3. 2025-10-25T10:34:00Z · Internal note — H&V service agent → H&V payment team

> I’m escalating this specific payment under case HV-050. Please check and confirm the payment stage recorded in H&V’s journal.

4. 2025-10-25T11:21:00Z · Internal note — H&V payment team → H&V service agent

> I checked the payment journal. The recorded stage is “sent”; this record does not confirm receipt by the recipient’s bank or supplier.

Attachments: none.

Case reference: id banking-050-at-04, track Banking & Financial Services, case 050, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The payment record shows your transfer as sent. This does not confirm receipt or credit by the recipient bank. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=SENT)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **signatory**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- payment_status: **SENT**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: requester='Mara Ellison', role='signatory', channel='secure_chat', verified=False]
- event 3 (H&V payment team): I’m escalating this specific payment under case HV-050. Please check and confirm the payment stage recorded in H&V’s journal. [facts: payment_asked=True]
- event 4 (H&V payment team): I checked the payment journal. The recorded stage is “sent”; this record does not confirm receipt by the recipient’s bank or supplier. [facts: payment_status='SENT']
- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment)

## Final result

reply (REPLIED)

# Case banking-050-at-04: Status of a Supplier Payment

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, writing over secure chat as the company signatory, asked the desk to check the stage of a transfer that the supplier Alder Quay Supplies says it has not received. The desk looked up the payment record, which shows the transfer as sent, and replied to her that this does not confirm the recipient bank has received or credited it, and that no new transfer was made. Her identity was not verified, and the case closed as replied with nothing further recorded for a person to do.

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
- request_type: **question**
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

## Final result

reply (REPLIED)

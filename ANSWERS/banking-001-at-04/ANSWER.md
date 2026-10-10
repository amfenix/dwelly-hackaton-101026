# Case banking-001-at-04: Was the one-off transfer sent?

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison asked over secure chat whether her £420 payment to Alder & Reed Workshop had been sent, since she could see the debit. The desk checked the transfer journal, which showed the transfer as sent, and replied on secure chat saying so, noting that this does not confirm the recipient bank has received or credited it and that no new transfer was made. Her identity was not verified, and nothing in the record is left for a person to do.

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

3. 2025-07-19T10:34:00Z · Internal note — H&V service agent → H&V transfer journal

> I am checking the journal entry for Mara Ellison's specific one-off £420 transfer to Alder & Reed Workshop. Please return the recorded transfer status.

4. 2025-07-19T11:21:00Z · Internal note — H&V transfer journal → H&V service agent

> Transfer status: SENT. This is H&V's outgoing-transfer record; recipient-bank receipt or credit is not confirmed.

Attachments: none.

Case reference: id banking-001-at-04, track Banking & Financial Services, case 001, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The payment record shows your £420.00 transfer to Alder & Reed Workshop as sent. This does not confirm receipt or credit by the recipient bank. No new transfer was made.


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
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **420.00**
- counterparty: **Alder & Reed Workshop**
- payment_asked: **True**
- payment_status: **SENT**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: amount='420.00']
- initial request (system): I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it. [facts: counterparty='Alder & Reed Workshop']
- event 3 (H&V transfer journal): I am checking the journal entry for Mara Ellison's specific one-off £420 transfer to Alder & Reed Workshop. Please return the recorded transfer status. [facts: payment_asked=True]
- event 4 (H&V transfer journal): Transfer status: SENT. This is H&V's outgoing-transfer record; recipient-bank receipt or credit is not confirmed. [facts: payment_status='SENT']
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

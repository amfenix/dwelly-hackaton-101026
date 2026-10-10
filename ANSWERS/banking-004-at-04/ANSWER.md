# Case banking-004-at-04: Why the transfer was declined

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellery, a verified customer on the secure portal, asked why her 14 July 2025 transfer to Northmere Housing Co-operative was not completed. The desk checked the payment record, which shows the transfer as declined with the permitted wording "The receiving bank declined the transfer," and sent that reply through the portal. It also said the record doesn't establish a different cause or authorise a retry, and that no new transfer was made. The case is closed with nothing left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-25 09:00:00 UTC

The request:

> I am the account holder and made a transfer to Northmere Housing Co-operative on 14 July 2025. The secure portal says it was not completed, but I cannot see why. Please explain the reason.

What happened up to now:

1. 2025-07-25T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> Transfer to Northmere Housing Co-operative — status: “Not completed”.

2. 2025-07-25T09:47:00Z · Secure portal — Mara Ellery → H&V service team

> I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason.

3. 2025-07-25T10:34:00Z · Internal note — H&V service agent → H&V transaction journal

> I am checking the decline code for Mara Ellery’s transfer to Northmere Housing Co-operative dated 14 July 2025. Please return the code and the customer-facing wording permitted for this transaction.

4. 2025-07-25T11:21:00Z · Internal note — H&V transaction journal → H&V service agent

> I found a decline code recorded for this transfer. The permitted customer-facing wording is: “The receiving bank declined the transfer.”

Attachments: none.

Case reference: id banking-004-at-04, track Banking & Financial Services, case 004, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellery, channel: secure_portal), by rule `do-reply`

  > The payment record shows your transfer to Northmere Housing Co-operative as declined (recorded reason: : “The receiving bank declined the transfer.). This does not establish a different cause or authorise a retry. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=question)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=DECLINED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **transfer**
- counterparty: **Northmere Housing Co-operative**
- subject_date: **2025-07-14**
- payment_asked: **True**
- payment_status: **DECLINED**
- payment_reason: **: “The receiving bank declined the transfer.**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellery): I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason. [facts: requester='Mara Ellery', role='customer', channel='secure_portal', verified=True]
- initial request (system): I am the account holder and made a transfer to Northmere Housing Co-operative on 14 July 2025. The secure portal says it was not completed, but I cannot see why. Please explain the reason. [facts: counterparty='Northmere Housing Co-operative', subject_date='2025-07-14']
- event 3 (H&V transaction journal): I am checking the decline code for Mara Ellery’s transfer to Northmere Housing Co-operative dated 14 July 2025. Please return the code and the customer-facing wording permitted for this transaction. [facts: payment_asked=True]
- event 4 (H&V transaction journal): I found a decline code recorded for this transfer. The permitted customer-facing wording is: “The receiving bank declined the transfer.” [facts: payment_status='DECLINED', payment_reason=': “The receiving bank declined the transfer.']
- event 2 (Mara Ellery): I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

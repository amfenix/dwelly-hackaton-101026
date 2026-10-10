# Case banking-040-at-04: Confirmation of a Specific Payment

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison asked over secure chat for a document showing the stage of her £74.00 payment (reference HV-040) to give to her repair contractor. The desk found that the document service had generated the record, and replied on secure chat that the document is available, that this doesn't confirm it was downloaded or that funds were credited, and that no email was sent. The case is closed as replied with nothing left for a person, though the requester was not verified.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-05 09:00:00 UTC

The request:

> I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage.

What happened up to now:

1. 2025-10-05T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> I show an outgoing payment of £74.00 dated 14 July 2025 in your transaction history. Its reference is HV-040 and its bank status is SENT.

2. 2025-10-05T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate.

3. 2025-10-05T10:34:00Z · Internal note — H&V service agent → H&V document service

> I matched the customer’s request to payment HV-040 in the authenticated secure-portal session. Please generate the payment record for this operation for delivery to the customer’s secure portal.

4. 2025-10-05T11:21:00Z · Internal note — H&V document service → H&V service agent

> Record HV-040 generated for the payment dated 14 July 2025, amount £74.00. The bank status on the record is SENT.

Attachments: none.

Case reference: id banking-040-at-04, track Banking & Financial Services, case 040, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The document record shows that the document is available. This does not confirm that the document was downloaded or that funds were credited. No email was sent.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `documents-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - document_ready → true (document_ready=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- amount: **74.00**
- reference: **HV-040**
- documents_asked: **True**
- document_ready: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- initial request (system): I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage. [facts: amount='74.00']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: reference='HV-040']
- event 3 (H&V document service): I matched the customer’s request to payment HV-040 in the authenticated secure-portal session. Please generate the payment record for this operation for delivery to the customer’s secure portal. [facts: documents_asked=True]
- event 4 (H&V document service): Record HV-040 generated for the payment dated 14 July 2025, amount £74.00. The bank status on the record is SENT. [facts: document_ready=True]
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

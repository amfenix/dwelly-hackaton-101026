# Case banking-040-at-03: Confirmation of a Specific Payment

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing over secure chat, asked for a document showing the current stage of her £74.00 payment HV-040 so she could give evidence of it to her repair contractor. The desk matched the request to the documents system and asked it to generate the payment record, but its answer has not come back, so the case closed as waiting and no actions were taken. The record shows her identity as not verified; what is left is the documents system's reply, which has not yet arrived.

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

Attachments: none.

Case reference: id banking-040-at-03, track Banking & Financial Services, case 040, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `documents-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - documents_asked → true (documents_asked=True)
  - document_ready absent → true (document_ready=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- amount: **74.00**
- reference: **HV-040**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- initial request (system): I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage. [facts: amount='74.00']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: reference='HV-040']
- event 3 (H&V document service): I matched the customer’s request to payment HV-040 in the authenticated secure-portal session. Please generate the payment record for this operation for delivery to the customer’s secure portal. [facts: documents_asked=True]
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

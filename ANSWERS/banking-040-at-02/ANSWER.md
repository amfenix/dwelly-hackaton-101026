# Case banking-040-at-02: Confirmation of a Specific Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, an unverified customer on secure chat, asked for a document showing the stage of her £74.00 payment (reference HV-040) to give to her repair contractor. The desk classed it as a document question and sent a query about HV-040 to the documents system, and the case closed in the asked state. The desk's attempt to send Mara a reply was refused because no document status had come back, so nothing has been sent to her and the answer from the documents system is still outstanding.

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

Attachments: none.

Case reference: id banking-040-at-02, track Banking & Financial Services, case 040, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: documents, about: document, reference: HV-040, amount: 74.00), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `documents-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = documents → true (args.system=documents)
  - next_system = documents → true (next_system=documents)
  - next_system absent → false (next_system=documents)
  - documents_asked absent → true (documents_asked=not known)
  - document_ready = false → not known (document_ready=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- amount: **74.00**
- reference: **HV-040**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- initial request (system): I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage. [facts: amount='74.00']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: reference='HV-040']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=documents); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

# Case banking-040-at-02: Confirmation of a Specific Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, an unverified customer on secure chat, asked for a document showing the current stage of her £74.00 payment HV-040 so she could share it with her repair contractor. The desk classified this as a document request about a transfer and sent a query to the payment system about HV-040 for £74.00. The query returned nothing, no document was produced or sent to her, and the case closed in the asked state, so a person would need to follow up with her.

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

- `ask_system` (system: payment, about: transfer, reference: HV-040, amount: 74.00), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=document)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **74.00**
- reference: **HV-040**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- initial request (system): I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage. [facts: amount='74.00']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: reference='HV-040']
- event 2 (Mara Ellison): I need a record for this particular payment to give my repair contractor. I can see HV-040 in my history, but I need a document showing its stage; I understand that the contractor’s confirmation of receipt is separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

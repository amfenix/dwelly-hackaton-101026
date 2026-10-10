# Case banking-040-at-01: Confirmation of a Specific Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked for a document showing the current stage of their £74.00 payment to a repair contractor, so they could share evidence of it. The desk classified this as a document question and sent a request to the documents system about the £74.00 payment. The bank history shows the payment as sent (reference HV-040). The case closed with that request made and no reply yet, so no document has gone to the customer and a person or later step must act once the documents system answers.

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

Attachments: none.

Case reference: id banking-040-at-01, track Banking & Financial Services, case 040, point 1, actor_next other.

## Actions taken

- `ask_system` (system: documents, about: document, amount: 74.00), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **document**
- amount: **74.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- initial request (system): I need a copy of the bank record for my £74.00 payment to a repair contractor, so I can share evidence of the payment with them. I can see the transaction in my secure portal, but need a document showing its current stage. [facts: amount='74.00']
- event 1 (Harrow & Vale Bank plc): I show an outgoing payment of £74.00 dated 14 July 2025 in your transaction history. Its reference is HV-040 and its bank status is SENT. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

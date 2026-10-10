# Case banking-044-at-01: One Line in the Supplier Batch

**Decision: ask_system**  (final state `ASKED`)

## Summary

The requester wanted to know whether the payment on row SUP-17 in their supplier batch was paid or rejected, since the batch only showed as processed. The desk classified this as a question about a batch and sent an inquiry about SUP-17 to the payment system, and the case closed in the asked state. The desk then tried to send a reply, but that was refused because no payment status had come back, so the requester has not yet been told whether the payment was paid or rejected.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-13 09:00:00 UTC

The request:

> I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected.

What happened up to now:

1. 2025-10-13T09:00:00Z · Business portal — H&V secure portal → Leona Voss

> Batch “Alderwick supplier payments” — status: Processed.

Attachments: none.

Case reference: id banking-044-at-01, track Banking & Financial Services, case 044, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: batch, reference: SUP-17), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **batch**
- reference: **SUP-17**
- request_type: **question**
- next_system: **payment**

Where they came from:

- initial request (system): I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected. [facts: reference='SUP-17']

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=payment); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

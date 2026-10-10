# Case banking-009-at-01: Confirming the amount sent

**Decision: ask_system**  (final state `ASKED`)

## Summary

The requester remembered entering £684.20 in a transfer draft but saw £648.20 on the final payment line, and asked the desk to confirm what amount H&V actually sent. The desk read the record, found the £648.20 payment line with no separate confirmation, and put a question about the transfer and that amount to the payment system, then closed the case as asked. Nothing has come back from the payment system yet, and the desk's attempt to reply to the requester was refused, so the sent amount is unconfirmed and a person needs to pick the case up.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-04 09:00:00 UTC

The request:

> I remember entering £684.20 in the transfer draft, but the final payment line shows £648.20. Please confirm the amount H&V actually sent.

What happened up to now:

1. 2025-08-04T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellwood

> Final payment line: £648.20 sent to your property manager.

Attachments: none.

Case reference: id banking-009-at-01, track Banking & Financial Services, case 009, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 648.20), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- amount: **648.20**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **payment**

Where they came from:

- initial request (system): I remember entering £684.20 in the transfer draft, but the final payment line shows £648.20. Please confirm the amount H&V actually sent. [facts: amount='648.20']
- event 1 (Harrow & Vale Bank plc): Final payment line: £648.20 sent to your property manager. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

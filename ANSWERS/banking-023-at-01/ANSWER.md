# Case banking-023-at-01: Unrecognised card purchase

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

The customer asked the bank to investigate a posted card purchase of £38.40 at Fern & Finch Books on 14 July 2025, which they did not recognise, and to tell them how to protect their card. The desk registered a request with the card team about the card payment, and the case closed as requested. A separate attempt to ask the card system a question was refused. The record does not show the card-protection advice being handled by the desk, and the agent's reply says that part has not yet been answered, so that is left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-01 09:00:00 UTC

The request:

> I want H&V to investigate a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025, which I do not recognise, and tell me how I can safely protect my card.

What happened up to now:

1. 2025-09-01T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> I show a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025. Its appearance in your transaction list does not establish who made it.

Attachments: none.

Case reference: id banking-023-at-01, track Banking & Financial Services, case 023, point 1, actor_next other.

## Actions taken

- `register_request` (team: card, about: card_payment), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `register` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = register → true (request_type=register)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- subject: **card_payment**
- amount: **38.40**
- subject_date: **2025-07-14**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **card**

Where they came from:

- initial request (system): I want H&V to investigate a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025, which I do not recognise, and tell me how I can safely protect my card. [facts: amount='38.40', subject_date='2025-07-14']
- event 1 (Harrow & Vale Bank plc): I show a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025. Its appearance in your transaction list does not establish who made it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); card-ask: next_system absent is false (next_system=card); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

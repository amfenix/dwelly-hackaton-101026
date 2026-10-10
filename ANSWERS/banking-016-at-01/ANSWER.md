# Case banking-016-at-01: Disputed Direct Debit amount

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

The customer asked for the £18.40 Direct Debit to Northmere Water Services (dated 9 July 2025) to be investigated because they dispute the amount debited. The desk classed it as a request to register, refused its attempt to query the recurring-payments system for this request type, and instead registered the request with the recurring team about the direct debit, closing the case as requested. The record shows no further steps and no outcome yet from that team, so the dispute itself is left for them.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-18 09:00:00 UTC

The request:

> I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited.

What happened up to now:

1. 2025-08-18T09:00:00Z · Secure portal — H&V secure portal → Tamsin Rook

> Statement activity: Direct Debit to Northmere Water Services — £18.40, dated 9 July 2025.

Attachments: none.

Case reference: id banking-016-at-01, track Banking & Financial Services, case 016, point 1, actor_next other.

## Actions taken

- `register_request` (team: recurring, about: direct_debit), by rule `do-request`

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

- subject: **direct_debit**
- amount: **18.40**
- counterparty: **Northmere Water Services because I dispute the amount debited**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **recurring**

Where they came from:

- initial request (system): I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited. [facts: amount='18.40', counterparty='Northmere Water Services because I dispute the amount debited']
- event 1 (H&V secure portal): Statement activity: Direct Debit to Northmere Water Services — £18.40, dated 9 July 2025. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

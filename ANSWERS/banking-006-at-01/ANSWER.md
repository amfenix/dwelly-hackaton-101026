# Case banking-006-at-01: Two Similar Transfers

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

The requester asked about two similar outgoing transfers to North Quay Utilities for £84.20, one marked Completed and one Pending. The desk's direct ask to the payment system was refused because this is a registration-type request, so it registered a request with the payment team about the transfer instead. The payment records have not been checked, it is not known whether the entries are a duplicate, and nothing has been stopped or returned; that is left to the payment team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-29 09:00:00 UTC

The request:

> Mira, the account holder, wants H&V to establish whether two similar outgoing transfer entries are one instruction shown twice or two separate instructions, and asks whether the second can be stopped or returned.

What happened up to now:

1. 2025-07-29T09:00:00Z · Secure portal — H&V → Mira Ellison

> Your payment activity shows two similar outgoing transfer entries to North Quay Utilities for £84.20. One is marked Completed and the other Pending.

Attachments: none.

Case reference: id banking-006-at-01, track Banking & Financial Services, case 006, point 1, actor_next other.

## Actions taken

- `register_request` (team: payment, about: transfer), by rule `do-request`

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

- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **payment**

Where they came from:

- event 1 (H&V): Your payment activity shows two similar outgoing transfer entries to North Quay Utilities for £84.20. One is marked Completed and the other Pending. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, instruction, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

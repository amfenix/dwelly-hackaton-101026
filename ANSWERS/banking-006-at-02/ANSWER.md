# Case banking-006-at-02: Two Similar Transfers

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mira Ellison, an unverified customer on secure chat, asked the desk to check whether two transfer instructions were separate and whether the pending one had been stopped or returned. The desk classed it as a request to register, refused the payment lookup because of that, and instead registered a request with the payment team about the transfer, so the case closed as REQUESTED. The desk did not establish whether the instructions are separate or whether the pending one was stopped or returned, so that remains open for a person, and her identity is still unverified.

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

2. 2025-07-29T09:47:00Z · Secure chat — Mira Ellison → H&V agent

> I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned.

Attachments: none.

Case reference: id banking-006-at-02, track Banking & Financial Services, case 006, point 2, actor_next bank.

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

- requester: **Mira Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **payment**

Where they came from:

- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: requester='Mira Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

# Case 029: Balance after a payment recovery request

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Enna Prysett asked the desk to restore £3,200 and confirm the sender had already been repaid, and also said she needs money for food in

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Enna Prysett
- Created: 2026-11-19 09:00+00:00
- Operator: Brackenfold Bank case desk

The request:

> Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted.

What happened up to now:

1. 2026-11-19T09:00:00Z · Internal ledger view — Brackenfold Bank account service → Brackenfold Bank case desk

> Morning booked entries: opening £500, incoming disputed payment £2,000, ordinary customer outgoing payment £600. Current booked ledger £1,900. Customer contact authentication passed.

2. 2026-11-19T09:10:00Z · Interbank request record — Synthetic Sender Bank → Brackenfold Bank recovery team

> Recovery requested for incoming reference IN-029, amount £2,000. Request received; investigation pending. This bank’s process assigns recovery decisions and hold reviews to the recovery team; case desk may request current status and hardship review.

3. 2026-11-19T09:15:00Z · Internal recovery view — Brackenfold Bank recovery team → Brackenfold Bank case desk

> Current reservation and recovery-status packet attached.
> 
> Attachments: [ledger-and-reservations.csv](attachments/ledger-and-reservations.csv), [recovery-status.json](attachments/recovery-status.json)

4. 2026-11-19T09:20:00Z · Authenticated customer chat — Enna Prysett → Brackenfold Bank case desk

> My screen says “recovery requested £2,000” and “reserved £1,200”. I copied those labels here. Did you take both? My available balance says £700.

5. 2026-11-19T09:25:00Z · Customer chat — Enna Prysett → Brackenfold Bank case desk

> Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted.

Attachments: `ledger-and-reservations.csv`, `recovery-status.json`.

Case reference: id 029, track Banking & Financial Services, case 029, point 5.

## Actions taken

- `register_request` (team: incoming, about: incoming_payment), by rule `do-request`

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

- requester: **Enna Prysett**
- role: **customer**
- subject: **incoming_payment**
- amount: **3200.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **incoming**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: requester='Enna Prysett', role='customer']
- event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: amount='3200.00']
- event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=incoming); next_system = payment is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=incoming); next_system = recurring is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=incoming); next_system = card is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: args.system = access is false (args.system=incoming); next_system = access is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=incoming); next_system = business is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=incoming); next_system = documents is false (next_system=incoming); next_system absent is false (next_system=incoming); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=incoming); next_system = tariff is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

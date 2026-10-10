# Case banking-019-at-05: Standing order date change

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Maeve Ellery, verified and writing through the secure portal, asked to move the next run of her standing order to Willow Yard Studios from 18 September to 22 September 2025, and she confirmed the change. The desk's query to the recurring system about the processing stage was refused, so it registered a change request with the recurring team instead, and the case closed as requested. The record doesn't show the date actually being changed or the processing stage being checked, so the recurring team still has to act on the request.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-24 09:00:00 UTC

The request:

> I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation.

What happened up to now:

1. 2025-08-24T09:00:00Z · Secure portal — H&V secure portal → Maeve Ellery

> Standing order status: active. Next scheduled run: 18 September 2025.

2. 2025-08-24T09:47:00Z · Secure chat — Maeve Ellery → H&V service agent

> I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation.

3. 2025-08-24T10:34:00Z · Internal note — H&V service agent → H&V case record

> I checked the active standing order and its next-run stage. The 18 September 2025 run is not yet being processed, so I can send the requested date change to Maeve for her secure confirmation.

4. 2025-08-24T11:21:00Z · Secure portal — H&V service agent → Maeve Ellery

> I’ve checked that the next run is not yet being processed and have sent the requested change from 18 September to 22 September 2025 for your secure confirmation. I have not changed the instruction on your behalf.

5. 2025-08-24T12:08:00Z · Secure portal — Maeve Ellery → H&V secure portal

> I confirm the change to 22 September 2025 for the next run of my standing order.

Attachments: none.

Case reference: id banking-019-at-05, track Banking & Financial Services, case 019, point 5, actor_next bank.

## Actions taken

- `register_request` (team: recurring, about: standing_order), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `recurring-instruction` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - verified → true (verified=True)
  - request_type = instruction → false (request_type=change)
  - request_type = change → true (request_type=change)
  - confirmation = given → true (confirmation=given)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Maeve Ellery**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **standing_order**
- counterparty: **Willow Yard Studios**
- subject_date: **2025-09-18**
- confirmation: **given**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- event 5 (Maeve Ellery): I confirm the change to 22 September 2025 for the next run of my standing order. [facts: requester='Maeve Ellery', role='customer', channel='secure_portal', verified=True]
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: counterparty='Willow Yard Studios']
- initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: subject_date='2025-09-18']
- event 5 (Maeve Ellery): I confirm the change to 22 September 2025 for the next run of my standing order. [facts: confirmation='given']
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

submit_request (REQUESTED)

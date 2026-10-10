# Case banking-019-at-05: Standing order date change

**Decision: wait**  (final state `WAITING`)

## Summary

Maeve Ellery, verified in the secure portal, asked to move the next run of her monthly standing order to Willow Yard Studios from 18 September to 22 September 2025, and she confirmed the change. The desk decided to wait: its rule says the system applies a customer-confirmed change, so no action was taken by the desk, and the case closed in a waiting state. The agent's later attempt to submit the request was refused because the case was no longer in a state that allows it, so nothing was submitted and the order still shows 18 September. The record does not say who picks the case up next or when the system will apply the change.

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

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `change-applied-by-the-system` — The customer confirmed the change in the secure portal; the system applies it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = given → true (confirmation=given)
  - registration_asked absent → true (registration_asked=not known)

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

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=change); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = instruction is false (request_type=change); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = instruction is false (request_type=change); recurring-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=change); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = instruction is false (request_type=change); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = instruction is false (request_type=change); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = instruction is false (request_type=change); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = instruction is false (request_type=change)

## Final result

wait (WAITING)

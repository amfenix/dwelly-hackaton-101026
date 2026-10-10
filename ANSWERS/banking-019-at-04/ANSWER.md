# Case banking-019-at-04: Standing order date change

**Decision: wait**  (final state `WAITING`)

## Summary

Maeve Ellery asked the desk to check whether the next run of her Willow Yard Studios standing order could still be moved from 18 September to 22 September 2025, and to send any eligible change to her for confirmation. The desk found the change had been sent to her for secure confirmation, changed nothing on the instruction itself, and closed the case as waiting. What is left is for Maeve to confirm the change in the secure portal; she had been identified but not verified, and her message was sent outside the portal.

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

Attachments: none.

Case reference: id banking-019-at-04, track Banking & Financial Services, case 019, point 4, actor_next other.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `change-waits-for-the-customer` — The change was sent to the portal; the customer has not confirmed it yet.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = requested → true (confirmation=requested)
  - registration_asked absent → true (registration_asked=not known)

Facts established:

- requester: **Maeve Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- counterparty: **Willow Yard Studios**
- subject_date: **2025-09-18**
- confirmation: **requested**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: requester='Maeve Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: counterparty='Willow Yard Studios']
- initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: subject_date='2025-09-18']
- event 4 (H&V service agent): I’ve checked that the next run is not yet being processed and have sent the requested change from 18 September to 22 September 2025 for your secure confirmation. I have not changed the instruction on your behalf. [facts: confirmation='requested']
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

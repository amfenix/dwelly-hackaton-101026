# Case banking-019-at-02: Standing order date change

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Maeve Ellery, an unverified customer on secure chat, asked to move the next run of her standing order to Willow Yard Studios from 18 September to 22 September 2025 and to have any eligible change sent to her for confirmation. The desk treated it as a change needing her confirmation, sent it to her for confirmation, and closed the case in that state. The desk's later request to check the recurring system's processing stage was refused because the case had already closed, so whether the run can still be moved is not established, and the standing order has not been changed. What remains is her confirmation, which the record shows had not yet been given.

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

Attachments: none.

Case reference: id banking-019-at-02, track Banking & Financial Services, case 019, point 2, actor_next bank.

## Actions taken

- `send_for_confirmation` (change: standing_order, counterparty=Willow Yard Studios, date=2025-09-18, to: Maeve Ellery), by rule `do-confirm`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `CONFIRM_PENDING`: rule `change-needs-confirmation` — A change is confirmed by the customer in the secure portal, not in chat or by email.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = none → true (confirmation=none)
  - registration_asked absent → true (registration_asked=not known)
- `CONFIRM_PENDING` → `CONFIRMATION_SENT`: rule `do-confirm`.
  - state = CONFIRM_PENDING → true (state=CONFIRM_PENDING)

Facts established:

- requester: **Maeve Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- counterparty: **Willow Yard Studios**
- subject_date: **2025-09-18**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: requester='Maeve Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: counterparty='Willow Yard Studios']
- initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: subject_date='2025-09-18']
- event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

send_for_confirmation (CONFIRMATION_SENT)

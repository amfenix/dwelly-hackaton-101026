# Case banking-012-at-05: New standing-order amount

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mira Ellery, a verified customer on the secure portal, asked to raise her standing order to Westmere Garden Cooperative from £42.00 to £68.00 a month and confirmed the change. The desk refused a preliminary ask of the recurring system, since a change request is not allowed that step, then submitted the request, and a request about the standing order was registered with the recurring team and the case closed as REQUESTED. The record does not show the standing order itself being changed, so that remains with the recurring team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-10 09:00:00 UTC

The request:

> Mira wants to increase her monthly standing order to the fictional Westmere Garden Cooperative from £42.00 to £68.00. She has not yet authorised the change.

What happened up to now:

1. 2025-08-10T09:00:00Z · Secure portal — H&V system → Mira Ellery

> Standing order to Westmere Garden Cooperative: £42.00 per month.

2. 2025-08-10T09:47:00Z · Secure chat — Mira Ellery → H&V agent

> I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet.

3. 2025-08-10T10:34:00Z · Internal note — H&V agent → H&V case record HV-012

> I checked that Mira is the verified owner of this standing order and may amend it. Her chat request is not authorisation, so the order remains unchanged until she confirms in the secure portal.

4. 2025-08-10T11:21:00Z · Secure portal — H&V agent → Mira Ellery

> I’ve sent the change from £42.00 to £68.00 per month for your confirmation in this session. I have not changed the standing order.

5. 2025-08-10T12:08:00Z · Secure portal — Mira Ellery → H&V

> I confirm the change to £68.00 per month for my standing order to Westmere Garden Cooperative.

Attachments: none.

Case reference: id banking-012-at-05, track Banking & Financial Services, case 012, point 5, actor_next bank.

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

- requester: **Mira Ellery**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **standing_order**
- amount: **68.00**
- counterparty: **Westmere Garden Cooperative**
- confirmation: **given**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- event 5 (Mira Ellery): I confirm the change to £68.00 per month for my standing order to Westmere Garden Cooperative. [facts: requester='Mira Ellery', role='customer', channel='secure_portal', verified=True]
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: amount='68.00']
- event 5 (Mira Ellery): I confirm the change to £68.00 per month for my standing order to Westmere Garden Cooperative. [facts: counterparty='Westmere Garden Cooperative']
- event 5 (Mira Ellery): I confirm the change to £68.00 per month for my standing order to Westmere Garden Cooperative. [facts: confirmation='given']
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

submit_request (REQUESTED)

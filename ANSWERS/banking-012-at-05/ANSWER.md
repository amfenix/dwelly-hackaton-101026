# Case banking-012-at-05: New standing-order amount

**Decision: wait**  (final state `WAITING`)

## Summary

_No summary: malformed: no text in the response (stop: max_tokens)._

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

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=change); register-what-fits-no-type: state = TRIAGED is false (state=WAITING); request_type = other is false (request_type=change); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = instruction is false (request_type=change); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = instruction is false (request_type=change); recurring-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=change); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = instruction is false (request_type=change); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = instruction is false (request_type=change); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = instruction is false (request_type=change); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = instruction is false (request_type=change)
- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

wait (WAITING)

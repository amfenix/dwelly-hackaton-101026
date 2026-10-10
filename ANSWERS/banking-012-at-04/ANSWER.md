# Case banking-012-at-04: New standing-order amount

**Decision: wait**  (final state `WAITING`)

## Summary

Mira Ellery, a customer writing over secure chat, asked to raise her standing order from £42.00 to £68.00 a month. The desk sent the change to her in the portal for confirmation, made no change to the standing order, and closed the case as waiting. The order stays at £42.00 until she confirms the change herself in the portal; the record also notes she is not verified and gave her instruction outside the portal.

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

Attachments: none.

Case reference: id banking-012-at-04, track Banking & Financial Services, case 012, point 4, actor_next other.

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

- requester: **Mira Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- amount: **68.00**
- confirmation: **requested**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: requester='Mira Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: amount='68.00']
- event 4 (H&V agent): I’ve sent the change from £42.00 to £68.00 per month for your confirmation in this session. I have not changed the standing order. [facts: confirmation='requested']
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

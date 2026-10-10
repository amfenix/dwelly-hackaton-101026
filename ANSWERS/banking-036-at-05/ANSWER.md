# Case banking-036-at-05: New correspondence address

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellison, a verified customer writing through the secure portal, asked to change the correspondence address on her profile and confirmed she wanted the new address used. The desk accepted this as a change request and registered it with the access team about her profile, and the case closed in the REQUESTED state. The record does not show the change being applied to her profile, so that remains with the access team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-27 09:00:00 UTC

The request:

> I have moved within the UK and want H&V to update the address used for my correspondence.

What happened up to now:

1. 2025-09-27T09:00:00Z · External message — Mara Ellison → Harrow & Vale Bank plc

> I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile.

2. 2025-09-27T09:47:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I’m escalating my request to change my correspondence address. I have completed the identity checks in this secure session and can confirm the change when the profile process asks me to.

3. 2025-09-27T10:34:00Z · Internal note — H&V service agent → H&V profile change process

> I have checked Mara’s identity and reviewed the workflow’s requirements. I’m opening the address-change process for case HV-036; no address is recorded in this note.

4. 2025-09-27T11:21:00Z · Secure portal — Mara Ellison → H&V profile change process

> I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence.

5. 2025-09-27T12:08:00Z · Internal note — H&V service agent → H&V profile change process

> I have submitted the verified request with the confirmations required by the workflow. I have not changed the address on Mara’s behalf without her secure confirmation.

Attachments: none.

Case reference: id banking-036-at-05, track Banking & Financial Services, case 036, point 5, actor_next bank.

## Actions taken

- `register_request` (team: access, about: profile), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `access-instruction` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = access → true (next_system=access)
  - access_asked absent → true (access_asked=not known)
  - verified → true (verified=True)
  - request_type = instruction → false (request_type=change)
  - request_type = change → true (request_type=change)
  - confirmation = given → true (confirmation=given)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **profile**
- confirmation: **given**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 4 (Mara Ellison): I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 4 (Mara Ellison): I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence. [facts: confirmation='given']
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

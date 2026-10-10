# Case banking-036-at-04: New correspondence address

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellison, a verified customer writing through the secure portal, asked the bank to update her correspondence address and confirmed the change herself. The desk registered a profile change request with the access team and closed the case as submit_request. The agent's later attempts to submit again, redirect to the secure process and escalate were all refused because the case was already closed in REQUESTED, and nothing in the record shows the address itself was changed, so any further processing is for the access team.

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

Attachments: none.

Case reference: id banking-036-at-04, track Banking & Financial Services, case 036, point 4, actor_next bank.

## Actions taken

- `register_request` (team: access, about: profile), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: rule `unprompted-confirmation-is-passed-on` — The customer confirmed the change on their own; the bank passes the confirmed change on.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = unprompted → true (confirmation=unprompted)
  - verified → true (verified=True)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **profile**
- access_asked: **True**
- confirmation: **unprompted**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 4 (Mara Ellison): I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 3 (H&V profile change process): I have checked Mara’s identity and reviewed the workflow’s requirements. I’m opening the address-change process for case HV-036; no address is recorded in this note. [facts: access_asked=True]
- event 4 (Mara Ellison): I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence. [facts: confirmation='unprompted']
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=REQUESTED); request_type = register is false (request_type=change); register-what-fits-no-type: state = TRIAGED is false (state=REQUESTED); request_type = other is false (request_type=change); payment-instruction: state = TRIAGED is false (state=REQUESTED); next_system = payment is false (next_system=access); request_type = instruction is false (request_type=change); incoming-instruction: state = TRIAGED is false (state=REQUESTED); next_system = incoming is false (next_system=access); request_type = instruction is false (request_type=change); recurring-instruction: state = TRIAGED is false (state=REQUESTED); next_system = recurring is false (next_system=access); request_type = instruction is false (request_type=change); card-instruction: state = TRIAGED is false (state=REQUESTED); next_system = card is false (next_system=access); request_type = instruction is false (request_type=change); access-instruction: state = TRIAGED is false (state=REQUESTED); access_asked absent is false (access_asked=True); request_type = instruction is false (request_type=change); business-instruction: state = TRIAGED is false (state=REQUESTED); next_system = business is false (next_system=access); request_type = instruction is false (request_type=change); documents-instruction: state = TRIAGED is false (state=REQUESTED); next_system = documents is false (next_system=access); request_type = instruction is false (request_type=change)
- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=REQUESTED); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change); not verified is false (verified=True)
- `escalate`: agent-escalates: state = TRIAGED is false (state=REQUESTED)

## Final result

submit_request (REQUESTED)

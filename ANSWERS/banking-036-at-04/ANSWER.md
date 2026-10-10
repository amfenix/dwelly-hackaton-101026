# Case banking-036-at-04: New correspondence address

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Mara Ellison, a verified customer, asked the desk to update the address it uses for her correspondence after she moved within the UK. Her email alone cannot change her profile, so the desk sent her a request to confirm the profile change and closed the case at that point. What is left is for Mara to confirm the change in the secure portal, as the record still shows no confirmation from her.

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

- `send_for_confirmation` (change: profile, to: Mara Ellison), by rule `do-confirm`

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **profile**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 4 (Mara Ellison): I confirm that I want H&V to use the new address I provided through the secure profile process for future correspondence. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

send_for_confirmation (CONFIRMATION_SENT)

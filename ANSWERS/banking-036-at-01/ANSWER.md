# Case banking-036-at-01: New correspondence address

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Mara Ellison, writing by external email, asked the desk to update the correspondence address on her profile after a move within the UK. She was not verified and had sent the request outside the portal, so the desk did not change anything and instead sent her a confirmation request for the profile change. Her profile stays as it is until she confirms through the secure portal, and nothing failed or was refused.

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

Attachments: none.

Case reference: id banking-036-at-01, track Banking & Financial Services, case 036, point 1, actor_next other.

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
- channel: **external_message**
- verified: **False**
- subject: **profile**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: requester='Mara Ellison', role='customer', channel='external_message', verified=False]
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

send_for_confirmation (CONFIRMATION_SENT)

# Case banking-036-at-01: New correspondence address

**Decision: redirect_secure**  (final state `REDIRECTED`)

## Summary

Mara Ellison, an unverified customer, emailed to ask that the address used for her correspondence be updated after a move within the UK. The desk did not change her profile; it replied to her by message, pointing her to the secure portal process, where her identity is checked, and saying nothing was changed. The case is closed as redirected, and a second redirect attempt was refused because the case was already in that state. Making the address change in the secure portal is left to Mara.

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

- `redirect_secure` (to: Mara Ellison, channel: external_message), by rule `do-redirect`

  > Please use the secure process in your secure portal to do this; it checks your identity there. We will never ask for your password, PIN or a verification code. Nothing on your profile was changed.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REDIRECT_PENDING`: rule `change-by-email` — An email does not change anything; the customer is pointed to the secure process.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - channel = external_message → true (channel=external_message)
  - role != third_party → true (role=customer)
- `REDIRECT_PENDING` → `REDIRECTED`: rule `do-redirect`.
  - state = REDIRECT_PENDING → true (state=REDIRECT_PENDING)

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
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: requester='Mara Ellison', role='customer', channel='external_message', verified=False]
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=REDIRECTED); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change)

## Final result

redirect_secure (REDIRECTED)

# Case banking-028-at-02: New phone number in profile

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Elowen Mercer, a verified customer on a call, asked to change the phone number on her profile because she no longer has her old phone, and asked for the approved way to confirm a replacement. The desk treated it as a profile change and registered a request with the access team, which completed without error. The record shows no confirmation of the replacement number and nothing further for a person to do beyond the access team handling the registered request.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-11 09:00:00 UTC

The request:

> I need to replace the phone number on my H&V profile. I no longer have access to the old phone, and I want to use the bank’s approved confirmation process.

What happened up to now:

1. 2025-09-11T09:00:00Z · External message — Elowen Mercer → Harrow & Vale Bank plc

> I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change.

2. 2025-09-11T09:47:00Z · Verified call — Elowen Mercer → H&V service agent

> After you completed H&V’s identification checks, I explained that the old phone is unavailable and asked for this to be escalated. I can confirm the replacement number through a secure bank process.

Attachments: none.

Case reference: id banking-028-at-02, track Banking & Financial Services, case 028, point 2, actor_next bank.

## Actions taken

- `register_request` (team: access, about: profile), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: rule `profile-change-to-the-process` — A verified customer's profile change is started in the protected change process.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - subject = profile → true (subject=profile)
  - access_asked absent → true (access_asked=not known)
  - verified → true (verified=True)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Elowen Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Elowen Mercer): After you completed H&V’s identification checks, I explained that the old phone is unavailable and asked for this to be escalated. I can confirm the replacement number through a secure bank process. [facts: requester='Elowen Mercer', role='customer', channel='verified_call', verified=True]
- event 1 (Elowen Mercer): I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

# Case banking-028-at-04: New phone number in profile

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Mercer, a verified customer, asked to change the phone number on her profile because she no longer has her old phone, and she said her email was a request, not her authorisation. The desk started the bank's secure profile-change process, which has asked her to review the replacement number and confirm it. It has not changed the number or bypassed the old-device check, and the case closed in a waiting state. What is left is for her to confirm the change in the secure portal; the desk's attempt to send a separate written reply was refused because the case was already waiting.

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

3. 2025-09-11T10:34:00Z · Secure portal — H&V service agent → H&V secure profile-change process

> I have started the approved phone-number change process following the verified call. I have not changed the profile number or bypassed the old-device check; the customer must confirm the change securely.

4. 2025-09-11T11:21:00Z · Secure portal — H&V secure profile-change process → Elowen Mercer

> Please review the replacement number entered in this secure process and confirm whether you want it applied to your profile. No change will be made until you confirm.

Attachments: none.

Case reference: id banking-028-at-04, track Banking & Financial Services, case 028, point 4, actor_next other.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `profile-change-waits-for-the-process` — The protected change process is running; it asks the customer to confirm.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - subject = profile → true (subject=profile)
  - access_asked → true (access_asked=True)
  - confirmation in [none, requested] → true (confirmation=requested)

Facts established:

- requester: **Elowen Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- access_asked: **True**
- confirmation: **requested**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Elowen Mercer): After you completed H&V’s identification checks, I explained that the old phone is unavailable and asked for this to be escalated. I can confirm the replacement number through a secure bank process. [facts: requester='Elowen Mercer', role='customer', channel='verified_call', verified=True]
- event 3 (H&V secure profile-change process): I have started the approved phone-number change process following the verified call. I have not changed the profile number or bypassed the old-device check; the customer must confirm the change securely. [facts: access_asked=True]
- event 4 (H&V secure profile-change process): Please review the replacement number entered in this secure process and confirm whether you want it applied to your profile. No change will be made until you confirm. [facts: confirmation='requested']
- event 1 (Elowen Mercer): I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change. [facts: instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=access); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=profile); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=access); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=access); tariff_status present is false (tariff_status=not known)

## Final result

wait (WAITING)

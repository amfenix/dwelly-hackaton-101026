# Case banking-028-at-01: New phone number in profile

**Decision: redirect_secure**  (final state `REDIRECTED`)

## Summary

Elowen Mercer emailed asking to change the phone number on her profile because she no longer has her old phone, and asked for the approved way to confirm a replacement. She is not verified and her email said it was not authorisation, so the desk changed nothing and sent her a message pointing her to the secure process in her portal, which checks identity there. The case closed as redirected, and two later attempts, one to query the access system and one to resend the redirect, were refused because the case was already closed; nothing is left for a person in the record.

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

Attachments: none.

Case reference: id banking-028-at-01, track Banking & Financial Services, case 028, point 1, actor_next other.

## Actions taken

- `redirect_secure` (to: Elowen Mercer, channel: external_message), by rule `do-redirect`

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

- requester: **Elowen Mercer**
- role: **customer**
- channel: **external_message**
- verified: **False**
- subject: **profile**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 1 (Elowen Mercer): I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change. [facts: requester='Elowen Mercer', role='customer', channel='external_message', verified=False]
- event 1 (Elowen Mercer): I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=REDIRECTED); args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=REDIRECTED); args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=REDIRECTED); args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=REDIRECTED); args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=REDIRECTED); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=REDIRECTED); args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=REDIRECTED); args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=REDIRECTED); args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change)
- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=REDIRECTED); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change)

## Final result

redirect_secure (REDIRECTED)

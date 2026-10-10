# Case banking-028-at-03: New phone number in profile

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Mercer, verified on a call, asked to replace the phone number on her profile because she no longer has her old phone. The desk made no change to the number and closed the case as waiting: the bank's protected profile-change process is already running and asks her to confirm the change securely, and no confirmation has been recorded yet. The desk refused two further requests made after the case reached waiting, one to ask the access system again and one to redirect her to the secure process, so nothing else was done, and the change stays pending until she confirms it.

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

Attachments: none.

Case reference: id banking-028-at-03, track Banking & Financial Services, case 028, point 3, actor_next bank.

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
  - confirmation in [none, requested] → true (confirmation=none)

Facts established:

- requester: **Elowen Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- access_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Elowen Mercer): After you completed H&V’s identification checks, I explained that the old phone is unavailable and asked for this to be escalated. I can confirm the replacement number through a secure bank process. [facts: requester='Elowen Mercer', role='customer', channel='verified_call', verified=True]
- event 3 (H&V secure profile-change process): I have started the approved phone-number change process following the verified call. I have not changed the profile number or bypassed the old-device check; the customer must confirm the change securely. [facts: access_asked=True]
- event 1 (Elowen Mercer): I need to change the phone number on my profile because I no longer have access to my old phone. Please tell me the approved way to confirm a replacement; this email is a request, not my authorisation to make the change. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=access); access_asked absent is false (access_asked=True); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change)
- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=WAITING); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change); not verified is false (verified=True)

## Final result

wait (WAITING)

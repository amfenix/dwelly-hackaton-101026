# Case banking-037-at-04: Profile Name Typo

**Decision: reply**  (final state `REPLIED`)

## Summary

Elowen Marr, verified on a call, asked for her profile name to be corrected from "Elowen Mar" to "Elowen Marr". The desk logged the request with the H&V data team as reference HV-037 and replied to her. The data team has not yet validated the basis for the correction, and the profile name is unchanged. Whatever supporting information the data team needs, and the correction itself, remains for a person to handle.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-29 09:00:00 UTC

The request:

> Please correct the spelling of my name in my H&V profile. It shows “Elowen Mar”; my correct name is “Elowen Marr”.

What happened up to now:

1. 2025-09-29T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Elowen Marr

> Profile status: The name displayed in your profile is “Elowen Mar”.

2. 2025-09-29T09:47:00Z · Verified call — Elowen Marr → H&V service agent

> After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information.

3. 2025-09-29T10:34:00Z · Internal note — H&V service agent → H&V data team

> I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made.

4. 2025-09-29T11:21:00Z · Internal note — H&V data team → H&V service agent

> I have logged HV-037 as received for review. The basis for the correction has not yet been validated, and the profile name remains unchanged.

Attachments: none.

Case reference: id banking-037-at-04, track Banking & Financial Services, case 037, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `registration-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=change)
  - registration_asked → true (registration_asked=True)
  - registered present → true (registered=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- registration_asked: **True**
- registered: **True**
- registration_ref: **HV-037**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **access**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: requester='Elowen Marr', role='customer', channel='verified_call', verified=True]
- event 3 (H&V data team): I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made. [facts: registration_asked=True]
- event 4 (H&V data team): I have logged HV-037 as received for review. The basis for the correction has not yet been validated, and the profile name remains unchanged. [facts: registered=True, registration_ref='HV-037']
- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=change); registration_asked absent is false (registration_asked=True); register-what-fits-no-type: request_type = other is false (request_type=change); registration_asked absent is false (registration_asked=True); payment-instruction: next_system = payment is false (next_system=access); request_type = instruction is false (request_type=change); incoming-instruction: next_system = incoming is false (next_system=access); request_type = instruction is false (request_type=change); recurring-instruction: next_system = recurring is false (next_system=access); request_type = instruction is false (request_type=change); card-instruction: next_system = card is false (next_system=access); request_type = instruction is false (request_type=change); access-instruction: request_type = instruction is false (request_type=change); business-instruction: next_system = business is false (next_system=access); request_type = instruction is false (request_type=change); documents-instruction: next_system = documents is false (next_system=access); request_type = instruction is false (request_type=change)
- `ask_system`: payment-ask: args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change)

## Final result

reply (REPLIED)

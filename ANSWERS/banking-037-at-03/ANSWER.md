# Case banking-037-at-03: Profile Name Typo

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Marr, verified on a call, asked for the spelling of their profile name to be corrected from "Elowen Mar" to "Elowen Marr". The desk found that a protected name review had already been opened and referred, and that the team's answer on what supporting information is needed had not yet come in, so it closed the case as waiting. The agent's later attempts to submit the request, escalate it and ask the access system were all refused because the case was already in the waiting state, and no profile change has been made. What remains is for the team's answer on supporting information to arrive and for a person to take the name correction forward.

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

Attachments: none.

Case reference: id banking-037-at-03, track Banking & Financial Services, case 037, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `registration-waits` — The team was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - registration_asked → true (registration_asked=True)
  - registered absent → true (registered=not known)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: requester='Elowen Marr', role='customer', channel='verified_call', verified=True]
- event 3 (H&V service agent): I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made. [facts: registration_asked=True]
- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=change); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=access); request_type = instruction is false (request_type=change); confirmation = given is false (confirmation=none)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)
- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); access-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change)

## Final result

wait (WAITING)

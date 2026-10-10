# Case banking-037-at-01: Profile Name Typo

**Decision: escalate**  (final state `ESCALATED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-29 09:00:00 UTC

The request:

> Please correct the spelling of my name in my H&V profile. It shows “Elowen Mar”; my correct name is “Elowen Marr”.

What happened up to now:

1. 2025-09-29T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Elowen Marr

> Profile status: The name displayed in your profile is “Elowen Mar”.

Attachments: none.

Case reference: id banking-037-at-01, track Banking & Financial Services, case 037, point 1, actor_next other.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- subject: **profile**
- request_type: **change**
- next_system: **access**
- reason: **AGENT_ESCALATED**

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); access-ask: next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change)
- `submit_request`: register: request_type = register is false (request_type=change); payment-instruction: next_system = payment is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); incoming-instruction: next_system = incoming is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); recurring-instruction: next_system = recurring is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); card-instruction: next_system = card is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); access-instruction: verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); business-instruction: next_system = business is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); documents-instruction: next_system = documents is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known)

## Final result

escalate (ESCALATED)

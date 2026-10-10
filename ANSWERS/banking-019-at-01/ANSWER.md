# Case banking-019-at-01: Standing order date change

**Decision: escalate**  (final state `ESCALATED`)

## Summary

The customer asked to move the date of their monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025, and to have the change sent to them for secure confirmation. The desk could not ask the recurring system because that step is refused for change requests, and it could not submit the request because the customer was not verified and had not confirmed, so it escalated the case and changed nothing. A person still needs to check whether the 18 September run can still be amended and to send the change to the customer for secure confirmation.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-24 09:00:00 UTC

The request:

> I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation.

What happened up to now:

1. 2025-08-24T09:00:00Z · Secure portal — H&V secure portal → Maeve Ellery

> Standing order status: active. Next scheduled run: 18 September 2025.

Attachments: none.

Case reference: id banking-019-at-01, track Banking & Financial Services, case 019, point 1, actor_next other.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- subject: **standing_order**
- counterparty: **Willow Yard Studios**
- subject_date: **2025-09-18**
- request_type: **change**
- next_system: **recurring**
- reason: **AGENT_ESCALATED**

Where they came from:

- initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: counterparty='Willow Yard Studios', subject_date='2025-09-18']

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, instruction, authority] is false (request_type=change)
- `submit_request`: register: request_type = register is false (request_type=change); payment-instruction: next_system = payment is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); incoming-instruction: next_system = incoming is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); recurring-instruction: verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); card-instruction: next_system = card is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); access-instruction: next_system = access is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); business-instruction: next_system = business is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known); documents-instruction: next_system = documents is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); confirmation = given is not known (confirmation=not known)

## Final result

escalate (ESCALATED)

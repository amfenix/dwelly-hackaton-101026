# Case banking-046-at-02: Revoke a former employee’s role

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Mara Ellery, verified on a call, asked H&V to revoke former employee Owen Bell's Payroll Approver role and to keep the review of his earlier operations separate. The desk could not submit the revocation or query the business system, because no next system was established and no confirmation was recorded, so it escalated the case and nothing has been revoked. A person still needs to action or route the role revocation and check her administrator mandate.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-17 09:00:00 UTC

The request:

> I am the verified business administrator for Larkmere Studio Ltd. The secure portal still shows former employee Owen Bell as an active Payroll Approver. Please revoke that role; we will review any operations previously authorised under it separately.

What happened up to now:

1. 2025-10-17T09:00:00Z · Business portal — Harrow & Vale Bank plc → Mara Ellery

> Active role: Payroll Approver. Assigned user: Owen Bell. Business: Larkmere Studio Ltd.

2. 2025-10-17T09:47:00Z · Verified call — Mara Ellery → H&V business banking agent

> My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate.

Attachments: none.

Case reference: id banking-046-at-02, track Banking & Financial Services, case 046, point 2, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- reason: **AGENT_ESCALATED**

Where they came from:

- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=instruction); payment-instruction: next_system = payment is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: next_system = recurring is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: next_system = card is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: next_system = access is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: next_system = business is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is not known (next_system=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)
- `ask_system`: payment-ask: args.system = payment is false (args.system=business); next_system = payment is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); incoming-ask: args.system = incoming is false (args.system=business); next_system = incoming is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); recurring-ask: args.system = recurring is false (args.system=business); next_system = recurring is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); card-ask: args.system = card is false (args.system=business); next_system = card is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); access-ask: args.system = access is false (args.system=business); next_system = access is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); business-ask: next_system = business is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction); documents-ask: args.system = documents is false (args.system=business); next_system = documents is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=instruction)

## Final result

escalate (ESCALATED)

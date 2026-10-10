# Case banking-046-at-04: Revoke a former employee’s role

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Mara Ellery, on a verified call, asked the desk to revoke former employee Owen Bell's Payroll Approver role for Larkmere Studio Ltd and to keep the review of earlier operations separate. The business system had already been asked and returned a status of "OTHER", the desk's attempt to submit the request was refused, and the case was escalated, so the revocation has not been done by the desk. A person still needs to review the business record and handle the revocation.

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

3. 2025-10-17T10:34:00Z · Internal note — H&V business banking agent → H&V admin process

> I am submitting the verified administrator’s instruction to revoke Owen Bell’s Payroll Approver role for Larkmere Studio Ltd. The administrator’s mandate and the role to be removed have been checked.

4. 2025-10-17T11:21:00Z · Internal note — H&V admin process → H&V business banking agent

> Revocation instruction processed. The admin-log status is available to the business administrator in the secure portal.

Attachments: none.

Case reference: id banking-046-at-04, track Banking & Financial Services, case 046, point 4, actor_next bank.

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
- business_asked: **True**
- business_status: **OTHER**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **business**
- reason: **AGENT_ESCALATED**

Where they came from:

- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- event 3 (H&V admin process): I am submitting the verified administrator’s instruction to revoke Owen Bell’s Payroll Approver role for Larkmere Studio Ltd. The administrator’s mandate and the role to be removed have been checked. [facts: business_asked=True]
- event 4 (H&V admin process): Revocation instruction processed. The admin-log status is available to the business administrator in the secure portal. [facts: business_status='OTHER']
- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: next_system = recurring is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: next_system = card is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: next_system = access is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: business_asked absent is false (business_asked=True); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is false (next_system=business); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)

## Final result

escalate (ESCALATED)

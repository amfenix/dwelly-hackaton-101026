# Case banking-046-at-03: Revoke a former employee’s role

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellery, verified by call as a customer, asked the desk to have H&V revoke former employee Owen Bell's Payroll Approver role. The desk passed the instruction to the business system and closed the case as waiting, because that system's answer had not come in. The agent's later attempt to submit the request was refused since the case was no longer in the right state, so no revocation was carried out and the role remains in place. What is left for a person is to pick the case up once the business system's answer arrives.

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

Attachments: none.

Case reference: id banking-046-at-03, track Banking & Financial Services, case 046, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `business-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_asked → true (business_asked=True)
  - business_status absent → true (business_status=not known)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **role**
- business_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **business**

Where they came from:

- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- event 3 (H&V admin process): I am submitting the verified administrator’s instruction to revoke Owen Bell’s Payroll Approver role for Larkmere Studio Ltd. The administrator’s mandate and the role to be removed have been checked. [facts: business_asked=True]
- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); register-what-fits-no-type: state = TRIAGED is false (state=WAITING); request_type = other is false (request_type=instruction); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=business); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=business); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=business); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=business); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=business); business-instruction: state = TRIAGED is false (state=WAITING); business_asked absent is false (business_asked=True); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=business)

## Final result

wait (WAITING)

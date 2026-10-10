# Case banking-046-at-02: Revoke a former employee’s role

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellery, a verified customer on a call, asked the desk to revoke former employee Owen Bell's Payroll Approver role and to keep any review of his earlier operations separate. The desk registered a request about the role with the business team and closed the case as requested. The record does not show that the role has actually been removed, and the review of earlier operations was not part of this request.

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

- `register_request` (team: business, about: role), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `business-instruction` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_asked absent → true (business_asked=not known)
  - verified → true (verified=True)
  - request_type = instruction → true (request_type=instruction)
  - request_type = change → false (request_type=instruction)
  - confirmation = given → false (confirmation=none)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **business**

Where they came from:

- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

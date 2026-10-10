# Case banking-046-at-04: Revoke a former employee’s role

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellery, on a verified call, asked H&V to revoke former employee Owen Bell's Payroll Approver role and to keep any review of his earlier operations separate. The desk passed the instruction to the business administration process, which returned a status of role_revoked, and replied to her on the call reporting that status. The reply also said that no other role or permission change was established or made, and the case is closed; the record shows nothing left for a person, and the review of earlier operations was not part of this step.

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

- `reply` (to: Mara Ellery, channel: verified_call), by rule `do-reply`

  > The business record shows role_revoked. This does not establish any other role or permission change. No additional approval or role change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `business-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_status present → true (business_status=ROLE_REVOKED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **role**
- business_asked: **True**
- business_status: **ROLE_REVOKED**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **business**

Where they came from:

- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- event 3 (H&V admin process): I am submitting the verified administrator’s instruction to revoke Owen Bell’s Payroll Approver role for Larkmere Studio Ltd. The administrator’s mandate and the role to be removed have been checked. [facts: business_asked=True]
- event 4 (H&V admin process): Revocation instruction processed. The admin-log status is available to the business administrator in the secure portal. [facts: business_status='ROLE_REVOKED']
- event 2 (Mara Ellery): My identity and administrator mandate have been checked. I confirm that Owen Bell is a former employee and instruct H&V to revoke his Payroll Approver role; please keep the review of any earlier operations separate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

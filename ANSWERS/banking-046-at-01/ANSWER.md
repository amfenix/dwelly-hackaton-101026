# Case banking-046-at-01: Revoke a former employee’s role

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was an instruction concerning a role, and the desk's records show Owen Bell's Payroll Approver role at Larkmere Studio Ltd as active, with no confirmation of a change on file. The desk decided to ask the business system about the role, did so, and closed the case with that as its outcome. The business system returned nothing, and the role was not revoked, so whether and how the revocation is carried out is still left for a person.

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

Attachments: none.

Case reference: id banking-046-at-01, track Banking & Financial Services, case 046, point 1, actor_next other.

## Actions taken

- `ask_system` (system: business, about: role), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `business-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = business → true (args.system=business)
  - next_system = business → true (next_system=business)
  - next_system absent → false (next_system=business)
  - business_asked absent → true (business_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **business**

Where they came from:

- event 1 (Harrow & Vale Bank plc): Active role: Payroll Approver. Assigned user: Owen Bell. Business: Larkmere Studio Ltd. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

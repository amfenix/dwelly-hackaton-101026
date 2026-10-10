# Case banking-045-at-03: New employee access request

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Nadia Bell, a customer writing over secure chat who has not been verified, followed up on an access request that still needed the company administrator's approval. The desk escalated the case, because only the person with that authority can approve it and the desk does not act for them. No actions were taken and nothing was granted or approved. A later attempt to query the business system was refused because the case had already closed as escalated, and what is left for a person is to check the authorised company-administrator record and, if confirmed, send the request to that administrator.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-15 09:00:00 UTC

The request:

> Nadia asked H&V to arrange secure-portal access for a new colleague so they could help with the company’s payment administration. Nadia does not have authority to assign user roles, and the company administrator’s approval was still required.

What happened up to now:

1. 2025-10-15T09:00:00Z · External message — Nadia Bell → Harrow & Vale Bank business support

> I work in finance operations at Merefield Design Studio Ltd. Please arrange secure-portal access for our new colleague, who will help with payment administration. I’m not the company administrator, so I can’t approve or assign their role.

2. 2025-10-15T09:47:00Z · Secure chat — Nadia Bell → H&V business support agent

> I’m following up to find out the next step for the access request. I still need the company administrator to approve it.

3. 2025-10-15T10:34:00Z · Secure chat — H&V business support agent → Nadia Bell

> I can’t grant access based on your email or your employee role. I’ll check the authorised company-administrator record and, if confirmed, send the request to that administrator for approval.

Attachments: none.

Case reference: id banking-045-at-03, track Banking & Financial Services, case 045, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: rule `no-authority` — Only the person with the authority may approve this; the desk does not act for them.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = authority → true (request_type=authority)
  - role != business_admin → true (role=customer)

Facts established:

- requester: **Nadia Bell**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **authority**
- reason: **NO_AUTHORITY**

Where they came from:

- event 2 (Nadia Bell): I’m following up to find out the next step for the access request. I still need the company administrator to approve it. [facts: requester='Nadia Bell', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V business support agent): I can’t grant access based on your email or your employee role. I’ll check the authorised company-administrator record and, if confirmed, send the request to that administrator for approval. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=ESCALATED); args.system = payment is false (args.system=business); next_system = payment is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); incoming-ask: state = TRIAGED is false (state=ESCALATED); args.system = incoming is false (args.system=business); next_system = incoming is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); recurring-ask: state = TRIAGED is false (state=ESCALATED); args.system = recurring is false (args.system=business); next_system = recurring is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); card-ask: state = TRIAGED is false (state=ESCALATED); args.system = card is false (args.system=business); next_system = card is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); access-ask: state = TRIAGED is false (state=ESCALATED); args.system = access is false (args.system=business); next_system = access is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); business-ask: state = TRIAGED is false (state=ESCALATED); next_system = business is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority); documents-ask: state = TRIAGED is false (state=ESCALATED); args.system = documents is false (args.system=business); next_system = documents is not known (next_system=not known); request_type not in [register, change, instruction, authority] is false (request_type=authority)

## Final result

escalate (ESCALATED)

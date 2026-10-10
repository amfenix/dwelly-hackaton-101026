# Case banking-045-at-02: New employee access request

**Decision: forward_to_authority**  (final state `FORWARDED`)

## Summary

Nadia Bell, a customer on secure chat whose identity was not verified, followed up on an access request that still needed the company administrator's approval. Because she is not a business administrator, the desk forwarded the role request to the verified company administrator and closed the case as forwarded. Approval stays with the administrator, and nothing in the record shows it has been given yet.

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

Attachments: none.

Case reference: id banking-045-at-02, track Banking & Financial Services, case 045, point 2, actor_next bank.

## Actions taken

- `forward_to_authority` (to: the verified company administrator, about: role, requester: Nadia Bell), by rule `do-forward`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `FORWARD_PENDING`: the agent asked for `forward_to_authority`, rule `forward-to-the-authority` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = authority → true (request_type=authority)
  - role != business_admin → true (role=customer)
- `FORWARD_PENDING` → `FORWARDED`: rule `do-forward`.
  - state = FORWARD_PENDING → true (state=FORWARD_PENDING)

Facts established:

- requester: **Nadia Bell**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **authority**
- next_system: **business**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Nadia Bell): I’m following up to find out the next step for the access request. I still need the company administrator to approve it. [facts: requester='Nadia Bell', role='customer', channel='secure_chat', verified=False]
- event 2 (Nadia Bell): I’m following up to find out the next step for the access request. I still need the company administrator to approve it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

forward_to_authority (FORWARDED)

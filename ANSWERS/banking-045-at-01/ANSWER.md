# Case banking-045-at-01: New employee access request

**Decision: forward_to_authority**  (final state `FORWARDED`)

## Summary

Nadia Bell, writing from outside the portal and not verified, asked for secure-portal access for a new colleague who would help with payment administration, and said she is not the company administrator and can't approve or assign their role. The desk treated it as a role request that needs an authority's approval and forwarded it to the verified company administrator, and the case is closed as forwarded. No access has been set up, so approving the new colleague's role is left to the company administrator.

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

Attachments: none.

Case reference: id banking-045-at-01, track Banking & Financial Services, case 045, point 1, actor_next other.

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
- channel: **external_message**
- verified: **False**
- subject: **role**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **authority**
- next_system: **business**

Where they came from:

- event 1 (Nadia Bell): I work in finance operations at Merefield Design Studio Ltd. Please arrange secure-portal access for our new colleague, who will help with payment administration. I’m not the company administrator, so I can’t approve or assign their role. [facts: requester='Nadia Bell', role='customer', channel='external_message', verified=False]
- event 1 (Nadia Bell): I work in finance operations at Merefield Design Studio Ltd. Please arrange secure-portal access for our new colleague, who will help with payment administration. I’m not the company administrator, so I can’t approve or assign their role. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

forward_to_authority (FORWARDED)

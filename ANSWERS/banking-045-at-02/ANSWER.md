# Case banking-045-at-02: New employee access request

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Nadia Bell, an unverified customer on secure chat, followed up on a request to give a new colleague portal access and asked for the next step; she said the company administrator still has to approve it. The desk decided she has no authority to approve or assign roles, so it closed the case as escalated and assigned no role. The agent's own escalate request with a handoff note was refused because the case was already in the escalated state, so the note is not recorded as accepted, and a person still needs to contact the company administrator through verified channels to approve the access and tell Nadia that this is the next step.

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
- event 2 (Nadia Bell): I’m following up to find out the next step for the access request. I still need the company administrator to approve it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `escalate`: agent-escalates: state = TRIAGED is false (state=ESCALATED)

## Final result

escalate (ESCALATED)

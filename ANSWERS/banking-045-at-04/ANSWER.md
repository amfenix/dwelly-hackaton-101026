# Case banking-045-at-04: New employee access request

**Decision: wait**  (final state `WAITING`)

## Summary

Nadia Bell, an unverified customer writing over secure chat, asked what happens next with her access request, noting that the company administrator still has to approve it. The desk found the bank had already sent the new-user access request to the administrator through the secure portal, so it took no action and closed the case as waiting. No access has been granted, and the request now rests with the administrator's decision.

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

4. 2025-10-15T11:21:00Z · Business portal — H&V business support agent → Verified company administrator for Merefield Design Studio Ltd

> I’ve sent the new-user access request to you through the secure portal for approval. No access has been granted; the request is awaiting your decision.

Attachments: none.

Case reference: id banking-045-at-04, track Banking & Financial Services, case 045, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `already-forwarded` — The request is with the person whose approval it needs.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = authority → true (request_type=authority)
  - bank_forwarded → true (bank_forwarded=True)

Facts established:

- requester: **Nadia Bell**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **role**
- bank_forwarded: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **authority**
- next_system: **business**

Where they came from:

- event 2 (Nadia Bell): I’m following up to find out the next step for the access request. I still need the company administrator to approve it. [facts: requester='Nadia Bell', role='customer', channel='secure_chat', verified=False]
- event 4 (H&V business support agent): the bank already acted: I’ve sent the new-user access request to you through the secure portal for approval. No access has been granted; the request is awaiting your decision.
- event 4 (H&V business support agent): I’ve sent the new-user access request to you through the secure portal for approval. No access has been granted; the request is awaiting your decision. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

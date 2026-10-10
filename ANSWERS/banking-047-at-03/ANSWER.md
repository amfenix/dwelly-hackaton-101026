# Case banking-047-at-03: Company Payment Limit

**Decision: wait**  (final state `WAITING`)

## Summary

Maeve Calder, an unverified viewer on secure chat, asked the desk to confirm the current company payment limit for a substantial supplier payment. The desk classed it as a request for a record fact and asked the business system (the H&V Limit Register) for the setting, but that system's answer is not in yet. The case is closed in a waiting state, no actions were taken and no reply has been sent to Maeve, so the limit is still to be shared once the business system responds.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-19 09:00:00 UTC

The request:

> Maeve wants to know the current outgoing-payment limit on her company profile before arranging a substantial supplier payment.

What happened up to now:

1. 2025-10-19T09:00:00Z · Business portal — Maeve Calder → H&V Business Support

> I can see a planned supplier payout in the portal, but I have not submitted it. I need to know the current outgoing-payment limit for our company profile before I arrange it.

2. 2025-10-19T09:47:00Z · Secure chat — Maeve Calder → H&V Business Support agent

> Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment.

3. 2025-10-19T10:34:00Z · Internal note — H&V Business Support agent → H&V Limit Register

> I’m checking Maeve Calder’s authority to view company limits and the active payment-limit setting before sharing any information.

Attachments: none.

Case reference: id banking-047-at-03, track Banking & Financial Services, case 047, point 3, actor_next bank.

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

- requester: **Maeve Calder**
- role: **viewer**
- channel: **secure_chat**
- verified: **False**
- subject: **limit**
- business_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **business**

Where they came from:

- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: requester='Maeve Calder', role='viewer', channel='secure_chat', verified=False]
- event 3 (H&V Limit Register): I’m checking Maeve Calder’s authority to view company limits and the active payment-limit setting before sharing any information. [facts: business_asked=True]
- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

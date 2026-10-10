# Case banking-047-at-04: Company Payment Limit

**Decision: reply**  (final state `REPLIED`)

## Summary

Maeve Calder asked over secure chat for the company's current payment limit. The desk checked the business limit register, which showed a maximum of £20,000 per outgoing payment and confirmed she may view limits, though her identity was not marked as verified and the record's status came back as "other", which the reply said does not establish a recognised business-record status. The desk sent her a reply with the £20,000.00 figure, made no approval or role change, and closed the case with nothing left for a person.

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

4. 2025-10-19T11:21:00Z · Internal note — H&V Limit Register → H&V Business Support agent

> Mandate check confirms Maeve Calder may view company limits. The active setting is a maximum of £20,000 per outgoing payment.

Attachments: none.

Case reference: id banking-047-at-04, track Banking & Financial Services, case 047, point 4, actor_next bank.

## Actions taken

- `reply` (to: Maeve Calder, channel: secure_chat), by rule `do-reply`

  > The business record shows other; maximum £20000.00. The answer does not establish a recognized business-record status. No additional approval or role change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `business-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_status present → true (business_status=OTHER)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Maeve Calder**
- role: **viewer**
- channel: **secure_chat**
- verified: **False**
- subject: **limit**
- business_asked: **True**
- business_status: **OTHER**
- business_limit: **20000.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **business**

Where they came from:

- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: requester='Maeve Calder', role='viewer', channel='secure_chat', verified=False]
- event 3 (H&V Limit Register): I’m checking Maeve Calder’s authority to view company limits and the active payment-limit setting before sharing any information. [facts: business_asked=True]
- event 4 (H&V Limit Register): Mandate check confirms Maeve Calder may view company limits. The active setting is a maximum of £20,000 per outgoing payment. [facts: business_status='OTHER', business_limit='20000.00']
- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

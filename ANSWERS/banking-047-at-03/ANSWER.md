# Case banking-047-at-03: Company Payment Limit

**Decision: wait**  (final state `WAITING`)

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
- request_type: **question**
- next_system: **business**

Where they came from:

- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: requester='Maeve Calder', role='viewer', channel='secure_chat', verified=False]
- event 3 (H&V Limit Register): I’m checking Maeve Calder’s authority to view company limits and the active payment-limit setting before sharing any information. [facts: business_asked=True]
- event 2 (Maeve Calder): Please confirm our current company payment limit. I’m authorised to view limits, and I need the setting for a substantial supplier payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=business); next_system = payment is false (next_system=business); next_system absent is false (next_system=business); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=business); next_system = incoming is false (next_system=business); next_system absent is false (next_system=business); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=business); next_system = recurring is false (next_system=business); next_system absent is false (next_system=business); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=business); next_system = card is false (next_system=business); next_system absent is false (next_system=business); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=business); next_system = access is false (next_system=business); next_system absent is false (next_system=business); business-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=business); business_asked absent is false (business_asked=True); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=business); next_system = documents is false (next_system=business); next_system absent is false (next_system=business)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

# Case banking-S44-at-04: The journal is unavailable

**Decision: wait**  (final state `WAITING`)

## Summary

Grace Adeyemi, who is unverified and wrote on secure chat, asked whether her £1,140 transfer to Larchmont Lettings had actually been sent. The desk classed it as a question about a payment, set the case to wait for the payment system's answer, and closed it in that waiting state. That answer never came in: the follow-up request to the payment system and the agent's attempt to escalate to a person were both refused because the case was no longer in the state those steps require. So the transfer status is unconfirmed and Grace has been told nothing about it. Someone still needs to verify her identity, check the payment record and reply.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-14 09:00:00 UTC

The request:

> I paid my December rent of £1,140 to Larchmont Lettings yesterday. Has H&V sent it?

What happened up to now:

1. 2025-12-14T09:00:00Z · Secure portal — H&V system → Grace Adeyemi

> One-off transfer to Larchmont Lettings, £1,140.00, 13 December 2025: debit shown in your account activity.

2. 2025-12-14T09:47:00Z · Secure chat — Grace Adeyemi → H&V service agent

> I paid my December rent of £1,140 to Larchmont Lettings yesterday and I can see it’s left my balance. Has H&V actually sent it?

3. 2025-12-14T10:34:00Z · Internal note — H&V service agent → H&V transfer journal

> I am checking the journal entry for Grace Adeyemi’s £1,140.00 one-off transfer to Larchmont Lettings dated 13 December 2025. Please return the recorded transfer status.

4. 2025-12-14T11:21:00Z · Internal note — H&V transfer journal → H&V service agent

> Service temporarily unavailable — no data returned.

Attachments: none.

Case reference: id banking-S44-at-04, track banking, case S44, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `payment-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_asked → true (payment_asked=True)
  - payment_status absent → true (payment_status=not known)

Facts established:

- requester: **Grace Adeyemi**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **1140.00**
- counterparty: **Larchmont Lettings yesterday**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Grace Adeyemi): I paid my December rent of £1,140 to Larchmont Lettings yesterday and I can see it’s left my balance. Has H&V actually sent it? [facts: requester='Grace Adeyemi', role='customer', channel='secure_chat', verified=False]
- event 2 (Grace Adeyemi): I paid my December rent of £1,140 to Larchmont Lettings yesterday and I can see it’s left my balance. Has H&V actually sent it? [facts: amount='1140.00', counterparty='Larchmont Lettings yesterday']
- event 3 (H&V transfer journal): I am checking the journal entry for Grace Adeyemi’s £1,140.00 one-off transfer to Larchmont Lettings dated 13 December 2025. Please return the recorded transfer status. [facts: payment_asked=True]
- event 2 (Grace Adeyemi): I paid my December rent of £1,140 to Larchmont Lettings yesterday and I can see it’s left my balance. Has H&V actually sent it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

# Case banking-007-at-03: International Transfer Status

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellwood, an unverified customer on secure chat, asked what stage her transfer had reached and whether the beneficiary's receipt is confirmed. The desk classified this as a question about a transfer, asked the payment system, and put the case into waiting, since the payment system's answer had not come in and the only confirmation on record is "none". The agent's later attempts to ask the payment system again, send a reply and escalate were all refused because the case was already in the waiting state, so nothing was sent to her and no one has been handed the case; a person still needs to check the payment record and answer her, without claiming beneficiary receipt and after verifying her identity.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-31 09:00:00 UTC

The request:

> I can see that H&V recorded my international transfer as sent, but I cannot tell what stage it has reached. Please check its current status and tell me whether receipt by the beneficiary has been confirmed.

What happened up to now:

1. 2025-07-31T09:00:00Z · Secure portal — H&V → Mara Ellwood

> H&V has recorded your international payment instruction as sent.

2. 2025-07-31T09:47:00Z · Secure chat — Mara Ellwood → H&V service agent

> I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it?

3. 2025-07-31T10:34:00Z · Internal note — H&V service agent → H&V Payment Team

> Please check the available trace for case HV-007 and tell me the current recorded stage. Please distinguish H&V's status from any confirmation of receipt by the beneficiary.

Attachments: none.

Case reference: id banking-007-at-03, track Banking & Financial Services, case 007, point 3, actor_next bank.

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

- requester: **Mara Ellwood**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: requester='Mara Ellwood', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V Payment Team): Please check the available trace for case HV-007 and tell me the current recorded stage. Please distinguish H&V's status from any confirmation of receipt by the beneficiary. [facts: payment_asked=True]
- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=payment); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=payment); tariff_status present is false (tariff_status=not known)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

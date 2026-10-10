# Case banking-009-at-03: Confirming the amount sent

**Decision: wait**  (final state `WAITING`)

## Summary

Verified customer Mara Ellwood asked, on a verified call, which amount H&V actually sent on her property-manager transfer. She remembers the draft as £684.20, but the final line shows £648.20. The desk put the case in WAITING for the payment system's answer, which had not come back, and its later attempts to ask the payment system again, to reply, and to escalate were all refused in that state. So nothing was sent to her and no one was handed the case; someone still needs to check the executed payment record, confirm the sent amount, and tell her whether it matches £648.20.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-04 09:00:00 UTC

The request:

> I remember entering £684.20 in the transfer draft, but the final payment line shows £648.20. Please confirm the amount H&V actually sent.

What happened up to now:

1. 2025-08-04T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellwood

> Final payment line: £648.20 sent to your property manager.

2. 2025-08-04T09:47:00Z · Verified call — Mara Ellwood → H&V service agent

> You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft.

3. 2025-08-04T10:34:00Z · Internal note — H&V service agent → H&V payment journal

> I’m checking the final instruction and execution record for Mara Ellwood’s completed property-manager transfer. Please confirm the amount H&V sent.

Attachments: none.

Case reference: id banking-009-at-03, track Banking & Financial Services, case 009, point 3, actor_next bank.

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
- channel: **verified_call**
- verified: **True**
- subject: **transfer**
- amount: **648.20**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: requester='Mara Ellwood', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: amount='648.20']
- event 3 (H&V payment journal): I’m checking the final instruction and execution record for Mara Ellwood’s completed property-manager transfer. Please confirm the amount H&V sent. [facts: payment_asked=True]
- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: confirmation='none', instructed_outside_portal=False]

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

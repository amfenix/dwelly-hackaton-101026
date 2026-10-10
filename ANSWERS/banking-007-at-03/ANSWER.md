# Case banking-007-at-03: International Transfer Status

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellwood, an unverified customer on secure chat, asked what stage her transfer had reached and whether the beneficiary has confirmed receiving it. The desk had already put the question to the payment system, and that system's answer had not come back, so the case closed as waiting and no actions were taken. The record shows no confirmation of receipt, and what remains is the payment system's reply, which is still outstanding.

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
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: requester='Mara Ellwood', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V Payment Team): Please check the available trace for case HV-007 and tell me the current recorded stage. Please distinguish H&V's status from any confirmation of receipt by the beneficiary. [facts: payment_asked=True]
- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

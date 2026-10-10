# Case banking-009-at-03: Confirming the amount sent

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellwood, verified on a call, asked about a transfer where she remembered the draft as £684.20 but the final line shows £648.20. The desk asked the payment system to confirm the amount actually sent and put the case in a waiting state, since that answer hasn't come in. No reply has gone to her yet, and what is left is to give her the amount from the payment record once it arrives.

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
- request_type: **record_fact**
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

## Final result

wait (WAITING)

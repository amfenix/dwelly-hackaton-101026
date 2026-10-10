# Case banking-009-at-04: Confirming the amount sent

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellwood, verified on a call, asked about her completed transfer, and she remembered the draft amount as £684.20 while the final line showed £648.20. The desk checked the payment record, which shows £648.20 as sent, and replied on the verified call that the transfer is recorded as sent, that this does not confirm receipt or credit by the recipient bank, and that no new transfer was made. The case is closed on that reply, with nothing left for a person in the record.

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

4. 2025-08-04T11:21:00Z · Internal note — H&V payment journal → H&V service agent

> The final instruction and execution record show £648.20. H&V sent £648.20; this record does not establish the amount received by the recipient.

Attachments: none.

Case reference: id banking-009-at-04, track Banking & Financial Services, case 009, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellwood, channel: verified_call), by rule `do-reply`

  > The payment record shows your £648.20 transfer as sent. This does not confirm receipt or credit by the recipient bank. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=SENT)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellwood**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **transfer**
- amount: **648.20**
- payment_asked: **True**
- payment_status: **SENT**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: requester='Mara Ellwood', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: amount='648.20']
- event 3 (H&V payment journal): I’m checking the final instruction and execution record for Mara Ellwood’s completed property-manager transfer. Please confirm the amount H&V sent. [facts: payment_asked=True]
- event 4 (H&V payment journal): The final instruction and execution record show £648.20. H&V sent £648.20; this record does not establish the amount received by the recipient. [facts: payment_status='SENT']
- event 2 (Mara Ellwood): You’ve completed your identification checks. I remember the transfer draft as £684.20, but the final line shows £648.20. Please check the amount in the completed instruction; I’m not asking you to rely on my memory of the draft. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

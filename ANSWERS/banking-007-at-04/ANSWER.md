# Case banking-007-at-04: International Transfer Status

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellwood asked over secure chat what stage her transfer had reached and whether the beneficiary had received it. The desk checked the payment record, which shows the transfer as sent with no confirmation of receipt, and replied on secure chat saying exactly that and that no new transfer was made. The case is closed as replied, and nothing is left for a person; her identity was not verified, though the reply made no change to the account.

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

4. 2025-07-31T11:21:00Z · Internal note — H&V Payment Team → H&V service agent

> Our current trace shows the instruction sent onward from H&V. The downstream processing status is pending, and our trace does not confirm receipt by the beneficiary.

Attachments: none.

Case reference: id banking-007-at-04, track Banking & Financial Services, case 007, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellwood, channel: secure_chat), by rule `do-reply`

  > The payment record shows your transfer as sent. This does not confirm receipt or credit by the recipient bank. No new transfer was made.


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
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- payment_status: **SENT**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: requester='Mara Ellwood', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V Payment Team): Please check the available trace for case HV-007 and tell me the current recorded stage. Please distinguish H&V's status from any confirmation of receipt by the beneficiary. [facts: payment_asked=True]
- event 4 (H&V Payment Team): Our current trace shows the instruction sent onward from H&V. The downstream processing status is pending, and our trace does not confirm receipt by the beneficiary. [facts: payment_status='SENT']
- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-007-at-04: International Transfer Status

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellwood, a customer on secure chat who had not been verified, asked what stage her transfer had reached and whether the beneficiary had confirmed receipt. The desk replied that the payment record shows the transfer as sent, that this does not confirm receipt or credit by the recipient bank, and that no new transfer was made. A second payment-system check was refused because the status was already in the case, and the case closed as replied, with nothing left for a person.

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
  - request_type != other → true (request_type=question)
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
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: requester='Mara Ellwood', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V Payment Team): Please check the available trace for case HV-007 and tell me the current recorded stage. Please distinguish H&V's status from any confirmation of receipt by the beneficiary. [facts: payment_asked=True]
- event 4 (H&V Payment Team): Our current trace shows the instruction sent onward from H&V. The downstream processing status is pending, and our trace does not confirm receipt by the beneficiary. [facts: payment_status='SENT']
- event 2 (Mara Ellwood): I can see the sent status, but I need to know what stage the transfer has reached. Can you check whether there is confirmation that the beneficiary received it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)

## Final result

reply (REPLIED)

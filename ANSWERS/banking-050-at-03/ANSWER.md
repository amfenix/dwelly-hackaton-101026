# Case banking-050-at-03: Status of a Supplier Payment

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing over secure chat as a company signatory, asked what stage a payment to Alder Quay Supplies had reached, saying the supplier had not received the funds. The desk classified it as a question about a transfer, moved the case to WAITING with the payment system as the next step, and closed it there with no payment answer; the later attempts to query the payment system and to escalate were both refused because the case was no longer in the TRIAGED state. Her identity is unverified and no payment record was read, so nothing about the payment has been stated, and a person still needs to verify her and check the payment stage.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-25 09:00:00 UTC

The request:

> I’m an authorised signatory for Northmere Studio Ltd. Our supplier says it has not received the payment we authorised for a materials invoice. Please tell me what stage H&V’s records show for that payment.

What happened up to now:

1. 2025-10-25T09:00:00Z · Business portal — H&V business portal → Mara Ellison

> Payment authorisation recorded for the materials invoice from Alder Quay Supplies.

2. 2025-10-25T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records.

3. 2025-10-25T10:34:00Z · Internal note — H&V service agent → H&V payment team

> I’m escalating this specific payment under case HV-050. Please check and confirm the payment stage recorded in H&V’s journal.

Attachments: none.

Case reference: id banking-050-at-03, track Banking & Financial Services, case 050, point 3, actor_next bank.

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

- requester: **Mara Ellison**
- role: **signatory**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: requester='Mara Ellison', role='signatory', channel='secure_chat', verified=False]
- event 3 (H&V payment team): I’m escalating this specific payment under case HV-050. Please check and confirm the payment stage recorded in H&V’s journal. [facts: payment_asked=True]
- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

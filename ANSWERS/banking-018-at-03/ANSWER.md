# Case banking-018-at-03: Two Future Payments

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, a verified caller, asked the desk to check whether two future £34.80 payments to Northmere Heating are duplicates and to remove the duplicate, though she could not say which line it was. The desk classed this as a standing-order instruction, asked the payment system about it and closed the case in a waiting state because that answer had not come back; nothing was cancelled or changed. The agent's later attempts to ask the payment system again, escalate to a person and ask the customer which transaction she meant were all refused because the case was no longer in the triaged state, so the case is still waiting on the payment system's reply.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-22 09:00:00 UTC

The request:

> I can see two future payments of £34.80 to Northmere Heating. Please check whether they are duplicates and remove the duplicate.

What happened up to now:

1. 2025-08-22T09:00:00Z · Secure portal — H&V secure portal → Mara Ellison

> Two future payment lines of £34.80 to Northmere Heating are shown. Their relationship has not been established.

2. 2025-08-22T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate.

3. 2025-08-22T10:34:00Z · Internal note — H&V service agent → H&V instruction journal

> I am checking the type and internal reference of each instruction behind the two future lines. I have not cancelled either instruction.

Attachments: none.

Case reference: id banking-018-at-03, track Banking & Financial Services, case 018, point 3, actor_next bank.

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
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **standing_order**
- amount: **34.80**
- counterparty: **Northmere Heating**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- initial request (system): I can see two future payments of £34.80 to Northmere Heating. Please check whether they are duplicates and remove the duplicate. [facts: amount='34.80', counterparty='Northmere Heating']
- event 3 (H&V instruction journal): I am checking the type and internal reference of each instruction behind the two future lines. I have not cancelled either instruction. [facts: payment_asked=True]
- event 2 (Mara Ellison): After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority, instruction] is false (request_type=instruction); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)
- `clarify`: clarify-transaction: state = TRIAGED is false (state=WAITING); amount absent is false (amount=34.80); counterparty absent is false (counterparty=Northmere Heating); clarify-card: state = TRIAGED is false (state=WAITING); args.need = which_card is false (args.need=which_transaction); amount absent is false (amount=34.80); counterparty absent is false (counterparty=Northmere Heating); clarify-instruction: state = TRIAGED is false (state=WAITING); args.need = which_instruction is false (args.need=which_transaction); amount absent is false (amount=34.80); counterparty absent is false (counterparty=Northmere Heating); clarify-details: state = TRIAGED is false (state=WAITING); args.need = more_details is false (args.need=which_transaction); amount absent is false (amount=34.80); counterparty absent is false (counterparty=Northmere Heating)

## Final result

wait (WAITING)

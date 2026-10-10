# Case banking-006-at-03: Two Similar Transfers

**Decision: wait**  (final state `WAITING`)

## Summary

Mira Ellison, writing over secure chat and not verified, asked whether her two similar transfers were separate instructions and whether the pending one had been stopped or returned. The desk classified it as a transfer question and put the case in WAITING for the payment system's answer, which has not come in. Its later attempts to ask the payment system again and to escalate were both refused because the case was no longer in the TRIAGED state, so nothing has been stopped, returned or changed, and no one has been handed the case through the desk. Her identity still needs verifying and the payment records still need checking, and the record shows no person assigned to do either.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-29 09:00:00 UTC

The request:

> Mira, the account holder, wants H&V to establish whether two similar outgoing transfer entries are one instruction shown twice or two separate instructions, and asks whether the second can be stopped or returned.

What happened up to now:

1. 2025-07-29T09:00:00Z · Secure portal — H&V → Mira Ellison

> Your payment activity shows two similar outgoing transfer entries to North Quay Utilities for £84.20. One is marked Completed and the other Pending.

2. 2025-07-29T09:47:00Z · Secure chat — Mira Ellison → H&V agent

> I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned.

3. 2025-07-29T10:34:00Z · Internal note — H&V agent → H&V payment instruction journal

> I’m checking the count and independent instruction references for Mira’s own payment instructions before advising. I have not cancelled or returned either instruction.

Attachments: none.

Case reference: id banking-006-at-03, track Banking & Financial Services, case 006, point 3, actor_next bank.

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

- requester: **Mira Ellison**
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

- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: requester='Mira Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V payment instruction journal): I’m checking the count and independent instruction references for Mira’s own payment instructions before advising. I have not cancelled or returned either instruction. [facts: payment_asked=True]
- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

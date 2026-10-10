# Case banking-006-at-03: Two Similar Transfers

**Decision: wait**  (final state `WAITING`)

## Summary

Mira Ellison, writing over secure chat and not yet verified, said she meant to make only one transfer and asked whether two similar transfers are separate instructions and whether the pending one has been stopped or returned. The desk classed it as a question about a transfer, marked the case as waiting on the payment system, and closed it there with no actions taken. The attempts afterwards to ask the payment system, submit a request and escalate were all refused because the case was already in the waiting state, so nothing has been cancelled or returned, the payment system's answer is not in, and her identity still needs to be verified and the two payments checked by a person.

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
- credentials_requested: **False**
- joint_holder_change: **False**

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
- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=question); register-what-fits-no-type: state = TRIAGED is false (state=WAITING); request_type = other is false (request_type=question); payment-instruction: state = TRIAGED is false (state=WAITING); payment_asked absent is false (payment_asked=True); verified is false (verified=False); request_type = instruction is false (request_type=question); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=payment); verified is false (verified=False); request_type = instruction is false (request_type=question)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

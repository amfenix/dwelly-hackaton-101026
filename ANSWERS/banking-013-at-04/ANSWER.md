# Case banking-013-at-04: Cancellation of a Future Payment Instruction

**Decision: wait**  (final state `WAITING`)

## Summary

Elodie Mercer, a verified customer using the secure portal, confirmed she wants the next run of her recurring studio-rent standing order cancelled. The desk asked the recurring system about it and closed the case as "wait" because that system's answer had not come in. Nothing has been cancelled: the follow-up ask, the submit_request and the escalation were all refused because the case was already in WAITING, so someone still needs to check for the recurring system's answer and carry out or decline the cancellation.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-12 09:00:00 UTC

The request:

> I set up a recurring payment for my studio rent and want H&V to cancel the next scheduled run before it starts. Please confirm that the future instruction is cancelled.

What happened up to now:

1. 2025-08-12T09:00:00Z · Secure portal — H&V → Elodie Mercer

> Your recurring studio-rent payment instruction is active. The next scheduled run has not started.

2. 2025-08-12T09:47:00Z · Verified call — Elodie Mercer → H&V agent

> I completed your identification checks. I want to cancel the next run of my studio-rent instruction; please escalate this and tell me how to confirm it securely.

3. 2025-08-12T10:34:00Z · Secure portal — Elodie Mercer → H&V

> I confirm that I want to cancel the future run of my recurring studio-rent payment instruction.

4. 2025-08-12T11:21:00Z · Internal note — H&V agent → H&V protected instruction process

> I checked that Elodie Mercer has authority over this instruction and that its next run has not started. I am submitting her secure-portal cancellation confirmation for instruction HV-013.

Attachments: none.

Case reference: id banking-013-at-04, track Banking & Financial Services, case 013, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `recurring-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_asked → true (recurring_asked=True)
  - recurring_status absent → true (recurring_status=not known)

Facts established:

- requester: **Elodie Mercer**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **standing_order**
- recurring_asked: **True**
- confirmation: **given**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: requester='Elodie Mercer', role='customer', channel='secure_portal', verified=True]
- event 4 (H&V protected instruction process): I checked that Elodie Mercer has authority over this instruction and that its next run has not started. I am submitting her secure-portal cancellation confirmation for instruction HV-013. [facts: recurring_asked=True]
- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: confirmation='given', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); recurring-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=recurring); recurring_asked absent is false (recurring_asked=True); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring)
- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = change is false (request_type=instruction); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = change is false (request_type=instruction); recurring-instruction: state = TRIAGED is false (state=WAITING); recurring_asked absent is false (recurring_asked=True); request_type = change is false (request_type=instruction); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = change is false (request_type=instruction); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = change is false (request_type=instruction); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = change is false (request_type=instruction); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = change is false (request_type=instruction)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

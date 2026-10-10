# Case banking-016-at-03: Disputed Direct Debit amount

**Decision: wait**  (final state `WAITING`)

## Summary

Tamsin Rook, a verified customer on a call, disputed the amount of an £18.40 Direct Debit to Northmere Water Services and asked for the Direct Debit team to investigate. The desk classified it as a register request for the recurring system, saw that the team had already been asked to register a review, and closed the case in WAITING with no actions taken, because the team's answer is not in yet. The agent's later attempts to ask the recurring system, submit the request and escalate were all refused because the case was no longer in the TRIAGED state, so nothing further was sent and the case now waits on the team's reply.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-18 09:00:00 UTC

The request:

> I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited.

What happened up to now:

1. 2025-08-18T09:00:00Z · Secure portal — H&V secure portal → Tamsin Rook

> Statement activity: Direct Debit to Northmere Water Services — £18.40, dated 9 July 2025.

2. 2025-08-18T09:47:00Z · Verified call — Tamsin Rook → H&V service agent

> I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge.

3. 2025-08-18T10:34:00Z · Internal note — H&V service agent → H&V Direct Debit team

> I am registering a review of the £18.40 Direct Debit charge to Northmere Water Services dated 9 July 2025. The customer’s inline statement is: “I dispute the amount debited.”

Attachments: none.

Case reference: id banking-016-at-03, track Banking & Financial Services, case 016, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `registration-waits` — The team was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type in [register, change] → true (request_type=register)
  - registration_asked → true (registration_asked=True)
  - registered absent → true (registered=not known)

Facts established:

- requester: **Tamsin Rook**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- amount: **18.40**
- counterparty: **Northmere Water Services because I dispute the amount debited**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **recurring**

Where they came from:

- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: requester='Tamsin Rook', role='customer', channel='verified_call', verified=True]
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: amount='18.40']
- initial request (system): I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited. [facts: counterparty='Northmere Water Services because I dispute the amount debited']
- event 3 (H&V service agent): I am registering a review of the £18.40 Direct Debit charge to Northmere Water Services dated 9 July 2025. The customer’s inline statement is: “I dispute the amount debited.” [facts: registration_asked=True]
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register)
- `submit_request`: register: state = TRIAGED is false (state=WAITING); registration_asked absent is false (registration_asked=True); register-what-fits-no-type: state = TRIAGED is false (state=WAITING); request_type = other is false (request_type=register); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = instruction is false (request_type=register); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = instruction is false (request_type=register); recurring-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=register); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = instruction is false (request_type=register); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = instruction is false (request_type=register); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = instruction is false (request_type=register); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = instruction is false (request_type=register)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

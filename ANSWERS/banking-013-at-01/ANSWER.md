# Case banking-013-at-01: Cancellation of a Future Payment Instruction

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request concerned a standing order, a recurring studio-rent payment instruction, and the desk classified it as an instruction. The desk's attempt to submit it was refused because the requester isn't verified and there is no confirmation to go ahead. It then asked the recurring-payments system about the standing order, and the case closed in that asked state. The portal shows the instruction as active and the next run not yet started, so nothing has been cancelled; the cancellation can only be submitted once the person's identity is verified and they confirm it.

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

Attachments: none.

Case reference: id banking-013-at-01, track Banking & Financial Services, case 013, point 1, actor_next other.

## Actions taken

- `ask_system` (system: recurring, about: standing_order), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `recurring-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = recurring → true (args.system=recurring)
  - next_system = recurring → true (next_system=recurring)
  - next_system absent → false (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 1 (H&V): Your recurring studio-rent payment instruction is active. The next scheduled run has not started. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: next_system = card is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: next_system = access is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: next_system = business is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is false (next_system=recurring); verified is not known (verified=not known); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)

## Final result

ask_system (ASKED)

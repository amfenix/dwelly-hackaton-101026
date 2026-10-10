# Case banking-013-at-01: Cancellation of a Future Payment Instruction

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was an instruction about a standing order, which the desk classified as concerning the studio-rent payment. The desk routed it to the recurring payments system and asked that system about the standing order, then closed the case at that step. The ask returned no new facts, so nothing has been cancelled or changed, and the only information on file is the portal note that the instruction is active and its next scheduled run hasn't started; whether the order should be stopped is still for a person to follow up.

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

## Final result

ask_system (ASKED)

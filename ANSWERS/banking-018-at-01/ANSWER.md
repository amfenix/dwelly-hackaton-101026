# Case banking-018-at-01: Two Future Payments

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was to check whether two future £34.80 payments to Northmere Heating were duplicates and to remove the duplicate. The desk classed it as a standing order instruction and asked the recurring system about it. That is the only action taken: nothing was removed or cancelled, and the check returned no new facts, so it is still unknown whether the payments are duplicates. The case closed at that step, so a person needs to review the standing order records and decide whether the two lines are separate orders or one shown twice.

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

Attachments: none.

Case reference: id banking-018-at-01, track Banking & Financial Services, case 018, point 1, actor_next other.

## Actions taken

- `ask_system` (system: recurring, about: standing_order, amount: 34.80), by rule `do-ask`

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
- amount: **34.80**
- counterparty: **Northmere Heating**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- initial request (system): I can see two future payments of £34.80 to Northmere Heating. Please check whether they are duplicates and remove the duplicate. [facts: amount='34.80', counterparty='Northmere Heating']
- event 1 (H&V secure portal): Two future payment lines of £34.80 to Northmere Heating are shown. Their relationship has not been established. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

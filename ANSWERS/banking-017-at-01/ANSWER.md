# Case banking-017-at-01: The Standing Order That Did Not Run

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a status question about a monthly rent standing order, after a note that this cycle's rent payment wasn't visible. The desk classified it as a standing order status request and asked the recurring payments system about it, and that question has been sent. No answer has come back yet, so whether the payment went out is still unknown. The record shows nothing further for a person to do beyond waiting for that reply.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-20 09:00:00 UTC

The request:

> I need to know whether my monthly standing order for rent was sent and, if it was not, why. The recipient says they have not received it.

What happened up to now:

1. 2025-08-20T09:00:00Z · External message — Elm Quay Property Services → Mara Ellery

> I can’t see your monthly rent payment for this cycle. Please check with your bank whether it was sent.

Attachments: none.

Case reference: id banking-017-at-01, track Banking & Financial Services, case 017, point 1, actor_next other.

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **recurring**

Where they came from:

- event 1 (Elm Quay Property Services): I can’t see your monthly rent payment for this cycle. Please check with your bank whether it was sent. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-020-at-01: What to Check Before Closing an Account

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elena Wren, writing as an unverified customer, asked which active instructions are linked to her account and what to consider before closing it after she moves her regular payments. The desk classified this as a question about standing orders and asked the recurring-payments system about them, then closed the case at that stage. The system's answer is not in the record, so no instructions have been listed to her, and her identity is still unverified, which leaves a person to follow up once a reply comes back.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-26 09:00:00 UTC

The request:

> I’m planning to close my H&V account after I move my regular payments. Please tell me what active instructions are linked to it and what I should consider before closing it.

What happened up to now:

1. 2025-08-26T09:00:00Z · External message — Elena Wren → Harrow & Vale Bank plc

> I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing?

Attachments: none.

Case reference: id banking-020-at-01, track Banking & Financial Services, case 020, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Elena Wren**
- role: **customer**
- channel: **external_message**
- verified: **False**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 1 (Elena Wren): I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing? [facts: requester='Elena Wren', role='customer', channel='external_message', verified=False]
- event 1 (Elena Wren): I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

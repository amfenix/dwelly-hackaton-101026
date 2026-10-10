# Case banking-020-at-02: What to Check Before Closing an Account

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elena Wren, writing through secure chat, asked which regular payments are still active before she makes any closure plans. The desk classed this as a question about a standing order and asked the recurring payments system about her standing orders, and that request went through; the record does not show any reply from that system. Her verified status is recorded as false, and no reply to Elena is recorded, so that is left for a person.

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

2. 2025-08-26T09:47:00Z · Secure chat — Elena Wren → H&V agent

> I’ve signed in and completed the account-holder checks. I want to know which regular payments are still active before I make any closure plans.

Attachments: none.

Case reference: id banking-020-at-02, track Banking & Financial Services, case 020, point 2, actor_next bank.

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
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Elena Wren): I’ve signed in and completed the account-holder checks. I want to know which regular payments are still active before I make any closure plans. [facts: requester='Elena Wren', role='customer', channel='secure_chat', verified=False]
- event 2 (Elena Wren): I’ve signed in and completed the account-holder checks. I want to know which regular payments are still active before I make any closure plans. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

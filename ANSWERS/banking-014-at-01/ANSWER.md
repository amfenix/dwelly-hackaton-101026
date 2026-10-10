# Case banking-014-at-01: Direct Debit mandate status

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked whether the Direct Debit mandate to Northmere Water Services is still active, after seeing a collection on their March statement. They did not want it cancelled or any assessment of what they owe. The desk treated this as a request to record a fact and put the question to the recurring payments system, and nothing has been cancelled or changed. The answer from that system had not come back when the case closed, so the mandate's status is still unknown.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-14 09:00:00 UTC

The request:

> I saw a Direct Debit collection to Northmere Water Services on my March statement, but I have not seen another one. Please tell me whether the mandate is currently active; I am not asking you to cancel it or assess what I owe the organisation.

What happened up to now:

1. 2025-08-14T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> Your statement for the period ending 31 March 2025 shows a Direct Debit collection to Northmere Water Services. This is a historic statement entry.

Attachments: none.

Case reference: id banking-014-at-01, track Banking & Financial Services, case 014, point 1, actor_next other.

## Actions taken

- `ask_system` (system: recurring, about: direct_debit), by rule `do-ask`

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
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **direct_debit**
- counterparty: **Northmere Water Services**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **recurring**

Where they came from:

- initial request (system): I saw a Direct Debit collection to Northmere Water Services on my March statement, but I have not seen another one. Please tell me whether the mandate is currently active; I am not asking you to cancel it or assess what I owe the organisation. [facts: counterparty='Northmere Water Services']
- event 1 (Harrow & Vale Bank plc): Your statement for the period ending 31 March 2025 shows a Direct Debit collection to Northmere Water Services. This is a historic statement entry. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

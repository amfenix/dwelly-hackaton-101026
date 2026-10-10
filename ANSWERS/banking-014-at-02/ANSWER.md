# Case banking-014-at-02: Direct Debit mandate status

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery asked over secure chat whether her Direct Debit mandate to Northmere Water Services is still active, and said she did not want it cancelled. The desk classed this as a question about a direct debit, routed it to the recurring payments system and asked that system about the mandate. Nothing was cancelled or changed, and the record shows no answer from the recurring system yet, so the mandate's status has not been reported back to her. Her identity is also marked as unverified.

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

2. 2025-08-14T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status.

Attachments: none.

Case reference: id banking-014-at-02, track Banking & Financial Services, case 014, point 2, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **direct_debit**
- counterparty: **Northmere Water Services**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellery): I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- initial request (system): I saw a Direct Debit collection to Northmere Water Services on my March statement, but I have not seen another one. Please tell me whether the mandate is currently active; I am not asking you to cancel it or assess what I owe the organisation. [facts: counterparty='Northmere Water Services']
- event 2 (Mara Ellery): I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-015-at-04: Cancel future Direct Debit collections

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, asked the desk to cancel her Northmere Fitness Direct Debit mandate. The desk had already put the question to the recurring system, whose answer had not come in, so it closed the case as "wait" and recorded no cancellation. The agent's later attempts to submit the request and to ask the recurring system again were both refused because the case was in WAITING, and the record shows confirmation as "none". A person still needs to pick the case up, and the record also notes that a collection may already be in process and would need separate reconciliation.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-16 09:00:00 UTC

The request:

> I want H&V to cancel my active Direct Debit mandate to Northmere Fitness so it cannot be used for future collections.

What happened up to now:

1. 2025-08-16T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> Direct Debit mandate: Northmere Fitness — Active.

2. 2025-08-16T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient.

3. 2025-08-16T10:34:00Z · Internal note — H&V service agent → H&V case record HV-015

> I completed the required identification checks and reviewed the collection-stage information. I cannot rule out a collection already being processed, so that needs separate reconciliation.

4. 2025-08-16T11:21:00Z · Business portal — H&V service agent → H&V Direct Debit service

> I have submitted Mara Ellison’s checked instruction to cancel the Northmere Fitness mandate. This submission records her instruction; I am not authorising it on her behalf.

Attachments: none.

Case reference: id banking-015-at-04, track Banking & Financial Services, case 015, point 4, actor_next bank.

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- counterparty: **Northmere Fitness**
- recurring_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: requester='Mara Ellison', role='customer', channel='verified_call']
- event 3 (H&V service agent): I completed the required identification checks and reviewed the collection-stage information. I cannot rule out a collection already being processed, so that needs separate reconciliation. [facts: verified=True]
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: counterparty='Northmere Fitness']
- event 4 (H&V Direct Debit service): I have submitted Mara Ellison’s checked instruction to cancel the Northmere Fitness mandate. This submission records her instruction; I am not authorising it on her behalf. [facts: recurring_asked=True]
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); recurring_asked absent is false (recurring_asked=True); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)
- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); recurring-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=recurring); recurring_asked absent is false (recurring_asked=True); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring)

## Final result

wait (WAITING)

# Case banking-015-at-02: Cancel future Direct Debit collections

**Decision: submit_request**  (final state `REQUESTED`)

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

Attachments: none.

Case reference: id banking-015-at-02, track Banking & Financial Services, case 015, point 2, actor_next bank.

## Actions taken

- `register_request` (team: recurring, about: direct_debit), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `recurring-instruction` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - verified → true (verified=True)
  - request_type = instruction → true (request_type=instruction)
  - request_type = change → false (request_type=instruction)
  - confirmation = given → false (confirmation=none)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- counterparty: **Northmere Fitness**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: counterparty='Northmere Fitness']
- event 2 (Mara Ellison): I’ve completed your identification checks. Please cancel my Northmere Fitness Direct Debit mandate; I understand this is an instruction to my bank, not a cancellation of my agreement with the recipient. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

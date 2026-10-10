# Case banking-015-at-01: Cancel future Direct Debit collections

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked Harrow & Vale to cancel their active Direct Debit mandate to Northmere Fitness so it can't be used for future collections. The desk classified this as a Direct Debit instruction and routed it to the recurring payments system. It then asked that system about the Direct Debit, and the case closed in the asked state. The desk did not submit the cancellation itself: that attempt was refused because the requester was not verified, and the record shows no cancellation carried out, so nothing further is recorded as pending for a person.

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

Attachments: none.

Case reference: id banking-015-at-01, track Banking & Financial Services, case 015, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **direct_debit**
- counterparty: **Northmere Fitness**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- initial request (system): I want H&V to cancel my active Direct Debit mandate to Northmere Fitness so it cannot be used for future collections. [facts: counterparty='Northmere Fitness']
- event 1 (Harrow & Vale Bank plc): Direct Debit mandate: Northmere Fitness — Active. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=recurring); verified is not known (verified=not known); incoming-instruction: next_system = incoming is false (next_system=recurring); verified is not known (verified=not known); recurring-instruction: verified is not known (verified=not known); card-instruction: next_system = card is false (next_system=recurring); verified is not known (verified=not known); access-instruction: next_system = access is false (next_system=recurring); verified is not known (verified=not known); business-instruction: next_system = business is false (next_system=recurring); verified is not known (verified=not known); documents-instruction: next_system = documents is false (next_system=recurring); verified is not known (verified=not known)

## Final result

ask_system (ASKED)

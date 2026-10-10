# Case banking-013-at-02: Cancellation of a Future Payment Instruction

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Elodie Mercer, a verified caller, asked to cancel the next run of her studio-rent standing order and wanted to know how to confirm it securely. The desk registered the request with the recurring payments team and closed the case as requested. No confirmation had been given. The record does not show that the cancellation has taken effect, so that depends on the recurring team acting on the request.

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

2. 2025-08-12T09:47:00Z · Verified call — Elodie Mercer → H&V agent

> I completed your identification checks. I want to cancel the next run of my studio-rent instruction; please escalate this and tell me how to confirm it securely.

Attachments: none.

Case reference: id banking-013-at-02, track Banking & Financial Services, case 013, point 2, actor_next other.

## Actions taken

- `register_request` (team: recurring, about: standing_order), by rule `do-request`

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

- requester: **Elodie Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 2 (Elodie Mercer): I completed your identification checks. I want to cancel the next run of my studio-rent instruction; please escalate this and tell me how to confirm it securely. [facts: requester='Elodie Mercer', role='customer', channel='verified_call', verified=True]
- event 2 (Elodie Mercer): I completed your identification checks. I want to cancel the next run of my studio-rent instruction; please escalate this and tell me how to confirm it securely. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

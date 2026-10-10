# Case banking-016-at-02: Disputed Direct Debit amount

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Tamsin Rook, verified on a call, disputed an £18.40 Direct Debit to Northmere Water Services and asked for it to be investigated. The desk registered a request with the recurring payments team about the direct debit, and the case closed as requested. Nothing further is recorded as left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-18 09:00:00 UTC

The request:

> I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited.

What happened up to now:

1. 2025-08-18T09:00:00Z · Secure portal — H&V secure portal → Tamsin Rook

> Statement activity: Direct Debit to Northmere Water Services — £18.40, dated 9 July 2025.

2. 2025-08-18T09:47:00Z · Verified call — Tamsin Rook → H&V service agent

> I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge.

Attachments: none.

Case reference: id banking-016-at-02, track Banking & Financial Services, case 016, point 2, actor_next bank.

## Actions taken

- `register_request` (team: recurring, about: direct_debit), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `register` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = register → true (request_type=register)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Tamsin Rook**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- amount: **18.40**
- counterparty: **Northmere Water Services because I dispute the amount debited**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **recurring**

Where they came from:

- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: requester='Tamsin Rook', role='customer', channel='verified_call', verified=True]
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: amount='18.40']
- initial request (system): I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited. [facts: counterparty='Northmere Water Services because I dispute the amount debited']
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

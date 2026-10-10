# Case banking-004-at-01: Why the transfer was declined

**Decision: ask_system**  (final state `ASKED`)

## Summary

The requester said they made a transfer to Northmere Housing Co-operative on 14 July 2025, that the secure portal shows it as not completed, and asked for the reason. The desk classified this as a question about a transfer, routed it to the payment system and sent that system a query about the transfer. The payment system's answer is not in the record, so the reason the transfer wasn't completed is still unknown, and someone will need to reply to the requester once that answer is available.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-25 09:00:00 UTC

The request:

> I am the account holder and made a transfer to Northmere Housing Co-operative on 14 July 2025. The secure portal says it was not completed, but I cannot see why. Please explain the reason.

What happened up to now:

1. 2025-07-25T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> Transfer to Northmere Housing Co-operative — status: “Not completed”.

Attachments: none.

Case reference: id banking-004-at-01, track Banking & Financial Services, case 004, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `payment-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = payment → true (args.system=payment)
  - next_system = payment → true (next_system=payment)
  - next_system absent → false (next_system=payment)
  - payment_asked absent → true (payment_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- counterparty: **Northmere Housing Co-operative**
- subject_date: **2025-07-14**
- request_type: **question**
- next_system: **payment**

Where they came from:

- initial request (system): I am the account holder and made a transfer to Northmere Housing Co-operative on 14 July 2025. The secure portal says it was not completed, but I cannot see why. Please explain the reason. [facts: counterparty='Northmere Housing Co-operative', subject_date='2025-07-14']

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

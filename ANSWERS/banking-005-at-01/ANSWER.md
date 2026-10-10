# Case banking-005-at-01: Request about a transfer to the wrong recipient

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

The customer asked for a request to be registered to seek the return of a £286.40 transfer sent to the wrong saved recipient. The desk classified it as a register request about a transfer and registered it with the payment team, and the case closed as requested. The money has not been recovered or the payment reversed, and what happens next is up to the payment team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-27 09:00:00 UTC

The request:

> I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return.

What happened up to now:

1. 2025-07-27T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Leona Mercer

> Transfer status: sent. This status confirms the transfer was sent from your H&V account; it does not confirm that the recipient has returned the money.

Attachments: none.

Case reference: id banking-005-at-01, track Banking & Financial Services, case 005, point 1, actor_next other.

## Actions taken

- `register_request` (team: payment, about: transfer), by rule `do-request`

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

- subject: **transfer**
- amount: **286.40**
- request_type: **register**
- next_system: **payment**

Where they came from:

- initial request (system): I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return. [facts: amount='286.40']

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

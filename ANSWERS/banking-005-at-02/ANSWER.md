# Case banking-005-at-02: Request about a transfer to the wrong recipient

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Leona Mercer, a verified customer calling in, asked the desk to register a request to seek the return of a £286.40 transfer she sent to the wrong saved recipient for a pottery-studio bill. The desk registered that request with the payment team and the case closed as requested. This only logs the request: nothing has been recovered, and the record doesn't say whether the money will come back or what the payment team will do next.

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

2. 2025-07-27T09:47:00Z · Verified call — Leona Mercer → H&V service agent

> I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return.

Attachments: none.

Case reference: id banking-005-at-02, track Banking & Financial Services, case 005, point 2, actor_next bank.

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

- requester: **Leona Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **transfer**
- amount: **286.40**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **payment**

Where they came from:

- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: requester='Leona Mercer', role='customer', channel='verified_call', verified=True]
- initial request (system): I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return. [facts: amount='286.40']
- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

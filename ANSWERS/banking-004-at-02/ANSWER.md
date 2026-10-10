# Case banking-004-at-02: Why the transfer was declined

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery, a verified customer on the secure portal, asked why her 14 July 2025 transfer to Northmere Housing Co-operative was not completed. The desk classified it as a request for a reason and sent a query about the transfer to the payment system. That query returned nothing, so no reason has been found and none has been given to her; the record shows no further step after the question was asked.

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

2. 2025-07-25T09:47:00Z · Secure portal — Mara Ellery → H&V service team

> I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason.

Attachments: none.

Case reference: id banking-004-at-02, track Banking & Financial Services, case 004, point 2, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=reason)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **transfer**
- counterparty: **Northmere Housing Co-operative**
- subject_date: **2025-07-14**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **reason**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellery): I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason. [facts: requester='Mara Ellery', role='customer', channel='secure_portal', verified=True]
- initial request (system): I am the account holder and made a transfer to Northmere Housing Co-operative on 14 July 2025. The secure portal says it was not completed, but I cannot see why. Please explain the reason. [facts: counterparty='Northmere Housing Co-operative', subject_date='2025-07-14']
- event 2 (Mara Ellery): I am the account holder and this was my transfer. Please tell me why it was not completed; the portal shows the status but no reason. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

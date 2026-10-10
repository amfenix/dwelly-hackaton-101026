# Case banking-043-at-01: Waiting for the Second Signatory

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery, a verified customer on the business portal, asked whether Northmere Studio Ltd's payroll payment package is waiting for her co-signer or has moved on. The desk classified this as a status request and sent a query about the package to the payment system. The record shows no answer from the payment system yet, so nothing has been reported back to her, and the case closed at that point.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-11 09:00:00 UTC

The request:

> I gave my first consent to Northmere Studio Ltd’s payroll payment package. I need to know whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions in the portal.

What happened up to now:

1. 2025-10-11T09:00:00Z · Business portal — Mara Ellery → Harrow & Vale Bank plc

> I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions.

Attachments: none.

Case reference: id banking-043-at-01, track Banking & Financial Services, case 043, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: payment_package), by rule `do-ask`

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **business_portal**
- verified: **True**
- subject: **payment_package**
- counterparty: **Northmere Studio Ltd’s payroll payment package**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: requester='Mara Ellery', role='customer', channel='business_portal', verified=True]
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: counterparty='Northmere Studio Ltd’s payroll payment package']
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

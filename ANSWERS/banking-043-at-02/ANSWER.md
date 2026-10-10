# Case banking-043-at-02: Waiting for the Second Signatory

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery, writing over secure chat and not verified, asked whether Northmere Studio Ltd's payroll payment package was still waiting for her co-signer after she gave her first consent. The desk classed it as a question about a payment package and sent an inquiry to the payment system, which returned nothing, so the case closed with that step done. No answer on the package's status has reached the case, and Mara has not been told anything about it; that, and her unverified status, are left for a person.

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

2. 2025-10-11T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act.

Attachments: none.

Case reference: id banking-043-at-02, track Banking & Financial Services, case 043, point 2, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **payment_package**
- counterparty: **Northmere Studio Ltd’s payroll payment package**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: counterparty='Northmere Studio Ltd’s payroll payment package']
- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

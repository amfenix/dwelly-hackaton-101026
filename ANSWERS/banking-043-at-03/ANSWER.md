# Case banking-043-at-03: Waiting for the Second Signatory

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellery asked over secure chat whether Northmere Studio Ltd's payroll payment package was still waiting for her co-signer or had moved on, after she gave her first consent. The desk asked the business system about the package and closed the case as waiting, because that system's answer has not come back; a second ask to the business system was refused once the case was in the waiting state. No actions were taken on the package, and her session is not verified. What remains is for the business system's reply to arrive so the status and the second signatory's position can be answered.

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

3. 2025-10-11T10:34:00Z · Internal note — H&V service agent → H&V signing log

> I’m checking the package’s signing queue against the business mandate before responding. I will not approve or release anything on either signer’s behalf.

Attachments: none.

Case reference: id banking-043-at-03, track Banking & Financial Services, case 043, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `business-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_asked → true (business_asked=True)
  - business_status absent → true (business_status=not known)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **payment_package**
- counterparty: **Northmere Studio Ltd’s payroll payment package**
- business_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **business**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: counterparty='Northmere Studio Ltd’s payroll payment package']
- event 3 (H&V signing log): I’m checking the package’s signing queue against the business mandate before responding. I will not approve or release anything on either signer’s behalf. [facts: business_asked=True]
- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=business); next_system = payment is false (next_system=business); next_system absent is false (next_system=business); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=business); next_system = incoming is false (next_system=business); next_system absent is false (next_system=business); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=business); next_system = recurring is false (next_system=business); next_system absent is false (next_system=business); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=business); next_system = card is false (next_system=business); next_system absent is false (next_system=business); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=business); next_system = access is false (next_system=business); next_system absent is false (next_system=business); business-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=business); business_asked absent is false (business_asked=True); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=business); next_system = documents is false (next_system=business); next_system absent is false (next_system=business); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=business); next_system = tariff is false (next_system=business); next_system absent is false (next_system=business)

## Final result

wait (WAITING)

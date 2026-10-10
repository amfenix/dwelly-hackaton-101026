# Case banking-043-at-02: Waiting for the Second Signatory

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery, writing on secure chat (not verified as the account holder), asked whether Northmere Studio Ltd's payroll payment package was still waiting on her co-signer after she gave her consent. The desk classed it as a status request and passed a query about the package to the payment system, then closed the case in that asked state. The desk did not send Mara a reply, because its reply rules were refused in that state, so she has not yet been told the package status or whether the second signatory still needs to act.

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
  - request_type not in [register, change, authority] → true (request_type=status)
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
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: counterparty='Northmere Studio Ltd’s payroll payment package']
- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

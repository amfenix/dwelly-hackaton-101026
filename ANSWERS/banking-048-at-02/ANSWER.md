# Case banking-048-at-02: The buyer said payment was sent

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison of Alder Quay Studio Ltd. asked, over secure chat, whether an identifiable credit for a workshop invoice had reached the business account. The requester was not verified, and the desk classed it as a status request about an incoming payment. It then put the question to the incoming payments system, which returned nothing in the record, so whether the payment has arrived is still unanswered. The record shows no further step for anyone to take.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-21 09:00:00 UTC

The request:

> Please check whether the payment our buyer says they sent for our workshop invoice has reached our H&V business account.

What happened up to now:

1. 2025-10-21T09:00:00Z · External message — Buyer → Alder Quay Studio Ltd.

> I've sent payment for the workshop invoice. Please let me know when it reaches you.

2. 2025-10-21T09:47:00Z · Secure chat — Mara Ellison, Alder Quay Studio Ltd. → H&V business support

> I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account.

Attachments: none.

Case reference: id banking-048-at-02, track Banking & Financial Services, case 048, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: incoming, about: incoming_payment), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `incoming-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = incoming → true (args.system=incoming)
  - next_system = incoming → true (next_system=incoming)
  - next_system absent → false (next_system=incoming)
  - incoming_asked absent → true (incoming_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison, Alder Quay Studio Ltd.**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **incoming**

Where they came from:

- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: requester='Mara Ellison, Alder Quay Studio Ltd.', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

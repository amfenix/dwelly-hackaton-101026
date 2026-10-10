# Case banking-001-at-01: Was the one-off transfer sent?

**Decision: ask_system**  (final state `ASKED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-19 09:00:00 UTC

The request:

> I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it.

What happened up to now:

1. 2025-07-19T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> One-off transfer to Alder & Reed Workshop: debit shown in your account activity.

Attachments: none.

Case reference: id banking-001-at-01, track Banking & Financial Services, case 001, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 420.00), by rule `do-ask`

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
- amount: **420.00**
- counterparty: **Alder & Reed Workshop**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- initial request (system): I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it. [facts: amount='420.00', counterparty='Alder & Reed Workshop']
- event 1 (Harrow & Vale Bank plc): One-off transfer to Alder & Reed Workshop: debit shown in your account activity. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

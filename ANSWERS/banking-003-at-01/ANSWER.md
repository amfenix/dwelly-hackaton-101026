# Case banking-003-at-01: Transfer Awaiting Authorisation

**Decision: ask_system**  (final state `ASKED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-23 09:00:00 UTC

The request:

> I saved a transfer instruction for an invoice in my secure portal, but there is no sent confirmation. Please check whether it has been submitted and tell me what stage it is at.

What happened up to now:

1. 2025-07-23T09:00:00Z · Secure portal — Elise Rowan → Harrow & Vale Bank plc

> I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent.

Attachments: none.

Case reference: id banking-003-at-01, track Banking & Financial Services, case 003, point 1, actor_next other.

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

- requester: **Elise Rowan**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 1 (Elise Rowan): I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent. [facts: requester='Elise Rowan', role='customer', channel='secure_portal', verified=True]
- event 1 (Elise Rowan): I created and saved a transfer instruction for an invoice in my secure portal. I have not seen a confirmation that it was sent. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=payment); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=payment); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=payment); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=payment); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=payment); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=payment); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

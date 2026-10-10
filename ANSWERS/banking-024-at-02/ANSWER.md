# Case banking-024-at-02: Reason for the Card Restriction

**Decision: ask_system**  (final state `ASKED`)

## Summary

Rowan Ellery, writing over secure chat as a cardholder whose card was declined at a grocery payment, asked which category of restriction applies and whether it has been lifted. The desk classified this as a card question, sent a query to the card system, and closed the case in the ASKED state. The card system returned no status, and the desk refused the follow-up reply because the case was no longer triaged and no card status was on record, so Rowan has not been told the restriction category or whether it was lifted. Rowan's identity is also unverified, and a person has to take the case from here.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-03 09:00:00 UTC

The request:

> Rowan wants to know why their H&V card became temporarily unavailable after it was declined during a grocery purchase, and whether the restriction has been lifted.

What happened up to now:

1. 2025-09-03T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Rowan Ellery

> Status: Your card is temporarily unavailable. This status does not show the reason.

2. 2025-09-03T09:47:00Z · Secure chat — Rowan Ellery → H&V Customer Support

> I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted.

Attachments: none.

Case reference: id banking-024-at-02, track Banking & Financial Services, case 024, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `card-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = card → true (args.system=card)
  - next_system = card → true (next_system=card)
  - next_system absent → false (next_system=card)
  - card_asked absent → true (card_asked=not known)
  - request_type not in [register, change, authority, instruction] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Rowan Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: requester='Rowan Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=card); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=card); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=card); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=card); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=card); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=card); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=card); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=card); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

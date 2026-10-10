# Case banking-002-at-01: Expected Incoming Payment

**Decision: ask_system**  (final state `ASKED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-21 09:00:00 UTC

The request:

> I’m expecting a contribution toward the cost of a shared pottery studio kiln. The sender told me by phone that they had transferred it, but I can’t see it in my H&V account; please check whether it has arrived.

What happened up to now:

1. 2025-07-21T09:00:00Z · External message — Sender → Elowen Marsh

> I’ve sent the contribution for the kiln by bank transfer.

Attachments: none.

Case reference: id banking-002-at-01, track Banking & Financial Services, case 002, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **incoming_payment**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**

Where they came from:

- event 1 (Sender): I’ve sent the contribution for the kiln by bank transfer. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=incoming); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=incoming); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=incoming); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=incoming); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=incoming); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=incoming); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

# Case banking-017-at-02: The Standing Order That Did Not Run

**Decision: ask_system**  (final state `ASKED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-20 09:00:00 UTC

The request:

> I need to know whether my monthly standing order for rent was sent and, if it was not, why. The recipient says they have not received it.

What happened up to now:

1. 2025-08-20T09:00:00Z · External message — Elm Quay Property Services → Mara Ellery

> I can’t see your monthly rent payment for this cycle. Please check with your bank whether it was sent.

2. 2025-08-20T09:47:00Z · Secure chat — Mara Ellery → Harrow & Vale Bank plc agent

> I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded.

Attachments: none.

Case reference: id banking-017-at-02, track Banking & Financial Services, case 017, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: recurring, about: standing_order), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `recurring-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = recurring → true (args.system=recurring)
  - next_system = recurring → true (next_system=recurring)
  - next_system absent → false (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=recurring); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=recurring); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=recurring); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=recurring); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=recurring); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=recurring); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

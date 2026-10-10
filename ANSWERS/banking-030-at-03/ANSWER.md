# Case banking-030-at-03: Replacement card request

**Decision: ask_system**  (final state `ASKED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-15 09:00:00 UTC

The request:

> Maren’s debit card had become unreliable, so she submitted a replacement request. She contacted H&V to find out whether the card was being made and whether it had been sent.

What happened up to now:

1. 2025-09-15T09:00:00Z · Secure portal — H&V secure portal → Maren Ellery

> Replacement request accepted. Reference: HV-030.

2. 2025-09-15T09:47:00Z · Secure chat — Maren Ellery → H&V agent

> I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent?

3. 2025-09-15T10:34:00Z · Secure chat — H&V agent → Maren Ellery

> I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account.

Attachments: none.

Case reference: id banking-030-at-03, track Banking & Financial Services, case 030, point 3, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Maren Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **True**
- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- event 2 (Maren Ellery): I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent? [facts: requester='Maren Ellery', role='customer', channel='secure_chat']
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: verified=True]
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=card); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=card); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=card); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=card); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=card); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=card); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

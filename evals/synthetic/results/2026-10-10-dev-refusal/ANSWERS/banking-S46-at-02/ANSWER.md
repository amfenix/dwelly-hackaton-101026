# Case banking-S46-at-02: Extra bullets and new channel names

**Decision: ask_system**  (final state `ASKED`)

## Summary

Nadia Okonjo asked whether the replacement debit card she ordered at the branch about a week ago has been sent, noting she is away from 22 December. The desk identified it as a card question and put the query to the card system, then closed the case as "asked". The card system's answer never came back to the case, so no card status was recorded and the reply to Nadia was refused; she has not been told whether the card was sent. What is left for a person is to check the card order (card ending 4417, ordered at the Elmbridge branch on 9 December 2025), confirm whether it has been posted, and tell her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-16 09:00:00 UTC

The request:

> I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent?

What happened up to now:

1. 2025-12-16T09:00:00Z · Branch visit — Nadia Okonjo → H&V branch adviser

> Branch visit note carried onto this case: on 9 December 2025 I reported that my debit card ending 4417 had stopped working at contactless and chip terminals. The adviser at the Elmbridge branch checked my identity and ordered a replacement card to be posted to my home address. I was told to keep using the app in the meantime.

2. 2025-12-16T09:47:00Z · Mobile app chat — Nadia Okonjo → H&V service agent

> I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent? I’m away for Christmas from the 22nd.

Attachments: none.

Case reference: id banking-S46-at-02, track banking, case S46, point 2, actor_next bank.

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

- requester: **Nadia Okonjo**
- role: **customer**
- subject: **card**
- subject_date: **2025-12-09**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Nadia Okonjo): I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent? I’m away for Christmas from the 22nd. [facts: requester='Nadia Okonjo', role='customer']
- event 1 (Nadia Okonjo): Branch visit note carried onto this case: on 9 December 2025 I reported that my debit card ending 4417 had stopped working at contactless and chip terminals. The adviser at the Elmbridge branch checked my identity and ordered a replacement card to be posted to my home address. I was told to keep using the app in the meantime. [facts: subject_date='2025-12-09']
- event 2 (Nadia Okonjo): I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent? I’m away for Christmas from the 22nd. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=card); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=card); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=card); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=card); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=card); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=card); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=card); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=card); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

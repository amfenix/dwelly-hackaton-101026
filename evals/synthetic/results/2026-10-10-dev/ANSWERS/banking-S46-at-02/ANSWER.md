# Case banking-S46-at-02: Extra bullets and new channel names

**Decision: ask_system**  (final state `ASKED`)

## Summary

Nadia Okonjo, a customer, asked whether the replacement debit card she ordered at the branch on 9 December has been sent, since she is away from the 22nd. The desk classified this as a card question and put it to the card system, which returned no details. The case closed at that step with no answer on whether the card has been sent, so that is still unanswered and left for a person to follow up.

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

Where they came from:

- event 2 (Nadia Okonjo): I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent? I’m away for Christmas from the 22nd. [facts: requester='Nadia Okonjo', role='customer']
- event 1 (Nadia Okonjo): Branch visit note carried onto this case: on 9 December 2025 I reported that my debit card ending 4417 had stopped working at contactless and chip terminals. The adviser at the Elmbridge branch checked my identity and ordered a replacement card to be posted to my home address. I was told to keep using the app in the meantime. [facts: subject_date='2025-12-09']
- event 2 (Nadia Okonjo): I ordered a replacement debit card at the branch a week ago and it still hasn’t come. Has it been sent? I’m away for Christmas from the 22nd. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

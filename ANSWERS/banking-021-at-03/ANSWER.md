# Case banking-021-at-03: Has My Replacement Card Been Sent?

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing over secure chat and not verified as the account holder, asked whether dispatch of her replacement card had been registered, since the portal only says the request was accepted. The desk classified it as a card question, asked the card system, and closed the case as waiting because that system's answer had not come in. No reply was sent, and later attempts to ask the card system again and to reply were refused because the case was already in the waiting state with no card status to report. What is left is for a person to pick the case up once the card system's answer arrives and to deal with the unverified identity before any card details are shared.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-28 09:00:00 UTC

The request:

> I need to know whether the replacement card ordered for my H&V account has actually been dispatched. The secure portal confirmed that my request was accepted, but I cannot see confirmation of delivery or dispatch.

What happened up to now:

1. 2025-08-28T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> Your replacement card request has been accepted. This confirms the request was received; it does not confirm dispatch or delivery.

2. 2025-08-28T09:47:00Z · Secure chat — Mara Ellison → Harrow & Vale Bank plc agent

> I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived.

3. 2025-08-28T10:34:00Z · Internal note — H&V agent → Card journal

> I’m checking the card journal for the dispatch record associated with case HV-021. The customer has asked whether dispatch was registered; please return the recorded status only.

Attachments: none.

Case reference: id banking-021-at-03, track Banking & Financial Services, case 021, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `card-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_asked → true (card_asked=True)
  - card_status absent → true (card_status=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- card_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (Card journal): I’m checking the card journal for the dispatch record associated with case HV-021. The customer has asked whether dispatch was registered; please return the recorded status only. [facts: card_asked=True]
- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=card); card_asked absent is false (card_asked=True); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=card); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=card); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=card); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=card); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=card); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=card); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=card); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=card); tariff_status present is false (tariff_status=not known)

## Final result

wait (WAITING)

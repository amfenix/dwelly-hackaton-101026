# Case banking-021-at-02: Has My Replacement Card Been Sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing over secure chat and not verified, asked whether dispatch of her replacement card had been registered, since the portal only said the request was accepted. The desk classified it as a status request about a card and sent a query to the card system. The case closed in the asked state with no answer recorded yet, so dispatch and delivery remain unconfirmed and the reply to her is still outstanding.

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

Attachments: none.

Case reference: id banking-021-at-02, track Banking & Financial Services, case 021, point 2, actor_next bank.

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **card**

Where they came from:

- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-024-at-02: Reason for the Card Restriction

**Decision: ask_system**  (final state `ASKED`)

## Summary

Rowan Ellery, writing over secure chat and not yet verified, said their card was declined at a grocery payment and asked what category of restriction applies and whether it has been lifted. The desk classed this as a card question and sent an ask to the card system, which accepted it with no details returned. The case closed at that step, so the restriction category and whether it was lifted remain unanswered, and Rowan's identity is still unverified for a person to deal with.

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
  - request_type not in [register, change, authority] → true (request_type=question)
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

Where they came from:

- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: requester='Rowan Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

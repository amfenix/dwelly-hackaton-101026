# Case banking-024-at-01: Reason for the Card Restriction

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a question about why a card had become unavailable, and the desk classed it as a card matter of the "reason" type. It sent a query about the card to the card system and closed the case in the asked state. The record shows no answer from the card system yet, so a person still needs to pick up the reply when it arrives and respond to the requester.

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

Attachments: none.

Case reference: id banking-024-at-01, track Banking & Financial Services, case 024, point 1, actor_next other.

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
  - request_type not in [register, change, instruction, authority] → true (request_type=reason)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **card**
- request_type: **reason**
- next_system: **card**

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

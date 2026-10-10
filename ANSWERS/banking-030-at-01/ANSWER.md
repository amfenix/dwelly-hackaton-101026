# Case banking-030-at-01: Replacement card request

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a status question about a card, apparently whether a replacement card is being made and has been sent. The desk classified it as a card status request and sent a query to the card system. The query returned nothing yet, and the case closed as asked. The record's only confirmation is a note that the secure portal accepted a replacement request, reference HV-030. Nothing is left for a person unless the card system's answer needs following up.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-15 09:00:00 UTC

The request:

> Maren’s debit card had become unreliable, so she submitted a replacement request. She contacted H&V to find out whether the card was being made and whether it had been sent.

What happened up to now:

1. 2025-09-15T09:00:00Z · Secure portal — H&V secure portal → Maren Ellery

> Replacement request accepted. Reference: HV-030.

Attachments: none.

Case reference: id banking-030-at-01, track Banking & Financial Services, case 030, point 1, actor_next other.

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

- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **card**

Where they came from:

- event 1 (H&V secure portal): Replacement request accepted. Reference: HV-030. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

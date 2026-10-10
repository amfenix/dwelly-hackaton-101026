# Case banking-021-at-01: Has My Replacement Card Been Sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a status question about a replacement card. The desk found that the bank's portal message only confirmed the request was received, not dispatch or delivery, so it sent a query to the card system and closed the case in the asked state. The record doesn't show an answer from the card system yet, so the dispatch status is still unknown.

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

Attachments: none.

Case reference: id banking-021-at-01, track Banking & Financial Services, case 021, point 1, actor_next other.

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

- event 1 (Harrow & Vale Bank plc): Your replacement card request has been accepted. This confirms the request was received; it does not confirm dispatch or delivery. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

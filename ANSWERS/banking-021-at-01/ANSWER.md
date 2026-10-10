# Case banking-021-at-01: Has My Replacement Card Been Sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

The desk treated the message as a question about a replacement card and asked the card system about it. The query went through and the case closed at that step, but the card system's reply has not come back into the case. The only confirmation on record is the bank's message that the replacement card request was accepted, which shows it was received and not that the card has been dispatched or delivered. Whether the card has shipped is still unknown and is left for a person to find out.

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
  - request_type not in [register, change, authority, instruction] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- event 1 (Harrow & Vale Bank plc): Your replacement card request has been accepted. This confirms the request was received; it does not confirm dispatch or delivery. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-025-at-01: Why a Card Attempt Was Declined

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara asked why her £18.40 card payment at North Quay Books was declined. The desk classed it as a card payment question and sent an enquiry about it to the card system, which accepted the request. The record shows no reason for the decline yet, since the card system's answer hasn't come back, so a person still needs to pass on the reason once it arrives.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-05 09:00:00 UTC

The request:

> Mara wants to know why her £18.40 card payment at North Quay Books was declined.

What happened up to now:

1. 2025-09-05T09:00:00Z · External message — North Quay Books payment terminal → Mara Ellison

> Payment not accepted. Please contact your bank.

Attachments: none.

Case reference: id banking-025-at-01, track Banking & Financial Services, case 025, point 1, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card_payment, amount: 18.40), by rule `do-ask`

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

- subject: **card_payment**
- amount: **18.40**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- initial request (system): Mara wants to know why her £18.40 card payment at North Quay Books was declined. [facts: amount='18.40']
- event 1 (North Quay Books payment terminal): Payment not accepted. Please contact your bank. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-048-at-01: The buyer said payment was sent

**Decision: ask_system**  (final state `ASKED`)

## Summary

A buyer asked to be told when their payment for a workshop invoice reaches the account. The desk classed it as a question about an incoming payment and sent an inquiry to the incoming-payments system, then closed the case at that step. No answer from that system is in the record, so whether the payment has arrived is still unknown, and the only evidence is the buyer's own message saying they sent it. Someone will need to look at the incoming-payments system's reply to tell the buyer.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-21 09:00:00 UTC

The request:

> Please check whether the payment our buyer says they sent for our workshop invoice has reached our H&V business account.

What happened up to now:

1. 2025-10-21T09:00:00Z · External message — Buyer → Alder Quay Studio Ltd.

> I've sent payment for the workshop invoice. Please let me know when it reaches you.

Attachments: none.

Case reference: id banking-048-at-01, track Banking & Financial Services, case 048, point 1, actor_next other.

## Actions taken

- `ask_system` (system: incoming, about: incoming_payment), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `incoming-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = incoming → true (args.system=incoming)
  - next_system = incoming → true (next_system=incoming)
  - next_system absent → false (next_system=incoming)
  - incoming_asked absent → true (incoming_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **incoming_payment**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**

Where they came from:

- event 1 (Buyer): I've sent payment for the workshop invoice. Please let me know when it reaches you. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

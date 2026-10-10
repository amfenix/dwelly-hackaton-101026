# Case banking-002-at-01: Expected Incoming Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

The sender said they had paid the kiln contribution by bank transfer, and the desk treated this as a status question about an incoming payment. It found no confirmation on record, and the payment was not marked as instructed outside the portal. It then sent a query to the incoming-payments system and closed the case in the asked state. The record shows no answer from that system and no further step, so whether the money has arrived is still unconfirmed.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-21 09:00:00 UTC

The request:

> I’m expecting a contribution toward the cost of a shared pottery studio kiln. The sender told me by phone that they had transferred it, but I can’t see it in my H&V account; please check whether it has arrived.

What happened up to now:

1. 2025-07-21T09:00:00Z · External message — Sender → Elowen Marsh

> I’ve sent the contribution for the kiln by bank transfer.

Attachments: none.

Case reference: id banking-002-at-01, track Banking & Financial Services, case 002, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **incoming_payment**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **incoming**

Where they came from:

- event 1 (Sender): I’ve sent the contribution for the kiln by bank transfer. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

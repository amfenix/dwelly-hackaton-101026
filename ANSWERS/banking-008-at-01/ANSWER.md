# Case banking-008-at-01: The purpose recorded with the transfer

**Decision: ask_system**  (final state `ASKED`)

## Summary

Someone from Mallow Pottery Works wrote asking to clarify the purpose of a transfer for a kiln repair, and the desk treated this as a request to look up a recorded fact about the transfer. It checked the record, found no confirmation and no sign of instruction outside the portal, and sent a query to the payment system about the transfer. That query is the only action taken: the payment system's answer hasn't come back, so what the purpose text says is still unknown, and nothing is left for a person unless the answer needs handling.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-02 09:00:00 UTC

The request:

> I paid Mallow Pottery Works for a kiln repair and have forgotten the purpose text I entered. They have emailed asking me to clarify it; please tell me what my transfer instruction recorded.

What happened up to now:

1. 2025-08-02T09:00:00Z · External message — Mallow Pottery Works → Elena Marlow

> I’m following up about your payment for the kiln repair. Please clarify the purpose of the transfer. “Please clarify the purpose.”

Attachments: none.

Case reference: id banking-008-at-01, track Banking & Financial Services, case 008, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `payment-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = payment → true (args.system=payment)
  - next_system = payment → true (next_system=payment)
  - next_system absent → false (next_system=payment)
  - payment_asked absent → true (payment_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **payment**

Where they came from:

- event 1 (Mallow Pottery Works): I’m following up about your payment for the kiln repair. Please clarify the purpose of the transfer. “Please clarify the purpose.” [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

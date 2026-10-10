# Case banking-008-at-01: The purpose recorded with the transfer

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mallow Pottery Works wrote asking about a payment for a kiln repair and asked for the purpose of the transfer to be clarified. The desk classified this as a question about a transfer and sent a query to the payment system, which was accepted, though the record shows no answer coming back. The case is closed as final at that step; nothing was sent to Mallow Pottery Works, and no purpose text has been supplied or recorded.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 1 (Mallow Pottery Works): I’m following up about your payment for the kiln repair. Please clarify the purpose of the transfer. “Please clarify the purpose.” [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

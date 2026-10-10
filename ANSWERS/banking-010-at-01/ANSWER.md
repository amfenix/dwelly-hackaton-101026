# Case banking-010-at-01: Refund visible in the account

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked whether a £42.80 refund from Northmere Home Supplies had reached their account. The desk treated it as a question about an incoming payment and sent a query to the incoming payments system, which accepted it, but no answer is in the case yet. So the refund's status is still unknown; the only entry found is the customer's outgoing transfer, and nothing confirms a refund. The record shows no further step or hand-off to a person, though the agent's own closing message says the case will go to a person if no answer arrives.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-06 09:00:00 UTC

The request:

> I can see my outgoing transfer to Northmere Home Supplies in my secure portal. The supplier told me it might return the £42.80, but I cannot tell whether that specific refund has reached my account. Please check the incoming entries and confirm its status.

What happened up to now:

1. 2025-08-06T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Elowen Marr

> Outgoing transfer — Northmere Home Supplies — £42.80 — shown in account history.

Attachments: none.

Case reference: id banking-010-at-01, track Banking & Financial Services, case 010, point 1, actor_next other.

## Actions taken

- `ask_system` (system: incoming, about: incoming_payment, amount: 42.80), by rule `do-ask`

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
- amount: **42.80**
- counterparty: **Northmere Home Supplies**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**

Where they came from:

- initial request (system): I can see my outgoing transfer to Northmere Home Supplies in my secure portal. The supplier told me it might return the £42.80, but I cannot tell whether that specific refund has reached my account. Please check the incoming entries and confirm its status. [facts: amount='42.80', counterparty='Northmere Home Supplies']
- event 1 (Harrow & Vale Bank plc): Outgoing transfer — Northmere Home Supplies — £42.80 — shown in account history. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

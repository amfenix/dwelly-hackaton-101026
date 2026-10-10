# Case banking-001-at-01: Was the one-off transfer sent?

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked whether H&V sent the £420.00 one-off transfer to Alder & Reed Workshop, which they could see as a debit in their account activity. The desk checked the case and found no confirmation of the transfer and no sign it was instructed outside the portal, so it asked the payment system about the transfer and closed the case in the asked state. The payment system's answer had not come back in the record, so the question of whether the transfer was sent remains open.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-19 09:00:00 UTC

The request:

> I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it.

What happened up to now:

1. 2025-07-19T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> One-off transfer to Alder & Reed Workshop: debit shown in your account activity.

Attachments: none.

Case reference: id banking-001-at-01, track Banking & Financial Services, case 001, point 1, actor_next other.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 420.00), by rule `do-ask`

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **transfer**
- amount: **420.00**
- counterparty: **Alder & Reed Workshop**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- initial request (system): I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it. [facts: amount='420.00', counterparty='Alder & Reed Workshop']
- event 1 (Harrow & Vale Bank plc): One-off transfer to Alder & Reed Workshop: debit shown in your account activity. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

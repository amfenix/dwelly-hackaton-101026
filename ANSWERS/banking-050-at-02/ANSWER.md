# Case banking-050-at-02: Status of a Supplier Payment

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing on secure chat as the company signatory, asked the desk to check what stage a payment had reached, because Alder Quay Supplies says it has not received the funds. The desk classified this as a question about a transfer and sent a query to the payment system, then closed the case at that step with no answer back yet. Her identity was not verified, and no reply has been sent to her, so a person still needs to give her the payment stage and check that it can be shared with an unverified requester.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-25 09:00:00 UTC

The request:

> I’m an authorised signatory for Northmere Studio Ltd. Our supplier says it has not received the payment we authorised for a materials invoice. Please tell me what stage H&V’s records show for that payment.

What happened up to now:

1. 2025-10-25T09:00:00Z · Business portal — H&V business portal → Mara Ellison

> Payment authorisation recorded for the materials invoice from Alder Quay Supplies.

2. 2025-10-25T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records.

Attachments: none.

Case reference: id banking-050-at-02, track Banking & Financial Services, case 050, point 2, actor_next bank.

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

- requester: **Mara Ellison**
- role: **signatory**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: requester='Mara Ellison', role='signatory', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I’m the company signatory for this payment. Alder Quay Supplies says it has not received the funds; please check the stage shown in H&V’s records. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

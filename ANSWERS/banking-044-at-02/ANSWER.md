# Case banking-044-at-02: One Line in the Supplier Batch

**Decision: ask_system**  (final state `ASKED`)

## Summary

Leona Voss, a viewer on secure chat whose identity was not verified, said the batch showed processed and asked whether row SUP-17 had actually been paid. The desk classified it as a status request about the batch and sent a query about SUP-17 to the payment system, and the case closed at that step. The payment system's answer is not in the record, so whether the row was paid is still unknown and nothing has yet been passed back to her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-13 09:00:00 UTC

The request:

> I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected.

What happened up to now:

1. 2025-10-13T09:00:00Z · Business portal — H&V secure portal → Leona Voss

> Batch “Alderwick supplier payments” — status: Processed.

2. 2025-10-13T09:47:00Z · Secure chat — Leona Voss → H&V service agent

> I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status.

Attachments: none.

Case reference: id banking-044-at-02, track Banking & Financial Services, case 044, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: payment, about: batch, reference: SUP-17), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Leona Voss**
- role: **viewer**
- channel: **secure_chat**
- verified: **False**
- subject: **batch**
- reference: **SUP-17**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **payment**

Where they came from:

- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: requester='Leona Voss', role='viewer', channel='secure_chat', verified=False]
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: reference='SUP-17']
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

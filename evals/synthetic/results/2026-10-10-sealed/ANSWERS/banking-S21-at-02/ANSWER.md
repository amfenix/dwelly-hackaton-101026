# Case banking-S21-at-02: Cheque paid in by app — where is it?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Imogen Thackeray, signed in over secure chat, asked where a £350 cheque she paid in through the app on Wednesday had gone, since it still wasn't in her balance. The desk classed it as a question about an incoming payment and sent a query about the £350 to the incoming payments system. The case closed at that step with no reply recorded, so it is not known where the cheque is or whether anything has gone wrong, and the record names no further step for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-21 09:00:00 UTC

The request:

> I paid a £350 cheque in through the app two days ago and it still isn’t in my balance. Where is it?

What happened up to now:

1. 2025-11-21T09:00:00Z · Secure portal — H&V system → Imogen Thackeray

> Mobile cheque deposit, reference HV-S21: £350.00 cheque image submitted to your current account ending 2209.

2. 2025-11-21T09:47:00Z · Secure chat — Imogen Thackeray → H&V service agent

> I paid this £350 cheque in through the app on Wednesday — it’s from my aunt — and it’s still not in my balance. I’ve signed in, so you can see my account. Where is it? Has something gone wrong with it?

Attachments: none.

Case reference: id banking-S21-at-02, track banking, case S21, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: incoming, about: incoming_payment, amount: 350.00), by rule `do-ask`

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

- requester: **Imogen Thackeray**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- amount: **350.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Imogen Thackeray): I paid this £350 cheque in through the app on Wednesday — it’s from my aunt — and it’s still not in my balance. I’ve signed in, so you can see my account. Where is it? Has something gone wrong with it? [facts: requester='Imogen Thackeray', role='customer', channel='secure_chat', verified=False]
- event 2 (Imogen Thackeray): I paid this £350 cheque in through the app on Wednesday — it’s from my aunt — and it’s still not in my balance. I’ve signed in, so you can see my account. Where is it? Has something gone wrong with it? [facts: amount='350.00']
- event 2 (Imogen Thackeray): I paid this £350 cheque in through the app on Wednesday — it’s from my aunt — and it’s still not in my balance. I’ve signed in, so you can see my account. Where is it? Has something gone wrong with it? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

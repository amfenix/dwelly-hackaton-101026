# Case banking-034-at-03: Explaining a service fee

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellery, an unverified customer on secure chat, asked the desk to escalate and check which tariff entry applied to a £3.20 fee on a withdrawal. The desk had already queried the tariff system, and it closed the case as waiting because that system's answer was not yet in. A repeat tariff request and an escalation to a person were both refused because the case was already in the waiting state, so nothing has reached a person and she has not been given an explanation of the fee. The case stays open for a person to pick up, and she still needs identity verification before any account details are shared.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-23 09:00:00 UTC

The request:

> I can see a £3.20 fee beside a foreign-currency cash withdrawal in my H&V secure portal, but I don't understand what the charge is for or how its amount was determined. Please check the fee against the tariff that applied to that transaction.

What happened up to now:

1. 2025-09-23T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> A £3.20 service fee is shown beside your foreign-currency cash withdrawal. The transaction and fee are listed in your secure portal.

2. 2025-09-23T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount.

3. 2025-09-23T10:34:00Z · Internal note — H&V service agent → H&V transaction records

> I am starting the review by matching the recorded transaction type and processing date against the tariff in force on that date. Case HV-034; no refund or account change is authorised by this review.

Attachments: none.

Case reference: id banking-034-at-03, track Banking & Financial Services, case 034, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `tariff-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = tariff → true (next_system=tariff)
  - tariff_asked → true (tariff_asked=True)
  - tariff_status absent → true (tariff_status=not known)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **fee**
- amount: **3.20**
- tariff_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **tariff**

Where they came from:

- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: amount='3.20']
- event 3 (H&V transaction records): I am starting the review by matching the recorded transaction type and processing date against the tariff in force on that date. Case HV-034; no refund or account change is authorised by this review. [facts: tariff_asked=True]
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=tariff); next_system = payment is false (next_system=tariff); next_system absent is false (next_system=tariff); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=tariff); next_system = incoming is false (next_system=tariff); next_system absent is false (next_system=tariff); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=tariff); next_system = recurring is false (next_system=tariff); next_system absent is false (next_system=tariff); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=tariff); next_system = card is false (next_system=tariff); next_system absent is false (next_system=tariff); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=tariff); next_system = access is false (next_system=tariff); next_system absent is false (next_system=tariff); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=tariff); next_system = business is false (next_system=tariff); next_system absent is false (next_system=tariff); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=tariff); next_system = documents is false (next_system=tariff); next_system absent is false (next_system=tariff); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=tariff); tariff_asked absent is false (tariff_asked=True)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

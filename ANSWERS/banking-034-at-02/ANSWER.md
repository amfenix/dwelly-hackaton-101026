# Case banking-034-at-02: Explaining a service fee

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellery, who is not verified, wrote through secure chat asking the desk to escalate and check which tariff entry applied to a £3.20 fee on a withdrawal and how it accounts for the amount. The desk classed it as a fee question and sent a query to the tariff system about the £3.20 fee, which went through without error. The tariff system's answer isn't in the record, so what the fee was and why remains unexplained, and no reply to the customer or escalation is recorded.

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

Attachments: none.

Case reference: id banking-034-at-02, track Banking & Financial Services, case 034, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: tariff, about: fee, amount: 3.20), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `tariff-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = tariff → true (args.system=tariff)
  - next_system = tariff → true (next_system=tariff)
  - next_system absent → false (next_system=tariff)
  - tariff_asked absent → true (tariff_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **fee**
- amount: **3.20**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **tariff**

Where they came from:

- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: amount='3.20']
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

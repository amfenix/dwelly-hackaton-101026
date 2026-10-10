# Case banking-034-at-01: Explaining a service fee

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked what a £3.20 fee beside a foreign-currency cash withdrawal in their secure portal is for, and how it was calculated against the tariff. The desk classed it as a request about a record fact on a fee and sent a question about that fee and amount to the documents system, and nothing on the account was changed. The case closed with the question asked; the record shows no answer from the documents system yet, so the explanation of the fee is still outstanding.

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

Attachments: none.

Case reference: id banking-034-at-01, track Banking & Financial Services, case 034, point 1, actor_next other.

## Actions taken

- `ask_system` (system: documents, about: fee, amount: 3.20), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `documents-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = documents → true (args.system=documents)
  - next_system = documents → true (next_system=documents)
  - next_system absent → false (next_system=documents)
  - documents_asked absent → true (documents_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **fee**
- amount: **3.20**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **documents**

Where they came from:

- initial request (system): I can see a £3.20 fee beside a foreign-currency cash withdrawal in my H&V secure portal, but I don't understand what the charge is for or how its amount was determined. Please check the fee against the tariff that applied to that transaction. [facts: amount='3.20']
- event 1 (Harrow & Vale Bank plc): A £3.20 service fee is shown beside your foreign-currency cash withdrawal. The transaction and fee are listed in your secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

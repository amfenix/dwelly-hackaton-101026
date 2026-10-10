# Case banking-023-at-02: Unrecognised card purchase

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellery, verified on a call, said she didn't recognise a £38.40 Fern & Finch Books card purchase from 14 July 2025. She asked the desk to raise it with the card team and to tell her how to protect her card. The desk registered the request with the card team, and the case closed as requested. The card-protection advice she asked for was not given, so that is still left for a person, and the desk's card check returned nothing, so the transaction was not confirmed against card records.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-01 09:00:00 UTC

The request:

> I want H&V to investigate a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025, which I do not recognise, and tell me how I can safely protect my card.

What happened up to now:

1. 2025-09-01T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> I show a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025. Its appearance in your transaction list does not establish who made it.

2. 2025-09-01T09:47:00Z · Verified call — Mara Ellery → H&V agent

> After completing your identification checks, I’m calling to report that I don’t recognise the Fern & Finch Books purchase. Please raise it with the card team and tell me how to protect my card safely.

Attachments: none.

Case reference: id banking-023-at-02, track Banking & Financial Services, case 023, point 2, actor_next bank.

## Actions taken

- `register_request` (team: card, about: card_payment), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `register` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = register → true (request_type=register)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card_payment**
- amount: **38.40**
- subject_date: **2025-07-14**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **card**

Where they came from:

- event 2 (Mara Ellery): After completing your identification checks, I’m calling to report that I don’t recognise the Fern & Finch Books purchase. Please raise it with the card team and tell me how to protect my card safely. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- initial request (system): I want H&V to investigate a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025, which I do not recognise, and tell me how I can safely protect my card. [facts: amount='38.40', subject_date='2025-07-14']
- event 2 (Mara Ellery): After completing your identification checks, I’m calling to report that I don’t recognise the Fern & Finch Books purchase. Please raise it with the card team and tell me how to protect my card safely. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

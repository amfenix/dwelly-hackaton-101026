# Case banking-035-at-02: Request to Review a Fee

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellison, a verified caller, asked the desk to review a £4.50 paper statement fee dated 18 June 2025, saying she had chosen electronic statements and disputes how the tariff was applied. The desk registered the request with the documents team, and the case closed as requested. A separate documents lookup was refused, so her statement-delivery preference was not checked, and the record shows no change or refund of the fee, so the review and any check of her preference are left for the team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-25 09:00:00 UTC

The request:

> Mara wants H&V to review whether a £4.50 paper statement fee, dated 18 June 2025, was correctly applied. She says she had chosen electronic statements and disputes the fee.

What happened up to now:

1. 2025-09-25T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> A £4.50 paper statement fee dated 18 June 2025 has been applied to your account. This notification does not confirm whether the fee will be changed.

2. 2025-09-25T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied.

Attachments: none.

Case reference: id banking-035-at-02, track Banking & Financial Services, case 035, point 2, actor_next bank.

## Actions taken

- `register_request` (team: documents, about: fee), by rule `do-request`

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **fee**
- amount: **4.50**
- subject_date: **2025-06-18**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: amount='4.50', subject_date='2025-06-18']
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=documents); next_system = payment is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=documents); next_system = incoming is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=documents); next_system = recurring is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=documents); next_system = card is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); access-ask: args.system = access is false (args.system=documents); next_system = access is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=documents); next_system = business is false (next_system=documents); next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register); documents-ask: next_system absent is false (next_system=documents); request_type not in [register, change, authority] is false (request_type=register)

## Final result

submit_request (REQUESTED)

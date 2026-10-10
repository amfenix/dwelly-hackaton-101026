# Case banking-016-at-04: Disputed Direct Debit amount

**Decision: reply**  (final state `REPLIED`)

## Summary

Tamsin Rook, verified on a call, asked for the £18.40 Direct Debit charge to Northmere Water Services to be investigated because she disputes the amount. The desk found the review had already been registered under reference HV-016, refused the agent's attempts to query the recurring system and to submit a new request, and sent a reply to the customer. The case is closed as replied, and the record lists nothing left for a person to do.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-18 09:00:00 UTC

The request:

> I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited.

What happened up to now:

1. 2025-08-18T09:00:00Z · Secure portal — H&V secure portal → Tamsin Rook

> Statement activity: Direct Debit to Northmere Water Services — £18.40, dated 9 July 2025.

2. 2025-08-18T09:47:00Z · Verified call — Tamsin Rook → H&V service agent

> I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge.

3. 2025-08-18T10:34:00Z · Internal note — H&V service agent → H&V Direct Debit team

> I am registering a review of the £18.40 Direct Debit charge to Northmere Water Services dated 9 July 2025. The customer’s inline statement is: “I dispute the amount debited.”

4. 2025-08-18T11:21:00Z · Internal note — H&V Direct Debit team → H&V case journal

> Case journal status: Review request for the £18.40 Direct Debit charge registered under reference HV-016.

Attachments: none.

Case reference: id banking-016-at-04, track Banking & Financial Services, case 016, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `registration-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - registration_asked → true (registration_asked=True)
  - registered present → true (registered=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Tamsin Rook**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **direct_debit**
- amount: **18.40**
- counterparty: **Northmere Water Services because I dispute the amount debited**
- registration_asked: **True**
- registered: **True**
- registration_ref: **HV-016**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **recurring**

Where they came from:

- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: requester='Tamsin Rook', role='customer', channel='verified_call', verified=True]
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: amount='18.40']
- initial request (system): I want H&V to investigate the £18.40 Direct Debit charge to Northmere Water Services because I dispute the amount debited. [facts: counterparty='Northmere Water Services because I dispute the amount debited']
- event 3 (H&V case journal): I am registering a review of the £18.40 Direct Debit charge to Northmere Water Services dated 9 July 2025. The customer’s inline statement is: “I dispute the amount debited.” [facts: registration_asked=True]
- event 4 (H&V Direct Debit team): Case journal status: Review request for the £18.40 Direct Debit charge registered under reference HV-016. [facts: registered=True, registration_ref='HV-016']
- event 2 (Tamsin Rook): I passed your identification checks, and no secrets were transcribed. I dispute the amount debited: “I dispute the amount debited.” Please have the Direct Debit team investigate this £18.40 charge. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=register)
- `submit_request`: register: registration_asked absent is false (registration_asked=True); payment-instruction: next_system = payment is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); recurring-instruction: request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); card-instruction: next_system = card is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); access-instruction: next_system = access is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); business-instruction: next_system = business is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is false (next_system=recurring); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none)

## Final result

reply (REPLIED)

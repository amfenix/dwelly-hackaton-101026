# Case banking-005-at-04: Request about a transfer to the wrong recipient

**Decision: reply**  (final state `REPLIED`)

## Summary

Leona Mercer, verified on a call, asked H&V to register a request to seek the return of a £286.40 transfer she sent to the wrong saved recipient. The record shows the payment team had already registered the return request (reference HV-005), so the desk refused its own attempts to ask the payment system and to submit a new request, and sent Leona a reply instead. The record notes that registration does not confirm the money will be returned, and it lists nothing left for a person to do.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-27 09:00:00 UTC

The request:

> I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return.

What happened up to now:

1. 2025-07-27T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Leona Mercer

> Transfer status: sent. This status confirms the transfer was sent from your H&V account; it does not confirm that the recipient has returned the money.

2. 2025-07-27T09:47:00Z · Verified call — Leona Mercer → H&V service agent

> I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return.

3. 2025-07-27T10:34:00Z · Internal note — H&V service agent → H&V payment team

> I have verified the payer and checked the transfer details for case HV-005. Please register the prescribed request to seek a return; the customer has confirmed the recipient was selected in error.

4. 2025-07-27T11:21:00Z · Internal note — H&V payment team → H&V service agent

> I have registered the return request for case HV-005 against the verified transfer. Registration does not confirm that the money will be returned.

Attachments: none.

Case reference: id banking-005-at-04, track Banking & Financial Services, case 005, point 4, actor_next bank.

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

- requester: **Leona Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **transfer**
- amount: **286.40**
- registration_asked: **True**
- registered: **True**
- registration_ref: **HV-005**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **payment**

Where they came from:

- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: requester='Leona Mercer', role='customer', channel='verified_call', verified=True]
- initial request (system): I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return. [facts: amount='286.40']
- event 3 (H&V payment team): I have verified the payer and checked the transfer details for case HV-005. Please register the prescribed request to seek a return; the customer has confirmed the recipient was selected in error. [facts: registration_asked=True]
- event 4 (H&V payment team): I have registered the return request for case HV-005 against the verified transfer. Registration does not confirm that the money will be returned. [facts: registered=True, registration_ref='HV-005']
- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register)
- `submit_request`: register: registration_asked absent is false (registration_asked=True); payment-instruction: request_type = instruction is false (request_type=register); incoming-instruction: next_system = incoming is false (next_system=payment); request_type = instruction is false (request_type=register); recurring-instruction: next_system = recurring is false (next_system=payment); request_type = instruction is false (request_type=register); card-instruction: next_system = card is false (next_system=payment); request_type = instruction is false (request_type=register); access-instruction: next_system = access is false (next_system=payment); request_type = instruction is false (request_type=register); business-instruction: next_system = business is false (next_system=payment); request_type = instruction is false (request_type=register); documents-instruction: next_system = documents is false (next_system=payment); request_type = instruction is false (request_type=register)

## Final result

reply (REPLIED)

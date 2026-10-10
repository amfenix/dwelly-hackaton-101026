# Case banking-005-at-03: Request about a transfer to the wrong recipient

**Decision: wait**  (final state `WAITING`)

## Summary

Leona Mercer, a verified caller, asked H&V to register a request to seek the return of a £286.40 transfer she sent to the wrong saved recipient. The desk classified it as a transfer registration request and routed it to payment, then closed the case in a waiting state because the team had already been asked to register it and its answer is not in yet. The agent's later attempts to query the payment system, submit the request and escalate were all refused because the case was no longer in the triaged state, so nothing was registered by the desk and the transfer was not checked in the payment records. What is left is for a person to await the team's answer on the registration.

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

Attachments: none.

Case reference: id banking-005-at-03, track Banking & Financial Services, case 005, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `registration-waits` — The team was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - registration_asked → true (registration_asked=True)
  - registered absent → true (registered=not known)

Facts established:

- requester: **Leona Mercer**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **transfer**
- amount: **286.40**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **payment**

Where they came from:

- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: requester='Leona Mercer', role='customer', channel='verified_call', verified=True]
- initial request (system): I sent a £286.40 transfer for a shared pottery-studio bill to the wrong saved recipient. Please register a request to seek its return. [facts: amount='286.40']
- event 3 (H&V service agent): I have verified the payer and checked the transfer details for case HV-005. Please register the prescribed request to seek a return; the customer has confirmed the recipient was selected in error. [facts: registration_asked=True]
- event 2 (Leona Mercer): I selected the wrong saved recipient for my pottery-studio bill transfer. My identity checks are complete, and I want H&V to register a request to seek the money's return. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority] is false (request_type=register)
- `submit_request`: register: state = TRIAGED is false (state=WAITING); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=payment); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

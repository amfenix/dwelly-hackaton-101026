# Case banking-023-at-03: Unrecognised card purchase

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellery, a verified caller, reported that she doesn't recognise a £38.40 card purchase at Fern & Finch Books on 14 July 2025. She asked for it to be raised with the card team and for advice on protecting her card. The desk classed it as a dispute registration and recorded that the team had been asked but its answer was not yet in, so the case closed as "wait" with no actions taken. The agent's later attempts to submit the request, ask the card system and escalate were all refused because the case was already in the waiting state, so nothing further was done and the card-protection question was not answered in the record.

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

3. 2025-09-01T10:34:00Z · Internal note — H&V agent → H&V card team

> I am opening case HV-023 for review of Mara Ellery’s specific posted purchase at Fern & Finch Books for £38.40 on 14 July 2025. The customer says she does not recognise it; no conclusion about the merchant or the purchase has been reached.

Attachments: none.

Case reference: id banking-023-at-03, track Banking & Financial Services, case 023, point 3, actor_next bank.

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

- requester: **Mara Ellery**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card_payment**
- amount: **38.40**
- subject_date: **2025-07-14**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **card**

Where they came from:

- event 2 (Mara Ellery): After completing your identification checks, I’m calling to report that I don’t recognise the Fern & Finch Books purchase. Please raise it with the card team and tell me how to protect my card safely. [facts: requester='Mara Ellery', role='customer', channel='verified_call', verified=True]
- initial request (system): I want H&V to investigate a posted card purchase at Fern & Finch Books for £38.40 on 14 July 2025, which I do not recognise, and tell me how I can safely protect my card. [facts: amount='38.40', subject_date='2025-07-14']
- event 3 (H&V agent): I am opening case HV-023 for review of Mara Ellery’s specific posted purchase at Fern & Finch Books for £38.40 on 14 July 2025. The customer says she does not recognise it; no conclusion about the merchant or the purchase has been reached. [facts: registration_asked=True]
- event 2 (Mara Ellery): After completing your identification checks, I’m calling to report that I don’t recognise the Fern & Finch Books purchase. Please raise it with the card team and tell me how to protect my card safely. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=card); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none)
- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); card-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card); request_type not in [register, change, authority] is false (request_type=register)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

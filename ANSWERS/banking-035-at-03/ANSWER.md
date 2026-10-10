# Case banking-035-at-03: Request to Review a Fee

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified by call, asked the desk to review a £4.50 paper statement fee dated 18 June 2025, saying she had chosen electronic statements and disputing how the tariff was applied. The desk classed it as a fee registration request and found that the team had already been asked to register it but had not yet answered, so it closed the case as waiting. Its later attempts to query the tariff system and to submit the request were both refused because the case was already in WAITING, so nothing was submitted or changed and the fee has not been reviewed; the case is left for a person to pick up once the registration answer comes in.

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

3. 2025-09-25T10:34:00Z · Internal note — H&V service agent → Tariff Team

> I have registered Mara Ellison’s request for review of the £4.50 paper statement fee dated 18 June 2025. Her reason is that she had chosen electronic statements; her inline request reads, “please check how the tariff was applied.”

Attachments: none.

Case reference: id banking-035-at-03, track Banking & Financial Services, case 035, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `registration-waits` — The team was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type in [register, change] → true (request_type=register)
  - registration_asked → true (registration_asked=True)
  - registered absent → true (registered=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **fee**
- amount: **4.50**
- subject_date: **2025-06-18**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **tariff**

Where they came from:

- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: amount='4.50', subject_date='2025-06-18']
- event 3 (H&V service agent): I have registered Mara Ellison’s request for review of the £4.50 paper statement fee dated 18 June 2025. Her reason is that she had chosen electronic statements; her inline request reads, “please check how the tariff was applied.” [facts: registration_asked=True]
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=tariff); next_system = payment is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=tariff); next_system = incoming is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=tariff); next_system = recurring is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=tariff); next_system = card is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=tariff); next_system = access is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=tariff); next_system = business is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=tariff); next_system = documents is false (next_system=tariff); next_system absent is false (next_system=tariff); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register)
- `submit_request`: register: state = TRIAGED is false (state=WAITING); registration_asked absent is false (registration_asked=True); register-what-fits-no-type: state = TRIAGED is false (state=WAITING); request_type = other is false (request_type=register); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=tariff); request_type = instruction is false (request_type=register); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=tariff); request_type = instruction is false (request_type=register); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=tariff); request_type = instruction is false (request_type=register); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=tariff); request_type = instruction is false (request_type=register); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=tariff); request_type = instruction is false (request_type=register); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=tariff); request_type = instruction is false (request_type=register); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=tariff); request_type = instruction is false (request_type=register)

## Final result

wait (WAITING)

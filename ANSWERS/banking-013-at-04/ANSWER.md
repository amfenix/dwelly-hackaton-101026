# Case banking-013-at-04: Cancellation of a Future Payment Instruction

**Decision: wait**  (final state `WAITING`)

## Summary

Elodie Mercer, a verified customer on the secure portal, asked to cancel the next run of her recurring studio-rent payment instruction. The desk did not cancel it: the case closed as "wait" because the recurring payments system had been asked about the instruction and its answer was not yet in. An attempt to submit the cancellation was refused, since the case was in the waiting state and the desk's confirmation check recorded "none" despite her portal message saying she confirmed. Nothing has been submitted or changed, so the instruction is not cancelled and a person needs to pick the case up once the recurring system answers.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-12 09:00:00 UTC

The request:

> I set up a recurring payment for my studio rent and want H&V to cancel the next scheduled run before it starts. Please confirm that the future instruction is cancelled.

What happened up to now:

1. 2025-08-12T09:00:00Z · Secure portal — H&V → Elodie Mercer

> Your recurring studio-rent payment instruction is active. The next scheduled run has not started.

2. 2025-08-12T09:47:00Z · Verified call — Elodie Mercer → H&V agent

> I completed your identification checks. I want to cancel the next run of my studio-rent instruction; please escalate this and tell me how to confirm it securely.

3. 2025-08-12T10:34:00Z · Secure portal — Elodie Mercer → H&V

> I confirm that I want to cancel the future run of my recurring studio-rent payment instruction.

4. 2025-08-12T11:21:00Z · Internal note — H&V agent → H&V protected instruction process

> I checked that Elodie Mercer has authority over this instruction and that its next run has not started. I am submitting her secure-portal cancellation confirmation for instruction HV-013.

Attachments: none.

Case reference: id banking-013-at-04, track Banking & Financial Services, case 013, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `recurring-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_asked → true (recurring_asked=True)
  - recurring_status absent → true (recurring_status=not known)

Facts established:

- requester: **Elodie Mercer**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **standing_order**
- recurring_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**

Where they came from:

- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: requester='Elodie Mercer', role='customer', channel='secure_portal', verified=True]
- event 4 (H&V protected instruction process): I checked that Elodie Mercer has authority over this instruction and that its next run has not started. I am submitting her secure-portal cancellation confirmation for instruction HV-013. [facts: recurring_asked=True]
- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); recurring_asked absent is false (recurring_asked=True); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)

## Final result

wait (WAITING)

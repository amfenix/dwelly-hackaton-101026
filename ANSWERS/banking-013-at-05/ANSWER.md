# Case banking-013-at-05: Cancellation of a Future Payment Instruction

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Elodie Mercer, a verified customer on the secure portal, asked to cancel the next run of her recurring studio-rent instruction (HV-013) and confirmed this in the portal. The desk did not submit the cancellation: the request was refused because its own confirmation fact stayed at "none", even though the recurring system now shows the instruction as CANCELLED, and the case was escalated. A person still needs to check the actual state of the instruction and whether the next run is cancelled, then either confirm that to her or process the cancellation through the proper confirmation step.

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

5. 2025-08-12T12:08:00Z · Internal note — H&V instruction log → H&V agent

> HV-013 — Future run cancelled. No payment was in progress when the cancellation was recorded.

Attachments: none.

Case reference: id banking-013-at-05, track Banking & Financial Services, case 013, point 5, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- requester: **Elodie Mercer**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **standing_order**
- recurring_asked: **True**
- recurring_status: **CANCELLED**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**
- reason: **AGENT_ESCALATED**

Where they came from:

- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: requester='Elodie Mercer', role='customer', channel='secure_portal', verified=True]
- event 4 (H&V instruction log): I checked that Elodie Mercer has authority over this instruction and that its next run has not started. I am submitting her secure-portal cancellation confirmation for instruction HV-013. [facts: recurring_asked=True]
- event 5 (H&V instruction log): HV-013 — Future run cancelled. No payment was in progress when the cancellation was recorded. [facts: recurring_status='CANCELLED']
- event 3 (Elodie Mercer): I confirm that I want to cancel the future run of my recurring studio-rent payment instruction. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: recurring_asked absent is false (recurring_asked=True); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: next_system = card is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: next_system = access is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: next_system = business is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is false (next_system=recurring); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)

## Final result

escalate (ESCALATED)

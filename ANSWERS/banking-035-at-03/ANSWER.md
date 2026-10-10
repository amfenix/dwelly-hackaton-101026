# Case banking-035-at-03: Request to Review a Fee

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, asked the desk to review a £4.50 paper statement fee dated 18 June 2025, saying she had chosen electronic statements and disputes how the tariff was applied. The desk found the registration had already been asked for, so it closed the case as waiting, because the team's answer has not come in yet. It refused the agent's attempts to submit the request again and to send a reply, and it took no other action. Nothing has been decided about whether the fee was correct, and the desk still has to wait for the registration answer before replying to her.

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
  - request_type = register → true (request_type=register)
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
- next_system: **documents**

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

- `submit_request`: register: state = TRIAGED is false (state=WAITING); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=documents); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=register); request_type = change is false (request_type=register); confirmation = given is false (confirmation=none)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); document_ready present is false (document_ready=not known)

## Final result

wait (WAITING)

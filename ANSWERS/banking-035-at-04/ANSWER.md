# Case banking-035-at-04: Request to Review a Fee

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, a verified customer on a call, asked the desk to review a £4.50 paper statement fee dated 18 June 2025, saying she had chosen electronic statements and disputes how the tariff was applied. The desk found her request already registered as HV-035 and routed to the Tariff Team, refused an attempt to query the tariff system directly, and sent her a reply confirming the registration. The record shows no decision on whether the fee was correct or will be changed, so that remains with the Tariff Team.

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

4. 2025-09-25T11:21:00Z · Internal note — H&V request log → H&V service agent

> Request HV-035 registered and routed to the Tariff Team. Registration does not indicate a decision on the fee.

Attachments: none.

Case reference: id banking-035-at-04, track Banking & Financial Services, case 035, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `registration-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=register)
  - registration_asked → true (registration_asked=True)
  - registered present → true (registered=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **fee**
- amount: **4.50**
- subject_date: **2025-06-18**
- registration_asked: **True**
- registered: **True**
- registration_ref: **HV-035**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **tariff**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: amount='4.50', subject_date='2025-06-18']
- event 3 (H&V request log): I have registered Mara Ellison’s request for review of the £4.50 paper statement fee dated 18 June 2025. Her reason is that she had chosen electronic statements; her inline request reads, “please check how the tariff was applied.” [facts: registration_asked=True]
- event 4 (H&V request log): Request HV-035 registered and routed to the Tariff Team. Registration does not indicate a decision on the fee. [facts: registered=True, registration_ref='HV-035']
- event 2 (Mara Ellison): After completing H&V’s identification checks, I asked you to review the £4.50 paper statement fee dated 18 June 2025. I had chosen electronic statements, so I dispute how the tariff was applied. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=tariff); next_system = payment is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: args.system = incoming is false (args.system=tariff); next_system = incoming is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=tariff); next_system = recurring is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=tariff); next_system = card is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: args.system = access is false (args.system=tariff); next_system = access is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=tariff); next_system = business is false (next_system=tariff); next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=tariff); next_system = documents is false (next_system=tariff); next_system absent is false (next_system=tariff); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: next_system absent is false (next_system=tariff); request_type not in [register, change, authority] is false (request_type=register)

## Final result

reply (REPLIED)

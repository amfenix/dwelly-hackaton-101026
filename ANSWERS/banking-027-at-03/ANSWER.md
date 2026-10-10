# Case banking-027-at-03: Access Restored

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, said she still can't sign in to her profile and asked for help restoring access. The desk found that an H&V service agent had already pointed her to the recovery option in the secure portal, so it decided to wait and closed the case in WAITING without taking any action. The agent's later attempts to query the access system and to redirect her to the secure process were both refused because the case was no longer in the triaged state. What remains is for Mara to complete the recovery checks in the secure portal, and nothing more can be done from the desk until she does.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-09 09:00:00 UTC

The request:

> I can’t sign in to my H&V profile after several unsuccessful attempts. Please help me regain access safely so I can review my household spending.

What happened up to now:

1. 2025-09-09T09:00:00Z · Secure portal — H&V app → Mara Ellison

> Sign-in declined. Use H&V’s secure recovery process to restore access.

2. 2025-09-09T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> I’ve completed H&V’s identification checks for this call. I still can’t sign in to my profile, and I need help restoring access; I’m not sharing any password or verification code.

3. 2025-09-09T10:34:00Z · Secure chat — H&V service agent → Mara Ellison

> I’m directing you to the recovery option in H&V’s secure portal. Complete the checks there; I won’t ask you to tell me your password or a verification code.

Attachments: none.

Case reference: id banking-027-at-03, track Banking & Financial Services, case 027, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `already-redirected` — The customer was pointed to the secure process; nothing to do until they use it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = access → true (request_type=access)
  - bank_redirected → true (bank_redirected=True)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **access**
- bank_redirected: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **access**

Where they came from:

- event 2 (Mara Ellison): I’ve completed H&V’s identification checks for this call. I still can’t sign in to my profile, and I need help restoring access; I’m not sharing any password or verification code. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 3 (H&V service agent): the bank already acted: I’m directing you to the recovery option in H&V’s secure portal. Complete the checks there; I won’t ask you to tell me your password or a verification code.
- event 3 (H&V service agent): I’m directing you to the recovery option in H&V’s secure portal. Complete the checks there; I won’t ask you to tell me your password or a verification code. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); access-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=access); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access)
- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=WAITING); request_type = instruction is false (request_type=access); not verified is false (verified=True)

## Final result

wait (WAITING)

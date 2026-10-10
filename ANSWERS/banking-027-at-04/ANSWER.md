# Case banking-027-at-04: Access Restored

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, a customer verified on a call, said she still can't sign in to her profile and asked for help restoring access, without sharing any password or code. The desk classified it as an access request and asked the access system about it; that question has been sent and the case closed in the asked state. Nothing in the record shows an answer from the access system yet, so whether her access is restored is still open and falls to whoever picks up the system's reply.

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

4. 2025-09-09T11:21:00Z · Secure portal — H&V recovery system → Mara Ellison

> Recovery checks completed securely. Return to sign-in.

Attachments: none.

Case reference: id banking-027-at-04, track Banking & Financial Services, case 027, point 4, actor_next bank.

## Actions taken

- `ask_system` (system: access, about: access), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `access-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = access → true (args.system=access)
  - next_system = access → true (next_system=access)
  - next_system absent → false (next_system=access)
  - access_asked absent → true (access_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=access)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **access**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **access**

Where they came from:

- event 2 (Mara Ellison): I’ve completed H&V’s identification checks for this call. I still can’t sign in to my profile, and I need help restoring access; I’m not sharing any password or verification code. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 4 (H&V recovery system): Recovery checks completed securely. Return to sign-in. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

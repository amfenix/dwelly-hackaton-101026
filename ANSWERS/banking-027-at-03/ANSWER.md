# Case banking-027-at-03: Access Restored

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, a customer verified on a call, asked for help restoring access to her profile because she can't sign in. The desk decided to wait: a service agent had already pointed her to the recovery option in H&V's secure portal, so there is nothing to do until she completes the checks there. The agent's attempt to send another secure-process redirect was refused because the case was already in the waiting state, so no new redirect went out, and nothing is left for a person unless she uses the portal and comes back.

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

- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

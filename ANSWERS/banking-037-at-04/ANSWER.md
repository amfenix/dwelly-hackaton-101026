# Case banking-037-at-04: Profile Name Typo

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Elowen Marr, verified on a call, asked for her profile name to be corrected from "Elowen Mar" to "Elowen Marr". The desk found the correction already registered for review by the data team as HV-037, then sent the profile change to her for confirmation in the secure portal. Nothing has been changed yet: the data team has not validated the basis for the correction, and the change awaits her confirmation.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-29 09:00:00 UTC

The request:

> Please correct the spelling of my name in my H&V profile. It shows “Elowen Mar”; my correct name is “Elowen Marr”.

What happened up to now:

1. 2025-09-29T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Elowen Marr

> Profile status: The name displayed in your profile is “Elowen Mar”.

2. 2025-09-29T09:47:00Z · Verified call — Elowen Marr → H&V service agent

> After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information.

3. 2025-09-29T10:34:00Z · Internal note — H&V service agent → H&V data team

> I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made.

4. 2025-09-29T11:21:00Z · Internal note — H&V data team → H&V service agent

> I have logged HV-037 as received for review. The basis for the correction has not yet been validated, and the profile name remains unchanged.

Attachments: none.

Case reference: id banking-037-at-04, track Banking & Financial Services, case 037, point 4, actor_next bank.

## Actions taken

- `send_for_confirmation` (change: profile, to: Elowen Marr), by rule `do-confirm`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `CONFIRM_PENDING`: rule `change-needs-confirmation` — A change is confirmed by the customer in the secure portal, not in chat or by email.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = none → true (confirmation=none)
- `CONFIRM_PENDING` → `CONFIRMATION_SENT`: rule `do-confirm`.
  - state = CONFIRM_PENDING → true (state=CONFIRM_PENDING)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **profile**
- registration_asked: **True**
- registered: **True**
- registration_ref: **HV-037**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: requester='Elowen Marr', role='customer', channel='verified_call', verified=True]
- event 3 (H&V data team): I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made. [facts: registration_asked=True]
- event 4 (H&V data team): I have logged HV-037 as received for review. The basis for the correction has not yet been validated, and the profile name remains unchanged. [facts: registered=True, registration_ref='HV-037']
- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

send_for_confirmation (CONFIRMATION_SENT)

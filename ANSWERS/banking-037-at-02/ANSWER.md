# Case banking-037-at-02: Profile Name Typo

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Elowen Marr, verified on a call, asked for her profile name to be corrected from "Elowen Mar" to "Elowen Marr". The desk treated this as a profile change needing her confirmation, and since none had been given, it sent the change to her for confirmation and closed the case. The correction is not applied until she confirms it in the secure portal, and the data team may still ask her for supporting information.

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

Attachments: none.

Case reference: id banking-037-at-02, track Banking & Financial Services, case 037, point 2, actor_next bank.

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
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: requester='Elowen Marr', role='customer', channel='verified_call', verified=True]
- event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

send_for_confirmation (CONFIRMATION_SENT)

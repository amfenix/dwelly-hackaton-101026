# Case banking-039-at-03: Permitted sign-in list for my profile

**Decision: ask_system**  (final state `ASKED`)

## Summary

Nerys Wren, a verified customer on the secure portal, asked for the permitted session extract for her profile to be delivered through the portal. The desk classified it as a document request about access and sent a query to the access system, which accepted it and returned nothing yet. The case closed at that step, so no session information has been given to her, and a person still needs to deliver the reply once the access system's answer is in the case.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-03 09:00:00 UTC

The request:

> I noticed an unusual sign-in notification for my H&V profile and want a permitted list of the sign-in sessions shown for it.

What happened up to now:

1. 2025-10-03T09:00:00Z · Secure portal — H&V app → Nerys Wren

> I generated a sign-in notification for a new device on 11 July 2025 at 08:42 UTC.

2. 2025-10-03T09:47:00Z · Verified call — Nerys Wren → H&V service agent

> After you completed the bank identification checks, I explained that the new-device notification looked unusual and asked for a list of sign-in sessions for my profile. I did not provide or ask you to record any secrets.

3. 2025-10-03T10:34:00Z · Secure portal — Nerys Wren → H&V Bank

> I confirm that I want the permitted session extract for my profile delivered through this secure portal.

Attachments: none.

Case reference: id banking-039-at-03, track Banking & Financial Services, case 039, point 3, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=document)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Nerys Wren**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **access**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **access**

Where they came from:

- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: requester='Nerys Wren', role='customer', channel='secure_portal', verified=True]
- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

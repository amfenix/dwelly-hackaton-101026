# Case banking-029-at-01: Is the new device linked?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, a verified customer on the secure portal, said she started registering her new tablet in the H&V app and left the screen before she could tell whether it had finished. The desk classified this as a status question about access and sent a query to the access system. The query returned nothing, and the desk has recorded no answer or further step, so the outcome of the registration is still unknown.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-13 09:00:00 UTC

The request:

> I started registering a new tablet for H&V mobile banking, but I am not sure the process finished. Please tell me whether the device is linked and whether it can be used for banking operations.

What happened up to now:

1. 2025-09-13T09:00:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I started registering my new tablet in the H&V app while setting it up. I left the screen before I could tell whether registration had finished.

Attachments: none.

Case reference: id banking-029-at-01, track Banking & Financial Services, case 029, point 1, actor_next other.

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
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **access**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **access**

Where they came from:

- event 1 (Mara Ellison): I started registering my new tablet in the H&V app while setting it up. I left the screen before I could tell whether registration had finished. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I started registering my new tablet in the H&V app while setting it up. I left the screen before I could tell whether registration had finished. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

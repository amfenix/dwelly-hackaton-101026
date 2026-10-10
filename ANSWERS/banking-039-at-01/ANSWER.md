# Case banking-039-at-01: Permitted sign-in list for my profile

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was a question about access, and the desk passed it to the access system by asking it about access. The case closed in the "asked" state, and the access system's answer has not come back into the case. Nothing is confirmed in the record, including the new-device sign-in note for 11 July 2025 at 08:42 UTC, so any follow-up on what the access system returns is left for a person.

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

Attachments: none.

Case reference: id banking-039-at-01, track Banking & Financial Services, case 039, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **access**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **access**

Where they came from:

- event 1 (H&V app): I generated a sign-in notification for a new device on 11 July 2025 at 08:42 UTC. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

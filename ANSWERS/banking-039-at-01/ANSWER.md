# Case banking-039-at-01: Permitted sign-in list for my profile

**Decision: ask_system**  (final state `ASKED`)

## Summary

The request was classed as a document request about account access. The desk passed it to the access system with an ask_system action, and the case closed in the ASKED state. The desk's later attempt to send a reply was refused because none of its reply rules applied once the case was in that state, and no access status had come back. Nothing is recorded as left for a person, but the access system's answer is still outstanding.

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
  - request_type not in [register, change, authority] → true (request_type=document)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- subject: **access**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **access**

Where they came from:

- event 1 (H&V app): I generated a sign-in notification for a new device on 11 July 2025 at 08:42 UTC. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=access); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=access); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

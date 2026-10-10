# Case banking-029-at-01: Is the new device linked?

**Decision: ask_system**  (final state `ASKED`)

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
  - request_type not in [register, change, authority] → true (request_type=question)
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
- request_type: **question**
- next_system: **access**

Where they came from:

- event 1 (Mara Ellison): I started registering my new tablet in the H&V app while setting it up. I left the screen before I could tell whether registration had finished. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I started registering my new tablet in the H&V app while setting it up. I left the screen before I could tell whether registration had finished. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=access); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=access); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

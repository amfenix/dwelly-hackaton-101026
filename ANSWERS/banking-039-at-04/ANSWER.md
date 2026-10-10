# Case banking-039-at-04: Permitted sign-in list for my profile

**Decision: wait**  (final state `WAITING`)

## Summary

Nerys Wren, a verified customer on the secure portal, asked for the permitted session extract for her profile, and the desk classified it as a document request about access. The access system had already been asked and its answer is not in yet, so the desk put the case in a final "wait" state; a second ask to the access system was refused because the case was no longer in the state that allows one. No reply, request or escalation was sent, and the case stays open until the access system's answer arrives and a person picks it up.

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

4. 2025-10-03T11:21:00Z · Internal note — H&V service agent → H&V security team

> I’m escalating case HV-039 and requesting the permitted session extract for Nerys Wren’s profile. Please determine the allowed scope and exclude internal detection details and anyone else’s data.

Attachments: none.

Case reference: id banking-039-at-04, track Banking & Financial Services, case 039, point 4, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `access-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = access → true (next_system=access)
  - access_asked → true (access_asked=True)
  - access_status absent → true (access_status=not known)

Facts established:

- requester: **Nerys Wren**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **access**
- access_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **access**

Where they came from:

- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: requester='Nerys Wren', role='customer', channel='secure_portal', verified=True]
- event 4 (H&V security team): I’m escalating case HV-039 and requesting the permitted session extract for Nerys Wren’s profile. Please determine the allowed scope and exclude internal detection details and anyone else’s data. [facts: access_asked=True]
- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); access-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=access); access_asked absent is false (access_asked=True); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access)

## Final result

wait (WAITING)

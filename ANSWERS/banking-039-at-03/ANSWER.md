# Case banking-039-at-03: Permitted sign-in list for my profile

**Decision: ask_system**  (final state `ASKED`)

## Summary

Nerys Wren, a verified customer on the secure portal, sent a message about access that the desk classed as a question; the message said she wants the permitted session extract for her profile delivered through the portal. The desk routed it to the access system and sent that system an ask about access, and the case closed in the asked state. A later attempt to send a reply was refused because the case was no longer in the triaged state and no access status had come back, so no reply has gone to her yet.

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
  - request_type not in [register, change, authority] → true (request_type=question)
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
- request_type: **question**
- next_system: **access**

Where they came from:

- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: requester='Nerys Wren', role='customer', channel='secure_portal', verified=True]
- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=access); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=access); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=access); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

# Case banking-024-at-03: Reason for the Card Restriction

**Decision: wait**  (final state `WAITING`)

## Summary

Rowan Ellery, who is not verified, asked over secure chat for the category of the restriction on their card after a declined grocery purchase and whether it has been lifted. The desk asked the card system and closed the case as waiting because its answer had not come in, so nothing has been told to Rowan. A second card query and an escalation to a person were both refused because the case was already in the waiting state, which leaves the case open with no card record in it. Someone still needs to verify Rowan's identity and check the card's restriction category and status.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-03 09:00:00 UTC

The request:

> Rowan wants to know why their H&V card became temporarily unavailable after it was declined during a grocery purchase, and whether the restriction has been lifted.

What happened up to now:

1. 2025-09-03T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Rowan Ellery

> Status: Your card is temporarily unavailable. This status does not show the reason.

2. 2025-09-03T09:47:00Z · Secure chat — Rowan Ellery → H&V Customer Support

> I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted.

3. 2025-09-03T10:34:00Z · Internal note — H&V Customer Support Agent → H&V Card Journal

> I’m checking the permitted category for this restriction and the limit on what I may disclose to Rowan.

Attachments: none.

Case reference: id banking-024-at-03, track Banking & Financial Services, case 024, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `card-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_asked → true (card_asked=True)
  - card_status absent → true (card_status=not known)

Facts established:

- requester: **Rowan Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- card_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: requester='Rowan Ellery', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V Card Journal): I’m checking the permitted category for this restriction and the limit on what I may disclose to Rowan. [facts: card_asked=True]
- event 2 (Rowan Ellery): I’m the cardholder and my card was declined while I was paying for groceries. Please tell me the category of the restriction and whether it has been lifted. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=card); card_asked absent is false (card_asked=True); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

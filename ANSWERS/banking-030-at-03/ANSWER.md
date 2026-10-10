# Case banking-030-at-03: Replacement card request

**Decision: ask_system**  (final state `ASKED`)

## Summary

Maren Ellery, a verified customer on secure chat, asked whether her replacement card was being made and whether it had been sent. The desk classified this as a status request about her card and put the question to the card system, changing nothing on her account. The card system's answer has not come back yet, so whether the card is being made or has been sent is still unknown.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-15 09:00:00 UTC

The request:

> Maren’s debit card had become unreliable, so she submitted a replacement request. She contacted H&V to find out whether the card was being made and whether it had been sent.

What happened up to now:

1. 2025-09-15T09:00:00Z · Secure portal — H&V secure portal → Maren Ellery

> Replacement request accepted. Reference: HV-030.

2. 2025-09-15T09:47:00Z · Secure chat — Maren Ellery → H&V agent

> I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent?

3. 2025-09-15T10:34:00Z · Secure chat — H&V agent → Maren Ellery

> I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account.

Attachments: none.

Case reference: id banking-030-at-03, track Banking & Financial Services, case 030, point 3, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `card-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = card → true (args.system=card)
  - next_system = card → true (next_system=card)
  - next_system absent → false (next_system=card)
  - card_asked absent → true (card_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=status)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Maren Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **True**
- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **card**

Where they came from:

- event 2 (Maren Ellery): I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent? [facts: requester='Maren Ellery', role='customer', channel='secure_chat']
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: verified=True]
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

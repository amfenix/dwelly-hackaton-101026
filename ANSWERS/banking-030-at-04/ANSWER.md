# Case banking-030-at-04: Replacement card request

**Decision: wait**  (final state `WAITING`)

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

4. 2025-09-15T11:21:00Z · Internal note — H&V agent → H&V card journal

> I checked the card journal for reference HV-030. The record shows the replacement is in manufacture; it does not confirm dispatch or delivery.

Attachments: none.

Case reference: id banking-030-at-04, track Banking & Financial Services, case 030, point 4, actor_next bank.

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

- requester: **Maren Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **True**
- subject: **card**
- card_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- event 2 (Maren Ellery): I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent? [facts: requester='Maren Ellery', role='customer', channel='secure_chat']
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: verified=True]
- event 4 (H&V card journal): I checked the card journal for reference HV-030. The record shows the replacement is in manufacture; it does not confirm dispatch or delivery. [facts: card_asked=True]
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=card); card_asked absent is false (card_asked=True); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card)

## Final result

wait (WAITING)

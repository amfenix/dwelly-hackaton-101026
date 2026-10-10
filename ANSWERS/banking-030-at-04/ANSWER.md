# Case banking-030-at-04: Replacement card request

**Decision: reply**  (final state `REPLIED`)

## Summary

Maren Ellery, a verified customer on secure chat, asked whether her replacement card was being made and whether it had been sent. The desk checked the card journal, which shows the card as in manufacture with no confirmation of dispatch or delivery, and replied on secure chat saying exactly that and that no card change was made. The case is closed as replied, and nothing is left for a person.

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

4. 2025-09-15T11:21:00Z · Internal note — H&V agent → H&V card journal

> I checked the card journal for reference HV-030. The record shows the replacement is in manufacture; it does not confirm dispatch or delivery.

Attachments: none.

Case reference: id banking-030-at-04, track Banking & Financial Services, case 030, point 4, actor_next bank.

## Actions taken

- `reply` (to: Maren Ellery, channel: secure_chat), by rule `do-reply`

  > The card journal shows in_manufacture. This does not establish dispatch or receipt. No additional card change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `card-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_status present → true (card_status=IN_MANUFACTURE)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Maren Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **True**
- subject: **card**
- card_asked: **True**
- card_status: **IN_MANUFACTURE**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**

Where they came from:

- event 2 (Maren Ellery): I submitted a replacement request because my card has become unreliable. Could you check whether it is being made and whether it has been sent? [facts: requester='Maren Ellery', role='customer', channel='secure_chat']
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: verified=True]
- event 4 (H&V card journal): I checked the card journal for reference HV-030. The record shows the replacement is in manufacture; it does not confirm dispatch or delivery. [facts: card_asked=True]
- event 4 (H&V agent): I checked the card journal for reference HV-030. The record shows the replacement is in manufacture; it does not confirm dispatch or delivery. [facts: card_status='IN_MANUFACTURE']
- event 3 (H&V agent): I’ve completed H&V’s identity checks in this secure chat. I’ll check the existing replacement record and won’t make any changes to your account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

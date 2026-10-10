# Case banking-021-at-04: Has My Replacement Card Been Sent?

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison asked over secure chat whether dispatch of her replacement card had been registered, since the portal only said the request was accepted. The desk checked the card journal, which shows the card as dispatched with no record of receipt, and replied to her on secure chat saying so and that no card change was made. Her identity was not verified on this chat, but the desk replied anyway because it was only a status check; the case is closed with nothing left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-28 09:00:00 UTC

The request:

> I need to know whether the replacement card ordered for my H&V account has actually been dispatched. The secure portal confirmed that my request was accepted, but I cannot see confirmation of delivery or dispatch.

What happened up to now:

1. 2025-08-28T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> Your replacement card request has been accepted. This confirms the request was received; it does not confirm dispatch or delivery.

2. 2025-08-28T09:47:00Z · Secure chat — Mara Ellison → Harrow & Vale Bank plc agent

> I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived.

3. 2025-08-28T10:34:00Z · Internal note — H&V agent → Card journal

> I’m checking the card journal for the dispatch record associated with case HV-021. The customer has asked whether dispatch was registered; please return the recorded status only.

4. 2025-08-28T11:21:00Z · Internal note — Card journal → H&V agent

> Dispatch status: registered. Receipt by the customer is not recorded.

Attachments: none.

Case reference: id banking-021-at-04, track Banking & Financial Services, case 021, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The card journal shows dispatched. This does not confirm that the customer has received the card. No additional card change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `card-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_status present → true (card_status=DISPATCHED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- card_asked: **True**
- card_status: **DISPATCHED**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **card**

Where they came from:

- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (Card journal): I’m checking the card journal for the dispatch record associated with case HV-021. The customer has asked whether dispatch was registered; please return the recorded status only. [facts: card_asked=True]
- event 4 (Card journal): Dispatch status: registered. Receipt by the customer is not recorded. [facts: card_status='DISPATCHED']
- event 2 (Mara Ellison): I’m following up because the portal only says my replacement card request was accepted. Please check whether dispatch has been registered; I don’t have confirmation that the card has arrived. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-022-at-04: Lost card blocked

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, verified on a call, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk checked the card journal, which shows the card as blocked, and replied to her on the verified call saying so, that this doesn't establish why it is blocked or whether it can be used, and that no additional card change was made. The case is closed as replied, and the record lists nothing left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-30 09:00:00 UTC

The request:

> I noticed my H&V debit card was missing after a visit to Alder Quay Market. Please block it immediately.

What happened up to now:

1. 2025-08-30T09:00:00Z · Verified call — Mara Ellison → H&V service agent

> After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note.

2. 2025-08-30T09:47:00Z · Internal note — H&V service agent → H&V card team

> I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call.

3. 2025-08-30T10:34:00Z · Secure portal — H&V service agent → H&V card system

> I have submitted the verified instruction to block Mara Ellison's missing card under case HV-022.

4. 2025-08-30T11:21:00Z · Secure portal — H&V card system → H&V service agent

> Card journal status: BLOCKED. The card is marked blocked.

Attachments: none.

Case reference: id banking-022-at-04, track Banking & Financial Services, case 022, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: verified_call), by rule `do-reply`

  > The card journal shows your card as blocked. This does not establish why the card is blocked or whether it can be used. No additional card change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `card-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=instruction)
  - next_system = card → true (next_system=card)
  - card_status present → true (card_status=BLOCKED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card**
- counterparty: **Alder Quay Market**
- card_asked: **True**
- card_status: **BLOCKED**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: counterparty='Alder Quay Market']
- event 3 (H&V card system): I have submitted the verified instruction to block Mara Ellison's missing card under case HV-022. [facts: card_asked=True]
- event 4 (H&V card system): Card journal status: BLOCKED. The card is marked blocked. [facts: card_status='BLOCKED']
- event 2 (H&V service agent): I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call. [facts: registration_asked=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

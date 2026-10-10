# Case banking-025-at-05: Why a Card Attempt Was Declined

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, verified on a call, asked why her £18.40 payment at North Quay Books was declined. The desk found the matching entry in the card authorisation journal, which shows it was declined because her available balance was insufficient, and replied to her on the verified call with that reason, noting it does not establish a different cause or authorise a retry. No card change was made, the case is closed as replied, and nothing is left for a person, though the recorded reason text was cut off after "£18.".

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-05 09:00:00 UTC

The request:

> Mara wants to know why her £18.40 card payment at North Quay Books was declined.

What happened up to now:

1. 2025-09-05T09:00:00Z · External message — North Quay Books payment terminal → Mara Ellison

> Payment not accepted. Please contact your bank.

2. 2025-09-05T09:47:00Z · Verified call — H&V agent → Mara Ellison

> I’ve completed the required identification checks. Please tell me which declined attempt you want me to investigate; I won’t ask you to share any secret codes.

3. 2025-09-05T10:34:00Z · Verified call — Mara Ellison → H&V agent

> I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt.

4. 2025-09-05T11:21:00Z · Internal note — H&V agent → H&V card authorisation journal

> I’m searching the journal for Mara Ellison’s North Quay Books authorisation attempt for £18.40, using the merchant and amount she identified. I’ll check the recorded response for that attempt.

5. 2025-09-05T12:08:00Z · Internal note — H&V card authorisation journal → H&V agent

> Matching authorisation found: declined because available balance was insufficient to cover the £18.40 authorisation at the time of the attempt.

Attachments: none.

Case reference: id banking-025-at-05, track Banking & Financial Services, case 025, point 5, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: verified_call), by rule `do-reply`

  > The card journal shows declined (recorded reason: available balance was insufficient to cover the £18.). This does not establish a different cause or authorise a retry. No additional card change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `card-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_status present → true (card_status=DECLINED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card_payment**
- amount: **18.40**
- card_asked: **True**
- card_status: **DECLINED**
- card_reason: **available balance was insufficient to cover the £18.**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **reason**
- next_system: **card**

Where they came from:

- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: requester='Mara Ellison', role='customer', channel='verified_call']
- event 2 (H&V agent): I’ve completed the required identification checks. Please tell me which declined attempt you want me to investigate; I won’t ask you to share any secret codes. [facts: verified=True]
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: amount='18.40']
- event 4 (H&V card authorisation journal): I’m searching the journal for Mara Ellison’s North Quay Books authorisation attempt for £18.40, using the merchant and amount she identified. I’ll check the recorded response for that attempt. [facts: card_asked=True]
- event 5 (H&V card authorisation journal): Matching authorisation found: declined because available balance was insufficient to cover the £18.40 authorisation at the time of the attempt. [facts: card_status='DECLINED', card_reason='available balance was insufficient to cover the £18.']
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-025-at-04: Why a Card Attempt Was Declined

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, asked why her £18.40 card payment at North Quay Books was declined. The desk identified her, classified this as a request for a reason on a card payment, and put the question to the card system. The card system's answer hasn't come back, so the case is closed in a waiting state with no actions taken, and nothing has been told to her yet about why the payment was declined.

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

Attachments: none.

Case reference: id banking-025-at-04, track Banking & Financial Services, case 025, point 4, actor_next bank.

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card_payment**
- amount: **18.40**
- card_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **reason**
- next_system: **card**

Where they came from:

- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: requester='Mara Ellison', role='customer', channel='verified_call']
- event 2 (H&V agent): I’ve completed the required identification checks. Please tell me which declined attempt you want me to investigate; I won’t ask you to share any secret codes. [facts: verified=True]
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: amount='18.40']
- event 4 (H&V card authorisation journal): I’m searching the journal for Mara Ellison’s North Quay Books authorisation attempt for £18.40, using the merchant and amount she identified. I’ll check the recorded response for that attempt. [facts: card_asked=True]
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

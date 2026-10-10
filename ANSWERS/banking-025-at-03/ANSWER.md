# Case banking-025-at-03: Why a Card Attempt Was Declined

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, verified on a call, asked why her £18.40 payment at North Quay Books was declined. The desk identified it as a card payment query and sent a question about that payment to the card system. The case closed with that question asked, and the record shows no reply yet, so the reason for the decline is still unknown and someone still needs to pass the answer to Mara once it arrives.

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

Attachments: none.

Case reference: id banking-025-at-03, track Banking & Financial Services, case 025, point 3, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card_payment, amount: 18.40), by rule `do-ask`

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
  - request_type not in [register, change, instruction, authority] → true (request_type=reason)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card_payment**
- amount: **18.40**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **reason**
- next_system: **card**

Where they came from:

- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: requester='Mara Ellison', role='customer', channel='verified_call']
- event 2 (H&V agent): I’ve completed the required identification checks. Please tell me which declined attempt you want me to investigate; I won’t ask you to share any secret codes. [facts: verified=True]
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: amount='18.40']
- event 3 (Mara Ellison): I’m calling to find out why my £18.40 payment at North Quay Books was declined. Please check that particular attempt. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

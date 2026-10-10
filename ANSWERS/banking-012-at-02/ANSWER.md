# Case banking-012-at-02: New standing-order amount

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Mira Ellery asked over secure chat to raise her standing order from £42.00 to £68.00 a month. She hadn't confirmed the change and wasn't verified, and she had made the request in chat rather than the portal. The desk did not change the order. It sent her a confirmation request for the £68.00 amount and closed the case in that state. The increase will only go ahead once she confirms it herself, and the standing order remains at £42.00 until then.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-10 09:00:00 UTC

The request:

> Mira wants to increase her monthly standing order to the fictional Westmere Garden Cooperative from £42.00 to £68.00. She has not yet authorised the change.

What happened up to now:

1. 2025-08-10T09:00:00Z · Secure portal — H&V system → Mira Ellery

> Standing order to Westmere Garden Cooperative: £42.00 per month.

2. 2025-08-10T09:47:00Z · Secure chat — Mira Ellery → H&V agent

> I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet.

Attachments: none.

Case reference: id banking-012-at-02, track Banking & Financial Services, case 012, point 2, actor_next bank.

## Actions taken

- `send_for_confirmation` (change: standing_order, amount=68.00, to: Mira Ellery), by rule `do-confirm`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `CONFIRM_PENDING`: rule `change-needs-confirmation` — A change is confirmed by the customer in the secure portal, not in chat or by email.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = none → true (confirmation=none)
  - registration_asked absent → true (registration_asked=not known)
- `CONFIRM_PENDING` → `CONFIRMATION_SENT`: rule `do-confirm`.
  - state = CONFIRM_PENDING → true (state=CONFIRM_PENDING)

Facts established:

- requester: **Mira Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- amount: **68.00**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: requester='Mira Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: amount='68.00']
- event 2 (Mira Ellery): I want to increase this standing order to £68.00 a month. The portal still shows £42.00, and I haven’t confirmed a change yet. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

send_for_confirmation (CONFIRMATION_SENT)

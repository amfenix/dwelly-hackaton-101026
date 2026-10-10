# Case banking-008-at-03: The purpose recorded with the transfer

**Decision: wait**  (final state `WAITING`)

## Summary

Elena Marlow asked the desk, through secure chat, to look up the purpose text her transfer instruction to Mallow Pottery Works recorded for a kiln repair payment. The desk checked the payment system, which has been asked but hasn't answered yet, so the case closed as waiting and no actions were taken. Her identity is still marked as not verified in the record even though she says she completed the checks, so what remains is the payment system's answer and confirmation of her identity before any reply with the purpose text.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-02 09:00:00 UTC

The request:

> I paid Mallow Pottery Works for a kiln repair and have forgotten the purpose text I entered. They have emailed asking me to clarify it; please tell me what my transfer instruction recorded.

What happened up to now:

1. 2025-08-02T09:00:00Z · External message — Mallow Pottery Works → Elena Marlow

> I’m following up about your payment for the kiln repair. Please clarify the purpose of the transfer. “Please clarify the purpose.”

2. 2025-08-02T09:47:00Z · Secure chat — Elena Marlow → H&V service agent

> I’ve completed the identity checks in this secure chat. I paid Mallow Pottery Works for a kiln repair, but I can’t remember the purpose text I entered; please look up what my instruction recorded.

3. 2025-08-02T10:34:00Z · Internal note — H&V service agent → H&V payment journal

> I’m searching the purpose field on Elena Marlow’s transfer instruction under case HV-008. I’ll provide her with the bank’s recorded text only and won’t send or rewrite a message to the supplier.

Attachments: none.

Case reference: id banking-008-at-03, track Banking & Financial Services, case 008, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `payment-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_asked → true (payment_asked=True)
  - payment_status absent → true (payment_status=not known)

Facts established:

- requester: **Elena Marlow**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **payment**

Where they came from:

- event 2 (Elena Marlow): I’ve completed the identity checks in this secure chat. I paid Mallow Pottery Works for a kiln repair, but I can’t remember the purpose text I entered; please look up what my instruction recorded. [facts: requester='Elena Marlow', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V payment journal): I’m searching the purpose field on Elena Marlow’s transfer instruction under case HV-008. I’ll provide her with the bank’s recorded text only and won’t send or rewrite a message to the supplier. [facts: payment_asked=True]
- event 2 (Elena Marlow): I’ve completed the identity checks in this secure chat. I paid Mallow Pottery Works for a kiln repair, but I can’t remember the purpose text I entered; please look up what my instruction recorded. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

# Case banking-002-at-03: Expected Incoming Payment

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Marsh, an unverified customer writing over secure chat, asked the desk to check whether H&V had received the pottery studio kiln contribution that the sender says they transferred. The desk asked the incoming-payments system and took no other action, and the case closed in a waiting state because that system's answer has not come back yet. Nothing is left for a person to do yet; the case depends on the incoming-payment check returning.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-21 09:00:00 UTC

The request:

> I’m expecting a contribution toward the cost of a shared pottery studio kiln. The sender told me by phone that they had transferred it, but I can’t see it in my H&V account; please check whether it has arrived.

What happened up to now:

1. 2025-07-21T09:00:00Z · External message — Sender → Elowen Marsh

> I’ve sent the contribution for the kiln by bank transfer.

2. 2025-07-21T09:47:00Z · Secure chat — Elowen Marsh → H&V service agent

> I’m escalating this because the contribution for our pottery studio kiln still isn’t showing in my account. The sender told me they transferred it, so please check whether H&V has received it.

3. 2025-07-21T10:34:00Z · Internal note — H&V service agent → H&V incoming-payment journal

> I’m checking incoming credits recorded for Elowen Marsh’s account now. I’ll report only what H&V’s records show.

Attachments: none.

Case reference: id banking-002-at-03, track Banking & Financial Services, case 002, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `incoming-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = incoming → true (next_system=incoming)
  - incoming_asked → true (incoming_asked=True)
  - incoming_found absent → true (incoming_found=not known)

Facts established:

- requester: **Elowen Marsh**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- incoming_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **incoming**

Where they came from:

- event 2 (Elowen Marsh): I’m escalating this because the contribution for our pottery studio kiln still isn’t showing in my account. The sender told me they transferred it, so please check whether H&V has received it. [facts: requester='Elowen Marsh', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V incoming-payment journal): I’m checking incoming credits recorded for Elowen Marsh’s account now. I’ll report only what H&V’s records show. [facts: incoming_asked=True]
- event 2 (Elowen Marsh): I’m escalating this because the contribution for our pottery studio kiln still isn’t showing in my account. The sender told me they transferred it, so please check whether H&V has received it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

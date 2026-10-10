# Case banking-S49-at-02: Three requests in one message

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## Summary

Declan Ashworth, who is not verified, wrote in secure chat with three questions: when his standing order to his sister next goes out, why he was charged £4.50 on 1 December, and a change of address. The desk treated the message as a change request, sent him a confirmation to complete in the secure portal, and closed the case there. A later attempt to check the recurring system was refused because the case was already closed, so none of the three questions has been answered, and they remain open for a person to pick up once he has verified and confirmed.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-12-19 09:00:00 UTC

The request:

> Three things: when does my standing order to my sister next go out, why was I charged £4.50 on 1 December, and please change my address to 14 Quillan Road — I’ve moved.

What happened up to now:

1. 2025-12-19T09:00:00Z · Secure portal — H&V system → Declan Ashworth

> Account activity: 1 December 2025 — charge £4.50.

2. 2025-12-19T09:47:00Z · Secure chat — Declan Ashworth → H&V service agent

> Three things please: when does my standing order to my sister Saoirse next go out, why was I charged £4.50 on 1 December, and can you change my address to 14 Quillan Road, Hebden Moor? I’ve just moved.

Attachments: none.

Case reference: id banking-S49-at-02, track banking, case S49, point 2, actor_next bank.

## Actions taken

- `send_for_confirmation` (change: standing_order, amount=4.50, to: Declan Ashworth), by rule `do-confirm`

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

- requester: **Declan Ashworth**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- amount: **4.50**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **recurring**

Where they came from:

- event 2 (Declan Ashworth): Three things please: when does my standing order to my sister Saoirse next go out, why was I charged £4.50 on 1 December, and can you change my address to 14 Quillan Road, Hebden Moor? I’ve just moved. [facts: requester='Declan Ashworth', role='customer', channel='secure_chat', verified=False]
- event 2 (Declan Ashworth): Three things please: when does my standing order to my sister Saoirse next go out, why was I charged £4.50 on 1 December, and can you change my address to 14 Quillan Road, Hebden Moor? I’ve just moved. [facts: amount='4.50']
- event 2 (Declan Ashworth): Three things please: when does my standing order to my sister Saoirse next go out, why was I charged £4.50 on 1 December, and can you change my address to 14 Quillan Road, Hebden Moor? I’ve just moved. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change)

## Final result

send_for_confirmation (CONFIRMATION_SENT)

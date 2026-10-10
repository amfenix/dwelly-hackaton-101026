# Case banking-008-at-04: The purpose recorded with the transfer

**Decision: reply**  (final state `REPLIED`)

## Summary

Elena Marlow asked, over secure chat, for the purpose text she had entered on her payment to Mallow Pottery Works for a kiln repair. The desk looked up the payment record, got a status it could not classify, and replied that it could not confirm a payment status yet and that no new transfer was made. Its reply did not give her the purpose text, although the payment journal noted "Deposit for kiln repair estimate". The desk still lists her as unverified despite her saying she completed the identity checks, and the case is closed with nothing further assigned to a person.

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

4. 2025-08-02T11:21:00Z · Internal note — H&V payment journal → H&V service agent

> Purpose field on the matching transfer instruction: “Deposit for kiln repair estimate”.

Attachments: none.

Case reference: id banking-008-at-04, track Banking & Financial Services, case 008, point 4, actor_next bank.

## Actions taken

- `reply` (to: Elena Marlow, channel: secure_chat), by rule `do-reply`

  > The payment record answered, but not with a clear status, so we cannot confirm one yet. The answer does not establish a recognized payment status or the recipient's outcome. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=question)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=OTHER)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Elena Marlow**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- payment_status: **OTHER**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Elena Marlow): I’ve completed the identity checks in this secure chat. I paid Mallow Pottery Works for a kiln repair, but I can’t remember the purpose text I entered; please look up what my instruction recorded. [facts: requester='Elena Marlow', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V payment journal): I’m searching the purpose field on Elena Marlow’s transfer instruction under case HV-008. I’ll provide her with the bank’s recorded text only and won’t send or rewrite a message to the supplier. [facts: payment_asked=True]
- event 4 (H&V payment journal): Purpose field on the matching transfer instruction: “Deposit for kiln repair estimate”. [facts: payment_status='OTHER']
- event 2 (Elena Marlow): I’ve completed the identity checks in this secure chat. I paid Mallow Pottery Works for a kiln repair, but I can’t remember the purpose text I entered; please look up what my instruction recorded. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)

## Final result

reply (REPLIED)

# Case banking-018-at-04: Two Future Payments

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, verified by call, asked the desk to check two future £34.80 payments to Northmere Heating and remove the duplicate. The desk found two separate instruction records behind them, one standing order and one direct debit mandate, and replied by call that the record shows two separate instructions. It said this does not establish execution or the recipient's outcome and that no new transfer was made. Nothing was cancelled or removed, and her request to escalate was not actioned. A check of the recurring system was refused, the case closed as replied, and no person is assigned.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-22 09:00:00 UTC

The request:

> I can see two future payments of £34.80 to Northmere Heating. Please check whether they are duplicates and remove the duplicate.

What happened up to now:

1. 2025-08-22T09:00:00Z · Secure portal — H&V secure portal → Mara Ellison

> Two future payment lines of £34.80 to Northmere Heating are shown. Their relationship has not been established.

2. 2025-08-22T09:47:00Z · Verified call — Mara Ellison → H&V service agent

> After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate.

3. 2025-08-22T10:34:00Z · Internal note — H&V service agent → H&V instruction journal

> I am checking the type and internal reference of each instruction behind the two future lines. I have not cancelled either instruction.

4. 2025-08-22T11:21:00Z · Internal note — H&V instruction journal → H&V service agent

> The entries match separate instruction records: one customer standing order and one direct debit mandate. Their types and internal references are distinct.

Attachments: none.

Case reference: id banking-018-at-04, track Banking & Financial Services, case 018, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: verified_call), by rule `do-reply`

  > The payment record shows 2 separate payment instructions. Their individual status is recorded without a single combined outcome. This does not establish execution or the recipient's outcome. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=instruction)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=OTHER)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **standing_order**
- amount: **34.80**
- counterparty: **Northmere Heating**
- payment_asked: **True**
- payment_status: **OTHER**
- payment_count: **2**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **payment**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Mara Ellison): After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- initial request (system): I can see two future payments of £34.80 to Northmere Heating. Please check whether they are duplicates and remove the duplicate. [facts: amount='34.80', counterparty='Northmere Heating']
- event 3 (H&V instruction journal): I am checking the type and internal reference of each instruction behind the two future lines. I have not cancelled either instruction. [facts: payment_asked=True]
- event 4 (H&V instruction journal): The entries match separate instruction records: one customer standing order and one direct debit mandate. Their types and internal references are distinct. [facts: payment_status='OTHER', payment_count=2]
- event 2 (Mara Ellison): After completing H&V's identity checks, I asked you to escalate this and remove the duplicate. I do not know which line is the duplicate. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=recurring); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); request_type not in [register, change, authority, instruction] is false (request_type=instruction); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)

## Final result

reply (REPLIED)

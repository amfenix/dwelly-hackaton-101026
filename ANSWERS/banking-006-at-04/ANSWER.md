# Case banking-006-at-04: Two Similar Transfers

**Decision: reply**  (final state `REPLIED`)

## Summary

Mira Ellison, writing over secure chat and not verified, asked whether her two transfers were separate instructions and whether the pending one had been stopped or returned. The desk replied that the payment record shows 2 separate instructions with no single combined outcome, that this doesn't establish execution or the recipient's outcome, and that no new transfer was made. The desk did not stop or return either instruction, and the reply doesn't say whether the pending one was stopped; the case closed on that reply with nothing further assigned to a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-29 09:00:00 UTC

The request:

> Mira, the account holder, wants H&V to establish whether two similar outgoing transfer entries are one instruction shown twice or two separate instructions, and asks whether the second can be stopped or returned.

What happened up to now:

1. 2025-07-29T09:00:00Z · Secure portal — H&V → Mira Ellison

> Your payment activity shows two similar outgoing transfer entries to North Quay Utilities for £84.20. One is marked Completed and the other Pending.

2. 2025-07-29T09:47:00Z · Secure chat — Mira Ellison → H&V agent

> I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned.

3. 2025-07-29T10:34:00Z · Internal note — H&V agent → H&V payment instruction journal

> I’m checking the count and independent instruction references for Mira’s own payment instructions before advising. I have not cancelled or returned either instruction.

4. 2025-07-29T11:21:00Z · Internal note — H&V payment instruction journal → H&V agent

> Journal match: two distinct instruction references for the same payee and amount. One instruction is Completed; the other is Pending.

Attachments: none.

Case reference: id banking-006-at-04, track Banking & Financial Services, case 006, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mira Ellison, channel: secure_chat), by rule `do-reply`

  > The payment record shows 2 separate payment instructions. Their individual status is recorded without a single combined outcome. This does not establish execution or the recipient's outcome. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=OTHER)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mira Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- payment_asked: **True**
- payment_status: **OTHER**
- payment_count: **2**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: requester='Mira Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V payment instruction journal): I’m checking the count and independent instruction references for Mira’s own payment instructions before advising. I have not cancelled or returned either instruction. [facts: payment_asked=True]
- event 4 (H&V payment instruction journal): Journal match: two distinct instruction references for the same payee and amount. One instruction is Completed; the other is Pending. [facts: payment_status='OTHER', payment_count=2]
- event 2 (Mira Ellison): I own this account and only meant to make one transfer. Please check whether these are separate instructions, and whether the pending one has been stopped or returned. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

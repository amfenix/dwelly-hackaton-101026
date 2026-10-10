# Case banking-044-at-04: One Line in the Supplier Batch

**Decision: reply**  (final state `REPLIED`)

## Summary

Leona Voss, a viewer who was not verified, asked over secure chat whether row SUP-17 in her batch had actually been paid, since the batch showed as processed. The desk checked the payment record, found the row rejected because the beneficiary details did not match the receiving institution's records, and replied on secure chat with that status and reason. The reply also said this does not establish a different cause or authorise a retry, and that no new transfer was made; the case is closed with nothing left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-13 09:00:00 UTC

The request:

> I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected.

What happened up to now:

1. 2025-10-13T09:00:00Z · Business portal — H&V secure portal → Leona Voss

> Batch “Alderwick supplier payments” — status: Processed.

2. 2025-10-13T09:47:00Z · Secure chat — Leona Voss → H&V service agent

> I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status.

3. 2025-10-13T10:34:00Z · Internal note — H&V service agent → H&V payment journal

> My first action is to look up row SUP-17 in the previously authorised batch and verify the status of that line specifically.

4. 2025-10-13T11:21:00Z · Business portal — H&V secure portal → Leona Voss

> Row SUP-17 — status: Rejected. Reason: Beneficiary details did not match the receiving institution’s records.

Attachments: none.

Case reference: id banking-044-at-04, track Banking & Financial Services, case 044, point 4, actor_next bank.

## Actions taken

- `reply` (to: Leona Voss, channel: secure_chat), by rule `do-reply`

  > The payment record shows your batch as rejected (recorded reason: Beneficiary details did not match the receiving institution’s records.). This does not establish a different cause or authorise a retry. No new transfer was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `payment-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_status present → true (payment_status=REJECTED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Leona Voss**
- role: **viewer**
- channel: **secure_chat**
- verified: **False**
- subject: **batch**
- reference: **SUP-17**
- payment_asked: **True**
- payment_status: **REJECTED**
- payment_reason: **Beneficiary details did not match the receiving institution’s records.**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: requester='Leona Voss', role='viewer', channel='secure_chat', verified=False]
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: reference='SUP-17']
- event 3 (H&V secure portal): My first action is to look up row SUP-17 in the previously authorised batch and verify the status of that line specifically. [facts: payment_asked=True]
- event 4 (H&V secure portal): Row SUP-17 — status: Rejected. Reason: Beneficiary details did not match the receiving institution’s records. [facts: payment_status='REJECTED', payment_reason='Beneficiary details did not match the receiving institution’s records.']
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

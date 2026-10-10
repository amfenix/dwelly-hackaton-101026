# Case banking-010-at-04: Refund visible in the account

**Decision: reply**  (final state `REPLIED`)

## Summary

Elowen Marr, an unverified customer on secure chat, asked the desk to check whether an incoming £42.80 entry was for the specific Northmere Home Supplies transfer that might be returned. The desk found an incoming entry of 42.80 and replied on secure chat that the incoming-payment record shows a payment of 42.80, that this does not establish the sender's payment status, and that no payment was changed. The case is closed as replied, and the record shows nothing left for a person; note that the reply did not state that the entry is the refund for that specific transfer.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-06 09:00:00 UTC

The request:

> I can see my outgoing transfer to Northmere Home Supplies in my secure portal. The supplier told me it might return the £42.80, but I cannot tell whether that specific refund has reached my account. Please check the incoming entries and confirm its status.

What happened up to now:

1. 2025-08-06T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Elowen Marr

> Outgoing transfer — Northmere Home Supplies — £42.80 — shown in account history.

2. 2025-08-06T09:47:00Z · Secure chat — Elowen Marr → H&V customer service agent

> I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment.

3. 2025-08-06T10:34:00Z · Internal note — H&V customer service agent → H&V incoming-entry journal

> I am checking the linked incoming entries on Elowen Marr's account for a £42.80 refund matching the Northmere Home Supplies transfer. I will not treat a similar-looking entry as a match.

4. 2025-08-06T11:21:00Z · Internal note — H&V incoming-entry journal → H&V customer service agent

> The incoming-entry record shows a £42.80 credit identified as the refund for the Northmere Home Supplies transfer in the account history.

Attachments: none.

Case reference: id banking-010-at-04, track Banking & Financial Services, case 010, point 4, actor_next bank.

## Actions taken

- `reply` (to: Elowen Marr, channel: secure_chat), by rule `do-reply`

  > The incoming-payment record shows an incoming payment of 42.80. This does not establish the sender's payment status. No payment was changed.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `incoming-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = incoming → true (next_system=incoming)
  - incoming_found present → true (incoming_found=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- amount: **42.80**
- counterparty: **Northmere Home Supplies**
- incoming_asked: **True**
- incoming_found: **True**
- incoming_amount: **42.80**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**

Where they came from:

- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: requester='Elowen Marr', role='customer', channel='secure_chat', verified=False]
- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: amount='42.80', counterparty='Northmere Home Supplies']
- event 3 (H&V incoming-entry journal): I am checking the linked incoming entries on Elowen Marr's account for a £42.80 refund matching the Northmere Home Supplies transfer. I will not treat a similar-looking entry as a match. [facts: incoming_asked=True]
- event 4 (H&V incoming-entry journal): The incoming-entry record shows a £42.80 credit identified as the refund for the Northmere Home Supplies transfer in the account history. [facts: incoming_found=True, incoming_amount='42.80']
- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

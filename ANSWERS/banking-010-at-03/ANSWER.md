# Case banking-010-at-03: Refund visible in the account

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Marr, an unverified customer on secure chat, asked the desk to check whether an incoming £42.80 entry matches the transfer Northmere Home Supplies said might be returned. The desk asked the incoming-payments system, but its answer is not yet in the case, so the case closed in a waiting state with no actions taken. A second request to the incoming system was refused because the case was already waiting, and nothing has been confirmed or sent to the customer, so the desk still has to act once that answer arrives.

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

Attachments: none.

Case reference: id banking-010-at-03, track Banking & Financial Services, case 010, point 3, actor_next bank.

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

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- amount: **42.80**
- counterparty: **Northmere Home Supplies**
- incoming_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **incoming**

Where they came from:

- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: requester='Elowen Marr', role='customer', channel='secure_chat', verified=False]
- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: amount='42.80', counterparty='Northmere Home Supplies']
- event 3 (H&V incoming-entry journal): I am checking the linked incoming entries on Elowen Marr's account for a £42.80 refund matching the Northmere Home Supplies transfer. I will not treat a similar-looking entry as a match. [facts: incoming_asked=True]
- event 2 (Elowen Marr): I am escalating this because Northmere Home Supplies said the £42.80 might be returned. Please check whether the incoming entry is for that specific transfer; I do not want it confused with another payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=incoming); next_system = payment is false (next_system=incoming); next_system absent is false (next_system=incoming); incoming-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=incoming); incoming_asked absent is false (incoming_asked=True); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=incoming); next_system = recurring is false (next_system=incoming); next_system absent is false (next_system=incoming); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=incoming); next_system = card is false (next_system=incoming); next_system absent is false (next_system=incoming); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=incoming); next_system = access is false (next_system=incoming); next_system absent is false (next_system=incoming); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=incoming); next_system = business is false (next_system=incoming); next_system absent is false (next_system=incoming); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=incoming); next_system = documents is false (next_system=incoming); next_system absent is false (next_system=incoming)

## Final result

wait (WAITING)

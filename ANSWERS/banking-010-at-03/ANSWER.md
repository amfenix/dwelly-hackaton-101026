# Case banking-010-at-03: Refund visible in the account

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Marr, writing over secure chat and not yet verified, asked whether the incoming £42.80 entry relates to her transfer to Northmere Home Supplies, which had said it might be returned. The desk classed it as an incoming-payment question and checked the incoming entries, but no result had come back, so the case closed as waiting with no actions taken. The agent's later attempts to ask the incoming system again, reply to her, and escalate with a note were all refused because the case was already in the waiting state, so nothing has been sent to her and the incoming result, along with identity verification, is still outstanding.

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
- request_type: **question**
- next_system: **incoming**
- credentials_requested: **False**
- joint_holder_change: **False**

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

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=incoming); next_system = payment is false (next_system=incoming); next_system absent is false (next_system=incoming); incoming-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=incoming); incoming_asked absent is false (incoming_asked=True); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=incoming); next_system = recurring is false (next_system=incoming); next_system absent is false (next_system=incoming); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=incoming); next_system = card is false (next_system=incoming); next_system absent is false (next_system=incoming); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=incoming); next_system = access is false (next_system=incoming); next_system absent is false (next_system=incoming); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=incoming); next_system = business is false (next_system=incoming); next_system absent is false (next_system=incoming); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=incoming); next_system = documents is false (next_system=incoming); next_system absent is false (next_system=incoming); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=incoming); next_system = tariff is false (next_system=incoming); next_system absent is false (next_system=incoming)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=incoming); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=incoming); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=incoming); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=incoming); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=incoming); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=incoming_payment); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=incoming); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=incoming); tariff_status present is false (tariff_status=not known)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

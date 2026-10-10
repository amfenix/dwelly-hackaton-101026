# Case 022: Available balance after a card purchase

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Rois Fenwick asked for a £600 amount to be returned to their available balance today, saying they need it for groceries. The desk could not act on it: its attempts to query the card system and to submit a request were both refused because the requester's verified status was not established. It escalated the case to a person, with a note to check whether a lingering £600 authorisation is linked to the £520 hotel purchase and to release it if eligible. Nothing was released or promised, and the case is closed as escalated, so card operations must decide whether to release it.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Rois Fenwick
- Created: 2026-11-10 09:00+00:00
- Operator: Brackenfold Bank case desk

The request:

> Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel.

What happened up to now:

1. 2026-11-10T09:00:00Z · Internal card view — Brackenfold Bank card ledger → Brackenfold Bank case desk

> Card and balance entries retrieved at 09:00. The account holder is Rois Fenwick; current contact authentication is recorded as passed.
> 
> Attachments: [card-entries.csv](attachments/card-entries.csv)

2. 2026-11-10T09:10:00Z · Authenticated customer chat — Rois Fenwick → Brackenfold Bank case desk

> The hotel took £600 and £520, so that is £1,120. My available balance is only £380. I thought the stay cost £520.

3. 2026-11-10T09:15:00Z · Merchant email, bank support copied — Alderclock Hotel → Rois Fenwick

> Your final stay receipt is attached. The stay ended this morning; the final card amount is £520.
> 
> Attachments: [hotel-receipt.pdf](attachments/hotel-receipt.pdf)

4. 2026-11-10T09:20:00Z · Internal procedure view — Brackenfold Bank card operations → Brackenfold Bank case desk

> Card servicing procedure: card operations can investigate a lingering linked authorisation following a completed purchase and release an eligible stale hold after checking linkage and current network state. Case desk may request investigation; it cannot release a hold itself. Release timing depends on those checks.

5. 2026-11-10T09:25:00Z · Customer chat — Rois Fenwick → Brackenfold Bank case desk

> Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel.

Attachments: `card-entries.csv`, `hotel-receipt.pdf`.

Case reference: id 022, track Banking & Financial Services, case 022, point 5.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- requester: **Rois Fenwick**
- role: **customer**
- subject: **card_payment**
- amount: **600.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**
- reason: **AGENT_ESCALATED**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 5 (Rois Fenwick): Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel. [facts: requester='Rois Fenwick', role='customer']
- event 2 (Rois Fenwick): The hotel took £600 and £520, so that is £1,120. My available balance is only £380. I thought the stay cost £520. [facts: amount='600.00']
- event 5 (Rois Fenwick): Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: next_system absent is false (next_system=card); request_type not in [register, change, authority, instruction] is false (request_type=instruction); access-ask: args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card)
- `submit_request`: register: request_type = register is false (request_type=instruction); register-what-fits-no-type: request_type = other is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=card); verified is not known (verified=not known); incoming-instruction: next_system = incoming is false (next_system=card); verified is not known (verified=not known); recurring-instruction: next_system = recurring is false (next_system=card); verified is not known (verified=not known); card-instruction: verified is not known (verified=not known); access-instruction: next_system = access is false (next_system=card); verified is not known (verified=not known); business-instruction: next_system = business is false (next_system=card); verified is not known (verified=not known); documents-instruction: next_system = documents is false (next_system=card); verified is not known (verified=not known)

## Final result

escalate (ESCALATED)

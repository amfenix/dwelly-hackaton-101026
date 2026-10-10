# Case 019: Duplicate payment to a cleaner

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer asked the desk to recall a £651 payment to an end-of-tenancy cleaner, which their letting agent had also paid from their rent, so they could get the money back faster. The desk classed it as a transfer instruction, routed it to the payment system and asked that system about the £651 transfer, and the case closed in that asked state. The payment system's answer is not in the record, no recall was submitted and nothing has changed on the payment, so what happens next is not recorded.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Created: 2026-09-23 (day precision)
- Bank: Harrow & Vale Bank plc
- Channel: In-app chat (personal banking)

The request:

> I paid an end-of-tenancy cleaner £651 on 12 August and it turns out my letting agent paid the same invoice from my rent. Co-Clean have agreed to refund one of them but it's been a week. Can you recall the payment from your side so I get it back faster?

What happened up to now:

1. 2026-09-23T00:00:00Z · Internal account view — Harrow & Vale Bank plc (case record) → Servicing agent (Harrow & Vale Bank plc)

> Customer: **Linda Ferris** — personal current account (landlord; her property at 53 Winchester Road is managed by Oakfield PM).
> | Date | Event |
> |---|---|
> | 12 Aug | Debit −£651.00, Faster Payment to CO-CLEAN SERVICES LTD, ref "INV 4471 53 WINCHESTER", new payee (CoP match at the time) |
> 
> Customer states the managing agency also paid Co-Clean's invoice 4471 from her rental funds on 15 Aug, so the contractor was paid twice. She spoke to Co-Clean on 17 Sep; they agreed to refund £651 "on the next payment run".

2. 2026-09-23T00:00:00Z · In-app chat (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> I paid an end-of-tenancy cleaner £651 on 12 August and it turns out my letting agent paid the same invoice from my rent. Co-Clean have agreed to refund one of them but it's been a week. Can you recall the payment from your side so I get it back faster?

3. 2026-09-23T00:00:00Z · In-app chat (personal banking) — Servicing agent (Harrow & Vale Bank plc) → Customer / caller

> Let me look at the payment and explain what a recall would and wouldn't do here.

4. 2026-09-23T00:00:00Z · In-app chat (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> It was a duplicate payment, isn't that exactly what recalls are for?

Attachments: `agency_statement_extract.txt`, `coclean_refund_agreement.eml`, `payment_confirmation_2026-08-12.pdf`.

Case reference: id 019, track Banking & Financial Services, case 019, point 4.

## Actions taken

- `ask_system` (system: payment, about: transfer, amount: 651.00), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `payment-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = payment → true (args.system=payment)
  - next_system = payment → true (next_system=payment)
  - next_system absent → false (next_system=payment)
  - payment_asked absent → true (payment_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Customer**
- role: **customer**
- subject: **transfer**
- amount: **651.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **payment**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 4 (Customer): It was a duplicate payment, isn't that exactly what recalls are for? [facts: requester='Customer', role='customer']
- event 2 (Customer): I paid an end-of-tenancy cleaner £651 on 12 August and it turns out my letting agent paid the same invoice from my rent. Co-Clean have agreed to refund one of them but it's been a week. Can you recall the payment from your side so I get it back faster? [facts: amount='651.00']
- event 4 (Customer): It was a duplicate payment, isn't that exactly what recalls are for? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

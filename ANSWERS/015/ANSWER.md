# Case 015: Unexpected first rent collection

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer said they never agreed to a £4,980 direct debit, whatever the notice said. The desk classed this as a direct debit instruction and asked the recurring payments system about the £4,980.00 debit. That system's reply came back empty, so nothing has been confirmed about the mandate or the payment, and nothing was cancelled or refunded. The case closed at that step, so the dispute itself is still unresolved and left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Created: 2026-09-14 (day precision)
- Bank: Harrow & Vale Bank plc
- Channel: Phone (personal banking)

The request:

> The letting agency has just taken nearly five grand out of my account by direct debit! I paid all the move-in money by bank transfer two weeks ago. My rent is £795. I'm massively overdrawn now. I want it all back today under the guarantee and I want that direct debit cancelled so they can never do this again.

What happened up to now:

1. 2026-09-14T00:00:00Z · Internal account view — Harrow & Vale Bank plc (case record) → Servicing agent (Harrow & Vale Bank plc)

> Customer: **Tunde Okoye** — personal current account.
> | Date | Event |
> |---|---|
> | 28 Aug | Faster Payment −£4,980.00 to HARROW & VALE RE LIME PROPERTY CA, ref "MOVE IN 14 GROVE" (advance tenancy payment; bank record does not show how the agency allocated it) |
> | 2 Sep | DD mandate H&V COLLECT / LIME PROPERTY created via originator invite |
> | 9 Sep | Advance notice (originator copy): "£4,980.00 will be collected on 14 September, then £795.00 monthly" |
> | 14 Sep | DD collection −£4,980.00 — paid; account now £3,100 overdrawn (arranged limit £1,000; unarranged portion incurs daily fee) |
> 
> Monthly rent per the customer: £795. The customer says he did not read the advance notice email.

2. 2026-09-14T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> [ID&V passed] The letting agency has just taken nearly five grand out of my account by direct debit! I paid all the move-in money by bank transfer two weeks ago. My rent is £795. I'm massively overdrawn now. I want it all back today under the guarantee and I want that direct debit cancelled so they can never do this again.

3. 2026-09-14T00:00:00Z · Phone (personal banking) — Servicing agent (Harrow & Vale Bank plc) → Customer / caller

> I'm sorry — that's a large amount to have taken unexpectedly. Let me look at the mandate and the notice.

4. 2026-09-14T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> I don't care what the notice said, I never agreed to £4,980 by direct debit.

Attachments: `dd_advance_notice_2026-09-09.eml`, `payment_confirmation_2026-08-28.pdf`, `statement_extract.csv`.

Case reference: id 015, track Banking & Financial Services, case 015, point 4.

## Actions taken

- `ask_system` (system: recurring, about: direct_debit, amount: 4980.00), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `recurring-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = recurring → true (args.system=recurring)
  - next_system = recurring → true (next_system=recurring)
  - next_system absent → false (next_system=recurring)
  - recurring_asked absent → true (recurring_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Customer**
- role: **customer**
- subject: **direct_debit**
- amount: **4980.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 4 (Customer): I don't care what the notice said, I never agreed to £4,980 by direct debit. [facts: requester='Customer', role='customer']
- event 4 (Customer): I don't care what the notice said, I never agreed to £4,980 by direct debit. [facts: amount='4980.00']
- event 4 (Customer): I don't care what the notice said, I never agreed to £4,980 by direct debit. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case 005: Direct Debit after move-out

**Decision: ask_system**  (final state `ASKED`)

## Summary

The customer, whose identity checks had passed, asked for the £875 direct debit taken in August and a second one due Monday to be refunded or stopped, and for the overdraft fee to be returned. The desk classed it as a direct debit instruction and put a question to the recurring payments system about the £875 debit. The record shows no answer from that system, and no refund, stop or fee decision was made. Everything the customer asked for is still with a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Created: 2026-09-25 (day precision)
- Bank: Harrow & Vale Bank plc
- Channel: Phone (personal banking)
- Contact start: 11:30 local UK time (individual message times not recorded)

The request:

> I moved out of my flat at the end of August. The agency took £875 on the 23rd, which has put me overdrawn, and I've just seen there's another one for £2,525 going out on Monday! I rang the agency and they said it's "already been submitted, they can't cancel it their side" and I should call you. I've got £600 in the account. What is this?

What happened up to now:

1. 2026-09-25T00:00:00Z · Internal account view — Harrow & Vale Bank plc (case record) → Servicing agent (Harrow & Vale Bank plc)

> Customer: **Gabriela Petrova** — personal current account, no arranged overdraft.
> Direct Debit mandate: H&V COLLECT / OAKFIELD PM, active since Feb 2025, monthly.
> | Date | Amount | Status |
> |---|---|---|
> | 24 Aug | −£875.00 | Collected |
> | 23 Sep | −£875.00 | Collected — account went £412 overdrawn; £6.50 unarranged overdraft fee applied 24 Sep |
> | **28 Sep (Mon)** | **−£2,525.00** | **Scheduled — collection instruction received from originator 24 Sep** |
> 
> On 25 Sep a £1,019.40 transfer from the customer's savings posted; available balance is now £600.00.
> 
> The customer states her tenancy at 78 Coombe Road ended on **31 Aug 2026**. The bank cannot see whether advance notices were sent for the Sep collections.

2. 2026-09-25T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> [ID&V passed] I moved out of my flat at the end of August. The agency took £875 on the 23rd, which has put me overdrawn, and I've just seen there's another one for £2,525 going out on Monday! I rang the agency and they said it's "already been submitted, they can't cancel it their side" and I should call you. I've got £600 in the account. What is this?

3. 2026-09-25T00:00:00Z · Phone (personal banking) — Servicing agent (Harrow & Vale Bank plc) → Customer / caller

> I'm sorry, that sounds really stressful. Let me look at the mandate.

4. 2026-09-25T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> I want all of it refunded — the August one, the September one, and Monday's stopped. And I want the overdraft fee back, it's not my fault.

Attachments: `agency_move_out_confirmation.eml`, `incoming_dd_instruction.json`, `statement_extract.csv`.

Case reference: id 005, track Banking & Financial Services, case 005, point 4.

## Actions taken

- `ask_system` (system: recurring, about: direct_debit, amount: 875.00), by rule `do-ask`

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
- amount: **875.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **recurring**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 4 (Customer): I want all of it refunded — the August one, the September one, and Monday's stopped. And I want the overdraft fee back, it's not my fault. [facts: requester='Customer', role='customer']
- event 2 (Customer): [ID&V passed] I moved out of my flat at the end of August. The agency took £875 on the 23rd, which has put me overdrawn, and I've just seen there's another one for £2,525 going out on Monday! I rang the agency and they said it's "already been submitted, they can't cancel it their side" and I should call you. I've got £600 in the account. What is this? [facts: amount='875.00']
- event 4 (Customer): I want all of it refunded — the August one, the September one, and Monday's stopped. And I want the overdraft fee back, it's not my fault. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

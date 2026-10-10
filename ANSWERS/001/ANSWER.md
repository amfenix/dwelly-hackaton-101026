# Case 001: Incoming payment under review

**Decision: ask_system**  (final state `ASKED`)

## Summary

A customer wrote that £750 was held in their account and they couldn't pay rent due tomorrow, and asked for the money to be released. The desk identified it as a question about an incoming payment and asked the incoming-payments system about the £750 hold. It did not release the hold, and the system's answer is not yet in the case, so the reason for the hold and any next step are still open for a person to follow up.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Created: 2026-09-24 (day precision)
- Bank: Harrow & Vale Bank plc
- Channel: Phone (personal banking)
- Contact start: 09:20 local UK time (individual message times not recorded)

The request:

> I've got no access to my money. It says £750 is held and I can't pay my rent tomorrow. What's going on?

What happened up to now:

1. 2026-09-24T00:00:00Z · Internal account view — Harrow & Vale Bank plc (case record) → Servicing agent (Harrow & Vale Bank plc)

> Customer: **Marcus Bell** — personal current account, 6 years with the bank, no previous fraud markers.
> | Date | Event |
> |---|---|
> | 21 Sep 14:10 | Credit +£2,600.00, Faster Payment from "L FARRELL" (Meridian Bank), ref "VAN" |
> | 21 Sep 16:40 | Debit −£1,850.00 to "BARCLAYCARD" (his own card, payee on file since 2022) |
> | 23 Sep 17:55 | **Inbound funds-recovery request** from Meridian: their customer reports the £2,600 as an authorised push payment scam ("vehicle not delivered"). Bank policy: place a hold on the disputed amount still available, respond to the sending bank within 2 working days |
> | 23 Sep 17:56 | Hold applied: £750.00 (all available funds); account balance £750.00, hold £750.00 |
> 
> Customer's contact history: none in the last 12 months. No other inbound payments from unknown parties in the last 90 days.

2. 2026-09-24T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> [ID&V passed] I've got no access to my money. It says £750 is held and I can't pay my rent tomorrow. What's going on?

3. 2026-09-24T00:00:00Z · Phone (personal banking) — Servicing agent (Harrow & Vale Bank plc) → Customer / caller

> I can see a hold was placed yesterday evening. I need to ask you about a payment you received on the 21st — £2,600 from an L Farrell.

4. 2026-09-24T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> That's the van. I sold my old Transit on a marketplace site, she came and picked it up Monday, paid me by transfer while she was standing in my drive. I've got the messages, the listing, the V5 handover — all of it. I used most of it to pay off my credit card. Why is that your business?

5. 2026-09-24T00:00:00Z · Phone (personal banking) — Servicing agent (Harrow & Vale Bank plc) → Customer / caller

> Thank you — that context matters. Let me explain what has happened and what I need from you.

6. 2026-09-24T00:00:00Z · Phone (personal banking) — Customer → Servicing agent (Harrow & Vale Bank plc)

> You need to release my money is what you need to do. My rent's £900 and it's due tomorrow.

Attachments: `account_hold_notice.txt`, `customer_evidence_listing.txt`, `customer_evidence_messages.txt`, `funds_recovery_request_MERIDIAN.txt`.

Case reference: id 001, track Banking & Financial Services, case 001, point 6.

## Actions taken

- `ask_system` (system: incoming, about: incoming_payment, amount: 750.00), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `incoming-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = incoming → true (args.system=incoming)
  - next_system = incoming → true (next_system=incoming)
  - next_system absent → false (next_system=incoming)
  - incoming_asked absent → true (incoming_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Customer**
- role: **customer**
- subject: **incoming_payment**
- amount: **750.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 6 (Customer): You need to release my money is what you need to do. My rent's £900 and it's due tomorrow. [facts: requester='Customer', role='customer']
- event 2 (Customer): [ID&V passed] I've got no access to my money. It says £750 is held and I can't pay my rent tomorrow. What's going on? [facts: amount='750.00']
- event 6 (Customer): You need to release my money is what you need to do. My rent's £900 and it's due tomorrow. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

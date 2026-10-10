# Case banking-S20-at-02: Bad exchange rate on a card payment in euros

**Decision: ask_system**  (final state `ASKED`)

## Summary

Felicity Marsh, who was not verified, asked through secure chat how a €500.00 card payment in Lyon came to be charged as £441.30, saying the rate looked much better online. The desk classed it as a question about a card payment and sent an inquiry to the card system about the £441.30 charge, and the case closed at that point. The card system's answer is not in the record, so no explanation of the rate or breakdown has been given, and that is still outstanding.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-20 09:00:00 UTC

The request:

> My €500.00 card payment in Lyon cost me £441.30. The rate I saw online that day was much better. How did you get that figure?

What happened up to now:

1. 2025-11-20T09:00:00Z · Secure portal — H&V secure portal → Felicity Marsh

> Card transaction: Librairie des Quais, Lyon — €500.00, debited £441.30, 7 November 2025, debit card ending 6671.

2. 2025-11-20T09:47:00Z · Secure chat — Felicity Marsh → H&V service agent

> I paid €500.00 by card in a bookshop in Lyon and you took £441.30. When I looked online that day the rate was much better than that. How did you arrive at £441.30? It seems far too much.

Attachments: none.

Case reference: id banking-S20-at-02, track banking, case S20, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card_payment, amount: 441.30), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `card-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = card → true (args.system=card)
  - next_system = card → true (next_system=card)
  - next_system absent → false (next_system=card)
  - card_asked absent → true (card_asked=not known)
  - request_type not in [register, change, authority, instruction] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Felicity Marsh**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card_payment**
- amount: **441.30**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **card**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Felicity Marsh): I paid €500.00 by card in a bookshop in Lyon and you took £441.30. When I looked online that day the rate was much better than that. How did you arrive at £441.30? It seems far too much. [facts: requester='Felicity Marsh', role='customer', channel='secure_chat', verified=False]
- event 2 (Felicity Marsh): I paid €500.00 by card in a bookshop in Lyon and you took £441.30. When I looked online that day the rate was much better than that. How did you arrive at £441.30? It seems far too much. [facts: amount='441.30']
- event 2 (Felicity Marsh): I paid €500.00 by card in a bookshop in Lyon and you took £441.30. When I looked online that day the rate was much better than that. How did you arrive at £441.30? It seems far too much. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

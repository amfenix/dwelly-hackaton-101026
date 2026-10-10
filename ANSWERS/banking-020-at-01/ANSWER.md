# Case banking-020-at-01: What to Check Before Closing an Account

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elena Wren, an unverified customer writing from outside the portal, asked what active instructions are linked to her account and what to consider before closing it. The desk classed this as a question about a standing order and asked the recurring-payments system about it, and the case closed in the ASKED state. No answer has come back from that system, and an attempted reply was refused, so Elena has received nothing yet and a person would need to pick up the case once the recurring-payments response is in.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-26 09:00:00 UTC

The request:

> I’m planning to close my H&V account after I move my regular payments. Please tell me what active instructions are linked to it and what I should consider before closing it.

What happened up to now:

1. 2025-08-26T09:00:00Z · External message — Elena Wren → Harrow & Vale Bank plc

> I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing?

Attachments: none.

Case reference: id banking-020-at-01, track Banking & Financial Services, case 020, point 1, actor_next other.

## Actions taken

- `ask_system` (system: recurring, about: standing_order), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Elena Wren**
- role: **customer**
- channel: **external_message**
- verified: **False**
- subject: **standing_order**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 1 (Elena Wren): I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing? [facts: requester='Elena Wren', role='customer', channel='external_message', verified=False]
- event 1 (Elena Wren): I’m planning to close my account once I’ve moved my regular payments. Could you tell me what active instructions are linked to it and what I should consider before closing? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=recurring); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=recurring); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=recurring); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=recurring); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=recurring); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); next_system = documents is false (next_system=recurring); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=recurring); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

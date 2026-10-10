# Case banking-047-at-01: Company Payment Limit

**Decision: ask_system**  (final state `ASKED`)

## Summary

Maeve Calder, a verified customer using the business portal, asked for the current outgoing-payment limit on her company profile before arranging a planned supplier payout she has not yet submitted. The desk classified this as a record-fact request and asked the business system about the limit; that request has been sent and the case closed in the asked state. The record shows no answer yet, so the limit has not been given to her, and the payout was not touched.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-19 09:00:00 UTC

The request:

> Maeve wants to know the current outgoing-payment limit on her company profile before arranging a substantial supplier payment.

What happened up to now:

1. 2025-10-19T09:00:00Z · Business portal — Maeve Calder → H&V Business Support

> I can see a planned supplier payout in the portal, but I have not submitted it. I need to know the current outgoing-payment limit for our company profile before I arrange it.

Attachments: none.

Case reference: id banking-047-at-01, track Banking & Financial Services, case 047, point 1, actor_next other.

## Actions taken

- `ask_system` (system: business, about: limit), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `business-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = business → true (args.system=business)
  - next_system = business → true (next_system=business)
  - next_system absent → false (next_system=business)
  - business_asked absent → true (business_asked=not known)
  - request_type not in [register, change, instruction, authority] → true (request_type=record_fact)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Maeve Calder**
- role: **customer**
- channel: **business_portal**
- verified: **True**
- subject: **limit**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **record_fact**
- next_system: **business**

Where they came from:

- event 1 (Maeve Calder): I can see a planned supplier payout in the portal, but I have not submitted it. I need to know the current outgoing-payment limit for our company profile before I arrange it. [facts: requester='Maeve Calder', role='customer', channel='business_portal', verified=True]
- event 1 (Maeve Calder): I can see a planned supplier payout in the portal, but I have not submitted it. I need to know the current outgoing-payment limit for our company profile before I arrange it. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

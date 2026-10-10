# Case banking-022-at-01: Lost card blocked

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, verified on a call, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk did not block it; it sent a query to the card system about the card and closed the case at that point. The block has not been submitted, so someone still needs to act on it once the card records come back.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-30 09:00:00 UTC

The request:

> I noticed my H&V debit card was missing after a visit to Alder Quay Market. Please block it immediately.

What happened up to now:

1. 2025-08-30T09:00:00Z · Verified call — Mara Ellison → H&V service agent

> After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note.

Attachments: none.

Case reference: id banking-022-at-01, track Banking & Financial Services, case 022, point 1, actor_next bank.

## Actions taken

- `ask_system` (system: card, about: card), by rule `do-ask`

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
  - request_type not in [register, change, authority] → true (request_type=instruction)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card**
- counterparty: **Alder Quay Market**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**

Where they came from:

- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: counterparty='Alder Quay Market']
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

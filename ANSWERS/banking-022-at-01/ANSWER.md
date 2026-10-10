# Case banking-022-at-01: Lost card blocked

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellison, verified on a call, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk recorded this as a card instruction and registered a request with the card team, and the case closed in the requested state. The desk did not block the card itself, and the record shows no confirmation that the block has happened, so that remains with the card team.

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

- `register_request` (team: card, about: card), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `card-instruction` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_asked absent → true (card_asked=not known)
  - verified → true (verified=True)
  - request_type = instruction → true (request_type=instruction)
  - request_type = change → false (request_type=instruction)
  - confirmation = given → false (confirmation=none)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

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

submit_request (REQUESTED)

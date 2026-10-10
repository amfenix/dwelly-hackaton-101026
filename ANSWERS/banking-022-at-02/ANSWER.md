# Case banking-022-at-02: Lost card blocked

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Mara Ellison, a verified caller, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk classified this as a card instruction and registered a request with the card team, which the system accepted. The record shows no confirmation that the block itself has taken effect, so that remains with the card team.

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

2. 2025-08-30T09:47:00Z · Internal note — H&V service agent → H&V card team

> I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call.

Attachments: none.

Case reference: id banking-022-at-02, track Banking & Financial Services, case 022, point 2, actor_next bank.

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
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**

Where they came from:

- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: counterparty='Alder Quay Market']
- event 2 (H&V service agent): I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call. [facts: registration_asked=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

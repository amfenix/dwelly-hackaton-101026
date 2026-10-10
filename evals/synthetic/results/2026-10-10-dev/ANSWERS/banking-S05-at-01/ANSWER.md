# Case banking-S05-at-01: Block my card, unblock it tomorrow, and refund two purchases

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Sofia Lindqvist, a verified customer on a call, said she had lost her debit card and asked for it to be blocked now, for an automatic unblock tomorrow, and for refunds of two purchases (£23.10 and £64.00). The desk classified it as a card instruction and registered a request with the card team, and the case closed as requested. The record shows nothing registered for the automatic unblock or the refunds, so those are left for a person or a separate request.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-05 09:00:00 UTC

The request:

> I’ve lost my debit card. Please block it now, unblock it automatically tomorrow if I find it, and refund the two purchases I don’t recognise — £23.10 and £64.00.

What happened up to now:

1. 2025-11-05T09:00:00Z · Verified call — Sofia Lindqvist → H&V service agent

> After H&V completed its identification checks, I reported that I’ve lost my debit card, probably on the bus home. I asked for it to be blocked right now. I also asked if it could unblock automatically tomorrow in case I find it in a coat pocket, and for a refund of two purchases I don’t recognise from last night: £23.10 and £64.00. No security details were recorded in the call note.

Attachments: none.

Case reference: id banking-S05-at-01, track banking, case S05, point 1, actor_next bank.

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
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Sofia Lindqvist**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card**
- amount: **23.10**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**

Where they came from:

- event 1 (Sofia Lindqvist): After H&V completed its identification checks, I reported that I’ve lost my debit card, probably on the bus home. I asked for it to be blocked right now. I also asked if it could unblock automatically tomorrow in case I find it in a coat pocket, and for a refund of two purchases I don’t recognise from last night: £23.10 and £64.00. No security details were recorded in the call note. [facts: requester='Sofia Lindqvist', role='customer', channel='verified_call', verified=True]
- event 1 (Sofia Lindqvist): After H&V completed its identification checks, I reported that I’ve lost my debit card, probably on the bus home. I asked for it to be blocked right now. I also asked if it could unblock automatically tomorrow in case I find it in a coat pocket, and for a refund of two purchases I don’t recognise from last night: £23.10 and £64.00. No security details were recorded in the call note. [facts: amount='23.10']
- event 1 (Sofia Lindqvist): After H&V completed its identification checks, I reported that I’ve lost my debit card, probably on the bus home. I asked for it to be blocked right now. I also asked if it could unblock automatically tomorrow in case I find it in a coat pocket, and for a refund of two purchases I don’t recognise from last night: £23.10 and £64.00. No security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: next_system absent is false (next_system=card); request_type not in [register, change, authority, instruction] is false (request_type=instruction); access-ask: args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card)

## Final result

submit_request (REQUESTED)

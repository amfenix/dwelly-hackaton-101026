# Case banking-S19-at-02: Formal complaint — I’m going to the Ombudsman

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Desmond Achterberg, an unverified customer on secure chat, said he had been charged £5 three months running without explanation and asked for a formal complaint to be logged today, or he would go to the Financial Ombudsman. The desk registered a request with the tariff team about the fee, and the case closed as requested. The record shows no change to the account and no refund. It also shows no reason found for the fee, and the request was classed as "other" with low confidence (0.53), so the record does not confirm it was logged as a formal complaint.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-19 09:00:00 UTC

The request:

> I’ve been charged £5 a month for three months and nobody told me why. I want a formal complaint logged, and if you don’t sort it I’m going to the Financial Ombudsman.

What happened up to now:

1. 2025-11-19T09:00:00Z · Secure portal — H&V secure portal → Desmond Achterberg

> Current account ending 9043: monthly account fee £5.00 on 1 August, 1 September and 1 October 2025.

2. 2025-11-19T09:47:00Z · Secure chat — Desmond Achterberg → H&V service agent

> Three months running you’ve taken £5 off me and nobody ever told me why. That’s £15 for nothing. I don’t want another explanation in a chat window — I want a formal complaint logged today. And I’m warning you: if this isn’t put right I’m going straight to the Financial Ombudsman.

Attachments: none.

Case reference: id banking-S19-at-02, track banking, case S19, point 2, actor_next bank.

## Actions taken

- `register_request` (team: tariff, about: fee), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `register-what-fits-no-type` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = other → true (request_type=other)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Desmond Achterberg**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **fee**
- amount: **5.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **other**
- next_system: **tariff**

Where they came from:

- event 2 (Desmond Achterberg): Three months running you’ve taken £5 off me and nobody ever told me why. That’s £15 for nothing. I don’t want another explanation in a chat window — I want a formal complaint logged today. And I’m warning you: if this isn’t put right I’m going straight to the Financial Ombudsman. [facts: requester='Desmond Achterberg', role='customer', channel='secure_chat', verified=False]
- event 2 (Desmond Achterberg): Three months running you’ve taken £5 off me and nobody ever told me why. That’s £15 for nothing. I don’t want another explanation in a chat window — I want a formal complaint logged today. And I’m warning you: if this isn’t put right I’m going straight to the Financial Ombudsman. [facts: amount='5.00']
- event 2 (Desmond Achterberg): Three months running you’ve taken £5 off me and nobody ever told me why. That’s £15 for nothing. I don’t want another explanation in a chat window — I want a formal complaint logged today. And I’m warning you: if this isn’t put right I’m going straight to the Financial Ombudsman. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

# Case banking-022-at-02: Lost card blocked

**Decision: wait**  (final state `WAITING`)

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

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `registration-waits` — The team was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - registration_asked → true (registration_asked=True)
  - registered absent → true (registered=not known)

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

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=card); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card)
- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)
- `clarify`: clarify-transaction: state = TRIAGED is false (state=WAITING); args.need = which_transaction is false (args.need=which_card); counterparty absent is false (counterparty=Alder Quay Market); clarify-card: state = TRIAGED is false (state=WAITING); counterparty absent is false (counterparty=Alder Quay Market); clarify-instruction: state = TRIAGED is false (state=WAITING); args.need = which_instruction is false (args.need=which_card); counterparty absent is false (counterparty=Alder Quay Market); clarify-details: state = TRIAGED is false (state=WAITING); args.need = more_details is false (args.need=which_card); counterparty absent is false (counterparty=Alder Quay Market)

## Final result

wait (WAITING)

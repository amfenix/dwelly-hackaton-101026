# Case banking-022-at-03: Lost card blocked

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk found that the card system had already been asked, and that a case had been opened and escalated, but the card system's answer has not come in, so the case closed in a waiting state with no action taken. The agent's attempt to submit the request was refused because the case was no longer in the triaged state, so the card has not been blocked by this desk, and the case stays on hold until the card system replies.

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

3. 2025-08-30T10:34:00Z · Secure portal — H&V service agent → H&V card system

> I have submitted the verified instruction to block Mara Ellison's missing card under case HV-022.

Attachments: none.

Case reference: id banking-022-at-03, track Banking & Financial Services, case 022, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `card-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = card → true (next_system=card)
  - card_asked → true (card_asked=True)
  - card_status absent → true (card_status=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **card**
- counterparty: **Alder Quay Market**
- card_asked: **True**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**

Where they came from:

- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: counterparty='Alder Quay Market']
- event 3 (H&V card system): I have submitted the verified instruction to block Mara Ellison's missing card under case HV-022. [facts: card_asked=True]
- event 2 (H&V service agent): I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call. [facts: registration_asked=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: state = TRIAGED is false (state=WAITING); request_type = register is false (request_type=instruction); registration_asked absent is false (registration_asked=True); payment-instruction: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); incoming-instruction: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); recurring-instruction: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); card-instruction: state = TRIAGED is false (state=WAITING); card_asked absent is false (card_asked=True); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); access-instruction: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); business-instruction: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none); documents-instruction: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=card); request_type = change is false (request_type=instruction); confirmation = given is false (confirmation=none)

## Final result

wait (WAITING)

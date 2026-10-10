# Case banking-022-at-04: Lost card blocked

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, verified on a call, reported her debit card missing after a visit to Alder Quay Market and asked for it to be blocked immediately. The desk found the card already showing as BLOCKED under case HV-022, and the registration request was sent to the team, but its answer isn't in yet, so the case closed as "wait" in WAITING with no actions taken. The desk refused the agent's attempt to send a reply because replies are only accepted once the case is triaged, so no confirmation has gone to the customer and the case is left for a person.

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

4. 2025-08-30T11:21:00Z · Secure portal — H&V card system → H&V service agent

> Card journal status: BLOCKED. The card is marked blocked.

Attachments: none.

Case reference: id banking-022-at-04, track Banking & Financial Services, case 022, point 4, actor_next bank.

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
- card_asked: **True**
- card_status: **BLOCKED**
- registration_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **instruction**
- next_system: **card**

Where they came from:

- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: counterparty='Alder Quay Market']
- event 3 (H&V card system): I have submitted the verified instruction to block Mara Ellison's missing card under case HV-022. [facts: card_asked=True]
- event 4 (H&V card system): Card journal status: BLOCKED. The card is marked blocked. [facts: card_status='BLOCKED']
- event 2 (H&V service agent): I have opened case HV-022 and escalated Mara Ellison's verified request for an immediate card block. Her instruction was confirmed during the checked call. [facts: registration_asked=True]
- event 1 (Mara Ellison): After H&V completed its identification checks, I reported that my debit card was missing after a visit to Alder Quay Market. I asked you to block it immediately; no security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=card); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=card); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=card); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=card); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=card); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=card); document_ready present is false (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=card); tariff_status present is false (tariff_status=not known)

## Final result

wait (WAITING)

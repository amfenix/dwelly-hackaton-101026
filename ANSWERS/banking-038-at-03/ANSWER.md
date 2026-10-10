# Case banking-038-at-03: Account confirmation available in the secure portal

**Decision: wait**  (final state `WAITING`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-01 09:00:00 UTC

The request:

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

What happened up to now:

1. 2025-10-01T09:00:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

2. 2025-10-01T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else.

3. 2025-10-01T10:34:00Z · Internal note — H&V service agent → H&V document service

> I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only.

Attachments: none.

Case reference: id banking-038-at-03, track Banking & Financial Services, case 038, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `documents-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - documents_asked → true (documents_asked=True)
  - document_ready absent → true (document_ready=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V document service): I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only. [facts: documents_asked=True]
- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=documents); next_system = payment is false (next_system=documents); next_system absent is false (next_system=documents); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=documents); next_system = incoming is false (next_system=documents); next_system absent is false (next_system=documents); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=documents); next_system = recurring is false (next_system=documents); next_system absent is false (next_system=documents); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=documents); next_system = card is false (next_system=documents); next_system absent is false (next_system=documents); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=documents); next_system = access is false (next_system=documents); next_system absent is false (next_system=documents); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=documents); next_system = business is false (next_system=documents); next_system absent is false (next_system=documents); documents-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=documents); documents_asked absent is false (documents_asked=True)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); document_ready present is false (document_ready=not known)

## Final result

wait (WAITING)

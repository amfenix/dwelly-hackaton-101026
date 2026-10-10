# Case banking-031-at-03: June statement in the secure portal

**Decision: wait**  (final state `WAITING`)

## Summary

Elowen Marr, writing over secure chat, said she couldn't find her June statement in the portal and asked for it to be placed there, not emailed. The desk classified this as a statement request, noted that the documents system had already been asked to check the June 2025 period, and closed the case in a waiting state because that system's answer hasn't come back. A second documents request and a reply to her were both refused, since the check had already run and there is no document result yet. Elowen is not verified, and nothing was sent to her; the record names no person or next step, only that the documents result is still outstanding.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-17 09:00:00 UTC

The request:

> I own my H&V account and need my June 2025 statement, but I cannot find it in the secure portal. Please make the statement available there.

What happened up to now:

1. 2025-09-17T09:00:00Z · Secure portal — Elowen Marr → H&V

> I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there.

2. 2025-09-17T09:47:00Z · Secure chat — Elowen Marr → H&V agent

> I’m escalating this because I still can’t find my June statement in the portal. I need the statement itself made available there; I’m not asking for it by email.

3. 2025-09-17T10:34:00Z · Internal note — H&V agent → Statements service

> I’m asking you to check the June 2025 statement period for the account owner and place the available document in her secure portal. Case reference HV-031.

Attachments: none.

Case reference: id banking-031-at-03, track Banking & Financial Services, case 031, point 3, actor_next bank.

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

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **statement**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 2 (Elowen Marr): I’m escalating this because I still can’t find my June statement in the portal. I need the statement itself made available there; I’m not asking for it by email. [facts: requester='Elowen Marr', role='customer', channel='secure_chat', verified=False]
- event 3 (Statements service): I’m asking you to check the June 2025 statement period for the account owner and place the available document in her secure portal. Case reference HV-031. [facts: documents_asked=True]
- event 2 (Elowen Marr): I’m escalating this because I still can’t find my June statement in the portal. I need the statement itself made available there; I’m not asking for it by email. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=documents); next_system = payment is false (next_system=documents); next_system absent is false (next_system=documents); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=documents); next_system = incoming is false (next_system=documents); next_system absent is false (next_system=documents); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=documents); next_system = recurring is false (next_system=documents); next_system absent is false (next_system=documents); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=documents); next_system = card is false (next_system=documents); next_system absent is false (next_system=documents); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=documents); next_system = access is false (next_system=documents); next_system absent is false (next_system=documents); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=documents); next_system = business is false (next_system=documents); next_system absent is false (next_system=documents); documents-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=documents); documents_asked absent is false (documents_asked=True)
- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); document_ready present is false (document_ready=not known)

## Final result

wait (WAITING)

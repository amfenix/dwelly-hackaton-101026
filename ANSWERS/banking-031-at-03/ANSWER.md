# Case banking-031-at-03: June statement in the secure portal

**Decision: wait**  (final state `WAITING`)

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
- request_type: **question**
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

## Final result

wait (WAITING)

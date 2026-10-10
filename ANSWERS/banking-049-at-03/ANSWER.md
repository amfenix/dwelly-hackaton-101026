# Case banking-049-at-03: Acquiring Report Ready

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Venn, who is not verified and wrote via secure chat, said she is the authorised manager for North Quay Printworks and asked for the acquiring report for 1–7 July 2025 because it wasn't showing as available. The desk asked the documents system and closed the case in WAITING, since that system's answer on whether the report is ready had not come back. A second documents query and the agent's escalation note were both refused because the case was already in WAITING, so nothing was released or promised. Someone still needs to check whether the report exists and verify Mara's identity and authority.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-23 09:00:00 UTC

The request:

> I need the acquiring report for 1–7 July 2025 to review the card sales and adjustments for my shop.

What happened up to now:

1. 2025-10-23T09:00:00Z · Business portal — Mara Venn → H&V business portal

> I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments.

2. 2025-10-23T09:47:00Z · Secure chat — Mara Venn → H&V service agent

> I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request.

3. 2025-10-23T10:34:00Z · Internal note — H&V service agent → H&V acquiring service

> I checked the manager’s authority for this business. Please prepare and place the acquiring report for 1–7 July 2025 in the secure portal for the authorised user.

Attachments: none.

Case reference: id banking-049-at-03, track Banking & Financial Services, case 049, point 3, actor_next bank.

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

- requester: **Mara Venn**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- subject_date: **2025-07-07**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: requester='Mara Venn', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: subject_date='2025-07-07']
- event 3 (H&V acquiring service): I checked the manager’s authority for this business. Please prepare and place the acquiring report for 1–7 July 2025 in the secure portal for the authorised user. [facts: documents_asked=True]
- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=documents); next_system = payment is false (next_system=documents); next_system absent is false (next_system=documents); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=documents); next_system = incoming is false (next_system=documents); next_system absent is false (next_system=documents); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=documents); next_system = recurring is false (next_system=documents); next_system absent is false (next_system=documents); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=documents); next_system = card is false (next_system=documents); next_system absent is false (next_system=documents); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=documents); next_system = access is false (next_system=documents); next_system absent is false (next_system=documents); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=documents); next_system = business is false (next_system=documents); next_system absent is false (next_system=documents); documents-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=documents); documents_asked absent is false (documents_asked=True); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=documents); next_system = tariff is false (next_system=documents); next_system absent is false (next_system=documents)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

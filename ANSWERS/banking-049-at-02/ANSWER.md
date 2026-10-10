# Case banking-049-at-02: Acquiring Report Ready

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Venn, writing over secure chat and not verified, said she is the authorised manager for North Quay Printworks. She asked the desk to escalate a request for the acquiring report covering 1–7 July 2025, which wasn't showing as available. The desk treated it as a question about a document and asked the documents system about it, and the case closed at that step. The system's answer isn't in the record, so whether the report is available is still unknown, nothing was escalated or changed, and her authority was not verified.

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

Attachments: none.

Case reference: id banking-049-at-02, track Banking & Financial Services, case 049, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: documents, about: document), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `documents-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = documents → true (args.system=documents)
  - next_system = documents → true (next_system=documents)
  - next_system absent → false (next_system=documents)
  - documents_asked absent → true (documents_asked=not known)
  - document_ready = false → not known (document_ready=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Venn**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- subject_date: **2025-07-07**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: requester='Mara Venn', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: subject_date='2025-07-07']
- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

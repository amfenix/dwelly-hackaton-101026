# Case banking-049-at-01: Acquiring Report Ready

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Venn, a verified customer using the business portal, asked for the acquiring report for North Quay Printworks covering 1–7 July 2025, so she could review card sales and adjustments. The desk classified it as a question about a document and sent an inquiry to the documents system, which accepted it and closed the case as asked. The documents system has returned no report or file details, so whether the report exists is still unknown, and no reply to Mara Venn has been recorded.

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

Attachments: none.

Case reference: id banking-049-at-01, track Banking & Financial Services, case 049, point 1, actor_next other.

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
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Venn**
- role: **customer**
- channel: **business_portal**
- verified: **True**
- subject: **document**
- subject_date: **2025-07-07**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: requester='Mara Venn', role='customer', channel='business_portal', verified=True]
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: subject_date='2025-07-07']
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

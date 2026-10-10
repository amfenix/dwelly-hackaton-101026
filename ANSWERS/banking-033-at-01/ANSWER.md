# Case banking-033-at-01: Transactions export

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, a verified customer writing through the secure portal, asked for a CSV export of her transactions from 6 to 9 May 2025 and wanted to know how to tell whether the export had been created. The desk classed it as a question about a document and sent an inquiry to the documents system, and the case closed in the asked state. The record does not show whether the export exists, so that answer is still to come from the documents system.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-21 09:00:00 UTC

The request:

> I need a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. The export screen is unclear, and I want to know when the file is available in my secure portal.

What happened up to now:

1. 2025-09-21T09:00:00Z · Secure portal — Mara Ellison → H&V

> I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created.

Attachments: none.

Case reference: id banking-033-at-01, track Banking & Financial Services, case 033, point 1, actor_next other.

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

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **document**
- subject_date: **2025-05-09**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: subject_date='2025-05-09']
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

# Case banking-033-at-02: Transactions export

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison asked, over secure chat, for a CSV export of her transactions from 6 to 9 May 2025 and to be told when the file is available in her secure portal. The desk classified it as a document request and sent a query to the documents system, which returned nothing, so there is no confirmation that the export exists. Her identity is still marked unverified, and the record shows no further step, so whether the file is ready is still unanswered.

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

2. 2025-09-21T09:47:00Z · Secure chat — Mara Ellison → H&V agent

> I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal.

Attachments: none.

Case reference: id banking-033-at-02, track Banking & Financial Services, case 033, point 2, actor_next bank.

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
  - request_type not in [register, change, authority] → true (request_type=document)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- subject_date: **2025-05-09**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: subject_date='2025-05-09']
- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

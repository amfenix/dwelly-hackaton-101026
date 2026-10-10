# Case banking-033-at-03: Transactions export

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison asked, over secure chat, for a CSV export of her transactions from 6 to 9 May 2025 and for word when the file is available in her secure portal. The desk found that the documents system had already been asked to create the export but had not yet confirmed it, so it took no action and closed the case as waiting. What is left is the documents system's confirmation that the export exists; her identity is also recorded as unverified, so the desk did not say the file is ready or when it will appear.

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

3. 2025-09-21T10:34:00Z · Internal note — H&V agent → Data service

> I’ve confirmed the authenticated profile and the customer’s secure-portal request. Please create the permitted CSV export for the verified account holder’s secure portal, covering 6–9 May 2025 only; do not send the data to a third party.

Attachments: none.

Case reference: id banking-033-at-03, track Banking & Financial Services, case 033, point 3, actor_next bank.

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
- subject_date: **2025-05-09**
- documents_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: subject_date='2025-05-09']
- event 3 (Data service): I’ve confirmed the authenticated profile and the customer’s secure-portal request. Please create the permitted CSV export for the verified account holder’s secure portal, covering 6–9 May 2025 only; do not send the data to a third party. [facts: documents_asked=True]
- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

# Case banking-033-at-04: Transactions export

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, a customer on secure chat, asked to be told when her CSV export of transactions for 6–9 May 2025 is available in her secure portal. The desk checked the documents system, which showed the export was created and ready, and replied in secure chat that the document is available, while noting this does not confirm it was downloaded and that no email was sent. The case is closed as replied, nothing is left for a person, and her identity was recorded as not verified.

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

4. 2025-09-21T11:21:00Z · Internal note — Data service → H&V agent

> Export created for the requested period and made available for placement in the customer’s secure portal.

Attachments: none.

Case reference: id banking-033-at-04, track Banking & Financial Services, case 033, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The document record shows that the document is available. This does not confirm that the document was downloaded or that funds were credited. No email was sent.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `documents-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - document_ready present → true (document_ready=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- subject_date: **2025-05-09**
- documents_asked: **True**
- document_ready: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: subject_date='2025-05-09']
- event 3 (Data service): I’ve confirmed the authenticated profile and the customer’s secure-portal request. Please create the permitted CSV export for the verified account holder’s secure portal, covering 6–9 May 2025 only; do not send the data to a third party. [facts: documents_asked=True]
- event 4 (Data service): Export created for the requested period and made available for placement in the customer’s secure portal. [facts: document_ready=True]
- event 2 (Mara Ellison): I’m escalating this because the export process is unclear to me. Please let me know when the file for that period is available in my secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

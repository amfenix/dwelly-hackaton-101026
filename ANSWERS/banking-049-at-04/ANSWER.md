# Case banking-049-at-04: Acquiring Report Ready

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Venn wrote on secure chat, saying she was the authorised manager and asking the desk to escalate her request for the acquiring report covering 1–7 July 2025, which wasn't showing as available to her. The desk checked the documents system, found the report placed in the secure portal, and replied in secure chat that the document is available, without confirming any download or credit, and the case closed with no escalation. Her identity was never verified, so only the availability notice was sent and no file was provided; the record lists nothing further for a person to do.

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

4. 2025-10-23T11:21:00Z · Internal note — H&V acquiring service → H&V service agent

> I placed the report for 1–7 July 2025 in the secure portal. Its report total is £236.00; placement confirms report availability only, not a settlement credit.

Attachments: none.

Case reference: id banking-049-at-04, track Banking & Financial Services, case 049, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Venn, channel: secure_chat), by rule `do-reply`

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

- requester: **Mara Venn**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- subject_date: **2025-07-07**
- documents_asked: **True**
- document_ready: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: requester='Mara Venn', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: subject_date='2025-07-07']
- event 3 (H&V acquiring service): I checked the manager’s authority for this business. Please prepare and place the acquiring report for 1–7 July 2025 in the secure portal for the authorised user. [facts: documents_asked=True]
- event 4 (H&V acquiring service): I placed the report for 1–7 July 2025 in the secure portal. Its report total is £236.00; placement confirms report availability only, not a settlement credit. [facts: document_ready=True]
- event 2 (Mara Venn): I’m the authorised manager for the shop. The report for the period I selected is not showing as available, so I’m asking you to escalate the file request. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

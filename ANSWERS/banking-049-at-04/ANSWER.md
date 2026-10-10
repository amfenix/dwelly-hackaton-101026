# Case banking-049-at-04: Acquiring Report Ready

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Venn, writing on secure chat, said the acquiring report for 1–7 July 2025 wasn't showing as available and asked the desk to escalate the file request. The desk's documents check showed the report was already placed in the secure portal, so it did not escalate. It replied on secure chat that the document is available, that this doesn't confirm it was downloaded or that funds were credited, and that no email was sent. Mara Venn was not verified, and nothing further is recorded as left for a person.

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
- request_type: **document**
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

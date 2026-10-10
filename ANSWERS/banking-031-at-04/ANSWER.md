# Case banking-031-at-04: June statement in the secure portal

**Decision: reply**  (final state `REPLIED`)

## Summary

Elowen Marr, a customer on secure chat whose identity is not verified, said she still couldn't find her June statement in the portal and wanted it made available there, not sent by email. The desk checked the documents record, which shows the statement is available as statement-031.pdf, and replied in secure chat saying so. The reply also said this doesn't confirm it was downloaded, and that no email was sent. The case is closed as replied, and nothing in the record is left for a person, though her verification status was not checked or changed.

_Written by a model from the record below; the sections below are the record._

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

4. 2025-09-17T11:21:00Z · Business portal — Statements service → H&V agent

> Statement HV-031 for June 2025 has been placed in the account owner's secure portal as statement-031.pdf. The displayed statement shows an opening balance of £410.00 and a closing balance of £386.00.

Attachments: `statement-031.pdf`.

Case reference: id banking-031-at-04, track Banking & Financial Services, case 031, point 4, actor_next bank.

## Actions taken

- `reply` (to: Elowen Marr, channel: secure_chat), by rule `do-reply`

  > The document record shows that the document (statement-031.pdf) is available. This does not confirm that the document was downloaded or that funds were credited. No email was sent.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `documents-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = documents → true (next_system=documents)
  - document_ready → true (document_ready=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **statement**
- documents_asked: **True**
- document_ready: **True**
- document_name: **statement-031.pdf**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Elowen Marr): I’m escalating this because I still can’t find my June statement in the portal. I need the statement itself made available there; I’m not asking for it by email. [facts: requester='Elowen Marr', role='customer', channel='secure_chat', verified=False]
- event 3 (Statements service): I’m asking you to check the June 2025 statement period for the account owner and place the available document in her secure portal. Case reference HV-031. [facts: documents_asked=True]
- event 4 (Statements service): Statement HV-031 for June 2025 has been placed in the account owner's secure portal as statement-031.pdf. The displayed statement shows an opening balance of £410.00 and a closing balance of £386.00. [facts: document_ready=True, document_name='statement-031.pdf']
- event 2 (Elowen Marr): I’m escalating this because I still can’t find my June statement in the portal. I need the statement itself made available there; I’m not asking for it by email. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

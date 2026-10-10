# Case banking-038-at-04: Account confirmation available in the secure portal

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison asked, over secure chat, for an account confirmation to be made available in her own secure portal and not sent to anyone else. The desk checked the documents system, which showed account-confirmation-038.pdf as available, and replied in the chat that the document is available, that this does not confirm it was downloaded or that funds were credited, and that no email was sent. The case is closed as replied; the record shows she was not verified in this chat, and nothing further is left for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-01 09:00:00 UTC

The request:

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

What happened up to now:

1. 2025-10-01T09:00:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I need a bank document confirming my account relationship for my records. Please make it available to me in the secure portal; I am not asking for a transfer.

2. 2025-10-01T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else.

3. 2025-10-01T10:34:00Z · Internal note — H&V service agent → H&V document service

> I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only.

4. 2025-10-01T11:21:00Z · Internal note — H&V document service → H&V service agent

> Issued: account-confirmation-038.pdf. Status: available to the verified account holder in the secure portal. Account relationship: active at issue date, 1 October 2025.

Attachments: `account-confirmation-038.pdf`.

Case reference: id banking-038-at-04, track Banking & Financial Services, case 038, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellison, channel: secure_chat), by rule `do-reply`

  > The document record shows that the document (account-confirmation-038.pdf) is available. This does not confirm that the document was downloaded or that funds were credited. No email was sent.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `documents-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type != other → true (request_type=question)
  - next_system = documents → true (next_system=documents)
  - document_ready → true (document_ready=True)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **document**
- documents_asked: **True**
- document_ready: **True**
- document_name: **account-confirmation-038.pdf**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**

Where they came from:

- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V document service): I’ve matched case HV-038 to the verified account holder’s request and checked the permitted document option. I’m requesting an account confirmation for release to her secure portal only. [facts: documents_asked=True]
- event 4 (H&V document service): Issued: account-confirmation-038.pdf. Status: available to the verified account holder in the secure portal. Account relationship: active at issue date, 1 October 2025. [facts: document_ready=True, document_name='account-confirmation-038.pdf']
- event 2 (Mara Ellison): I’m escalating my request for an account confirmation. I only need the document in my own secure portal, not sent to anyone else. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-032-at-04: Archived Statement Request

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellison, writing over secure chat, asked whether an archived copy of her January 2024 statement is available. The desk checked the documents record, found the statement available, and replied in the chat saying so, with the caveat that this doesn't confirm a download or any credited funds, and that no email was sent. Her identity was not verified, and the record shows nothing further left for a person to do.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-19 09:00:00 UTC

The request:

> I need a copy of my January 2024 statement for my household records. Please let me know if it is available.

What happened up to now:

1. 2025-09-19T09:00:00Z · Secure chat — Mara Ellison → H&V service agent

> I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available?

2. 2025-09-19T09:47:00Z · Internal note — H&V service agent → H&V archive group

> I’ve checked the account-holder mandate in this secure session. Please confirm whether the January 2024 statement is available and can be ordered; I haven’t promised availability or a fee.

3. 2025-09-19T10:34:00Z · Internal note — H&V archive group → H&V service agent

> The archive check confirms that the January 2024 statement is available to order. Any applicable charge is subject to the current tariff.

4. 2025-09-19T11:21:00Z · Business portal — H&V service agent → H&V statement service

> I’m ordering the permitted January 2024 statement period for case HV-032, following the archive availability check and the account-holder’s request.

Attachments: none.

Case reference: id banking-032-at-04, track Banking & Financial Services, case 032, point 4, actor_next bank.

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
- subject: **statement**
- documents_asked: **True**
- document_ready: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (H&V archive group): I’ve checked the account-holder mandate in this secure session. Please confirm whether the January 2024 statement is available and can be ordered; I haven’t promised availability or a fee. [facts: documents_asked=True]
- event 3 (H&V archive group): The archive check confirms that the January 2024 statement is available to order. Any applicable charge is subject to the current tariff. [facts: document_ready=True]
- event 1 (Mara Ellison): I’m the account holder and need my January 2024 statement for my household records. Could you check whether an archived copy is available? [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-033-at-01: Transactions export

**Decision: ask_system**  (final state `ASKED`)

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

Where they came from:

- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: subject_date='2025-05-09']
- event 1 (Mara Ellison): I’m requesting a CSV export of my transactions from 6 May through 9 May 2025 for my own budgeting. I’m not sure how to tell whether the export has been created. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

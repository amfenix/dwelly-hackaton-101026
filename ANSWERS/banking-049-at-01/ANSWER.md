# Case banking-049-at-01: Acquiring Report Ready

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Venn, a verified customer using the business portal, asked for the acquiring report covering 1–7 July 2025 so she could review card sales and adjustments. The desk identified the request as a document request and sent it to the documents system, which accepted it, and the case closed in the ASKED state. The documents system's answer never came back into the case, so no document status is recorded and the desk's attempt to reply to her was refused; a person still needs to check the documents system's result and get back to her.

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

Attachments: none.

Case reference: id banking-049-at-01, track Banking & Financial Services, case 049, point 1, actor_next other.

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

- requester: **Mara Venn**
- role: **customer**
- channel: **business_portal**
- verified: **True**
- subject: **document**
- subject_date: **2025-07-07**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **documents**

Where they came from:

- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: requester='Mara Venn', role='customer', channel='business_portal', verified=True]
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: subject_date='2025-07-07']
- event 1 (Mara Venn): I selected 1–7 July 2025 for North Quay Printworks’ acquiring report. I need the file to review the card sales and adjustments. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=ASKED); document_ready present is false (document_ready=not known)

## Final result

ask_system (ASKED)

# Case banking-031-at-01: June statement in the secure portal

**Decision: ask_system**  (final state `ASKED`)

## Summary

Elowen Marr, a verified customer using the secure portal, asked for help finding her June 2025 statement, and the desk routed this to the documents system and sent it a query about the statement. The documents system accepted the request, but its answer is not yet in the record, so the desk's attempt to reply to her was refused and she has not been told whether the statement is available. The case closed in the asked state with nothing yet sent to the customer.

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

Attachments: none.

Case reference: id banking-031-at-01, track Banking & Financial Services, case 031, point 1, actor_next other.

## Actions taken

- `ask_system` (system: documents, about: statement), by rule `do-ask`

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
  - document_ready = false → not known (document_ready=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Elowen Marr**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **statement**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **documents**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 1 (Elowen Marr): I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there. [facts: requester='Elowen Marr', role='customer', channel='secure_portal', verified=True]
- event 1 (Elowen Marr): I own this account and need my June 2025 statement for my monthly records, but I cannot find it in the secure portal. Please help me access the statement there. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=ASKED); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=ASKED); next_system = payment is false (next_system=documents); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=ASKED); next_system = incoming is false (next_system=documents); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=ASKED); next_system = recurring is false (next_system=documents); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=ASKED); next_system = card is false (next_system=documents); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=ASKED); next_system = access is false (next_system=documents); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=ASKED); next_system = business is false (next_system=documents); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=statement); documents-reply: state = TRIAGED is false (state=ASKED); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=ASKED); next_system = tariff is false (next_system=documents); tariff_status present is false (tariff_status=not known)

## Final result

ask_system (ASKED)

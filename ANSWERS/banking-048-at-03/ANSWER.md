# Case banking-048-at-03: The buyer said payment was sent

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing for Alder Quay Studio Ltd. over secure chat, asked the desk to check whether an identifiable credit had arrived for a workshop invoice her buyer says was paid. The desk looked at the incoming account activity, but no result has come back yet, so it closed the case as "wait" in the WAITING state; a second request to query the incoming system was refused because that check had already been made. Nothing has been confirmed about whether the payment arrived, Ellison is not verified on this chat, and no reply or escalation was sent, so the case stays open for a person to pick up.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-21 09:00:00 UTC

The request:

> Please check whether the payment our buyer says they sent for our workshop invoice has reached our H&V business account.

What happened up to now:

1. 2025-10-21T09:00:00Z · External message — Buyer → Alder Quay Studio Ltd.

> I've sent payment for the workshop invoice. Please let me know when it reaches you.

2. 2025-10-21T09:47:00Z · Secure chat — Mara Ellison, Alder Quay Studio Ltd. → H&V business support

> I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account.

3. 2025-10-21T10:34:00Z · Internal note — H&V business support agent → H&V account transaction journal

> I’m checking Alder Quay Studio Ltd.’s incoming account activity for an identifiable credit matching the payment details available to the bank.

Attachments: none.

Case reference: id banking-048-at-03, track Banking & Financial Services, case 048, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `incoming-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = incoming → true (next_system=incoming)
  - incoming_asked → true (incoming_asked=True)
  - incoming_found absent → true (incoming_found=not known)

Facts established:

- requester: **Mara Ellison, Alder Quay Studio Ltd.**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **incoming_payment**
- incoming_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **incoming**

Where they came from:

- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: requester='Mara Ellison, Alder Quay Studio Ltd.', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V account transaction journal): I’m checking Alder Quay Studio Ltd.’s incoming account activity for an identifiable credit matching the payment details available to the bank. [facts: incoming_asked=True]
- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); args.system = payment is false (args.system=incoming); next_system = payment is false (next_system=incoming); next_system absent is false (next_system=incoming); incoming-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=incoming); incoming_asked absent is false (incoming_asked=True); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=incoming); next_system = recurring is false (next_system=incoming); next_system absent is false (next_system=incoming); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=incoming); next_system = card is false (next_system=incoming); next_system absent is false (next_system=incoming); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=incoming); next_system = access is false (next_system=incoming); next_system absent is false (next_system=incoming); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=incoming); next_system = business is false (next_system=incoming); next_system absent is false (next_system=incoming); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=incoming); next_system = documents is false (next_system=incoming); next_system absent is false (next_system=incoming); document_ready = false is not known (document_ready=not known); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=incoming); next_system = tariff is false (next_system=incoming); next_system absent is false (next_system=incoming)

## Final result

wait (WAITING)

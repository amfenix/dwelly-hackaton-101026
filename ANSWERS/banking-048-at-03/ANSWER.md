# Case banking-048-at-03: The buyer said payment was sent

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing for Alder Quay Studio Ltd. over secure chat, asked the desk to check whether an identifiable credit for a buyer's workshop invoice payment had reached the account. The desk classified it as a status request about an incoming payment and asked the incoming-payments system, but that system's answer had not come back, so the case closed in a waiting state with no actions taken. Her identity was not verified, and nothing is recorded as left for a person beyond the pending answer.

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
- request_type: **status**
- next_system: **incoming**

Where they came from:

- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: requester='Mara Ellison, Alder Quay Studio Ltd.', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V account transaction journal): I’m checking Alder Quay Studio Ltd.’s incoming account activity for an identifiable credit matching the payment details available to the bank. [facts: incoming_asked=True]
- event 2 (Mara Ellison, Alder Quay Studio Ltd.): I'm the authorised accountant for our business. Our buyer says they sent payment for the workshop invoice, but I can't reconcile it in our incoming activity. Please check whether an identifiable credit has reached our account. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

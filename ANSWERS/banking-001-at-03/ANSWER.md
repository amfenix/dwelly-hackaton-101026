# Case banking-001-at-03: Was the one-off transfer sent?

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, who is not verified and wrote over secure chat, asked whether H&V had sent her £420 one-off transfer to Alder & Reed Workshop, since she can see the debit. The desk read the case, classified it as a transfer question, and put it into WAITING with the outcome "wait", because the payment system had been asked but its answer was not in. The later attempts to query the payment system again and to escalate to a person were both refused because the case was no longer in TRIAGED, so the transfer status is still unknown, no actions were taken, and nothing in the record shows the case being handed to anyone, though identity verification and a transfer status check are still needed.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-07-19 09:00:00 UTC

The request:

> I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it.

What happened up to now:

1. 2025-07-19T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellison

> One-off transfer to Alder & Reed Workshop: debit shown in your account activity.

2. 2025-07-19T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status.

3. 2025-07-19T10:34:00Z · Internal note — H&V service agent → H&V transfer journal

> I am checking the journal entry for Mara Ellison's specific one-off £420 transfer to Alder & Reed Workshop. Please return the recorded transfer status.

Attachments: none.

Case reference: id banking-001-at-03, track Banking & Financial Services, case 001, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `payment-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_asked → true (payment_asked=True)
  - payment_status absent → true (payment_status=not known)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **transfer**
- amount: **420.00**
- counterparty: **Alder & Reed Workshop**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: requester='Mara Ellison', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: amount='420.00']
- initial request (system): I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it. [facts: counterparty='Alder & Reed Workshop']
- event 3 (H&V transfer journal): I am checking the journal entry for Mara Ellison's specific one-off £420 transfer to Alder & Reed Workshop. Please return the recorded transfer status. [facts: payment_asked=True]
- event 2 (Mara Ellison): I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment); tariff-ask: state = TRIAGED is false (state=WAITING); args.system = tariff is false (args.system=payment); next_system = tariff is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

# Case banking-041-at-02: Payroll file receipt confirmation

**Decision: ask_system**  (final state `ASKED`)

## Summary

Mara Ellison, writing as the company's authorised file uploader over secure chat (not verified), asked only whether H&V had received batch-041.csv (reference HV-041, £420.00 for Staff A), and said she was not asking for any payment to be approved or released. The desk classed it as a question about a batch and put a receipt query to the payment system, which accepted it. No answer has come back yet, so the receipt status is still unknown and no reply on it has been sent to her.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-07 09:00:00 UTC

The request:

> Please confirm whether my June 2025 payroll file, batch-041.csv, was received. I need to know the file's receipt status; I am not asking the bank to authorise payments on the company's behalf.

What happened up to now:

1. 2025-10-07T09:00:00Z · Business portal — Mara Ellison, authorised file uploader → H&V business portal

> I uploaded batch-041.csv for Northmere Studio Ltd.'s June 2025 payroll under reference HV-041. It lists Staff A at £420.00 and Staff B at £385.00; please confirm whether the file was received.

2. 2025-10-07T09:47:00Z · Secure chat — Mara Ellison → H&V service agent

> I am the company's authorised file uploader, and I can see that I submitted batch-041.csv, but I cannot tell whether H&V received it. Please check receipt only; I am not asking you to approve or release any payment.

Attachments: `batch-041.csv`.

Case reference: id banking-041-at-02, track Banking & Financial Services, case 041, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: payment, about: batch, reference: HV-041, amount: 420.00), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `payment-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = payment → true (args.system=payment)
  - next_system = payment → true (next_system=payment)
  - next_system absent → false (next_system=payment)
  - payment_asked absent → true (payment_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **uploader**
- channel: **secure_chat**
- verified: **False**
- subject: **batch**
- amount: **420.00**
- reference: **HV-041**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Mara Ellison): I am the company's authorised file uploader, and I can see that I submitted batch-041.csv, but I cannot tell whether H&V received it. Please check receipt only; I am not asking you to approve or release any payment. [facts: requester='Mara Ellison', role='uploader', channel='secure_chat', verified=False]
- event 1 (Mara Ellison, authorised file uploader): I uploaded batch-041.csv for Northmere Studio Ltd.'s June 2025 payroll under reference HV-041. It lists Staff A at £420.00 and Staff B at £385.00; please confirm whether the file was received. [facts: amount='420.00', reference='HV-041']
- event 2 (Mara Ellison): I am the company's authorised file uploader, and I can see that I submitted batch-041.csv, but I cannot tell whether H&V received it. Please check receipt only; I am not asking you to approve or release any payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

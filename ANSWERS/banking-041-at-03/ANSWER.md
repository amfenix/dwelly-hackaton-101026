# Case banking-041-at-03: Payroll file receipt confirmation

**Decision: wait**  (final state `WAITING`)

## Summary

Mara Ellison, writing as the company's file uploader over secure chat, asked the desk to check only whether H&V received batch-041.csv (reference HV-041, £420.00 for Staff A). The desk asked the business system's import journal and closed the case as waiting, because that system's answer has not come back yet. No actions were taken and no payment was approved or released, and her identity was not verified. What is left is for the business system's reply to arrive so receipt can be confirmed to her.

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

3. 2025-10-07T10:34:00Z · Internal note — H&V service agent → H&V import journal

> I am checking the import journal for receipt of batch-041.csv under reference HV-041, as my first step in this escalation.

Attachments: `batch-041.csv`.

Case reference: id banking-041-at-03, track Banking & Financial Services, case 041, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `business-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_asked → true (business_asked=True)
  - business_status absent → true (business_status=not known)

Facts established:

- requester: **Mara Ellison**
- role: **uploader**
- channel: **secure_chat**
- verified: **False**
- subject: **batch**
- amount: **420.00**
- reference: **HV-041**
- business_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **business**

Where they came from:

- event 2 (Mara Ellison): I am the company's authorised file uploader, and I can see that I submitted batch-041.csv, but I cannot tell whether H&V received it. Please check receipt only; I am not asking you to approve or release any payment. [facts: requester='Mara Ellison', role='uploader', channel='secure_chat', verified=False]
- event 1 (Mara Ellison, authorised file uploader): I uploaded batch-041.csv for Northmere Studio Ltd.'s June 2025 payroll under reference HV-041. It lists Staff A at £420.00 and Staff B at £385.00; please confirm whether the file was received. [facts: amount='420.00', reference='HV-041']
- event 3 (H&V import journal): I am checking the import journal for receipt of batch-041.csv under reference HV-041, as my first step in this escalation. [facts: business_asked=True]
- event 2 (Mara Ellison): I am the company's authorised file uploader, and I can see that I submitted batch-041.csv, but I cannot tell whether H&V received it. Please check receipt only; I am not asking you to approve or release any payment. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

wait (WAITING)

# Case banking-043-at-04: Waiting for the Second Signatory

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellery asked over secure chat whether Northmere Studio Ltd's payroll payment package was still waiting for the second signatory after she gave her first consent. The desk checked the business record, which shows the package as awaiting the second signatory, and replied to her in secure chat with that status, stating that no approval or role change was made. Her identity was not verified, though the request was only a status check, and nothing is left for a person in the record.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-11 09:00:00 UTC

The request:

> I gave my first consent to Northmere Studio Ltd’s payroll payment package. I need to know whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions in the portal.

What happened up to now:

1. 2025-10-11T09:00:00Z · Business portal — Mara Ellery → Harrow & Vale Bank plc

> I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions.

2. 2025-10-11T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act.

3. 2025-10-11T10:34:00Z · Internal note — H&V service agent → H&V signing log

> I’m checking the package’s signing queue against the business mandate before responding. I will not approve or release anything on either signer’s behalf.

4. 2025-10-11T11:21:00Z · Internal note — H&V service agent → H&V case record HV-043

> I’ve checked the queue against the mandate: Mara Ellery is confirmed as the first signatory, and the second signatory must provide their own consent. The queue shows no second consent and no individual payment submissions.

Attachments: none.

Case reference: id banking-043-at-04, track Banking & Financial Services, case 043, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellery, channel: secure_chat), by rule `do-reply`

  > The business record shows awaiting_second_signatory. This does not approve the request for the second signatory. No additional approval or role change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `business-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = business → true (next_system=business)
  - business_status present → true (business_status=AWAITING_SECOND_SIGNATORY)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **payment_package**
- counterparty: **Northmere Studio Ltd’s payroll payment package**
- business_asked: **True**
- business_status: **AWAITING_SECOND_SIGNATORY**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **business**

Where they came from:

- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 1 (Mara Ellery): I give my first consent to Northmere Studio Ltd’s payroll payment package. Please confirm whether it is waiting for my co-signer or has moved on; I can’t see any separate payment submissions. [facts: counterparty='Northmere Studio Ltd’s payroll payment package']
- event 3 (H&V service agent): I’m checking the package’s signing queue against the business mandate before responding. I will not approve or release anything on either signer’s behalf. [facts: business_asked=True]
- event 4 (H&V service agent): I’ve checked the queue against the mandate: Mara Ellery is confirmed as the first signatory, and the second signatory must provide their own consent. The queue shows no second consent and no individual payment submissions. [facts: business_status='AWAITING_SECOND_SIGNATORY']
- event 2 (Mara Ellery): I’ve given my consent, but I’m unsure what happens next. Please check the package status and tell me whether the second signatory still needs to act. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

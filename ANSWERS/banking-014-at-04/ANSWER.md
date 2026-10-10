# Case banking-014-at-04: Direct Debit mandate status

**Decision: reply**  (final state `REPLIED`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-14 09:00:00 UTC

The request:

> I saw a Direct Debit collection to Northmere Water Services on my March statement, but I have not seen another one. Please tell me whether the mandate is currently active; I am not asking you to cancel it or assess what I owe the organisation.

What happened up to now:

1. 2025-08-14T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> Your statement for the period ending 31 March 2025 shows a Direct Debit collection to Northmere Water Services. This is a historic statement entry.

2. 2025-08-14T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status.

3. 2025-08-14T10:34:00Z · Internal note — H&V service agent → H&V mandate journal

> For case HV-014, please check the current bank-record status of Mara Ellery's Northmere Water Services Direct Debit mandate. I am requesting a status check only and am not making a change.

4. 2025-08-14T11:21:00Z · Internal note — H&V mandate journal → H&V service agent

> I checked the payer-side mandate record on 14 August 2025. The Northmere Water Services Direct Debit mandate status is Active.

Attachments: none.

Case reference: id banking-014-at-04, track Banking & Financial Services, case 014, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellery, channel: secure_chat), by rule `do-reply`

  > The standing-order record shows active. This does not guarantee that the future payment will execute. No additional instruction or change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `recurring-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_status present → true (recurring_status=ACTIVE)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **direct_debit**
- counterparty: **Northmere Water Services**
- recurring_asked: **True**
- recurring_status: **ACTIVE**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellery): I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- initial request (system): I saw a Direct Debit collection to Northmere Water Services on my March statement, but I have not seen another one. Please tell me whether the mandate is currently active; I am not asking you to cancel it or assess what I owe the organisation. [facts: counterparty='Northmere Water Services']
- event 3 (H&V mandate journal): For case HV-014, please check the current bank-record status of Mara Ellery's Northmere Water Services Direct Debit mandate. I am requesting a status check only and am not making a change. [facts: recurring_asked=True]
- event 4 (H&V mandate journal): I checked the payer-side mandate record on 14 August 2025. The Northmere Water Services Direct Debit mandate status is Active. [facts: recurring_status='ACTIVE']
- event 2 (Mara Ellery): I saw that collection on my March statement and have not seen another one. Could you check whether the mandate is currently active? Please don't cancel it; I only need its status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

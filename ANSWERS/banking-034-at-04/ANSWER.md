# Case banking-034-at-04: Explaining a service fee

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellery asked over secure chat why a £3.20 fee appeared against a withdrawal, and asked the desk to escalate and check which tariff entry applied. The tariff review found that the fee matches the entry for a foreign-currency cash withdrawal on its processing date, so the desk replied to her with that result and did not escalate. The reply states that no refund or account change was authorised or made. Her identity was still unverified, and the record shows nothing left open for a person.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-23 09:00:00 UTC

The request:

> I can see a £3.20 fee beside a foreign-currency cash withdrawal in my H&V secure portal, but I don't understand what the charge is for or how its amount was determined. Please check the fee against the tariff that applied to that transaction.

What happened up to now:

1. 2025-09-23T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Mara Ellery

> A £3.20 service fee is shown beside your foreign-currency cash withdrawal. The transaction and fee are listed in your secure portal.

2. 2025-09-23T09:47:00Z · Secure chat — Mara Ellery → H&V service agent

> I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount.

3. 2025-09-23T10:34:00Z · Internal note — H&V service agent → H&V transaction records

> I am starting the review by matching the recorded transaction type and processing date against the tariff in force on that date. Case HV-034; no refund or account change is authorised by this review.

4. 2025-09-23T11:21:00Z · Internal note — H&V service agent → H&V case record

> I checked the transaction record against the applicable tariff entry. The record identifies a foreign-currency cash withdrawal, and the £3.20 fee matches the entry applicable to that transaction on its processing date.

Attachments: none.

Case reference: id banking-034-at-04, track Banking & Financial Services, case 034, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellery, channel: secure_chat), by rule `do-reply`

  > The tariff review shows matches. This confirms the recorded fee matches the applicable tariff; it does not authorise a refund or account change. No fee or account change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `tariff-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = tariff → true (next_system=tariff)
  - tariff_status present → true (tariff_status=MATCHES)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **fee**
- amount: **3.20**
- tariff_asked: **True**
- tariff_status: **MATCHES**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **tariff**

Where they came from:

- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: amount='3.20']
- event 3 (H&V service agent): I am starting the review by matching the recorded transaction type and processing date against the tariff in force on that date. Case HV-034; no refund or account change is authorised by this review. [facts: tariff_asked=True]
- event 4 (H&V service agent): I checked the transaction record against the applicable tariff entry. The record identifies a foreign-currency cash withdrawal, and the £3.20 fee matches the entry applicable to that transaction on its processing date. [facts: tariff_status='MATCHES']
- event 2 (Mara Ellery): I don't understand the £3.20 fee shown against this withdrawal. Please escalate this and check which tariff entry applied and how it accounts for the amount. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

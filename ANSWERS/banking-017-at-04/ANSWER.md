# Case banking-017-at-04: The Standing Order That Did Not Run

**Decision: reply**  (final state `REPLIED`)

## Summary

Mara Ellery, an unverified customer on secure chat, asked the desk to check whether her rent standing order was executed and what status the bank recorded. The desk found the scheduled run recorded as not executed and replied on secure chat with that status, noting it doesn't show whether a later run will execute and that no instruction or change was made. The case is closed with nothing left for a person.

One correction to the agent's own account: the journal does give a reason, insufficient cleared funds at the scheduled processing time, but the reply to Mara did not include it.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-08-20 09:00:00 UTC

The request:

> I need to know whether my monthly standing order for rent was sent and, if it was not, why. The recipient says they have not received it.

What happened up to now:

1. 2025-08-20T09:00:00Z · External message — Elm Quay Property Services → Mara Ellery

> I can’t see your monthly rent payment for this cycle. Please check with your bank whether it was sent.

2. 2025-08-20T09:47:00Z · Secure chat — Mara Ellery → Harrow & Vale Bank plc agent

> I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded.

3. 2025-08-20T10:34:00Z · Internal note — Harrow & Vale Bank plc agent → H&V standing-order journal

> I am checking the journal entry for Mara Ellery’s scheduled monthly rent standing order. I need the recorded outcome and any reason shown for that specific run.

4. 2025-08-20T11:21:00Z · Internal note — H&V standing-order journal → Harrow & Vale Bank plc agent

> I found the scheduled run recorded as not executed. The journal reason is insufficient cleared funds at the scheduled processing time.

Attachments: none.

Case reference: id banking-017-at-04, track Banking & Financial Services, case 017, point 4, actor_next bank.

## Actions taken

- `reply` (to: Mara Ellery, channel: secure_chat), by rule `do-reply`

  > The standing-order record shows not_executed. This does not establish whether a later run will execute. No additional instruction or change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `recurring-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = recurring → true (next_system=recurring)
  - recurring_status present → true (recurring_status=NOT_EXECUTED)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Mara Ellery**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- recurring_asked: **True**
- recurring_status: **NOT_EXECUTED**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **status**
- next_system: **recurring**

Where they came from:

- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: requester='Mara Ellery', role='customer', channel='secure_chat', verified=False]
- event 3 (H&V standing-order journal): I am checking the journal entry for Mara Ellery’s scheduled monthly rent standing order. I need the recorded outcome and any reason shown for that specific run. [facts: recurring_asked=True]
- event 4 (H&V standing-order journal): I found the scheduled run recorded as not executed. The journal reason is insufficient cleared funds at the scheduled processing time. [facts: recurring_status='NOT_EXECUTED']
- event 2 (Mara Ellery): I’ve been told my rent payment hasn’t arrived. Please check the scheduled standing-order run and tell me whether H&V executed it and what status the bank has recorded. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

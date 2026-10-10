# Case banking-S13-at-02: Raise my overdraft to £2,000

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Priya Hollins asked over secure chat to raise her arranged overdraft from £500 to £2,000, wanting it in place before the weekend. The desk did not change the limit, since a limit change is put to the team that decides; it registered a request about the limit with the business team and closed the case as submitted. The request is not approved, the record does not show the £2,000 limit will be in place by the weekend, and Priya is recorded as not verified, so the decision is left to the business team.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-13 09:00:00 UTC

The request:

> Please raise my arranged overdraft from £500 to £2,000 before the weekend.

What happened up to now:

1. 2025-11-13T09:00:00Z · Secure portal — H&V secure portal → Priya Hollins

> Current account ending 6058: arranged overdraft limit £500.00.

2. 2025-11-13T09:47:00Z · Secure chat — Priya Hollins → H&V service agent

> Could you raise my arranged overdraft from £500 to £2,000? I’d like it in place before the weekend because I have a car repair bill coming. I’ve banked with you for nine years, so I’m hoping it’s straightforward.

Attachments: none.

Case reference: id banking-S13-at-02, track banking, case S13, point 2, actor_next bank.

## Actions taken

- `register_request` (team: business, about: limit), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: rule `limit-or-role-change-is-a-review` — A limit or a role is not changed on request; it is put to the team that decides.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - subject in [limit, "role"] → true (subject=limit)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Priya Hollins**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **limit**
- amount: **2000.00**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **business**

Where they came from:

- event 2 (Priya Hollins): Could you raise my arranged overdraft from £500 to £2,000? I’d like it in place before the weekend because I have a car repair bill coming. I’ve banked with you for nine years, so I’m hoping it’s straightforward. [facts: requester='Priya Hollins', role='customer', channel='secure_chat', verified=False]
- event 2 (Priya Hollins): Could you raise my arranged overdraft from £500 to £2,000? I’d like it in place before the weekend because I have a car repair bill coming. I’ve banked with you for nine years, so I’m hoping it’s straightforward. [facts: amount='2000.00']
- event 2 (Priya Hollins): Could you raise my arranged overdraft from £500 to £2,000? I’d like it in place before the weekend because I have a car repair bill coming. I’ve banked with you for nine years, so I’m hoping it’s straightforward. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

# Case banking-S03-at-05: Standing-order change “confirmed” in chat, not in the portal

**Decision: wait**  (final state `WAITING`)

## Summary

Callum Ashby asked over secure chat to raise his standing order from £30 to £45 a month, and the desk decided to wait: the change has been sent to his secure portal as a pending amendment, and the standing order itself has not been changed. His "yes I confirm" in chat was not accepted as confirmation, and his identity was not verified in the chat. The agent's attempt to redirect him to the secure process was refused because the case was already in a waiting state, so no actions were taken, and what is left is for Callum to open the pending amendment in the portal and confirm it there.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-03 09:00:00 UTC

The request:

> Callum Ashby wants to raise his monthly standing order to the fictional Brackenridge Climbing Club from £30.00 to £45.00.

What happened up to now:

1. 2025-11-03T09:00:00Z · Secure portal — H&V system → Callum Ashby

> Standing order to Brackenridge Climbing Club: £30.00 per month, paid on the 15th.

2. 2025-11-03T09:47:00Z · Secure chat — Callum Ashby → H&V agent

> Hi, the club has put the monthly fee up, so I need to raise this standing order from £30 to £45 a month. I haven’t changed anything myself yet. Could you set that up?

3. 2025-11-03T10:34:00Z · Internal note — H&V agent → H&V case record HV-S03

> I checked that Callum Ashby is the verified owner of this standing order and may amend it. A chat request is not authorisation; the order stays at £30.00 until he confirms the amendment in the secure portal.

4. 2025-11-03T11:21:00Z · Secure portal — H&V agent → Callum Ashby

> I’ve sent the change from £30.00 to £45.00 per month to your secure portal for you to confirm. I have not changed the standing order. Please open the pending amendment in the portal and confirm it there.

5. 2025-11-03T12:08:00Z · Secure chat — Callum Ashby → H&V agent

> yes I confirm, go ahead. £45 from now on please. Saves me logging in again.

Attachments: none.

Case reference: id banking-S03-at-05, track banking, case S03, point 5, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `change-waits-for-the-customer` — The change was sent to the portal; the customer has not confirmed it yet.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = requested → true (confirmation=requested)
  - registration_asked absent → true (registration_asked=not known)

Facts established:

- requester: **Callum Ashby**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **standing_order**
- amount: **45.00**
- confirmation: **requested**
- instructed_outside_portal: **False**
- request_type: **change**
- next_system: **recurring**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 5 (Callum Ashby): yes I confirm, go ahead. £45 from now on please. Saves me logging in again. [facts: requester='Callum Ashby', role='customer', channel='secure_chat', verified=False]
- event 2 (Callum Ashby): Hi, the club has put the monthly fee up, so I need to raise this standing order from £30 to £45 a month. I haven’t changed anything myself yet. Could you set that up? [facts: amount='45.00']
- event 4 (H&V agent): I’ve sent the change from £30.00 to £45.00 per month to your secure portal for you to confirm. I have not changed the standing order. Please open the pending amendment in the portal and confirm it there. [facts: confirmation='requested', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=WAITING); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change)

## Final result

wait (WAITING)

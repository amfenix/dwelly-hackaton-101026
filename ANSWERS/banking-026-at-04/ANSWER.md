# Case banking-026-at-04: A Safe Route to a Forgotten PIN

**Decision: reply**  (final state `REPLIED`)

## Summary

Maren Ellwood wrote on secure chat that she had forgotten her debit card PIN and asked for the safe way to deal with it, saying she would not send the PIN in chat. The desk sent her one reply stating that the access record shows "other", that this does not establish a password, PIN or access change, and that no secret was handled and no access change was made. The record does not show the reply pointing her to the PIN procedure, although the access team notes say it was opened in the secure portal. It also still lists her as not verified, a mismatch with the access team's note that the check was complete, and nobody has resolved it.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-07 09:00:00 UTC

The request:

> Maren forgot the PIN for her H&V debit card and wants to use the bank’s safe process to regain access without sharing the PIN in a message.

What happened up to now:

1. 2025-09-07T09:00:00Z · Secure chat — Maren Ellwood → H&V agent

> I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat.

2. 2025-09-07T09:47:00Z · Internal note — H&V agent → Access team

> I’m escalating HV-026 for the prescribed PIN route. The required customer check is complete in the secure portal; I have not asked for or recorded a PIN.

3. 2025-09-07T10:34:00Z · Internal note — Access team → H&V agent

> The prescribed PIN procedure is available for this case. Please open it for the checked customer in the secure portal; the PIN must not be sent in correspondence.

4. 2025-09-07T11:21:00Z · Secure portal — H&V agent → Maren Ellwood

> I’ve opened the prescribed PIN procedure for you in the secure portal, following the completed check. Please continue through that procedure there; I cannot see your PIN.

Attachments: none.

Case reference: id banking-026-at-04, track Banking & Financial Services, case 026, point 4, actor_next bank.

## Actions taken

- `reply` (to: Maren Ellwood, channel: secure_chat), by rule `do-reply`

  > The access record shows other. This does not establish a password, PIN, or access change. No secret was handled and no additional access change was made.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REPLY_PENDING`: the agent asked for `reply`, rule `access-reply` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = access → true (next_system=access)
  - access_status present → true (access_status=OTHER)
- `REPLY_PENDING` → `REPLIED`: rule `do-reply`.
  - state = REPLY_PENDING → true (state=REPLY_PENDING)

Facts established:

- requester: **Maren Ellwood**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- access_asked: **True**
- access_status: **OTHER**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **access**

Where they came from:

- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: requester='Maren Ellwood', role='customer', channel='secure_chat', verified=False]
- event 2 (Access team): I’m escalating HV-026 for the prescribed PIN route. The required customer check is complete in the secure portal; I have not asked for or recorded a PIN. [facts: access_asked=True]
- event 3 (Access team): The prescribed PIN procedure is available for this case. Please open it for the checked customer in the secure portal; the PIN must not be sent in correspondence. [facts: access_status='OTHER']
- event 4 (H&V agent): I’ve opened the prescribed PIN procedure for you in the secure portal, following the completed check. Please continue through that procedure there; I cannot see your PIN. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

reply (REPLIED)

# Case banking-026-at-02: A Safe Route to a Forgotten PIN

**Decision: wait**  (final state `WAITING`)

## Summary

Maren Ellwood, a customer on secure chat, said she had forgotten her debit card PIN and asked for the safe way to handle it, without sending the PIN in chat. The desk classified this as a card access request, saw that the Access team had already been asked and its answer was not yet in, and closed the case in WAITING with the outcome "wait". The agent's attempt to redirect her to the secure process was refused because the case was no longer in the triaged state, so she has not been told anything, and her identity is still unverified. The record shows no PIN was requested or recorded, and the Access team's answer is what remains outstanding.

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

Attachments: none.

Case reference: id banking-026-at-02, track Banking & Financial Services, case 026, point 2, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `access-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = access → true (next_system=access)
  - access_asked → true (access_asked=True)
  - access_status absent → true (access_status=not known)

Facts established:

- requester: **Maren Ellwood**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- access_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **access**

Where they came from:

- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: requester='Maren Ellwood', role='customer', channel='secure_chat', verified=False]
- event 2 (Access team): I’m escalating HV-026 for the prescribed PIN route. The required customer check is complete in the secure portal; I have not asked for or recorded a PIN. [facts: access_asked=True]
- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `redirect_secure`: redirect-to-the-secure-process: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

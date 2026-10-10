# Case banking-026-at-01: A Safe Route to a Forgotten PIN

**Decision: redirect_secure**  (final state `REDIRECTED`)

## Summary

Maren Ellwood, an unverified customer on secure chat, said she had forgotten the PIN for her debit card and asked for the safe way to deal with it. The desk classified this as a card access request and redirected her to the secure process in her secure portal, where her identity is checked. The message told her the bank never asks for a password, PIN or verification code, and that nothing on her profile was changed. The case is closed as redirected, and the record lists nothing left for a person to do.

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

Attachments: none.

Case reference: id banking-026-at-01, track Banking & Financial Services, case 026, point 1, actor_next bank.

## Actions taken

- `redirect_secure` (to: Maren Ellwood, channel: secure_chat), by rule `do-redirect`

  > Please use the secure process in your secure portal to do this; it checks your identity there. We will never ask for your password, PIN or a verification code. Nothing on your profile was changed.


## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REDIRECT_PENDING`: the agent asked for `redirect_secure`, rule `redirect-to-the-secure-process` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = access → true (request_type=access)
  - request_type = instruction → false (request_type=access)
  - not verified → true (verified=False)
- `REDIRECT_PENDING` → `REDIRECTED`: rule `do-redirect`.
  - state = REDIRECT_PENDING → true (state=REDIRECT_PENDING)

Facts established:

- requester: **Maren Ellwood**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **card**

Where they came from:

- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: requester='Maren Ellwood', role='customer', channel='secure_chat', verified=False]
- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

redirect_secure (REDIRECTED)

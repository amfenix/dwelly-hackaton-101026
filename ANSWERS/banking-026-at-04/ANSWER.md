# Case banking-026-at-04: A Safe Route to a Forgotten PIN

**Decision: wait**  (final state `WAITING`)

## Summary

Maren Ellwood wrote in secure chat that she had forgotten her debit card PIN and asked for the safe way to deal with it. The desk classed it as an access request about a card and found that the bank had already opened the prescribed PIN procedure for her in the secure portal. It took no action and closed the case as waiting, since nothing more can happen until she uses that procedure. The desk's own attempt to send a reply was refused because the case was already in the waiting state, so no reply went out from the desk, and nothing is left for a person unless she does not complete the portal steps.

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

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `already-redirected` — The customer was pointed to the secure process; nothing to do until they use it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = access → true (request_type=access)
  - bank_redirected → true (bank_redirected=True)

Facts established:

- requester: **Maren Ellwood**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **card**
- access_asked: **True**
- access_status: **OTHER**
- bank_redirected: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **access**
- next_system: **access**

Where they came from:

- event 1 (Maren Ellwood): I’ve forgotten the PIN for my H&V debit card and need to use it again. Please tell me the safe way to deal with this; I won’t send my PIN in chat. [facts: requester='Maren Ellwood', role='customer', channel='secure_chat', verified=False]
- event 2 (Access team): I’m escalating HV-026 for the prescribed PIN route. The required customer check is complete in the secure portal; I have not asked for or recorded a PIN. [facts: access_asked=True]
- event 3 (Access team): The prescribed PIN procedure is available for this case. Please open it for the checked customer in the secure portal; the PIN must not be sent in correspondence. [facts: access_status='OTHER']
- event 4 (H&V agent): the bank already acted: I’ve opened the prescribed PIN procedure for you in the secure portal, following the completed check. Please continue through that procedure there; I cannot see your PIN.
- event 4 (H&V agent): I’ve opened the prescribed PIN procedure for you in the secure portal, following the completed check. Please continue through that procedure there; I cannot see your PIN. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=access); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=access); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=access); tariff_status present is false (tariff_status=not known)

## Final result

wait (WAITING)

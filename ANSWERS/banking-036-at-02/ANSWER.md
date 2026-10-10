# Case banking-036-at-02: New correspondence address

**Decision: send_for_confirmation**  (final state `CONFIRMATION_SENT`)

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-09-27 09:00:00 UTC

The request:

> I have moved within the UK and want H&V to update the address used for my correspondence.

What happened up to now:

1. 2025-09-27T09:00:00Z · External message — Mara Ellison → Harrow & Vale Bank plc

> I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile.

2. 2025-09-27T09:47:00Z · Secure portal — Mara Ellison → Harrow & Vale Bank plc

> I’m escalating my request to change my correspondence address. I have completed the identity checks in this secure session and can confirm the change when the profile process asks me to.

Attachments: none.

Case reference: id banking-036-at-02, track Banking & Financial Services, case 036, point 2, actor_next bank.

## Actions taken

- `send_for_confirmation` (change: profile, to: Mara Ellison), by rule `do-confirm`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `CONFIRM_PENDING`: rule `change-needs-confirmation` — A change is confirmed by the customer in the secure portal, not in chat or by email.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = change → true (request_type=change)
  - confirmation = none → true (confirmation=none)
  - registration_asked absent → true (registration_asked=not known)
- `CONFIRM_PENDING` → `CONFIRMATION_SENT`: rule `do-confirm`.
  - state = CONFIRM_PENDING → true (state=CONFIRM_PENDING)

Facts established:

- requester: **Mara Ellison**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **profile**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **change**
- next_system: **access**

Where they came from:

- event 2 (Mara Ellison): I’m escalating my request to change my correspondence address. I have completed the identity checks in this secure session and can confirm the change when the profile process asks me to. [facts: requester='Mara Ellison', role='customer', channel='secure_portal', verified=True]
- event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `reply`: registration-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = payment is false (next_system=access); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = incoming is false (next_system=access); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = recurring is false (next_system=access); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = card is false (next_system=access); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = business is false (next_system=access); business_status present is false (business_status=not known); documents-reply: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = documents is false (next_system=access); document_ready present is false (document_ready=not known)

## Final result

send_for_confirmation (CONFIRMATION_SENT)

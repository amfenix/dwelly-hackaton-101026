# Case banking-044-at-03: One Line in the Supplier Batch

**Decision: wait**  (final state `WAITING`)

## What the system received

- Source role: Authorised business user
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-13 09:00:00 UTC

The request:

> I can see that our supplier batch is marked processed, but I need to know whether the payment on row SUP-17 was paid or rejected.

What happened up to now:

1. 2025-10-13T09:00:00Z · Business portal — H&V secure portal → Leona Voss

> Batch “Alderwick supplier payments” — status: Processed.

2. 2025-10-13T09:47:00Z · Secure chat — Leona Voss → H&V service agent

> I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status.

3. 2025-10-13T10:34:00Z · Internal note — H&V service agent → H&V payment journal

> My first action is to look up row SUP-17 in the previously authorised batch and verify the status of that line specifically.

Attachments: none.

Case reference: id banking-044-at-03, track Banking & Financial Services, case 044, point 3, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `WAITING`: rule `payment-waits` — The system was asked; its answer is not in yet.
  - state = TRIAGED → true (state=TRIAGED)
  - next_system = payment → true (next_system=payment)
  - payment_asked → true (payment_asked=True)
  - payment_status absent → true (payment_status=not known)

Facts established:

- requester: **Leona Voss**
- role: **viewer**
- channel: **secure_chat**
- verified: **False**
- subject: **batch**
- reference: **SUP-17**
- payment_asked: **True**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **question**
- next_system: **payment**

Where they came from:

- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: requester='Leona Voss', role='viewer', channel='secure_chat', verified=False]
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: reference='SUP-17']
- event 3 (H&V payment journal): My first action is to look up row SUP-17 in the previously authorised batch and verify the status of that line specifically. [facts: payment_asked=True]
- event 2 (Leona Voss): I’m authorised to view our payouts. The batch shows processed, but I can’t tell whether row SUP-17, for our studio materials supplier, was paid. Please check that row’s status. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

Requests the policy refused:

- `ask_system`: payment-ask: state = TRIAGED is false (state=WAITING); next_system absent is false (next_system=payment); payment_asked absent is false (payment_asked=True); incoming-ask: state = TRIAGED is false (state=WAITING); args.system = incoming is false (args.system=payment); next_system = incoming is false (next_system=payment); next_system absent is false (next_system=payment); recurring-ask: state = TRIAGED is false (state=WAITING); args.system = recurring is false (args.system=payment); next_system = recurring is false (next_system=payment); next_system absent is false (next_system=payment); card-ask: state = TRIAGED is false (state=WAITING); args.system = card is false (args.system=payment); next_system = card is false (next_system=payment); next_system absent is false (next_system=payment); access-ask: state = TRIAGED is false (state=WAITING); args.system = access is false (args.system=payment); next_system = access is false (next_system=payment); next_system absent is false (next_system=payment); business-ask: state = TRIAGED is false (state=WAITING); args.system = business is false (args.system=payment); next_system = business is false (next_system=payment); next_system absent is false (next_system=payment); documents-ask: state = TRIAGED is false (state=WAITING); args.system = documents is false (args.system=payment); next_system = documents is false (next_system=payment); next_system absent is false (next_system=payment)
- `escalate`: agent-escalates: state = TRIAGED is false (state=WAITING)

## Final result

wait (WAITING)

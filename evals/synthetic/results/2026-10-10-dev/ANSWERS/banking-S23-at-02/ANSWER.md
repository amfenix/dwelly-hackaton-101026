# Case banking-S23-at-02: Why did my savings rate drop?

**Decision: ask_system**  (final state `ASKED`)

## Summary

Bertram Oyelaran, writing over secure chat, asked what happened to his rate, whether it will drop again, and whether he should move his money into a fixed bond. The desk could not verify him and could not identify a subject, so it sent the rate question to the tariff system, and that answer has not come back yet. Still open for a person: his identity is unverified, and the record shows no answer on the rate change, on whether it will drop again, or on the fixed bond question.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-23 09:00:00 UTC

The request:

> The interest rate on my Easy Access Saver has gone down and I wasn’t expecting it. Why did it drop, and when?

What happened up to now:

1. 2025-11-23T09:00:00Z · Secure portal — Bertram Oyelaran → Harrow & Vale Bank plc

> My Easy Access Saver ending 3058 is paying less interest than it used to. Why has the rate dropped, and since when?

2. 2025-11-23T09:47:00Z · Secure chat — Bertram Oyelaran → H&V service agent

> I’m signed in. I don’t remember being told about any change. Can you check what happened to the rate? And is it going to drop again — should I be moving my money into a fixed bond instead?

Attachments: none.

Case reference: id banking-S23-at-02, track banking, case S23, point 2, actor_next bank.

## Actions taken

- `ask_system` (system: tariff, about: unknown), by rule `do-ask`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ASK_PENDING`: the agent asked for `ask_system`, rule `tariff-ask` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - args.system = tariff → true (args.system=tariff)
  - next_system = tariff → not known (next_system=not known)
  - next_system absent → true (next_system=not known)
  - tariff_asked absent → true (tariff_asked=not known)
  - request_type not in [register, change, authority] → true (request_type=question)
- `ASK_PENDING` → `ASKED`: rule `do-ask`.
  - state = ASK_PENDING → true (state=ASK_PENDING)

Facts established:

- requester: **Bertram Oyelaran**
- role: **customer**
- channel: **secure_chat**
- verified: **False**
- subject: **unknown**
- confirmation: **none**
- instructed_outside_portal: **True**
- request_type: **question**
- next_system: **tariff**

Where they came from:

- event 2 (Bertram Oyelaran): I’m signed in. I don’t remember being told about any change. Can you check what happened to the rate? And is it going to drop again — should I be moving my money into a fixed bond instead? [facts: requester='Bertram Oyelaran', role='customer', channel='secure_chat', verified=False]
- event 2 (Bertram Oyelaran): I’m signed in. I don’t remember being told about any change. Can you check what happened to the rate? And is it going to drop again — should I be moving my money into a fixed bond instead? [facts: confirmation='none', instructed_outside_portal=True]

## Escalated

No.

## What failed

- nothing

## Final result

ask_system (ASKED)

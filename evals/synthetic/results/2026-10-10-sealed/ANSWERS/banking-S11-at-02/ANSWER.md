# Case banking-S11-at-02: Paid “HMRC” after a phone call — I want my money back

**Decision: submit_request**  (final state `REQUESTED`)

## Summary

Rosalind Pike, verified on a call, reported that she sent £2,400 to an account ending 7731 after a caller claiming to be from HMRC demanded unpaid tax, and asked for the money to be recovered immediately. The desk classed this as an incoming-payment matter and registered a request with the incoming team, and the case closed as requested. The record shows no recall or refund being carried out, so recovering the money is left to that team, and nothing in the record confirms it will come back.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-11-11 09:00:00 UTC

The request:

> A man rang me saying he was from HMRC and that I owed unpaid tax. He made me send £2,400 to an account he gave me, about an hour ago. I think it was a scam. I want my money back right now.

What happened up to now:

1. 2025-11-11T09:00:00Z · Secure portal — Harrow & Vale Bank plc → Rosalind Pike

> One-off transfer of £2,400.00 to a new payee, account ending 7731: status sent, from your account ending 4417.

2. 2025-11-11T09:47:00Z · Verified call — Rosalind Pike → H&V service agent

> After H&V completed its identification checks, I said that about an hour ago a man rang me saying he was from HMRC. He told me I owed unpaid tax and that bailiffs would come today unless I paid straight away, and he gave me the account ending 7731 to pay into. I sent £2,400. Now I think it was a scam. Please get my money back right now, before he takes it out — every minute counts. He said he would ring me back at noon; should I keep him talking? No security details were recorded in the call note.

Attachments: none.

Case reference: id banking-S11-at-02, track banking, case S11, point 2, actor_next bank.

## Actions taken

- `register_request` (team: incoming, about: incoming_payment), by rule `do-request`

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `REQUEST_PENDING`: the agent asked for `submit_request`, rule `register` accepted it.
  - state = TRIAGED → true (state=TRIAGED)
  - request_type = register → true (request_type=register)
  - registration_asked absent → true (registration_asked=not known)
- `REQUEST_PENDING` → `REQUESTED`: rule `do-request`.
  - state = REQUEST_PENDING → true (state=REQUEST_PENDING)

Facts established:

- requester: **Rosalind Pike**
- role: **customer**
- channel: **verified_call**
- verified: **True**
- subject: **incoming_payment**
- amount: **2400.00**
- counterparty: **HMRC and that I owed unpaid tax**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **register**
- next_system: **incoming**
- credentials_requested: **False**
- joint_holder_change: **False**

Where they came from:

- event 2 (Rosalind Pike): After H&V completed its identification checks, I said that about an hour ago a man rang me saying he was from HMRC. He told me I owed unpaid tax and that bailiffs would come today unless I paid straight away, and he gave me the account ending 7731 to pay into. I sent £2,400. Now I think it was a scam. Please get my money back right now, before he takes it out — every minute counts. He said he would ring me back at noon; should I keep him talking? No security details were recorded in the call note. [facts: requester='Rosalind Pike', role='customer', channel='verified_call', verified=True]
- event 2 (Rosalind Pike): After H&V completed its identification checks, I said that about an hour ago a man rang me saying he was from HMRC. He told me I owed unpaid tax and that bailiffs would come today unless I paid straight away, and he gave me the account ending 7731 to pay into. I sent £2,400. Now I think it was a scam. Please get my money back right now, before he takes it out — every minute counts. He said he would ring me back at noon; should I keep him talking? No security details were recorded in the call note. [facts: amount='2400.00']
- initial request (system): A man rang me saying he was from HMRC and that I owed unpaid tax. He made me send £2,400 to an account he gave me, about an hour ago. I think it was a scam. I want my money back right now. [facts: counterparty='HMRC and that I owed unpaid tax']
- event 2 (Rosalind Pike): After H&V completed its identification checks, I said that about an hour ago a man rang me saying he was from HMRC. He told me I owed unpaid tax and that bailiffs would come today unless I paid straight away, and he gave me the account ending 7731 to pay into. I sent £2,400. Now I think it was a scam. Please get my money back right now, before he takes it out — every minute counts. He said he would ring me back at noon; should I keep him talking? No security details were recorded in the call note. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

No.

## What failed

- nothing

## Final result

submit_request (REQUESTED)

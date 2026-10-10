# The 8 points still differing at 95% (141/149)

The committed run (`ANSWERS/`, `results.jsonl`, commit 61ab351) matches the bank's next step at 141
of the 149 public decision points where the bank acts next (`uv run python evals/score_points.py
--show`). This note looks at the other 8 one by one: what the desk was given, what the bank did
next, what the case's own summary (`index.md`, "Next action at escalation") says, and what the
desk decided. Three of them raise questions about the input itself, listed at the end for the
team.

Notation: `015@4` is case 015 cut after event 4; the bank's step is read from event 5.

## Summary

| Point | Bank's next event | `index.md` next action | Desk | Where the difference comes from |
|---|---|---|---|---|
| 015@4 | portal record "mandate … — Cancelled" | submit the cancellation | wait | **input**: a status record not marked as a system record |
| 025@1 | asks which attempt | check the card authorisation journal | ask the card system | **input**: the request is shown before the customer made it |
| 026@1 | escalates to the access team | the PIN procedure is in the portal | redirect to the secure process | **label**: the next event and the summary disagree; the desk follows the summary |
| 026@3 | opens the PIN procedure for the customer | the PIN procedure is in the portal | reply | desk: replied instead of redirecting |
| 036@4 | submits the confirmed request to the process | open the profile-change process | wait | **source**: same situation as 028@5, opposite step |
| 036@5 | "your new address is marked as current" | open the profile-change process | wait | **source**: no system answer in the history before the bank says it is done |
| 037@4 | the data team's portal record to the customer | refer HV-037 to the data team | escalate | desk: escalated though the review was registered |
| 045@2 | "I'll check the administrator record" | send to the verified administrator | forward to the administrator | **label**: the next event and the summary disagree; the desk follows the summary |

## Point by point

### 015@4 — Cancel future Direct Debit collections

- **Given:** a verified call asking to cancel the Northmere Fitness mandate (2); the agent's note
  on the collection stage (3); the agent submits the cancellation to the Direct Debit service (4).
- **Next (5):** `Secure portal | Harrow & Vale Bank plc -> Mara Ellison`: "Direct Debit mandate:
  Northmere Fitness — Cancelled."
- **Desk:** `wait` — the instruction was submitted and no answer is in yet.
- **Why it differs:** event 5 is the Direct Debit service's result shown in the portal, in the
  same shape as event 1 ("… — Active."). The converter marks a portal record as `system` only when
  it has a `status:` field, so this one is `conversation`, and the label reads it as the bank
  replying. The desk's step is right; the record is not recognised.
- **Check:** should the converter also mark `<thing>: <name> — <status>` portal records from the
  bank as `system`?

### 025@1 — Why a card attempt was declined

- **Given:** only event 1, the shop's terminal to the customer: "Payment not accepted. Please
  contact your bank." **And** the case's `request`: "Mara wants to know why her £18.40 card payment
  at North Quay Books was declined."
- **Next (2):** a verified call, the agent to the customer: "Please tell me which declined attempt
  you want me to investigate."
- **Desk:** `ask_system` (card) — the request already names the amount and the shop.
- **Why it differs:** at point 1 the customer has not contacted the bank yet (her own words come
  at event 3), but the converter shows the `Initial request` at every point. The desk knows from
  the request what the bank did not know at that moment, so it skips the question. The `request`
  is also written in the third person: it is a summary of the case, not a message.
- **Check:** should a point show the `Initial request` only once the customer's own request is in
  the visible events? Is point 1 a real decision point here at all (the bank speaks first at 2)?

### 026@1 — A safe route to a forgotten PIN

- **Given:** the customer asks in secure chat for the safe way to deal with a forgotten PIN.
- **Next (2):** an internal note to the access team, escalating for the prescribed PIN route.
- **Summary's next action:** "The secure PIN procedure is available in Maren's portal for her to
  continue."
- **Desk:** `redirect_secure` — point the customer to the secure process.
- **Why it differs:** the next event is the internal step; the summary describes the step towards
  the customer. The desk does what the summary says.
- **Check:** should we score against `next_action` as well as the next event (both are in
  `track/expected.json`)?

### 026@3 — the same case, after the access team answered

- **Given:** the access team: "The prescribed PIN procedure is available for this case. Please open
  it for the checked customer in the secure portal."
- **Next (4):** the agent opens the procedure and points the customer to it.
- **Desk:** `reply` — the agent chose to reply on `access_status: OTHER` (the reader has no status
  for "procedure available").
- **Why it differs:** the desk's own judgement. Two fixes are possible: a status for "procedure
  available" in `check_access`, and/or let `redirect_secure` be the answer to an access request once
  the access team has answered.

### 036@4 and 036@5 — New correspondence address

- **Given:** a verified customer asks to change the address (1, 2); the agent opens the profile
  change process (3); the customer confirms in the process (4).
- **036@4 next (5):** the agent submits the confirmed request to the process.
- **036@5 next (6):** the bank tells the customer the new address is current.
- **Desk:** `wait` at both — the customer's confirmation in the process is applied by the process.
- **Why it differs:** case 028 (phone number) has the same shape and the opposite step: there the
  process asks for the confirmation (028 event 4), and after the customer confirms, the process
  applies the change by itself (028 event 6). In 036 there is no request from the process before the
  customer confirms, the bank submits by hand, and no system answer appears before the bank says
  the address is current. Whatever rule the desk follows, one of 028@5 and 036@4 differs.
- **Check:** is 036's history complete in the source (a missing process request and a missing
  process answer), or are the two cases simply different?

### 037@4 — Profile name typo

- **Given:** the correction was referred to the data team (3), which logged it as received for
  review (4). The facts include `registered: true`, `registration_ref: HV-037`.
- **Next (5):** the data team's portal record to the customer: received for review, name not changed.
- **Desk:** `escalate` — the agent tried to submit again and to ask the access system, both refused,
  then escalated. The policy accepts `reply` here; the agent did not try it.
- **Why it differs:** the desk's own judgement; triage also called the request a `change` instead
  of `register` in this run. In the previous run the same point matched.

### 045@2 — New employee access request

- **Given:** an employee asks for a colleague's portal access and says she is not the company
  administrator (1, 2).
- **Next (3):** the agent: "I'll check the authorised company-administrator record and, if
  confirmed, send the request to that administrator for approval."
- **Summary's next action:** "The agent sent the access request to the verified company
  administrator through the secure portal for approval."
- **Desk:** `forward_to_authority`.
- **Why it differs:** as in 026@1, the next event is an intermediate step, while the summary names
  the step the desk took.

## Questions for the team

1. **What is the right answer at a point: the next event, or the case's "Next action at
   escalation"?** At 026@1 and 045@2 they disagree, and the desk follows the summary. Scoring
   against either (or accepting both) changes the number by 2 points.
2. **Should a point show the `Initial request` before the customer has made it?** (025@1) Today
   every point carries the request, which is a third-person summary of the whole case, so a point
   early in the history can know more than the bank did.
3. **Should the converter mark a bank portal record of the form `<thing>: <name> — <status>` as
   `system`?** (015@4) Today only records with a `status:` field are.
4. **Is case 036 complete in the source?** It lacks the process's confirmation request and its
   answer that case 028 has.
5. **Two of the 8 are the desk's own judgement (026@3, 037@4).** They can be fixed with a status for
   "procedure available" and by letting `redirect_secure` answer an access request; we hold them
   until the input questions are settled, to avoid tuning to single cases.

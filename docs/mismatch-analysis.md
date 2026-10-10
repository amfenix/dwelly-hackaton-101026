# Where the desk's next step differs from the bank's: the public banking cases

The run committed at the repository root (`ANSWERS/`, `results.jsonl`, commit 859014b; policy as of f60e4d0)
answers every decision point of the 50 public banking cases. At the 149 points where the bank acts
next (the agent's own notes to a case record are not decisions and are left out), the desk's
decision matches the bank's next step at **112 (75%)**:

| Bank's next step | Matched |
|---|---|
| ask a system | 31 / 37 |
| wait for an answer | 36 / 38 |
| reply to the customer | 35 / 59 |
| submit a request or instruction | 8 / 12 |
| send a change for confirmation | 2 / 3 |

The bank's next step is labelled from the next event of the history (`track/expected.json`). The
37 differences below are grouped by cause; each group says what needs attention. Some are not
errors of the desk but of the labelling (group 1): the real accuracy is higher than 75%.

## 1. The labelling, not the desk (about 9 points)

The next event does not always say plainly what the bank decided.

| Point | What happened | Note |
|---|---|---|
| 019@3 | the desk sent the date change for confirmation; the bank did the same | "for your secure confirmation" is not caught as a confirmation request |
| 020@2, 021@2 | the desk asked the instruction register / card journal; so did the bank | the word "register(ed)" in the bank's note was read as "submit a request" |
| 042@3, 044@3 | the desk waits for the system; the system's answer arrives next as a portal record to the customer | an answer delivered straight to the customer is labelled "reply" |
| 027@3, 027@4 | the recovery system and the app message the customer by themselves | a system acting on its own is labelled "reply"; the desk's step there is to wait |
| 012@5, 019@5 | the customer confirmed; the desk passes the confirmed change on; the system then applies it and tells the customer | arguably right; the history shows no step by the bank in between |

**Done:** `evals/score_points.py` now labels a system or an app messaging the customer as `wait`,
reads a registration only in "register … request/review/case", and catches "for your
confirmation". The same run scores **113 / 149 (76%)**; the remaining 042@3, 044@3 (an answer that
reaches the customer as the bank's own portal record) and 012@5 (a system applying a confirmed
change) are left as they are: the next event alone cannot tell them apart.

## 2. A routing bug: an enum value read as a field (046)

`route-business` is `subject in [limit, role]`. `role` is also a field (the requester's role), so
the condition compares the subject with the requester's role (`customer`) and is never true for
`subject = role`. In 046@2 no system is chosen, and the verified administrator's instruction to
revoke a role is refused.

**Done:** the policy writes the value quoted, `subject in [limit, 'role']`; the engine refuses to
load a bare word that is both a field and a value of what it is compared with, and says to quote it
(`docs/policy.md`, Conditions). Live: 046@2 now submits the administrator's instruction.

## 3. Facts the functions do not read (track/functions.py)

| Point | The record says | The reader returns | Function |
|---|---|---|---|
| 030@4 | the agent's note: "I checked the card journal… the replacement is in manufacture" | only `card_asked` | `check_card`: an agent's note that reports a system's result is an answer |
| 032@3, 032@4 | archive: "the statement is available **to order**" | `document_ready: true` | `check_documents`: "available to order" is not ready; the statement still has to be ordered |
| 036@4, 028@5 | the customer confirms **inside the protected profile-change process** | `confirmation: none` | `check_confirmation`: a confirmation given in the process the bank started counts |
| 013@5 | the customer confirmed in the portal before the bank asked; the log says the run was cancelled | `confirmation: none` | same function: a portal confirmation that the history accepts counts even without a prior bank request |
| 046@4 | "Revocation instruction processed" | `business_status: OTHER` | `check_business`: map "revocation processed" to `ROLE_REVOKED` |
| 006@4, 018@4 | two separate instructions, one completed and one pending / a standing order and a mandate | `payment_status: OTHER` | the status is right to be `OTHER`; `reply_customer` has no template for "two separate instructions" (`payment_count`), so the agent does not trust a reply |
| 039@5 | the security team limited the session extract | `access_status: OTHER` | a session extract is a document; see 4c |
| 034@4 | the agent's note: the £3.20 fee matches the tariff entry | nothing | no reader covers a tariff check (see 4d) |

## 4. Decisions and rules the policy lacks (track/policy.yaml)

**a. The bank speaks to the customer before any system answers (025@1, 030@2, 027@2).** It asks
which attempt to investigate, acknowledges and says what it will check, or directs the customer to
the secure recovery route. The policy can only reply from a system's answer. Add a decision for
this, e.g. `clarify` (ask the customer for what the check needs) and `redirect_secure` (point to the
secure process; never handle a secret) — the extreme cases expect `redirect_secure` too.

**b. Passing a request to the person with the authority (045@2–4).** A new user's access needs the
company administrator; the bank sends the request to the administrator for approval. The policy
escalates (`NO_AUTHORITY`). Add `forward_to_authority`: send to the verified holder of the
authority, approve nothing.

**c. A change through the bank's protected process (028@2, 036@2, 037).** For profile changes the
bank starts the protected change process, which sends the confirmation itself; the desk's own
`send_for_confirmation` is the same step under another name (028@2, 036@2 are close to right). 037
is a name **correction**: the bank opens a review with the data team, but triage said `change`.
**Done:** once the history shows a registration (`registration_asked`), the registration rules
apply whatever the triage said, and the change rules do not — what the bank already did outranks
the classifier. Live: 037@3 now waits for the data team. 037@2 (before any registration) is still
triaged as a change: see 5.

**d. No system for fees and tariffs (034).** `fee` is routed to `documents`, which does not hold
tariffs. Add a `tariff` check (a reader and a route) or route `fee` to `payment` with a tariff
reader. **Waiting for** the reader `check_tariff` (asked of the track functions' owner); the route
follows once its fields are fixed.

**e. Asking before changing is refused for instructions (018@2, 006@2).** The rule `<system>-ask`
excludes `request_type = instruction`, but the cases check first ("compare the instructions before
any change"). **Done:** `ask_system` is allowed for `instruction` while the system has not been
asked. Live: 018@2 now asks the payment system instead of escalating.

## 5. Triage (the classifier's questions in `triage`)

| Point | Request | Triage | Should be |
|---|---|---|---|
| 006 | "are these separate instructions?" | `register` | `status` |
| 037 | correct a typo in my name | `change` | `register` (a correction goes to the data team) |
| 018 | "remove the duplicate" | `instruction` | the first step is a check (see 4e) |

**Needs:** tune the option wording with an eval on these requests (`evals/`), and let the history
override triage (4c).

## 6. The agent's judgement (system prompt, `agent.instructions`)

| Point | Facts | The agent | Should |
|---|---|---|---|
| 042@4 | the validation report is ready (`VALIDATION_FAILED`); the requester is an authorised report viewer | escalated: "role viewer, not verified" | reply: viewing a report is what a viewer may do |
| 013@5 | the instruction log says the future run is cancelled | tried to submit again, then escalated | reply within the record |
| 006@4, 018@4 | the journal answered (`OTHER`, two instructions) | escalated or registered | reply that they are two separate instructions (needs the template in 3) |

**Needs:** the instructions should say that a system's answer of `OTHER` is still an answer to
report narrowly, and that a viewer may view; and a reply template for each of these answers, so
the reply tool is safe to use.

## Order of work

1. Fix the scoring labels (1) so the number is trustworthy.
2. Fix the routing bug (2) and add the engine's load-time check.
3. Function fixes (3) — the track functions' owner.
4. Policy: let the history outrank triage (4c), allow asking before an instruction (4e), add a
   tariff route (4d).
5. New decisions `clarify`, `redirect_secure`, `forward_to_authority` (4a, 4b) — also needed by the
   extreme cases.
6. Triage wording and the agent's instructions (5, 6), measured with evals.

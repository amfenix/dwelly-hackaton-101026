# Banking & Financial Services: analysis of the public example cases

An analysis of the 50 public example cases of the Banking & Financial Services track
([DwellyOrg/HackatonPublicCases](https://github.com/DwellyOrg/HackatonPublicCases)). They are
for development only; results are submitted for the challenge cases, not for these.

## How a case is built

- `index.md`: the initial request, an overview, **Next action at escalation** (the first step a
  person took), and the **Outcome** (what happened and what is still not established).
- `history.md`: 5–6 events, nearly always in this order:
  1. context: a portal notification, a third party's message, or a recipient's complaint;
  2. the customer's request (secure chat, verified call or portal);
  3. **internal note**: the agent asks an internal system;
  4. **internal note**: the system answers with a fact;
  5. the reply to the customer in the secure or business portal.
- A change that matters (a standing-order amount or date, a phone number) adds steps: the change is
  sent to the customer's portal, the customer confirms it there, the system records it.

## Types of request

| Group | Cases | What the bank does |
|---|---|---|
| Status of a transfer or payment | 001, 002, 003, 006, 007, 009, 010, 040, 044, 048, 050 | checks a journal, states the status |
| Why something was declined or did not run | 004, 017, 024, 025 | journal → the wording it may disclose |
| A fact from a record | 008, 011, 014, 018, 020, 029, 034, 047 | reads a field: purpose, date, mandate, limit, tariff |
| Register a request (not a decision) | 005, 016, 023, 035, 037 | opens a case with a team, gives its number, **promises no outcome** |
| A change the customer confirms | 012, 013, 015, 019, 028, 036 | sends the change to the portal; the customer confirms; the system applies it |
| An action on a verified request | 022 (block a card), 046 (an administrator revokes a role) | runs it through the protected process |
| A document or export in the portal | 031, 032, 033, 038, 039, 042, 049 | a service places the file (the attachment) in the portal |
| Access, PIN, recovery | 026, 027 | points to the secure process; never handles the secret |
| Card status | 021, 030 | the card journal |
| Business authority | 041, 043, 045 | checks the mandate; **approves nothing on a signatory's or administrator's behalf**; forwards to the administrator |

## Internal systems the agent asks

- **Journals and registers:** transfer, payment, instruction and transaction journals; the
  incoming-payment journal; the standing-order and mandate journals; the card and card-authorisation
  journals; the signing log; the import journal; the access log; the admin log; the limit register;
  the instruction register.
- **Teams and services:** payment team, Direct Debit team, card team, tariff team, data team,
  security team, access team; statements, archive, document, data and acquiring services; the
  protected instruction and profile-change processes.

## The rule of every outcome: a narrow answer

Each outcome states **only what the system showed** and names what is **not** established:

- "Sent" is not "received or credited by the recipient's bank" (001, 009, 040, 050).
- "No incoming payment found" is not "the sender did not pay" (002, 048).
- "Request registered" is not "the money will be returned" or "the fee will be refunded"
  (005, 016, 023, 035).
- "Batch processed" is not "every row was paid" (044); "file received" is not "file processed" (041).
- "Report available" is not "funds credited" (049).

## Constraints the cases hold to

- **Never act for the customer:** do not authorise a saved draft (003), approve for the second
  signatory (043), or grant a role without the administrator (045).
- **Changes only through confirmation in the secure portal,** never on a chat message or an email
  (012, 019, 028: "the earlier email was not treated as authorisation").
- **Check before changing:** two similar payments are compared first and nothing is cancelled
  (006, 018); a cancellation checks that the run has not started (013, 015).
- **Do not advise paying again** without checking for pending activity (017).
- **Never handle secrets:** PIN, password (026, 027).
- **Disclose only what is permitted:** a restriction's category, not its basis (024); the
  permitted wording of a decline (004).
- **Check authority:** a viewing mandate (047), an authorised uploader or signatory (041, 050).

## Attachments (9 cases)

`statement-031.pdf`, `statement-032.pdf`, `transactions-033.csv`, `account-confirmation-038.pdf`,
`sessions-039.txt`, `payment-record-040.pdf`, `batch-041.csv`, `validation-042.txt`,
`merchant-report-049.csv`. Almost all are what a service **produced** for the customer; only
`batch-041.csv` was uploaded by the customer.

## What it means for the policy

- The agent chooses which system to ask and about what; a function answers with the fact; the reply
  to the customer is built from that fact, not from the agent's words.
- Signals are of the kind `check(system, subject)`, `register_request(team)`,
  `send_for_confirmation(change)`, `reply` and `escalate`, with enum arguments.
- Facts include: the customer's verification and authority (verified, role, mandate), the type of
  request, the system's answer (a status and what it does not establish), and the customer's
  confirmation of a change.
- "What is not established" is a required part of every reply; a function can build it from a
  template per kind of check.
- Open question: the input format of the challenge cases (likely a history cut at a decision point,
  with the next action and a narrow answer expected). It decides how `adapt_case` reads
  `index.md` and `history.md`.

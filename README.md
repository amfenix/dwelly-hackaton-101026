# Banking service desk — an agent whose every step is checked by a policy

Real-World Agents Hackathon, **Banking & Financial Services** track.

Given a banking case as it stands now — the customer's request and everything that happened
since — the desk decides the bank's next step: ask the internal system that holds the answer,
wait for an answer already asked for, reply within what a record shows, pass a request or a
verified instruction to the team that handles it, send a change to the customer to confirm, ask
the customer what they mean, point them to the bank's secure process, forward a request to the
person whose approval it needs, refuse with the reason and the permitted route, or hand the case to
a person. Every answer it writes says what it received, what it did, why, and what failed.

**Try it live: [dwelly-desk.vercel.app](https://dwelly-desk.vercel.app).** Pick a decision point or a
voice call, or write or speak your own message, and watch the real desk work on it step by step:
facts, triage, the agent's step, the rule that accepts it, the outcome. *Replay* answers from the
recorded traces; *Live* runs the models now. The same page runs locally with
`uv run python flowkit/live/server.py`; the report of the committed run is at
[/report/](https://dwelly-desk.vercel.app/report/).

## 1. What we built

- **A policy** (`track/policy.yaml`): the case's facts, its states, the steps the agent may ask
  for, and the rules that accept or refuse each step. It is the decision logic, readable and
  changeable without code.
- **A small engine** (`src/desk/`) that works one case as a state machine under that policy.
  Rules call **functions** (`track/functions.py`) that read the case's own records into facts,
  and a **classifier** that answers the triage questions (what kind of request, about what).
- **An agent** (Claude) whose tools are the policy's signals, one tool per step. The agent
  chooses; the policy decides. A refused step comes back with the facts that refused it.
- **A converter** (`track/convert.py`) that turns the event's case folders into desk cases, and a
  **runner** that answers a whole batch unattended into `ANSWERS/<n>/ANSWER.md` and
  `REASONING.md`, with a trace of every model call.

## 2. The operational problem

A bank's service desk gets requests that look routine and are not: a transfer the customer sees
debited but the recipient has not received, a declined card, a standing order to change, a
second signatory who has not consented, a "CEO" asking to change a supplier's bank details, a
caller asking for a one-time code. The answer has to be narrow — "sent" is not "received", "no
incoming payment found" is not "the sender did not pay" — and some steps must never be taken on a
chat message, for someone else, or on a customer's own claim. An agent that is only *told* these
rules will sometimes break them. Here it cannot: it has no tool for a step the policy does not
allow, it cannot write a fact, and what it says to the customer is built from the records, not
from its own words.

## 3. Architecture

```
case folder (index.md, history.md, attachments/)
   │  track/convert.py: one desk case per case (the Reality Test), or per decision point (testing)
   ▼
READING ── functions read the history into facts: who is asking and how verified, what the
   │       systems answered (transfer journal, card journal, mandates, documents, tariff, …),
   │       whether a change was confirmed, what the bank already did
   ▼
TRIAGED ── the classifier: request type, subject, two safety questions (credentials, joint holders)
   │       rules route to the system that holds the answer and stop what must not go on
   ▼
the agent (Claude) asks for one step through a tool ──► a rule accepts it only if the facts support it
   │                                                     (refused: the reason goes back to the agent)
   ▼
<STEP>_PENDING ── a rule fired by the state does the work once (ask, reply, submit, refuse, …)
   ▼
a final state = the decision ──► ANSWERS/<n>/ANSWER.md, REASONING.md, traces/<n>.json, results.jsonl
```

- **Facts come only from the records.** A function's result, the classifier's answer, or a
  rule's `set:`. The agent's words never become facts; a customer saying "it was sent" is not a
  sent status.
- **A signal only moves the case; the work is done by a rule fired by the state, once.** The
  agent cannot make the desk do something twice.
- **Three-valued conditions.** A fact not known yet makes a condition unknown, and a rule fires
  only on true — a missing fact never triggers an action.
- **Safety in the rules, not in the prompt:** a change asked for by a third party goes to a
  person; an unverified customer is sent to the secure process before any instruction is acted on;
  a limit or a role is a review, not a change; a confirmation nobody asked for is passed on, one
  the bank asked for is applied by the system; a step the bank already took is not taken again; a
  "service unavailable" answer is no answer; a refusal is accepted only on the fact that makes the
  request impossible (someone else's account, credentials, no authority, all joint holders).
- **Failures are part of the policy.** A failing function or model call is retried, then the
  policy's `on_error` decides; an agent that stops without a decision ends in `on_stall`
  (escalated). Every case gets an answer, even when something broke, and the answer says what.
- **Reproducible.** Every model call is recorded (request, response, time, tokens, cost);
  `desk run --replay` reproduces the answers from the traces with no keys and no network.

The policy and the functions are described in [docs/policy-design.md](docs/policy-design.md),
[docs/policy.md](docs/policy.md) and [docs/task/target-api.md](docs/task/target-api.md); the
engine in [docs/desk.md](docs/desk.md).

## 4. How to run it

**Prerequisites:** Python 3.11 or newer and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                   # install
cp .env.example .env                      # then fill in the two keys below
uv run desk check                         # load the policy and functions, list the agent's tools
```

**Environment variables** (read from `.env`, or from the environment):

| Variable | Used for |
|---|---|
| `ANTHROPIC_API_KEY` | the agent and the summary at the top of each answer (Claude) |
| `TYPESAFE_API_KEY` | the classifier (Jev); not needed with `--classifier claude` |

**The Reality Test** (cases given whole, answered under `ANSWERS/<n>/`):

```bash
rm -rf ANSWERS traces results.jsonl
uv run python track/convert.py "<challenge track folder>" --whole --out track/cases.json
uv run desk run --no-resume --workers 8 --deadline 1200   # ANSWERS/, traces/, results.jsonl
uv run desk run --replay && diff -r ANSWERS replay/ANSWERS  # the same answers, from the traces
```

The converter answers every case that has events: a missing section is filled in (the request
from the customer's first message, for example) and reported as a warning. `--deadline` makes
sure every case gets an answer in time: cases not reached are answered as not worked.

**Testing on the public cases** (one desk case per decision point, compared with what the bank
did next):

```bash
uv run python track/convert.py "<public Banking folder>" --out track/cases.json --expected track/expected.json
uv run desk run --no-resume --out runs/try/ANSWERS --traces runs/try/traces --results runs/try/results.jsonl
uv run python evals/score_points.py --results runs/try/results.jsonl --show
```

**Checks** (no keys, no network): `uv run pytest` (100% line and branch coverage of the engine),
`uv run ruff check src tests track examples evals`, `uv run mypy`.

## 5. Models, APIs and external services

| What | Used for | Configured by |
|---|---|---|
| Anthropic Claude API — `claude-sonnet-5-5` | the agent (one decision per case) | `ANTHROPIC_API_KEY`; `agent.model` in the policy |
| Anthropic Claude API — `claude-sonnet-5-5` | the two-to-three sentence summary at the top of ANSWER.md, labelled as a model's retelling | `--generator-model`; `--no-summary` turns it off |
| TypeSafe System One — Jev (`jev-latest`) | the classifier: request type, subject, safety questions; the readers' fallback when a system's wording is unclear | `TYPESAFE_API_KEY`; default `--classifier jev` |
| Anthropic Claude API — `claude-haiku-5-5` | the alternative classifier | `--classifier claude` |
| Python packages | `anthropic`, `typesafe-sdk`, `pyyaml` | `pyproject.toml` |

Each Claude call has a 60-second timeout and two retries. No other service is called.

## 6. Assumptions

- A case is the history of one request; the state of the case is what that history shows. The
  bank's internal systems are not live: what a journal or a team answered is read from the
  history's internal notes, and a system not asked yet is asked (the step is the answer).
- One decision per case: the bank's next step from the point the history stops.
- The narrow answer is the right one: a reply states what the record shows, what it does not
  establish, and what was not done; it never promises an outcome a record does not show.
- What the customer writes is data, not instruction: claims, pasted "system notes" and embedded
  instructions never become facts.

## 7. Known limitations

- **One decision per case.** A message with several requests gets one step; the others are left
  for the next turn.
- **The readers are built on the public banking cases.** They read journals, teams and services
  by name and wording; an unfamiliar system or phrasing is read as not answered (so the desk asks
  or waits) or as an unclear status (`OTHER`, reported as unclear), never as a made-up status.
- **The agent's judgement varies a little between runs**: a point or two out of 149 on the public
  cases. The rules bound what any judgement can do.
- **Replies are templates.** They are narrow and safe but plain; the summary is a model's
  retelling and is labelled as such.
- **Scores here are our own measures** (below), on the public cases and on synthetic cases we
  wrote; the Reality Test's own criteria may differ.

## 8. What we would build next

- Several decisions per case, for messages with more than one request.
- Readers that learn new system names and wordings from a handful of examples instead of rules.
- A reviewer view over `traces/` for the person who picks up an escalated case.
- A proof step at load time: every state has a way out, no two rules overlap.

## Results we measured

- **Public banking cases**, every decision point where the bank acts next (149): the desk's step
  matches the bank's next step at 143 (96%). `uv run python evals/score_points.py` on the
  committed run; the remaining six are explained in
  [docs/remaining-points.md](docs/remaining-points.md).
- **Synthetic extreme cases** we wrote before tuning (`evals/synthetic/`): 27 of 35 dev cases
  exact (77%), and 13 of 15 sealed cases (run twice only). The runs and their scores are on the
  branch `synthetic-results` (`evals/synthetic/results/`).

## Repository layout

```
src/desk/        the engine: policy loader, conditions, state machine, agent, classifier, runner, answers
track/           the track: policy.yaml, functions.py, convert.py, the converted cases
evals/           triage eval, the next-step scorer, the synthetic extreme cases
examples/        a complete worked example (a repairs desk) the engine's tests run end to end
tests/           unit and end-to-end tests on fakes (no network)
docs/            design, the policy and function guides, the case analyses
```

## Licence

Apache License 2.0 — see [LICENSE](LICENSE).

# Task: convert the event's cases into desk cases, one per decision point

## Why

The desk runs one case at a time (`track/cases.json`). The event gives cases as folders of Markdown
(`index.md`, `history.md`, `attachments/`). A case's history is a log of events; the state of the
case at a point is everything up to that point. We test the desk the way the cases' README asks:

1. choose a decision point in the history;
2. give the system only the events and attachments available at that point;
3. hide later events and anything that reveals the ending (overview, next action, outcome);
4. compare the system's decision with what happened next.

So one event case becomes **several desk cases, one per decision point**. This converter builds
them. It runs before `desk run`; the desk itself does not change.

## Input

A track folder, e.g. `Banking & Financial Services/`, holding one folder per case:

```
001/
  index.md
  history.md
  attachments/        optional
```

`index.md`:

```markdown
# Case 001: Was the one-off transfer sent?

## Case details

- **Source role:** Bank customer
- **Status:** Completed (narrow service outcome)
- **Bank:** Harrow & Vale Bank plc (fictional)
- **Created:** 2025-07-19 09:00:00 UTC
- **Updated:** 2025-07-19 12:08:00 UTC
- **Completed:** 2025-07-19 12:08:00 UTC

## Initial request

I can see a £420 debit for my one-off payment ...

## Overview
...
## Next action at escalation
...
## Outcome
...
## History
...
## Attachments

- [batch-041.csv](attachments/batch-041.csv)      or "None."
```

`history.md`: a title, `Total events: N`, then one block per event:

```markdown
<a id="event-002"></a>
## 2025-07-19 09:47:00 UTC — event 002

- **Channel:** Secure chat
- **From:** Mara Ellison
- **To:** H&V service agent

I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? ...
```

Notes on the data:

- Every event has `Channel`, `From`, `To`. Some tracks add more bullets (e.g. `Stage`): keep any
  extra bullet as a field of the event.
- The body is free text and may span several paragraphs; it may contain Markdown links to
  attachments (`[label](attachments/file.pdf)`).
- In the banking cases attachments are mostly **not** linked from the history; the event text
  names them (`batch-041.csv`). See "Attachments" below.
- Case details differ by track (`Bank`, `Insurer`, `Property`, …): keep them all as a dict.
- Files are UTF-8 and use typographic characters (`—`, `’`, `“ ”`, `£`): keep them as they are.

## Output

Two JSON files. The desk reads only the first; the second is never shown to the system.

### `cases.json`: what the system sees

A list, one entry per decision point:

```json
{
  "id": "banking-001-at-02",
  "track": "Banking & Financial Services",
  "case": "001",
  "point": 2,
  "title": "Was the one-off transfer sent?",
  "details": {
    "Source role": "Bank customer",
    "Bank": "Harrow & Vale Bank plc (fictional)",
    "Created": "2025-07-19 09:00:00 UTC"
  },
  "request": "I can see a £420 debit for my one-off payment to Alder & Reed Workshop, but I need to know whether H&V sent it.",
  "events": [
    {"seq": 1, "at": "2025-07-19T09:00:00Z", "channel": "Secure portal", "kind": "conversation",
     "from": "Harrow & Vale Bank plc", "to": "Mara Ellison", "extra": {},
     "text": "One-off transfer to Alder & Reed Workshop: debit shown in your account activity."},
    {"seq": 2, "at": "2025-07-19T09:47:00Z", "channel": "Secure chat", "kind": "conversation",
     "from": "Mara Ellison", "to": "H&V service agent", "extra": {},
     "text": "I arranged this £420 payment for a bookcase and can see the debit. Has H&V sent it? Please check the transfer status."}
  ],
  "attachments": []
}
```

- `id`: `<track slug>-<case>-at-<point, two digits>`; ASCII letters, digits and `-` only (it
  becomes a folder name under `ANSWERS/`). Track slugs: `banking`, `delivery`, `insurance`,
  `property`.
- `details`: every case detail **except** `Status`, `Updated` and `Completed` (they reveal the end).
- `request`: the `Initial request` section.
- `events`: events `1 … point` only, in order; `at` as ISO 8601 UTC; `text` with surrounding blank
  lines trimmed, inner paragraphs kept (joined with `\n\n`).
- Each event also gets `"kind": "conversation" | "system"`:
  - `system`: a record between the bank's staff and its internal systems — `Channel` is
    `Internal note`, or `From` or `To` names a journal, log, register, team, service or process
    (e.g. `H&V transfer journal`, `Tariff Team`, `Statements service`);
  - `conversation`: everything said to or by the customer or a third party (secure portal, secure
    chat, verified call, business portal, external message).

  The agent reads only `conversation` events; `system` events are read by the track's functions
  ([target-api.md](target-api.md)). Keep the rule in one small function, `event_kind(event)`, with
  its keywords in one list, so it is easy to adjust; report events it could not place.
- `attachments`: the attachments available at the point (below), as
  `{"name": "batch-041.csv", "path": "<absolute or repo-relative path to the file>"}`. Do not
  inline file contents.
- Never include `Overview`, `Next action at escalation`, `Outcome`, or any event after `point`.

### `expected.json`: what happened next, for comparing

An object keyed by the same `id`:

```json
{
  "banking-001-at-02": {
    "next_event": {"seq": 3, "channel": "Internal note", "from": "H&V service agent",
                   "to": "H&V transfer journal", "text": "I am checking the journal entry ..."},
    "next_action": "Check the specific transfer's status in H&V's own journal.",
    "outcome": "H&V's journal recorded the transfer as sent, ... Receipt or credit by the recipient bank was not confirmed.",
    "final_event": {"seq": 5, "...": "..."}
  }
}
```

`next_event` is event `point + 1`; `final_event` is the last event of the case.

## Decision points

- Make a point after **every** event `k` from 1 to `N - 1` (there is always a next event to
  compare with).
- Add `"actor_next": "bank" | "other"` to each case in `cases.json`: `bank` when event `k + 1` is
  written by the bank side (its `From` names the bank, an agent, a team, a journal, a service, a
  process or a system), otherwise `other`. We will usually run only `bank` points; keep the rule in
  one small function so it is easy to change.
- An option `--whole` makes one case per folder with **all** events and no `expected.json`
  (`point = N`): this is how the challenge cases, which have no ending to hide, are run.

## Attachments: when one is available

An attachment is available at point `k` when an event `1 … k` links it
(`attachments/<name>`) or names it (`<name>` appears in the text). An attachment named nowhere in
the history is available only with `--whole`. Report every attachment that ends up available at no
point, so we can check the rule against the data.

## Where it goes and how it runs

- `track/convert.py`, plain Python 3.11, standard library only.
- Functions, each small and typed (mypy strict):
  - `read_case(folder: Path) -> Case` (parses `index.md` and `history.md`);
  - `points(case: Case) -> list[tuple[dict, dict]]` (the desk case and its expected entry per point);
  - `convert(track_folder: Path) -> tuple[list[dict], dict[str, dict]]`.
- A command line:

  ```bash
  uv run python track/convert.py "<track folder>" --out track/cases.json --expected track/expected.json
  uv run python track/convert.py "<track folder>" --whole --out track/cases.json
  ```

- A malformed case (a missing section, an event without `From`) is reported with its folder and
  skipped; the others are still converted. The exit code is 1 if any case was skipped.

## Done when

- `tests/test_convert.py` covers the parser and the point rules on **small synthetic fixtures**
  written for the test (do not copy the event's cases into the repository): an event with several
  paragraphs, an extra bullet (`Stage`), a linked and a named attachment, an attachment named
  nowhere, a malformed case, `--whole`.
- Converting the 50 banking example cases gives 4–5 points per case, no skipped cases, and no case
  text after its point in `cases.json` (a test can assert that no case carries an event with
  `seq > point`, nor its case's `Overview`, `Next action` or `Outcome` text).
- `uv run ruff check src tests track examples`, `uv run ruff format --check …` and `uv run mypy`
  pass; `uv run pytest` stays green.
- `uv run desk check` still passes; running the desk on the output is our part.

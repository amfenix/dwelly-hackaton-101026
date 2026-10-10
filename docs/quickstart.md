# Quickstart for the team

## The idea

Every case runs as a state machine whose logic is the policy, `track/policy.yaml`. The agent
(Claude) decides nothing and writes no fact: it only sends signals, which are its tools. A rule of
the policy accepts a signal and runs, or refuses it with the reason. Facts are written only by
rules: from functions (`track/functions.py`), from the classifier (`ask:`, Jev or Claude) and from
`set:`. For every case the system writes `ANSWERS/<n>/ANSWER.md` and `REASONING.md`, and records
every model call in `traces/`.

## What to edit

| What | Where |
|---|---|
| facts, states, the agent's signals, rules | `track/policy.yaml` |
| lookups and actions (a `@function`, named by a rule's `call:`) | `track/functions.py` |
| the records and the incoming cases | `track/world.json`, `track/cases.json` |
| a test for every rule you add | `tests/test_track.py` |
| the wording of classifier questions, the agent's choices | `evals/*.yaml` |

`examples/repairs/` is a complete worked example to copy patterns from; the tests run it, so
leave it as it is.

`src/desk/` is the engine: leave it alone unless the whole team agrees on the change.
How to write the policy and the functions: [policy.md](policy.md); its example loads as it is.

A function returns the facts it found and lets the policy decide; it returns `{}` when it found
nothing and raises when it failed. Anything that writes dedupes on `ctx.key`. The agent's words
are never sent out: the text is built from the records.

## Start

```bash
git clone git@github.com:amfenix/dwelly-hackaton-101026.git && cd dwelly-hackaton-101026
uv sync
cp .env.example .env        # fill in ANTHROPIC_API_KEY and TYPESAFE_API_KEY (Jev classifies)
uv run desk check           # the policy and functions load; lists the agent's tools
```

## The loop

```bash
uv run desk check           # after every policy change: says exactly what is wrong
uv run pytest               # no keys, no network; must be green
uv run desk run --no-resume --out runs/try/ANSWERS --traces runs/try/traces --results runs/try/results.jsonl
                            # a real run into runs/ (ignored by git); read REASONING.md
uv run desk eval evals/triage.yaml --models claude-haiku-5-5,jev-latest --runs 3
                            # tune the classifier's questions
uv run python evals/score_points.py --results runs/try/results.jsonl --show
                            # how many next steps match what the bank did; lists every one that differs
```

`evals/score_points.py` reads the bank's next step from the next event of each case
(`track/expected.json`) and compares it with the desk's decision; without `--results` it scores the
run at the root. [mismatch-analysis.md](mismatch-analysis.md) explains the differences of the last
committed run and what needs attention.

## The cases

`track/cases.json` holds the public banking cases, one desk case per decision point, and
`track/expected.json` what the bank did next; `track/synthetic/` holds our extreme cases
([evals/synthetic/README.md](../evals/synthetic/README.md)). Both are made by `track/convert.py`
([task](task/case-conversion.md)).

## The run at the repository root

`desk run` writes to the root by default: `ANSWERS/<id>/ANSWER.md` and `REASONING.md`, `traces/`
and `results.jsonl`. These are committed: they are what the event reads. Each run replaces them:

```bash
rm -rf ANSWERS traces results.jsonl                            # copy them elsewhere first to keep them
uv run desk run --no-resume                                    # ANSWERS/, traces/, results.jsonl
uv run desk run --replay && diff -r ANSWERS replay/ANSWERS     # the same answers, from the traces
```

- `--no-resume` works every case again; without it, a case that already has an answer is skipped
  (so a run cut short can be resumed).
- Clear the old folders first: a re-run replaces the answers of its own cases only.

## The submission run

The challenge cases are given whole, with no ending to hide: one desk case per case, answered
under `ANSWERS/<n>/`.

```bash
rm -rf ANSWERS traces results.jsonl
uv run python track/convert.py "<challenge track folder>" --whole --out track/cases.json
uv run desk run --no-resume
uv run desk run --replay && diff -r ANSWERS replay/ANSWERS
```

`.env` is ignored by git: the repository is public, and keys live only there.

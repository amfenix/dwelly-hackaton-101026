# Next-step and refusal experiment

The candidate keeps the desk's existing one-signal, one-outcome state machine. It adds no
model stage. The agent instructions distinguish the immediate step from later operations,
prefer permitted record lookups before unnecessary clarification or escalation, and preserve
pending checks and urgent protective instructions. Verified customers, signatories and admins
may check an identifiable payment/business record before choosing an approval route; this
does not approve a payment or grant access.

Refusal actions include a typed policy reason, supporting facts, the provenance of those
facts, and a permitted alternative. Classifier inferences are labelled as inferences and link
to the saved triage input; parsed roles and bank statuses link to their existing reader notes.
This is provenance, not a guarantee that the classifier interpreted the request correctly.
The action no longer invents a portal consent procedure or a company administrator for every
refusal. An unknown request type is not sufficient grounds for refusal. Third-party process
questions and mixed representation requests can go for review without disclosing account data.

The desk still selects one primary action, so this change does not solve complete handling of
multiple independent requests. A refusal may offer an alternative without executing it.

## Test the modified version

From this checkout, after installing the usual dependencies:

```bash
uv run python evals/next_step_experiment.py prepare
uv run python evals/next_step_experiment.py run --env /path/to/local.env
uv run python evals/next_step_experiment.py score
```

`prepare` and `score` make no API calls. By default, `run` executes **only the 35 candidate
cases** under `runs/evidence-next-step/candidate/`. It uses the unmodified synthetic
scorer at `b3aa612`. Both commits must exist in the local Git object store. The default dev run
excludes the 15 sealed cases. The manifest is used only for cut selection and offline scoring, never
included in classifier or agent input.

Run the 15 sealed extreme cases separately, keeping the candidate code unchanged:

```bash
uv run python evals/next_step_experiment.py run --split sealed --env /path/to/local.env
uv run python evals/next_step_experiment.py score --split sealed
```

These commands default to `runs/evidence-next-step-sealed/` and only run the candidate.
They do not rerun the 35 development cases. The current workspace has previously inspected
these cases with a different architecture, so this is the manifest's sealed subset, not an
untouched evaluation for the whole development process.

The default uses Claude for classification (Haiku 5.5), with Sonnet 5.5 for the agent and
summary, using `ANTHROPIC_API_KEY`. The published 80% run used Jev classification, so this
comparison with that saved score also includes a classifier change.
Use `--classifier jev` on both `prepare` and `run` if `TYPESAFE_API_KEY` is configured.
The original code at `db5f80f` is snapshotted offline. Running it is optional: use `--arm both`
for a paired 35 + 35 run with identical model settings, or `--arm baseline` for that arm alone.

Inputs, code, scorer and settings are pinned in `experiment.json`. A changed configuration
requires a new `--out` directory. Saved complete arms are reused; partial or failed arms require
inspection before another run. Committed root answers, traces and results are never replaced.
Missing/error results remain failures in the fixed denominator. `comparison.json` contains
the selected arms' native action scores and completion counts, plus changed cases when both
arms are selected; no manual label mapping occurs.

Check exact and safe scores, then inspect the changed answers for unsupported claims, missed
requests, premature refusal and unnecessary delay. These development cases establish a local
regression comparison, not unseen-case generalisation. The recorded development and sealed-subset results, execution evidence and limitations are
in `evals/synthetic/results/2026-10-10-next-step/SCORE.md`.

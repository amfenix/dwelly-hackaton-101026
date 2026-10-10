# Section 3 reader regressions

The reader changes cover the public banking points listed in section 3 of
`docs/mismatch-analysis.md`. They are based on main revision `1485e77`; the evaluated
reader revision is `ac751eb`.

## Regression coverage

The tests load the checked-in converter output from `track/cases.json`, rather than
reconstructing the positive examples by hand.

| Point | Required facts or reply |
|---|---|
| 030@4 | `card_asked: true`, `card_status: IN_MANUFACTURE` from the agent's checked-result note |
| 032@3, 032@4 | `document_ready: false` for a statement available to order |
| 028@5, 036@4 | `confirmation: given` within the bank-started protected profile process |
| 013@5 | `confirmation: given` for the prior portal confirmation explicitly accepted by the bank |
| 046@4 | `business_status: ROLE_REVOKED` for the processed revocation |
| 006@4, 018@4 | `payment_status: OTHER`, `payment_count: 2`, and a narrow separate-instruction reply |
| 034@4 | `tariff_asked: true`, `tariff_status: MATCHES` |

Negative regressions exclude planned or conditional process starts, questions,
negated/future confirmation, another customer's confirmation, unresolved pronouns,
mismatched references and card endpoints, and tariff questions or conditions.
Both classifier adapters also retain fake-client and recorded-replay tests.

`check_tariff` returns only `tariff_asked: bool` and
`tariff_status: enum [MATCHES, MISMATCH, OTHER]`. Safe tariff reply templates are
implemented. The tariff fields, reading trigger, route and rules still need to be
wired into `track/policy.yaml` by the policy owner; the current live policy does not
call this reader.

## Checks

- API tests: 156 passed.
- Full suite: 542 passed, 1 skipped (external public converter fixture not configured).
- All 12 readers on all 208 public points: 2,496 invocations with no errors, invalid fields, or input mutations; no classifier calls. Facts are saved locally in `runs/reader-regressions/reader-facts.json`.
- Ruff lint and Python formatting, strict mypy, `desk check`, and `git diff --check` pass.
- The repository's coverage threshold remains 100% for `src/desk`; it does not measure track-reader coverage.
- Scoped review completed after resolving the confirmation and endpoint-matching findings.

## Fresh model run

The live run uses Claude, with the default Haiku classifier and Sonnet agent and
summary generator. The local environment was copied from banking baseline at the
user's request. No credentials are committed. JEV remains covered by fake tests;
this run does not measure live JEV accuracy.

From this branch, using the repository's Python environment:

```bash
desk --env .env run --no-resume --workers 4 \
  --out runs/reader-regressions/ANSWERS \
  --traces runs/reader-regressions/traces \
  --results runs/reader-regressions/results.jsonl
python evals/score_points.py --results runs/reader-regressions/results.jsonl --show
```

The paths above are under the original workspace's `runs/` directory when running
from the isolated worktree. Full results, traces and answers remain local and are
ignored by Git.

The latest main's committed run scores **118/149 (79%)** with the same scorer.
The fresh branch run scores **120/149 (80.5%, rounded to 81%)**:

| Expected next step | Matched |
|---|---|
| Ask system | 33/39 |
| Clarify | 0/1 |
| Forward to authority | 1/1 |
| Redirect securely | 0/1 |
| Reply | 39/50 |
| Send for confirmation | 2/2 |
| Submit request | 8/10 |
| Wait | 37/45 |

All 208 distinct case points produced answers, reasoning files, traces and results.
There were zero case errors, zero recorded model-call errors and zero replayed
calls. The run recorded 1,110 Claude calls and completed in 510.8 seconds.

Compared with the committed baseline, three mismatches became matches (013@3,
030@4, 036@4), and one match became a mismatch (037@4). Two other decisions changed
while remaining mismatches (028@5, 036@5). This is a single model run, with classifier
and agent variation; the two-point score difference is not an isolated measurement
of reader changes. Reader fact regressions pass independently of those decisions.

The score still includes the policy's ordering gaps at 032@3/4 and the missing
tariff route at 034@4. Other remaining mismatches are listed in the saved score;
the scorer's labels were not changed in this branch.

Local evidence is under `runs/reader-regressions/`: `score.txt`, `score-changes.json`,
`run-metadata.json` (revision and input/source hashes), `reader-facts.json`, and the
complete answers, traces and `results.jsonl`.

An earlier run based on `c1a5b06` was stopped after a newer policy push arrived.
Its 82 completed points are preserved under `runs/reader-regressions-c1a5b06-partial/`
and are excluded from the final score.

# Task 2 validation

The banking API lives in `track/functions.py`. Its new readers use the converted case history,
not `world.json`. The original payments demo functions remain available so the existing policy
and examples continue to work. Wiring the new fields and functions into the banking policy is
the separate policy task described in `target-api.md`.

`tests/test_track_api.py` uses synthetic cases. The public examples are not repository fixtures.
For the local acceptance run, the 50 banking folders were processed by task 1's actual converter,
with one case after each event except the last and only the attachments available at that point.
The converter includes the focused portal-record fix in
[PR #3](https://github.com/amfenix/dwelly-hackaton-101026/pull/3), which targets the task 1 branch.
This labels the bank-authored structured answers in cases 042 and 044 as `system`.

The run covers 208 decision points: 2,288 reader calls, 6,656 action calls and 208 briefings.
Actions are exercised with each of the eight `next_system` values.
Returned fields are checked against the task's declared types and enums. The run also checks
that the case input is not modified, raw system-event bodies do not enter the briefing, and
representative answers are extracted after their system replies.

Validation on 10 October 2026 passed with no execution errors or representative-answer
mismatches, including the previously missed answers in 006, 010, 013, 040, 042, 043 and 044.
Case 006 returns two instructions and `OTHER`, preserving the mixed completed/pending result
instead of assigning one status to both. This is a contract and regression run, not a complete
accuracy score for all 50 cases.

Status fallback and confirmation use `ctx.classify`. Tests exercise fake Jev and Claude clients
and recorded replay; the public-case run uses a fake classifier returning `unknown`. No live
model calls or model API credentials were used, and live classification accuracy remains unverified.

The full suite passes with 442 tests, including 116 track API tests. Ruff lint and formatting,
strict mypy, and `desk check` also pass.

## Answers outside the status enums

`OTHER` preserves an unrecognized or mixed system answer as evidence without inventing a status.
These public-example answers need review if the policy needs more detailed fields:

| Case | Function | System answer describes |
|---|---|---|
| 006 | `check_payment` | Two instructions with different statuses; `payment_count` is two |
| 008 | `check_payment` | A payment purpose field, rather than an execution status |
| 018 | `check_payment` | Distinct instruction types and references |
| 026 | `check_access` | An available PIN procedure, rather than a started procedure |
| 039 | `check_access` | The scope of a session extract, rather than its delivery status |
| 046 | `check_business` | A processed revocation instruction and availability of the admin-log status |
| 047 | `check_business` | A company limit; `business_limit` is returned separately |

The corresponding evidence notes group the facts from each source event within a reader call,
including the event number, system name and original answer. `find_subject` now extracts only
amount, counterparty, reference and date; subject classification belongs to policy triage.

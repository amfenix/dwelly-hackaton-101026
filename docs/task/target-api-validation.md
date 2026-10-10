# Task 2 validation

The banking API lives in `track/functions.py`. Its new readers use the converted case history,
not `world.json`. The original payments demo functions remain available so the existing policy
and examples continue to work. Wiring the new fields and functions into the banking policy is
the separate policy task described in `target-api.md`.

`tests/test_track_api.py` uses synthetic cases. The public examples are not repository fixtures.
For the local acceptance run, the 50 banking folders were parsed into the converter's input
format in memory, with one case after each event except the last. Only internal-note events
were marked `system`; each point received only the attachments named by its visible events.
This exercises the API independently of the separate converter task.

The run covers 208 decision points: 2,288 reader calls, 832 action calls and 208 briefings.
Returned fields are checked against the task's declared types and enums. The run also checks
that the case input is not modified, raw system-event bodies do not enter the briefing, and
representative answers are extracted after their system replies.

Validation on 10 October 2026 passed with no execution errors or representative-answer
mismatches. All 407 tests passed, including 81 API tests; core coverage remains 100%.
Ruff lint and formatting, strict mypy, and `desk check` passed. Review findings were fixed and
their regression tests passed. No model calls or API credentials were used.

## Answers outside the status enums

`OTHER` preserves an unrecognized system answer as evidence without inventing a status.
These public-example answers need review if the policy needs more detailed fields:

| Case | Function | System answer describes |
|---|---|---|
| 008 | `check_payment` | A payment purpose field, rather than an execution status |
| 018 | `check_payment` | Distinct instruction types and references |
| 026 | `check_access` | An available PIN procedure, rather than a started procedure |
| 039 | `check_access` | The scope of a session extract, rather than its delivery status |
| 046 | `check_business` | A processed revocation instruction and availability of the admin-log status |
| 047 | `check_business` | A company limit; `business_limit` is returned separately |

The corresponding evidence notes include the event number, system name and original answer.

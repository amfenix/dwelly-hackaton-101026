# 433ventures — Dwelly Hackathon Report

433ventures is the team behind this interactive report for the Dwelly Hackathon.

Editable Flowkit project: `desk-results.json`.

Open the canvas at http://127.0.0.1:5190/?project=desk-results while Flowkit is running.
The portable `viewer.html` includes the full design and its four connected screens.
For the browsable web UI, open `preview/screens/results@desktop.html`.
The page adapts to the browser width; the export index also links to dedicated mobile previews.

## Report chapters

- **Overview**: an editorial cover, four outcome metrics, a distribution chart, and a filterable casebook.
- **Human judgment**: three policy boundaries with expandable reviewer next steps.
- **Inside a decision**: Ben Hart's request, recorded facts, illustrative policy path, and expandable governing rule.
- **Policy explorer**: the six-state journey, all eight rules with exact conditions,
  seven typed facts, two agent signals, retries and fallbacks, and the actual policy YAML.
  Rules can be filtered by automatic execution or agent signal and expanded individually.
  The explorer is a read-only snapshot of `track/policy.yaml`, not an editor or simulator;
  refresh it when the policy changes.

The report uses an ink-green, cream, and lime palette, editorial serif headlines,
oversized figures, and chapter navigation. Native radio filters and details/summary
disclosures work without JavaScript. The overview includes an expandable methodology.

The shared component registry includes the report shell, masthead, cover, headings, badges,
metric cards, case table, distribution chart, and evidence note. Colors, spacing,
and type use tokens. Visible copy is stored in the English translation catalog.
Desktop and mobile layouts are included; light is the default theme.

## The report on real runs

`build_report.py` writes the same design from our actual runs into `report/` (static pages, no
JavaScript, no server):

```sh
uv run python flowkit/build_report.py                 # root run + runs/synthetic-dev if present
open flowkit/report/index.html
```

- **Overview**: decision points of the committed run (`results.jsonl`, `ANSWERS/`), how many match the
  bank's next step (`evals/score_points.py`), the outcome mix, and a filterable casebook.
- **Human judgment**: every handoff, with the agent's own escalation note (from `REASONING.md`)
  and what the bank actually did next.
- **Unseen cases**: the synthetic run scored against `evals/synthetic/banking/manifest.yaml`
  (`evals/synthetic/score.py`), with unsafe outcomes called out.
- **A review page per decision point**: what the desk saw, the established facts and their
  sources, actions and reply text, the governing rule, the decision trail, and the comparison.
- **Policy explorer**: generated from the current `track/policy.yaml`.

Rebuild after every run or policy change. The `preview/` folder below is the original design
export with sample data.

## Sample data and integration

This is a UI prototype, not a connected results application. There was no saved
`results.jsonl` or trace output in the repository when it was designed.
Names, amounts, and limits come from `track/cases.json` and `track/world.json`.
Outcomes are illustrative expectations under `track/policy.yaml`, assuming payment
classification and a successful permitted action in case 1. No model run or payment
was performed. Only case 2 has a detailed review screen; other handoff cards link
to that explicitly labeled review example.

To connect real results, map `RunResult.to_line()` to the overview and handoffs;
use `RunResult.to_trace()` for case facts, actions, failures, and the decision journal.
Do not treat an escalation as an execution failure: the output has a separate error field.

## Refresh the preview

Export the `results`, `handoffs`, `case-review`, and `policy-explorer` screens through Flowkit's
`export_html` tool into this folder's `preview` directory, with the light theme
and desktop/mobile viewports. Then run:

```sh
python3 flowkit/prepare_preview.py
```

This converts in-screen hash links to neighboring exported pages and replaces fixed
viewport metadata with device-width metadata. Export `viewer.html` separately via
Flowkit's `export_viewer` with `full: true` for the portable canvas.

Validation: Flowkit reported no problems, and all four screens were visually
inspected at desktop and mobile sizes. Browser checks confirmed the acted and
handoff filters and the methodology disclosure with keyboard interaction.

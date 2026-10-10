# The live desk playground (with voice)

Proposed and built by KaushikKC. Status: agreed with the team, with two changes from review (below);
built on branch `kaushik/live-desk`.

## The idea in one line

A **playground** where anyone picks, writes, speaks or simulates a call to the banking desk and
**watches the real desk work on it live**: facts, triage, policy, Claude's decision, the policy's
check and the final outcome, step by step as they happen.

## Decisions from review

1. **A separate dataset for voice.** Every call comes in on an unsafe channel: the bank doesn't
   know who is speaking. So voice never reuses the public cases (portal, secure chat, verified
   calls). It has its own 24 calls, `evals/voice/banking/calls.yaml`, each with the expected next
   action and what must not happen ([evals/voice/README.md](../../evals/voice/README.md)).
2. **Stateless.** The server keeps nothing between requests. Each run gets the whole case and
   returns the whole outcome, the spoken answer included, in one stream. A call is one message:
   it never continues an earlier call, and no case state is saved.

## Why

The report (`flowkit/report/`) shows what the desk decided on recorded runs. It is an
observatory: it shows results, but nobody can try the desk. For the demo, and for us while
tuning, we want to give the desk a case and see it run:

- judges can try their own cases, including tricky ones ("here's my PIN, reset my password");
- we can watch a refusal happen live: Claude proposes a step, a rule says no, and Claude tries again;
- it shows that the desk is a running system, not a set of pre-made pages.

## What it looks like

A fifth chapter of the report, **05 Live desk**, in the same design. It has two panels.

**Left, the case (input):**

| Input | How |
|---|---|
| **Speak** | tap the mic and speak as a caller: the words become **one message on an `Unverified call`**, and the desk runs live |
| **Simulate a call** | pick one of the 24 dataset calls → **▶ Simulate**: the caller's words are read aloud in a caller's voice, the desk runs live, and the answer is spoken |
| **Pick** (text only) | any of the 208 decision points from `track/cases.json`; never used for voice |
| **Write** | a blank case: the request, plus "+ Customer writes", "+ Bank asks a system" and "+ System answers" |

Every event can be edited or removed before running. For example: take case 001 at point 02,
press "+ System answers: Transfer status: SENT", run it again, and the decision changes from
*ask a system* to *reply*.

**Right, the desk at work (output, streaming):**

- **A pipeline strip:** Facts → Triage → Policy → Agent → Check → Decision, with the active stage lit.
- **A facts board:** each fact appears as it is found, tagged by its source (function, classifier or policy).
- **A live feed of cards:**
  - **functions:** what each one read from the records, with the evidence line;
  - **classifier:** Claude Haiku labels the request, for example `request_type = status`;
  - **policy rules:** which rule fired, with each condition ✓;
  - **agent:** Claude Sonnet's own words and the tool it called, for example `ask_system(system: payment)`;
  - **check:** ✓ accepted by rule `payment-ask`, or ✗ refused with the reason;
  - **action:** what was done, and for a reply the text, written from the facts and not by Claude.
- **The decision card:** the outcome, the reply text, time and cost, and a comparison: with what
  the bank did next (public points), or with the dataset's expected action and its "must not"
  list (voice calls). On a voice run, the spoken answer plays.

## Run modes

| Mode | Claude's answers | Needs | Use |
|---|---|---|---|
| **Replay** | from the recorded run (`traces/`) | nothing: no key, no network, no cost | public points as they are; safe for a demo with bad Wi-Fi |
| **Live** | Claude answers now | `ANTHROPIC_API_KEY` in `.env` | edited cases, cases of your own, **every voice call** |

Both run the **same engine, policy and functions** as `desk run`. Replay re-runs the case
through the real engine and only answers the model calls from the recording.

## Voice: how it fits

The desk itself does not change. Voice is only a new way in and a new way out:

```
speak ──► ElevenLabs speech-to-text ──► one message on an Unverified call ──► the desk (unchanged)
                                                                                   │
spoken answer ◄── ElevenLabs text-to-speech ◄── the outcome, in the same stream ◄──┘
```

**Safety rules that hold:**

- **A call is never verified.** The channel is `Unverified call`, so the bank's rules on
  verification and authority still apply. A caller saying "I'm the admin" approves nothing.
- **Only the run's own outcome is spoken:** the reply a rule accepted (written by a function from
  the facts), or a fixed line we wrote per outcome. Claude's own words are never read out, and the
  page cannot send text of its own to be spoken. The caller's voice reads only dataset text.
- **The keys stay on the server,** in `.env` (ignored by git): `ANTHROPIC_API_KEY`,
  `ELEVENLABS_API_KEY`. The page never sees them.
- **Live only.** Voice calls always run live, never from a recording.

| Piece | We use |
|---|---|
| Claude (classifier, agent) | Anthropic API: Haiku classifies, Sonnet decides |
| Speech-to-text | ElevenLabs `scribe_v2` |
| Text-to-speech | ElevenLabs `eleven_flash_v2_5`: the bank speaks as "Alice" (British); the simulated caller as "George" |

A real phone number (a telephony provider in front of the same server) stays optional and is not built.

## What exists (branch `kaushik/live-desk`)

- `flowkit/live/server.py`: the stateless server (Python standard library + PyYAML). It runs one
  case through the real desk, streams every journal entry and model call, and speaks the outcome.
  The engine (`src/desk/`) is not changed.
- `flowkit/live/index.html`: the page, in the report's design, at `http://127.0.0.1:8770/live/`.
  It also serves the report at `/report/`.
- `evals/voice/`: the 24-call dataset, `build.py` → `track/voice/cases.json` and `expected.json`.
- **Replay coverage:** 175 of the 208 public points replay cleanly. The other 33 were recorded
  under an earlier policy, so they need live mode, or a fresh `desk run` to re-record them.
- **Voice baseline:** the current policy matches **5 of 24** calls. It is safe on secrets and
  attacks (it hands them to a person), but it starts account checks for unknown callers. The
  gaps and the fixes they need are in [evals/voice/README.md](../../evals/voice/README.md).

Run it: `uv run python flowkit/live/server.py`, then open `http://127.0.0.1:8770/live/`.

## Questions for the team

1. Should `build_report.py` link to **05 Live desk** from the other chapters?
2. Policy and functions owners: the four fixes in `evals/voice/README.md` (the `Unverified call`
   channel, a safety rule before routing, `refuse` and `redirect_secure`, fraud in progress first).
3. Should we re-run `desk run` on the current policy so all 208 public points replay?

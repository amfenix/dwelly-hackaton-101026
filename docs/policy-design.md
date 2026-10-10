# Policy design: the banking track

How `track/policy.yaml` decides what to do next in a banking case. It builds on the two tasks:
[case conversion](task/case-conversion.md) gives one desk case per decision point, and
[the track's functions](task/target-api.md) read that case's records into facts. The patterns it
follows come from [the analysis of the example cases](cases-analysis.md).

## Principles

- **One decision point is one case.** The input is a case's details, its request, events `1 … k`
  and the attachments available then. The answer is what to do next at that point.
- **Doing nothing is a decision.** A history can be cut anywhere; when the bank has asked a system
  and the answer is not in yet, the right answer is to wait.
- **Facts come from the records.** Functions read the `system` events (what journals, teams and
  services answered) into fields. The customer saying "it was sent" is not a fact.
- **The agent decides, the policy checks.** The agent reads the conversation and the facts and
  sends the decision as a signal. A rule accepts it only when the facts support it.
- **A signal only moves the case.** A rule with `on:` does `set:` and `to:` only; the work (asking
  a system, replying) is done by a rule with no `on:`, fired by the state, once. The agent cannot
  make the desk do something twice.
- **Explicit rules.** One rule per system and situation, even when that makes the policy long:
  every decision is readable in REASONING.md as the rule that fired and the facts it saw.

## States

```
NEW ──► READING ──► TRIAGED ──► <decision>_PENDING ──► final state
        functions    classifier    agent's signal,      a rule with no on:
        read the     asks the      or a rule            calls the action
        history      request type                       function
```

| Final state | Outcome | When |
|---|---|---|
| `ASKED` | `ask_system` | the answer the decision needs is not in the history yet: ask the system that holds it |
| `WAITING` | `wait` | the system was asked and has not answered yet |
| `REPLIED` | `reply` | the answer is in: reply to the customer within it |
| `REQUESTED` | `submit_request` | pass a request to a team or system: a review, or the customer's own verified instruction |
| `CONFIRMATION_SENT` | `send_for_confirmation` | a change was asked for in chat, by email or by call: send it to the secure portal for the customer to confirm |
| `ESCALATED` | `escalate` | no authority, a secret asked for, facts that conflict, a request the desk cannot place |

## Reading the history

In `READING`, one rule per function, each with no `to:`: a rule with no `on:` fires once per visit
to a state, so they run in order, and the last one moves the case on.

```yaml
- { name: read-requester,    when: "state = READING", call: identify_requester }
- { name: read-subject,      when: "state = READING", call: find_subject }
- { name: read-payment,      when: "state = READING", call: check_payment }
- { name: read-incoming,     when: "state = READING", call: check_incoming }
- { name: read-recurring,    when: "state = READING", call: check_recurring }
- { name: read-card,         when: "state = READING", call: check_card }
- { name: read-access,       when: "state = READING", call: check_access }
- { name: read-business,     when: "state = READING", call: check_business }
- { name: read-documents,    when: "state = READING", call: check_documents }
- { name: read-registration, when: "state = READING", call: check_registration }
- { name: read-confirmation, when: "state = READING", call: check_confirmation }
- name: triage
  when: "state = READING"
  ask:
    request_type:
      choice: "What does the customer want from the bank now?"
      options:
        status: the stage or status of a payment, card, file or request
        reason: why something was declined, restricted or did not run
        record_fact: a detail from a record (a date, a purpose, a limit, a fee, a mandate)
        register: a dispute, a review or a return to be looked into
        change: a change to a payment instruction, a mandate or the profile
        instruction: an instruction to act now (block a card, cancel, revoke a role)
        document: a statement, an export, a report or a confirmation in the portal
        access: signing in, a PIN, a device, the sessions on the profile
        authority: something only another person may approve (a signatory, an administrator)
  to: TRIAGED
```

## Safety rules: first, before the agent

```yaml
- name: no-authority           # 043, 045: nothing approved for a signatory or an administrator
  when: "state = TRIAGED and request_type = authority and role != business_admin"
  set: { reason: NO_AUTHORITY }
  to: ESCALATED
- name: secrets                # 026, 027: PIN and password only through the secure process
  when: "state = TRIAGED and request_type = access"
  set: { next_system: access }
  to: REPLY_PENDING            # the reply names the secure route, never a secret
- name: change-needs-confirmation   # 012, 019, 028: a chat or an email is not an authorisation
  when: "state = TRIAGED and request_type = change and confirmation = none"
  to: CONFIRM_PENDING
- name: change-waits-for-the-customer
  when: "state = TRIAGED and request_type = change and confirmation = requested"
  to: WAITING
```

## Routing: which system holds the answer

A system the bank already asked (`<check>_asked`) is the one that holds the answer; otherwise the
subject decides; with neither, the agent names the system in `ask_system` and that rule sets
`next_system`. Each routing rule applies only while `next_system` is absent. `set:` takes
constants, so one rule per family:

```yaml
- { name: route-payment,   when: "state = TRIAGED and subject in [transfer, batch, payment_package]", set: { next_system: payment } }
- { name: route-incoming,  when: "state = TRIAGED and subject = incoming_payment",                    set: { next_system: incoming } }
- { name: route-recurring, when: "state = TRIAGED and subject in [standing_order, direct_debit]",     set: { next_system: recurring } }
- { name: route-card,      when: "state = TRIAGED and subject in [card, card_payment]",               set: { next_system: card } }
- { name: route-business,  when: "state = TRIAGED and subject in [limit, role]",                      set: { next_system: business } }
- { name: route-documents, when: "state = TRIAGED and subject in [statement, document]",              set: { next_system: documents } }
```

## Deciding: three rules per system

For each system, the same three rules. Waiting needs no agent; asking and replying are the agent's
call, checked against the facts.

```yaml
- name: payment-wait           # asked, not answered: nothing to do but wait
  when: "state = TRIAGED and next_system = payment and payment_asked and payment_status absent"
  to: WAITING
- name: payment-ask
  on: ask_system
  when: "state = TRIAGED and next_system = payment and args.system = payment and payment_asked absent"
  to: ASK_PENDING
- name: payment-reply
  on: reply
  when: "state = TRIAGED and next_system = payment and payment_status present"
  to: REPLY_PENDING
```

Then the work, once, by state:

```yaml
- { name: do-ask,     when: "state = ASK_PENDING",     call: ask_system,            to: ASKED }
- { name: do-reply,   when: "state = REPLY_PENDING",   call: reply_customer,        to: REPLIED }
- { name: do-request, when: "state = REQUEST_PENDING", call: register_request,      to: REQUESTED }
- { name: do-confirm, when: "state = CONFIRM_PENDING", call: send_for_confirmation, to: CONFIRMATION_SENT }
```

## Requests to a team or system (one decision)

The cases treat two things alike: a **review** a team is asked to open (005, 016, 023, 035, 037),
and the customer's own **instruction** passed to the system that carries it out (013, 015, 022,
046). In both the bank records and forwards; it neither decides the review nor acts on its own
authority:

- 022: "I have submitted the verified instruction to block Mara Ellison's missing card";
- 046: "I am submitting the verified administrator's instruction to revoke … The administrator's
  mandate and the role to be removed have been checked";
- 013: "I checked that Elodie Mercer has authority over this instruction and that its next run has
  not started. I am submitting her secure-portal cancellation confirmation";
- 015: "This submission records her instruction; I am not authorising it on her behalf".

So both end in `REQUESTED`. What differs is what must hold first:

| Kind | Must hold | Cases |
|---|---|---|
| review | the customer is identified | 005, 016, 023, 035, 037 |
| instruction | `verified`, and the requester's authority (`role`) over what is changed; a cancellation of a future run also needs that it has not started (or says it cannot be ruled out) | 013, 015, 022, 046 |

The answer says which: "submitted for review" or "your instruction was submitted", and never that
the review succeeded or that the system carried it out, until a later point shows it.

## The agent

The agent gets the request and the `conversation` events (never the `system` events), the facts so
far, and one tool per signal: `ask_system(system)`, `reply`, `submit_request`,
`send_for_confirmation`, `escalate(note)`. It decides **from the facts** what the bank does next.

The system prompt describes the desk rather than commanding the agent: what each decision means,
when the cases took it, and what the bank never does (act for a customer, approve for someone
else, handle a secret, claim more than a record shows). A refused signal comes back with the facts
that refused it; an agent that stops without a decision ends in `on_stall` (`ESCALATED`).

## Fields the policy owns

On top of the functions' fields ([target-api.md](task/target-api.md)):

| Field | Type | Set by |
|---|---|---|
| `request_type` | enum (the triage options) | the classifier |
| `next_system` | enum `payment, incoming, recurring, card, access, business, documents, registration` | the routing rules |
| `reason` | enum `NO_AUTHORITY, CONFLICT, UNCLEAR, AGENT_ESCALATED, ACTION_FAILED, NOT_HANDLED` | the rules that escalate |

## Testing it

Every example case is converted at every point; each point's expected decision comes from the next
event and the outcome ([case-conversion.md](task/case-conversion.md), `expected.json`). The
comparison:

- the decision (final state) and, for `ask_system`, the system: exact;
- the reply's "established" and "not established" statements: by meaning, in an eval.

## Open

- The exact list of `request_type` options and their wording, tuned with an eval on the examples.
- Whether `WAITING` is also right at points after the customer was sent something to confirm, for
  every kind of change.

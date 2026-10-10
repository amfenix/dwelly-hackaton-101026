# Case banking-039-at-05: Permitted sign-in list for my profile

**Decision: escalate**  (final state `ESCALATED`)

## Summary

Nerys Wren, a verified customer on the secure portal, asked for a permitted extract of the sign-in sessions on her profile, after reporting an unusual new-device sign-in. The desk could not release it: the access check came back as "OTHER", so it did not establish what could be shared, the attempt to submit the request was refused because this is a document request and not an instruction or change, and no tool available could produce or deliver the extract. The case was escalated, and nothing has been sent to her; a person still has to decide what session information can be released, deliver it through the portal, and consider whether the sign-in needs a security review.

_Written by a model from the record below; the sections below are the record._

## What the system received

- Source role: Bank customer
- Bank: Harrow & Vale Bank plc (fictional)
- Created: 2025-10-03 09:00:00 UTC

The request:

> I noticed an unusual sign-in notification for my H&V profile and want a permitted list of the sign-in sessions shown for it.

What happened up to now:

1. 2025-10-03T09:00:00Z · Secure portal — H&V app → Nerys Wren

> I generated a sign-in notification for a new device on 11 July 2025 at 08:42 UTC.

2. 2025-10-03T09:47:00Z · Verified call — Nerys Wren → H&V service agent

> After you completed the bank identification checks, I explained that the new-device notification looked unusual and asked for a list of sign-in sessions for my profile. I did not provide or ask you to record any secrets.

3. 2025-10-03T10:34:00Z · Secure portal — Nerys Wren → H&V Bank

> I confirm that I want the permitted session extract for my profile delivered through this secure portal.

4. 2025-10-03T11:21:00Z · Internal note — H&V service agent → H&V security team

> I’m escalating case HV-039 and requesting the permitted session extract for Nerys Wren’s profile. Please determine the allowed scope and exclude internal detection details and anyone else’s data.

5. 2025-10-03T12:08:00Z · Internal note — H&V security team → H&V service agent

> I’ve limited the extract to the permitted session details and withheld device and network identifiers. The origin of the new session is not determined.

Attachments: none.

Case reference: id banking-039-at-05, track Banking & Financial Services, case 039, point 5, actor_next bank.

## Actions taken

- none

## Decision and why

How the case moved:

- `READING` → `TRIAGED`: rule `triage`.
  - state = READING → true (state=READING)
- `TRIAGED` → `ESCALATED`: the agent asked for `escalate`, rule `agent-escalates` accepted it.
  - state = TRIAGED → true (state=TRIAGED)

Facts established:

- requester: **Nerys Wren**
- role: **customer**
- channel: **secure_portal**
- verified: **True**
- subject: **access**
- access_asked: **True**
- access_status: **OTHER**
- confirmation: **none**
- instructed_outside_portal: **False**
- request_type: **document**
- next_system: **access**
- reason: **AGENT_ESCALATED**

Where they came from:

- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: requester='Nerys Wren', role='customer', channel='secure_portal', verified=True]
- event 4 (H&V security team): I’m escalating case HV-039 and requesting the permitted session extract for Nerys Wren’s profile. Please determine the allowed scope and exclude internal detection details and anyone else’s data. [facts: access_asked=True]
- event 5 (H&V security team): I’ve limited the extract to the permitted session details and withheld device and network identifiers. The origin of the new session is not determined. [facts: access_status='OTHER']
- event 3 (Nerys Wren): I confirm that I want the permitted session extract for my profile delivered through this secure portal. [facts: confirmation='none', instructed_outside_portal=False]

## Escalated

Yes: the case ended as **escalate** in `ESCALATED`.
A person picking this up has the facts above, the actions already taken, and the step-by-step record in REASONING.md.

## What failed

- nothing

Requests the policy refused:

- `submit_request`: register: request_type = register is false (request_type=document); payment-instruction: next_system = payment is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); incoming-instruction: next_system = incoming is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); recurring-instruction: next_system = recurring is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); card-instruction: next_system = card is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); access-instruction: access_asked absent is false (access_asked=True); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); business-instruction: next_system = business is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none); documents-instruction: next_system = documents is false (next_system=access); request_type = instruction is false (request_type=document); request_type = change is false (request_type=document); confirmation = given is false (confirmation=none)

## Final result

escalate (ESCALATED)

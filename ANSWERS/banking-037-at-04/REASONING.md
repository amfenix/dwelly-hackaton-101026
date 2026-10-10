# Case banking-037-at-04: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-037-at-04:read-requester:1).
4. Note from `read-requester`: event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: requester='Elowen Marr', role='customer', channel='verified_call', verified=True]
5. `identify_requester` found {"requester": "Elowen Marr", "role": "customer", "channel": "verified_call", "verified": true}.
6. `requester`: not known → Elowen Marr (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. `channel`: not known → verified_call (by `read-requester`).
9. `verified`: not known → True (by `read-requester`).
10. Rule `read-subject` fired: state = READING → true (state=READING).
11. Called `find_subject` (attempt 1, key banking-037-at-04:read-subject:2).
12. `find_subject` found {}.
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key banking-037-at-04:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key banking-037-at-04:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key banking-037-at-04:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key banking-037-at-04:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key banking-037-at-04:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key banking-037-at-04:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key banking-037-at-04:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key banking-037-at-04:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key banking-037-at-04:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key banking-037-at-04:read-registration:12).
42. Note from `read-registration`: event 3 (H&V data team): I have opened the protected name review and referred HV-037 for checking under procedure. The customer has requested a spelling correction; please determine what supporting information is required. No profile change has been made. [facts: registration_asked=True]
43. Note from `read-registration`: event 4 (H&V data team): I have logged HV-037 as received for review. The basis for the correction has not yet been validated, and the profile name remains unchanged. [facts: registered=True, registration_ref='HV-037']
44. `check_registration` found {"registration_asked": true, "registered": true, "registration_ref": "HV-037"}.
45. `registration_asked`: not known → True (by `read-registration`).
46. `registered`: not known → True (by `read-registration`).
47. `registration_ref`: not known → HV-037 (by `read-registration`).
48. Rule `read-confirmation` fired: state = READING → true (state=READING).
49. Called `check_confirmation` (attempt 1, key banking-037-at-04:read-confirmation:13).
50. Note from `read-confirmation`: event 2 (Elowen Marr): After completing H&V’s identification checks, I explained that my profile shows “Elowen Mar” but my correct name is “Elowen Marr”. Please escalate a correction request; I understand the data team may ask for supporting information. [facts: confirmation='none', instructed_outside_portal=False]
51. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
52. `confirmation`: not known → none (by `read-confirmation`).
53. `instructed_outside_portal`: not known → False (by `read-confirmation`).
54. Rule `triage` fired: state = READING → true (state=READING).
55. Classifier (jev jev-latest) on `request_type`: change, confidence 0.45 → change.
56. Classifier (jev jev-latest) on `subject`: profile, confidence 1.00 → profile.
57. `request_type`: not known → change (by `triage`).
58. `subject`: not known → profile (by `triage`).
59. State `READING` → `TRIAGED` (by `triage`).
60. Rule `route-access` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [access, profile] → true (subject=profile).
61. `next_system`: not known → access (by `route-access`).
62. The agent asked for `submit_request` {}.
63. Refused `submit_request` in `TRIAGED`: register: request_type = register is false (request_type=change); registration_asked absent is false (registration_asked=True); payment-instruction: next_system = payment is false (next_system=access); request_type = instruction is false (request_type=change); incoming-instruction: next_system = incoming is false (next_system=access); request_type = instruction is false (request_type=change); recurring-instruction: next_system = recurring is false (next_system=access); request_type = instruction is false (request_type=change); card-instruction: next_system = card is false (next_system=access); request_type = instruction is false (request_type=change); access-instruction: request_type = instruction is false (request_type=change); business-instruction: next_system = business is false (next_system=access); request_type = instruction is false (request_type=change); documents-instruction: next_system = documents is false (next_system=access); request_type = instruction is false (request_type=change).
64. The agent asked for `ask_system` {"system": "access"}.
65. Refused `ask_system` in `TRIAGED`: payment-ask: args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change).
66. The agent asked for `escalate` {"note": "Verified caller (verified call, ID checks completed) asks to correct the name on their H&V profile from \"Elowen Mar\" to \"Elowen Marr\". The request was already registered as HV-037. The request is a change type, so a standard submit or system lookup was refused. Please pass it to the data team for a name correction. The customer knows supporting documents may be requested. No change has been made and nothing is confirmed to the customer yet."}.
67. Rule `agent-escalates` (on `escalate`) fired: state = TRIAGED → true (state=TRIAGED).
68. `reason`: not known → AGENT_ESCALATED (by `agent-escalates`).
69. State `TRIAGED` → `ESCALATED` (by `agent-escalates`).
70. The case closed in `ESCALATED`: **escalate**.

## Model calls

5 calls, 11016 tokens in, 858 out, 8.421 s, cost $0.0268; models: claude-sonnet-5-5, jev-1.13.0.

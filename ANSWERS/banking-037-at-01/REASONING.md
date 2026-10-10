# Case banking-037-at-01: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-037-at-01:read-requester:1).
4. `identify_requester` found {}.
5. Rule `read-subject` fired: state = READING → true (state=READING).
6. Called `find_subject` (attempt 1, key banking-037-at-01:read-subject:2).
7. `find_subject` found {}.
8. Rule `read-payment` fired: state = READING → true (state=READING).
9. Called `check_payment` (attempt 1, key banking-037-at-01:read-payment:3).
10. `check_payment` found {}.
11. Rule `read-incoming` fired: state = READING → true (state=READING).
12. Called `check_incoming` (attempt 1, key banking-037-at-01:read-incoming:4).
13. `check_incoming` found {}.
14. Rule `read-recurring` fired: state = READING → true (state=READING).
15. Called `check_recurring` (attempt 1, key banking-037-at-01:read-recurring:5).
16. `check_recurring` found {}.
17. Rule `read-card` fired: state = READING → true (state=READING).
18. Called `check_card` (attempt 1, key banking-037-at-01:read-card:6).
19. `check_card` found {}.
20. Rule `read-access` fired: state = READING → true (state=READING).
21. Called `check_access` (attempt 1, key banking-037-at-01:read-access:7).
22. `check_access` found {}.
23. Rule `read-business` fired: state = READING → true (state=READING).
24. Called `check_business` (attempt 1, key banking-037-at-01:read-business:8).
25. `check_business` found {}.
26. Rule `read-documents` fired: state = READING → true (state=READING).
27. Called `check_documents` (attempt 1, key banking-037-at-01:read-documents:9).
28. `check_documents` found {}.
29. Rule `read-tariff` fired: state = READING → true (state=READING).
30. Called `check_tariff` (attempt 1, key banking-037-at-01:read-tariff:10).
31. `check_tariff` found {}.
32. Rule `read-bank-actions` fired: state = READING → true (state=READING).
33. Called `check_bank_actions` (attempt 1, key banking-037-at-01:read-bank-actions:11).
34. `check_bank_actions` found {}.
35. Rule `read-registration` fired: state = READING → true (state=READING).
36. Called `check_registration` (attempt 1, key banking-037-at-01:read-registration:12).
37. `check_registration` found {}.
38. Rule `read-confirmation` fired: state = READING → true (state=READING).
39. Called `check_confirmation` (attempt 1, key banking-037-at-01:read-confirmation:13).
40. `check_confirmation` found {}.
41. Rule `triage` fired: state = READING → true (state=READING).
42. Classifier (jev jev-latest) on `request_type`: change, confidence 0.46 → change.
43. Classifier (jev jev-latest) on `credentials_requested`: 0.01 → False.
44. Classifier (jev jev-latest) on `joint_holder_change`: 0.05 → False.
45. Classifier (jev jev-latest) on `subject`: profile, confidence 1.00 → profile.
46. `request_type`: not known → change (by `triage`).
47. `credentials_requested`: not known → False (by `triage`).
48. `joint_holder_change`: not known → False (by `triage`).
49. `subject`: not known → profile (by `triage`).
50. State `READING` → `TRIAGED` (by `triage`).
51. Rule `route-access` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [access, profile] → true (subject=profile).
52. `next_system`: not known → access (by `route-access`).
53. The agent asked for `ask_system` {"system": "access"}.
54. Refused `ask_system` in `TRIAGED`: payment-ask: args.system = payment is false (args.system=access); next_system = payment is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=access); next_system = incoming is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: args.system = recurring is false (args.system=access); next_system = recurring is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=access); next_system = card is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=access); next_system = business is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=access); next_system = documents is false (next_system=access); next_system absent is false (next_system=access); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: args.system = tariff is false (args.system=access); next_system = tariff is false (next_system=access); next_system absent is false (next_system=access); request_type not in [register, change, authority] is false (request_type=change).
55. The agent asked for `submit_request` {}.
56. Refused `submit_request` in `TRIAGED`: register: request_type = register is false (request_type=change); register-what-fits-no-type: request_type = other is false (request_type=change); payment-instruction: next_system = payment is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); incoming-instruction: next_system = incoming is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); recurring-instruction: next_system = recurring is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); card-instruction: next_system = card is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); access-instruction: verified is not known (verified=not known); request_type = instruction is false (request_type=change); business-instruction: next_system = business is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change); documents-instruction: next_system = documents is false (next_system=access); verified is not known (verified=not known); request_type = instruction is false (request_type=change).
57. The agent asked for `escalate` {"note": "Customer asks to correct the profile name from \"Elowen Mar\" to \"Elowen Marr\". This is a profile change request. Not a credentials request and not a joint-holder change. Asking the access system and submitting the request were both refused by policy, and the customer's identity is not verified. A person needs to verify the customer and handle the legal-name correction, which usually needs supporting ID."}.
58. Rule `agent-escalates` (on `escalate`) fired: state = TRIAGED → true (state=TRIAGED).
59. `reason`: not known → AGENT_ESCALATED (by `agent-escalates`).
60. State `TRIAGED` → `ESCALATED` (by `agent-escalates`).
61. The case closed in `ESCALATED`: **escalate**.

## Model calls

5 calls, 10877 tokens in, 685 out, 5.972 s, cost $0.0242; models: claude-sonnet-5-5, jev-1.13.0.

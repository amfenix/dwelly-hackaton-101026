# Case banking-019-at-01: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-019-at-01:read-requester:1).
4. `identify_requester` found {}.
5. Rule `read-subject` fired: state = READING → true (state=READING).
6. Called `find_subject` (attempt 1, key banking-019-at-01:read-subject:2).
7. Note from `read-subject`: initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: counterparty='Willow Yard Studios', subject_date='2025-09-18']
8. `find_subject` found {"counterparty": "Willow Yard Studios", "subject_date": "2025-09-18"}.
9. `counterparty`: not known → Willow Yard Studios (by `read-subject`).
10. `subject_date`: not known → 2025-09-18 (by `read-subject`).
11. Rule `read-payment` fired: state = READING → true (state=READING).
12. Called `check_payment` (attempt 1, key banking-019-at-01:read-payment:3).
13. `check_payment` found {}.
14. Rule `read-incoming` fired: state = READING → true (state=READING).
15. Called `check_incoming` (attempt 1, key banking-019-at-01:read-incoming:4).
16. `check_incoming` found {}.
17. Rule `read-recurring` fired: state = READING → true (state=READING).
18. Called `check_recurring` (attempt 1, key banking-019-at-01:read-recurring:5).
19. `check_recurring` found {}.
20. Rule `read-card` fired: state = READING → true (state=READING).
21. Called `check_card` (attempt 1, key banking-019-at-01:read-card:6).
22. `check_card` found {}.
23. Rule `read-access` fired: state = READING → true (state=READING).
24. Called `check_access` (attempt 1, key banking-019-at-01:read-access:7).
25. `check_access` found {}.
26. Rule `read-business` fired: state = READING → true (state=READING).
27. Called `check_business` (attempt 1, key banking-019-at-01:read-business:8).
28. `check_business` found {}.
29. Rule `read-documents` fired: state = READING → true (state=READING).
30. Called `check_documents` (attempt 1, key banking-019-at-01:read-documents:9).
31. `check_documents` found {}.
32. Rule `read-tariff` fired: state = READING → true (state=READING).
33. Called `check_tariff` (attempt 1, key banking-019-at-01:read-tariff:10).
34. `check_tariff` found {}.
35. Rule `read-bank-actions` fired: state = READING → true (state=READING).
36. Called `check_bank_actions` (attempt 1, key banking-019-at-01:read-bank-actions:11).
37. `check_bank_actions` found {}.
38. Rule `read-registration` fired: state = READING → true (state=READING).
39. Called `check_registration` (attempt 1, key banking-019-at-01:read-registration:12).
40. `check_registration` found {}.
41. Rule `read-confirmation` fired: state = READING → true (state=READING).
42. Called `check_confirmation` (attempt 1, key banking-019-at-01:read-confirmation:13).
43. `check_confirmation` found {}.
44. Rule `triage` fired: state = READING → true (state=READING).
45. Classifier (jev jev-latest) on `request_type`: change, confidence 0.98 → change.
46. Classifier (jev jev-latest) on `credentials_requested`: 0.05 → False.
47. Classifier (jev jev-latest) on `joint_holder_change`: 0.03 → False.
48. Classifier (jev jev-latest) on `subject`: standing_order, confidence 1.00 → standing_order.
49. `request_type`: not known → change (by `triage`).
50. `credentials_requested`: not known → False (by `triage`).
51. `joint_holder_change`: not known → False (by `triage`).
52. `subject`: not known → standing_order (by `triage`).
53. State `READING` → `TRIAGED` (by `triage`).
54. Rule `route-recurring` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [standing_order, direct_debit] → true (subject=standing_order).
55. `next_system`: not known → recurring (by `route-recurring`).
56. The agent asked for `ask_system` {"system": "recurring"}.
57. Refused `ask_system` in `TRIAGED`: payment-ask: args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change).
58. The agent asked for `submit_request` {}.
59. Refused `submit_request` in `TRIAGED`: register: request_type = register is false (request_type=change); register-what-fits-no-type: request_type = other is false (request_type=change); payment-instruction: next_system = payment is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); incoming-instruction: next_system = incoming is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); recurring-instruction: verified is not known (verified=not known); request_type = instruction is false (request_type=change); card-instruction: next_system = card is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); access-instruction: next_system = access is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); business-instruction: next_system = business is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); documents-instruction: next_system = documents is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change).
60. The agent asked for `redirect_secure` {}.
61. Refused `redirect_secure` in `TRIAGED`: redirect-to-the-secure-process: request_type = access is false (request_type=change); request_type = instruction is false (request_type=change); not verified is not known (verified=not known).
62. The agent stopped in `TRIAGED` (turn limit (4)); the policy's on_stall applies.
63. `reason`: not known → NOT_HANDLED (by `on_stall`).
64. State `TRIAGED` → `ESCALATED` (by `on_stall`).
65. The case closed in `ESCALATED`: **escalate**.

## Model calls

5 calls, 13339 tokens in, 716 out, 8.233 s, cost $0.0294; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> Asking the system isn't allowed for a change request, so I'll submit the change instead.

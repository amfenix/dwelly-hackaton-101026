# Case 022: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key 022:read-requester:1).
4. Note from `read-requester`: event 5 (Rois Fenwick): Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel. [facts: requester='Rois Fenwick', role='customer']
5. `identify_requester` found {"requester": "Rois Fenwick", "role": "customer"}.
6. `requester`: not known → Rois Fenwick (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. Rule `read-subject` fired: state = READING → true (state=READING).
9. Called `find_subject` (attempt 1, key 022:read-subject:2).
10. Note from `read-subject`: event 2 (Rois Fenwick): The hotel took £600 and £520, so that is £1,120. My available balance is only £380. I thought the stay cost £520. [facts: amount='600.00']
11. `find_subject` found {"amount": "600.00"}.
12. `amount`: not known → 600.00 (by `read-subject`).
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key 022:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key 022:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key 022:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key 022:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key 022:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key 022:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key 022:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key 022:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key 022:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key 022:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key 022:read-confirmation:13).
45. Note from `read-confirmation`: event 5 (Rois Fenwick): Can you get the £600 back into my available money today? I need groceries and cannot wait for a generic answer about the hotel. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: instruction, confidence 0.45 → instruction.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.02 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.04 → False.
53. Classifier (jev jev-latest) on `subject`: card_payment, confidence 0.89 → card_payment.
54. `request_type`: not known → instruction (by `triage`).
55. `credentials_requested`: not known → False (by `triage`).
56. `joint_holder_change`: not known → False (by `triage`).
57. `subject`: not known → card_payment (by `triage`).
58. State `READING` → `TRIAGED` (by `triage`).
59. Rule `route-card` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [card, card_payment] → true (subject=card_payment).
60. `next_system`: not known → card (by `route-card`).
61. The agent asked for `ask_system` {"system": "card"}.
62. Refused `ask_system` in `TRIAGED`: payment-ask: args.system = payment is false (args.system=card); next_system = payment is false (next_system=card); next_system absent is false (next_system=card); incoming-ask: args.system = incoming is false (args.system=card); next_system = incoming is false (next_system=card); next_system absent is false (next_system=card); recurring-ask: args.system = recurring is false (args.system=card); next_system = recurring is false (next_system=card); next_system absent is false (next_system=card); card-ask: next_system absent is false (next_system=card); request_type not in [register, change, authority, instruction] is false (request_type=instruction); access-ask: args.system = access is false (args.system=card); next_system = access is false (next_system=card); next_system absent is false (next_system=card); business-ask: args.system = business is false (args.system=card); next_system = business is false (next_system=card); next_system absent is false (next_system=card); documents-ask: args.system = documents is false (args.system=card); next_system = documents is false (next_system=card); next_system absent is false (next_system=card); document_ready = false is not known (document_ready=not known); tariff-ask: args.system = tariff is false (args.system=card); next_system = tariff is false (next_system=card); next_system absent is false (next_system=card).
63. The agent asked for `submit_request` {}.
64. Refused `submit_request` in `TRIAGED`: register: request_type = register is false (request_type=instruction); register-what-fits-no-type: request_type = other is false (request_type=instruction); payment-instruction: next_system = payment is false (next_system=card); verified is not known (verified=not known); incoming-instruction: next_system = incoming is false (next_system=card); verified is not known (verified=not known); recurring-instruction: next_system = recurring is false (next_system=card); verified is not known (verified=not known); card-instruction: verified is not known (verified=not known); access-instruction: next_system = access is false (next_system=card); verified is not known (verified=not known); business-instruction: next_system = business is false (next_system=card); verified is not known (verified=not known); documents-instruction: next_system = documents is false (next_system=card); verified is not known (verified=not known).
65. The agent asked for `escalate` {"note": "Customer Rois Fenwick (contact authentication recorded as passed, but 'verified' fact not established in desk) asks for a £600 hold to be released today. Hotel final charge £520 completed (merchant receipt), a separate £600 authorisation appears to linger, leaving available balance £380. Needs card operations to check linkage of the £600 authorisation to the £520 purchase and current network state, and release if eligible stale hold. Desk cannot release itself; submit_request and ask were refused (verified unknown). Customer is urgent (groceries today); do not promise release timing."}.
66. Rule `agent-escalates` (on `escalate`) fired: state = TRIAGED → true (state=TRIAGED).
67. `reason`: not known → AGENT_ESCALATED (by `agent-escalates`).
68. State `TRIAGED` → `ESCALATED` (by `agent-escalates`).
69. The case closed in `ESCALATED`: **escalate**.

## Model calls

5 calls, 12779 tokens in, 922 out, 10.38 s, cost $0.0303; models: claude-sonnet-5-5, jev-1.13.0.

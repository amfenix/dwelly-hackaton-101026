# Case 013: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key 013:read-requester:1).
4. Note from `read-requester`: event 2 (Customer): I got a letter saying my rent direct debit failed on the 18th. But I can see £750 went out to the agency on the 21st. The agency have texted me that the payment "failed" and I should pay manually today so I'm not in arrears. I don't want to be in arrears but I also don't want to pay twice. What's going on? [facts: requester='Customer', role='customer']
5. `identify_requester` found {"requester": "Customer", "role": "customer"}.
6. `requester`: not known → Customer (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. Rule `read-subject` fired: state = READING → true (state=READING).
9. Called `find_subject` (attempt 1, key 013:read-subject:2).
10. Note from `read-subject`: event 2 (Customer): I got a letter saying my rent direct debit failed on the 18th. But I can see £750 went out to the agency on the 21st. The agency have texted me that the payment "failed" and I should pay manually today so I'm not in arrears. I don't want to be in arrears but I also don't want to pay twice. What's going on? [facts: amount='750.00']
11. `find_subject` found {"amount": "750.00"}.
12. `amount`: not known → 750.00 (by `read-subject`).
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key 013:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key 013:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key 013:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key 013:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key 013:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key 013:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key 013:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key 013:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key 013:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key 013:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key 013:read-confirmation:13).
45. Note from `read-confirmation`: event 3 (Servicing agent (Harrow & Vale Bank plc)): Let me check both dates on the mandate. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: question, confidence 0.90 → question.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.02 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.04 → False.
53. Classifier (jev jev-latest) on `subject`: direct_debit, confidence 1.00 → direct_debit.
54. `request_type`: not known → question (by `triage`).
55. `credentials_requested`: not known → False (by `triage`).
56. `joint_holder_change`: not known → False (by `triage`).
57. `subject`: not known → direct_debit (by `triage`).
58. State `READING` → `TRIAGED` (by `triage`).
59. Rule `route-recurring` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [standing_order, direct_debit] → true (subject=direct_debit).
60. `next_system`: not known → recurring (by `route-recurring`).
61. The agent asked for `ask_system` {"system": "recurring"}.
62. Rule `recurring-ask` (on `ask_system`) fired: state = TRIAGED → true (state=TRIAGED); args.system = recurring → true (args.system=recurring); next_system = recurring → true (next_system=recurring); next_system absent → false (next_system=recurring); recurring_asked absent → true (recurring_asked=not known); request_type not in [register, change, authority] → true (request_type=question).
63. State `TRIAGED` → `ASK_PENDING` (by `recurring-ask`).
64. Rule `do-ask` fired: state = ASK_PENDING → true (state=ASK_PENDING).
65. Called `ask_system` (attempt 1, key 013:do-ask:17).
66. Action in the world: `ask_system` {"system": "recurring", "about": "direct_debit", "amount": "750.00"}.
67. `ask_system` found {}.
68. State `ASK_PENDING` → `ASKED` (by `do-ask`).
69. The case closed in `ASKED`: **ask_system**.

## Model calls

3 calls, 5596 tokens in, 456 out, 4.35 s, cost $0.0112; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> I've asked the recurring payments system to check the Direct Debit mandate and the dates of the failed and successful payments. Once its answer is in the case, we can tell you whether the £750 on the 21st covered your rent. Until then, please don't pay the agency again. That should avoid you paying twice.

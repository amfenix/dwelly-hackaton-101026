# Case 017: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key 017:read-requester:1).
4. Note from `read-requester`: event 4 (Violetta): Our director wants this logged as a formal missing-funds complaint if it isn't found today. [facts: requester='Violetta', role='customer']
5. `identify_requester` found {"requester": "Violetta", "role": "customer"}.
6. `requester`: not known → Violetta (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. Rule `read-subject` fired: state = READING → true (state=READING).
9. Called `find_subject` (attempt 1, key 017:read-subject:2).
10. Note from `read-subject`: event 2 (Violetta (bookkeeper)): Hi, we're £1,750 out on yesterday's balancing and we think a credit is missing from your statement. Our download shows £30,078.94 of credits but the closing balance only works if credits were £31,828.94. Can you investigate a missing payment? Round number — we think something's been lost. [facts: amount='1750.00']
11. `find_subject` found {"amount": "1750.00"}.
12. `amount`: not known → 1750.00 (by `read-subject`).
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key 017:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key 017:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key 017:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key 017:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key 017:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key 017:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key 017:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key 017:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key 017:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key 017:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key 017:read-confirmation:13).
45. Note from `read-confirmation`: event 4 (Violetta): Our director wants this logged as a formal missing-funds complaint if it isn't found today. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: register, confidence 0.95 → register.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.01 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.03 → False.
53. Classifier (jev jev-latest) on `subject`: incoming_payment, confidence 0.54 → incoming_payment.
54. `request_type`: not known → register (by `triage`).
55. `credentials_requested`: not known → False (by `triage`).
56. `joint_holder_change`: not known → False (by `triage`).
57. `subject`: not known → incoming_payment (by `triage`).
58. State `READING` → `TRIAGED` (by `triage`).
59. Rule `route-incoming` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [incoming_payment] → true (subject=incoming_payment).
60. `next_system`: not known → incoming (by `route-incoming`).
61. The agent asked for `ask_system` {"system": "incoming"}.
62. Refused `ask_system` in `TRIAGED`: payment-ask: args.system = payment is false (args.system=incoming); next_system = payment is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); incoming-ask: next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); recurring-ask: args.system = recurring is false (args.system=incoming); next_system = recurring is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); card-ask: args.system = card is false (args.system=incoming); next_system = card is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority, instruction] is false (request_type=register); access-ask: args.system = access is false (args.system=incoming); next_system = access is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); business-ask: args.system = business is false (args.system=incoming); next_system = business is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register); documents-ask: args.system = documents is false (args.system=incoming); next_system = documents is false (next_system=incoming); next_system absent is false (next_system=incoming); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=register); tariff-ask: args.system = tariff is false (args.system=incoming); next_system = tariff is false (next_system=incoming); next_system absent is false (next_system=incoming); request_type not in [register, change, authority] is false (request_type=register).
63. The agent asked for `submit_request` {}.
64. Rule `register` (on `submit_request`) fired: state = TRIAGED → true (state=TRIAGED); request_type = register → true (request_type=register); registration_asked absent → true (registration_asked=not known).
65. State `TRIAGED` → `REQUEST_PENDING` (by `register`).
66. Rule `do-request` fired: state = REQUEST_PENDING → true (state=REQUEST_PENDING).
67. Called `register_request` (attempt 1, key 017:do-request:17).
68. Action in the world: `register_request` {"team": "incoming", "about": "incoming_payment"}.
69. `register_request` found {}.
70. State `REQUEST_PENDING` → `REQUESTED` (by `do-request`).
71. The case closed in `REQUESTED`: **submit_request**.

## Model calls

5 calls, 13853 tokens in, 642 out, 7.371 s, cost $0.0296; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> I've passed this to the team that handles missing-payment investigations. The case shows it as a request to register the £1,750.00 discrepancy, so I couldn't look up the day's activity myself.
> 
> The team will compare your export with the account's full-day activity. Your director also asked for a formal missing-funds complaint if the credit isn't found today. I haven't confirmed that has been logged, because nothing in the case shows it.
> 
> I haven't found any lost payment. Nothing yet shows whether a £1,750.00 credit is missing or whether the gap has another cause.

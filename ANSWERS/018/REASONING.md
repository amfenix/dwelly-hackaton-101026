# Case 018: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key 018:read-requester:1).
4. Note from `read-requester`: event 4 (Customer): I know it's less than the rent. I've told the agency I'll sort it. I just need it changed. [facts: requester='Customer', role='customer']
5. `identify_requester` found {"requester": "Customer", "role": "customer"}.
6. `requester`: not known → Customer (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. Rule `read-subject` fired: state = READING → true (state=READING).
9. Called `find_subject` (attempt 1, key 018:read-subject:2).
10. Note from `read-subject`: event 2 (Customer): [ID&V passed] I need to change my rent standing order to £400 from next month. I can't afford £500 at the minute — I lost my job in July and I'm doing bits of agency work. When I'm back in proper work I'll put it up to £550 to catch up. Can you do that today? [facts: amount='400.00']
11. `find_subject` found {"amount": "400.00"}.
12. `amount`: not known → 400.00 (by `read-subject`).
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key 018:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key 018:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key 018:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key 018:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key 018:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key 018:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key 018:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key 018:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key 018:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key 018:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key 018:read-confirmation:13).
45. Note from `read-confirmation`: event 4 (Customer): I know it's less than the rent. I've told the agency I'll sort it. I just need it changed. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: change, confidence 1.00 → change.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.02 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.02 → False.
53. Classifier (jev jev-latest) on `subject`: standing_order, confidence 1.00 → standing_order.
54. `request_type`: not known → change (by `triage`).
55. `credentials_requested`: not known → False (by `triage`).
56. `joint_holder_change`: not known → False (by `triage`).
57. `subject`: not known → standing_order (by `triage`).
58. State `READING` → `TRIAGED` (by `triage`).
59. Rule `route-recurring` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [standing_order, direct_debit] → true (subject=standing_order).
60. `next_system`: not known → recurring (by `route-recurring`).
61. Rule `change-needs-confirmation` fired: state = TRIAGED → true (state=TRIAGED); request_type = change → true (request_type=change); confirmation = none → true (confirmation=none); registration_asked absent → true (registration_asked=not known). A change is confirmed by the customer in the secure portal, not in chat or by email.
62. State `TRIAGED` → `CONFIRM_PENDING` (by `change-needs-confirmation`).
63. Rule `do-confirm` fired: state = CONFIRM_PENDING → true (state=CONFIRM_PENDING).
64. Called `send_for_confirmation` (attempt 1, key 018:do-confirm:17).
65. Action in the world: `send_for_confirmation` {"change": "standing_order, amount=400.00", "to": "Customer"}.
66. `send_for_confirmation` found {}.
67. State `CONFIRM_PENDING` → `CONFIRMATION_SENT` (by `do-confirm`).
68. The case closed in `CONFIRMATION_SENT`: **send_for_confirmation**.
69. The agent asked for `ask_system` {"system": "recurring"}.
70. Refused `ask_system` in `CONFIRMATION_SENT`: payment-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority, instruction] is false (request_type=change); access-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); document_ready = false is not known (document_ready=not known); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change).
71. The agent asked for `submit_request` {}.
72. Refused `submit_request` in `CONFIRMATION_SENT`: register: state = TRIAGED is false (state=CONFIRMATION_SENT); request_type = register is false (request_type=change); register-what-fits-no-type: state = TRIAGED is false (state=CONFIRMATION_SENT); request_type = other is false (request_type=change); payment-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = payment is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); incoming-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = incoming is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); recurring-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); verified is not known (verified=not known); request_type = instruction is false (request_type=change); card-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = card is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); access-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = access is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); business-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = business is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change); documents-instruction: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system = documents is false (next_system=recurring); verified is not known (verified=not known); request_type = instruction is false (request_type=change).

## Model calls

5 calls, 16388 tokens in, 708 out, 8.626 s, cost $0.0353; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> The case is already closed as final: a confirmation has been sent to the customer (outcome `send_for_confirmation`). I tried to look up the standing order and to submit the change. The desk refused both, because the case is no longer open for new actions.
> 
> Nothing was changed on the standing order. The customer hasn't replied to the confirmation, so the change to £400 is still waiting on that confirmation. Nothing more is needed from the bank at this point.

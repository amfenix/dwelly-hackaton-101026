# Case 029: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key 029:read-requester:1).
4. Note from `read-requester`: event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: requester='Enna Prysett', role='customer']
5. `identify_requester` found {"requester": "Enna Prysett", "role": "customer"}.
6. `requester`: not known → Enna Prysett (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. Rule `read-subject` fired: state = READING → true (state=READING).
9. Called `find_subject` (attempt 1, key 029:read-subject:2).
10. Note from `read-subject`: event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: amount='3200.00']
11. `find_subject` found {"amount": "3200.00"}.
12. `amount`: not known → 3200.00 (by `read-subject`).
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key 029:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key 029:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key 029:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key 029:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key 029:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key 029:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key 029:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key 029:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key 029:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key 029:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key 029:read-confirmation:13).
45. Note from `read-confirmation`: event 5 (Enna Prysett): Please restore the £3,200 you took and confirm the sender has already been paid back. I also need money for food while this is sorted. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: register, confidence 0.81 → register.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.02 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.07 → False.
53. Classifier (jev jev-latest) on `subject`: incoming_payment, confidence 0.85 → incoming_payment.
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
67. Called `register_request` (attempt 1, key 029:do-request:17).
68. Action in the world: `register_request` {"team": "incoming", "about": "incoming_payment"}.
69. `register_request` found {}.
70. State `REQUEST_PENDING` → `REQUESTED` (by `do-request`).
71. The case closed in `REQUESTED`: **submit_request**.

## Model calls

5 calls, 12666 tokens in, 701 out, 8.754 s, cost $0.0279; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> I've passed your case to the recovery team, which decides recovery requests and hold reviews. This includes your request for a hardship review, because you need money for food while this is sorted.
> 
> I can't confirm that the sender has been paid back, and I can't restore the money myself. The records show only that a recovery was requested for incoming reference IN-029 (£2,000). That request has been received and is still under investigation. I can see no repayment to the sender and no decision yet.
> 
> Your ledger shows the £2,000 incoming payment, and your screen also shows a £1,200 reservation. The records I have don't explain the £3,200 total you mention, so I haven't confirmed that figure. The recovery team will look at the recovery and the reservation together.

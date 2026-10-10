# Case banking-019-at-02: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-019-at-02:read-requester:1).
4. Note from `read-requester`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: requester='Maeve Ellery', role='customer', channel='secure_chat', verified=False]
5. `identify_requester` found {"requester": "Maeve Ellery", "role": "customer", "channel": "secure_chat", "verified": false}.
6. `requester`: not known → Maeve Ellery (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. `channel`: not known → secure_chat (by `read-requester`).
9. `verified`: not known → False (by `read-requester`).
10. Rule `read-subject` fired: state = READING → true (state=READING).
11. Called `find_subject` (attempt 1, key banking-019-at-02:read-subject:2).
12. Note from `read-subject`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: counterparty='Willow Yard Studios']
13. Note from `read-subject`: initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: subject_date='2025-09-18']
14. `find_subject` found {"counterparty": "Willow Yard Studios", "subject_date": "2025-09-18"}.
15. `counterparty`: not known → Willow Yard Studios (by `read-subject`).
16. `subject_date`: not known → 2025-09-18 (by `read-subject`).
17. Rule `read-payment` fired: state = READING → true (state=READING).
18. Called `check_payment` (attempt 1, key banking-019-at-02:read-payment:3).
19. `check_payment` found {}.
20. Rule `read-incoming` fired: state = READING → true (state=READING).
21. Called `check_incoming` (attempt 1, key banking-019-at-02:read-incoming:4).
22. `check_incoming` found {}.
23. Rule `read-recurring` fired: state = READING → true (state=READING).
24. Called `check_recurring` (attempt 1, key banking-019-at-02:read-recurring:5).
25. `check_recurring` found {}.
26. Rule `read-card` fired: state = READING → true (state=READING).
27. Called `check_card` (attempt 1, key banking-019-at-02:read-card:6).
28. `check_card` found {}.
29. Rule `read-access` fired: state = READING → true (state=READING).
30. Called `check_access` (attempt 1, key banking-019-at-02:read-access:7).
31. `check_access` found {}.
32. Rule `read-business` fired: state = READING → true (state=READING).
33. Called `check_business` (attempt 1, key banking-019-at-02:read-business:8).
34. `check_business` found {}.
35. Rule `read-documents` fired: state = READING → true (state=READING).
36. Called `check_documents` (attempt 1, key banking-019-at-02:read-documents:9).
37. `check_documents` found {}.
38. Rule `read-tariff` fired: state = READING → true (state=READING).
39. Called `check_tariff` (attempt 1, key banking-019-at-02:read-tariff:10).
40. `check_tariff` found {}.
41. Rule `read-registration` fired: state = READING → true (state=READING).
42. Called `check_registration` (attempt 1, key banking-019-at-02:read-registration:11).
43. `check_registration` found {}.
44. Rule `read-confirmation` fired: state = READING → true (state=READING).
45. Called `check_confirmation` (attempt 1, key banking-019-at-02:read-confirmation:12).
46. Note from `read-confirmation`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: confirmation='none', instructed_outside_portal=True]
47. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": true}.
48. `confirmation`: not known → none (by `read-confirmation`).
49. `instructed_outside_portal`: not known → True (by `read-confirmation`).
50. Rule `triage` fired: state = READING → true (state=READING).
51. Classifier (jev jev-latest) on `request_type`: change, confidence 0.98 → change.
52. Classifier (jev jev-latest) on `subject`: standing_order, confidence 1.00 → standing_order.
53. `request_type`: not known → change (by `triage`).
54. `subject`: not known → standing_order (by `triage`).
55. State `READING` → `TRIAGED` (by `triage`).
56. Rule `route-recurring` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [standing_order, direct_debit] → true (subject=standing_order).
57. `next_system`: not known → recurring (by `route-recurring`).
58. Rule `change-needs-confirmation` fired: state = TRIAGED → true (state=TRIAGED); request_type = change → true (request_type=change); confirmation = none → true (confirmation=none); registration_asked absent → true (registration_asked=not known). A change is confirmed by the customer in the secure portal, not in chat or by email.
59. State `TRIAGED` → `CONFIRM_PENDING` (by `change-needs-confirmation`).
60. Rule `do-confirm` fired: state = CONFIRM_PENDING → true (state=CONFIRM_PENDING).
61. Called `send_for_confirmation` (attempt 1, key banking-019-at-02:do-confirm:16).
62. Action in the world: `send_for_confirmation` {"change": "standing_order, counterparty=Willow Yard Studios, date=2025-09-18", "to": "Maeve Ellery"}.
63. `send_for_confirmation` found {}.
64. State `CONFIRM_PENDING` → `CONFIRMATION_SENT` (by `do-confirm`).
65. The case closed in `CONFIRMATION_SENT`: **send_for_confirmation**.
66. The agent asked for `ask_system` {"system": "recurring"}.
67. Refused `ask_system` in `CONFIRMATION_SENT`: payment-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = payment is false (args.system=recurring); next_system = payment is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); incoming-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = incoming is false (args.system=recurring); next_system = incoming is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); recurring-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); card-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = card is false (args.system=recurring); next_system = card is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); access-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = access is false (args.system=recurring); next_system = access is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); business-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = business is false (args.system=recurring); next_system = business is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); documents-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = documents is false (args.system=recurring); next_system = documents is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change); tariff-ask: state = TRIAGED is false (state=CONFIRMATION_SENT); args.system = tariff is false (args.system=recurring); next_system = tariff is false (next_system=recurring); next_system absent is false (next_system=recurring); request_type not in [register, change, authority] is false (request_type=change).

## Model calls

4 calls, 9563 tokens in, 504 out, 5.461 s, cost $0.0203; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> The case is already closed: the change request was sent to you for secure confirmation. I tried to check the standing order's processing stage, but the desk refused because the case is final. So I haven't confirmed whether the 18 September run can still be moved to 22 September.
> 
> Nothing has been changed on the standing order. Your identity is also still unverified, and no confirmation has come back from you yet. Nothing more can be done on this case until you confirm through the secure process.

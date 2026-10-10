# Case banking-019-at-04: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-019-at-04:read-requester:1).
4. Note from `read-requester`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: requester='Maeve Ellery', role='customer', channel='secure_chat', verified=False]
5. `identify_requester` found {"requester": "Maeve Ellery", "role": "customer", "channel": "secure_chat", "verified": false}.
6. `requester`: not known → Maeve Ellery (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. `channel`: not known → secure_chat (by `read-requester`).
9. `verified`: not known → False (by `read-requester`).
10. Rule `read-subject` fired: state = READING → true (state=READING).
11. Called `find_subject` (attempt 1, key banking-019-at-04:read-subject:2).
12. Note from `read-subject`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: counterparty='Willow Yard Studios']
13. Note from `read-subject`: initial request (system): I want to move the date of my active monthly standing order to Willow Yard Studios from 18 September 2025 to 22 September 2025. Please check whether the next run can still be changed and send the change to me for secure confirmation. [facts: subject_date='2025-09-18']
14. `find_subject` found {"counterparty": "Willow Yard Studios", "subject_date": "2025-09-18"}.
15. `counterparty`: not known → Willow Yard Studios (by `read-subject`).
16. `subject_date`: not known → 2025-09-18 (by `read-subject`).
17. Rule `read-payment` fired: state = READING → true (state=READING).
18. Called `check_payment` (attempt 1, key banking-019-at-04:read-payment:3).
19. `check_payment` found {}.
20. Rule `read-incoming` fired: state = READING → true (state=READING).
21. Called `check_incoming` (attempt 1, key banking-019-at-04:read-incoming:4).
22. `check_incoming` found {}.
23. Rule `read-recurring` fired: state = READING → true (state=READING).
24. Called `check_recurring` (attempt 1, key banking-019-at-04:read-recurring:5).
25. `check_recurring` found {}.
26. Rule `read-card` fired: state = READING → true (state=READING).
27. Called `check_card` (attempt 1, key banking-019-at-04:read-card:6).
28. `check_card` found {}.
29. Rule `read-access` fired: state = READING → true (state=READING).
30. Called `check_access` (attempt 1, key banking-019-at-04:read-access:7).
31. `check_access` found {}.
32. Rule `read-business` fired: state = READING → true (state=READING).
33. Called `check_business` (attempt 1, key banking-019-at-04:read-business:8).
34. `check_business` found {}.
35. Rule `read-documents` fired: state = READING → true (state=READING).
36. Called `check_documents` (attempt 1, key banking-019-at-04:read-documents:9).
37. `check_documents` found {}.
38. Rule `read-tariff` fired: state = READING → true (state=READING).
39. Called `check_tariff` (attempt 1, key banking-019-at-04:read-tariff:10).
40. `check_tariff` found {}.
41. Rule `read-bank-actions` fired: state = READING → true (state=READING).
42. Called `check_bank_actions` (attempt 1, key banking-019-at-04:read-bank-actions:11).
43. `check_bank_actions` found {}.
44. Rule `read-registration` fired: state = READING → true (state=READING).
45. Called `check_registration` (attempt 1, key banking-019-at-04:read-registration:12).
46. `check_registration` found {}.
47. Rule `read-confirmation` fired: state = READING → true (state=READING).
48. Called `check_confirmation` (attempt 1, key banking-019-at-04:read-confirmation:13).
49. Note from `read-confirmation`: event 4 (H&V service agent): I’ve checked that the next run is not yet being processed and have sent the requested change from 18 September to 22 September 2025 for your secure confirmation. I have not changed the instruction on your behalf. [facts: confirmation='requested']
50. Note from `read-confirmation`: event 2 (Maeve Ellery): I’m escalating my request to move the next run of my standing order to Willow Yard Studios from 18 September to 22 September 2025. Please check its processing stage and send any eligible change to me for confirmation. [facts: instructed_outside_portal=True]
51. `check_confirmation` found {"confirmation": "requested", "instructed_outside_portal": true}.
52. `confirmation`: not known → requested (by `read-confirmation`).
53. `instructed_outside_portal`: not known → True (by `read-confirmation`).
54. Rule `triage` fired: state = READING → true (state=READING).
55. Classifier (jev jev-latest) on `request_type`: change, confidence 0.98 → change.
56. Classifier (jev jev-latest) on `subject`: standing_order, confidence 1.00 → standing_order.
57. `request_type`: not known → change (by `triage`).
58. `subject`: not known → standing_order (by `triage`).
59. State `READING` → `TRIAGED` (by `triage`).
60. Rule `route-recurring` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [standing_order, direct_debit] → true (subject=standing_order).
61. `next_system`: not known → recurring (by `route-recurring`).
62. Rule `change-waits-for-the-customer` fired: state = TRIAGED → true (state=TRIAGED); request_type = change → true (request_type=change); confirmation = requested → true (confirmation=requested); registration_asked absent → true (registration_asked=not known). The change was sent to the portal; the customer has not confirmed it yet.
63. State `TRIAGED` → `WAITING` (by `change-waits-for-the-customer`).
64. The case closed in `WAITING`: **wait**.
65. The agent asked for `reply` {}.
66. Refused `reply` in `WAITING`: registration-reply: state = TRIAGED is false (state=WAITING); registration_asked is not known (registration_asked=not known); registered present is false (registered=not known); payment-reply: state = TRIAGED is false (state=WAITING); next_system = payment is false (next_system=recurring); payment_status present is false (payment_status=not known); incoming-reply: state = TRIAGED is false (state=WAITING); next_system = incoming is false (next_system=recurring); incoming_found present is false (incoming_found=not known); recurring-reply: state = TRIAGED is false (state=WAITING); recurring_status present is false (recurring_status=not known); card-reply: state = TRIAGED is false (state=WAITING); next_system = card is false (next_system=recurring); card_status present is false (card_status=not known); access-reply: state = TRIAGED is false (state=WAITING); next_system = access is false (next_system=recurring); access_status present is false (access_status=not known); business-reply: state = TRIAGED is false (state=WAITING); next_system = business is false (next_system=recurring); business_status present is false (business_status=not known); not (business_status = ROLE_REVOKED and subject != "role") is not known (business_status=not known, subject=standing_order); documents-reply: state = TRIAGED is false (state=WAITING); next_system = documents is false (next_system=recurring); document_ready is not known (document_ready=not known); tariff-reply: state = TRIAGED is false (state=WAITING); next_system = tariff is false (next_system=recurring); tariff_status present is false (tariff_status=not known).

## Model calls

4 calls, 7890 tokens in, 473 out, 4.532 s, cost $0.0165; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> The change is already with the customer for secure confirmation, and the case is waiting on her. Nothing is left for the desk to do.
> The change to your standing order is waiting for your secure confirmation, and I haven't altered the instruction myself.
> 
> The desk checked that the next payment to Willow Yard Studios isn't being processed yet. The request to move it from 18 September to 22 September 2025 has been sent to you to confirm. The case is now waiting on you, and there's nothing more for the bank to do until you respond.
> 
> My attempt to send a further reply was refused because the case is already in a waiting state. The earlier portal message stands as the update.

# Case banking-036-at-01: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-036-at-01:read-requester:1).
4. Note from `read-requester`: event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: requester='Mara Ellison', role='customer', channel='external_message', verified=False]
5. `identify_requester` found {"requester": "Mara Ellison", "role": "customer", "channel": "external_message", "verified": false}.
6. `requester`: not known → Mara Ellison (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. `channel`: not known → external_message (by `read-requester`).
9. `verified`: not known → False (by `read-requester`).
10. Rule `read-subject` fired: state = READING → true (state=READING).
11. Called `find_subject` (attempt 1, key banking-036-at-01:read-subject:2).
12. `find_subject` found {}.
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key banking-036-at-01:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key banking-036-at-01:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key banking-036-at-01:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key banking-036-at-01:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key banking-036-at-01:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key banking-036-at-01:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key banking-036-at-01:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key banking-036-at-01:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key banking-036-at-01:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key banking-036-at-01:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key banking-036-at-01:read-confirmation:13).
45. Note from `read-confirmation`: event 1 (Mara Ellison): I have moved within the UK and am writing to let you know. Please update the address you use for my correspondence; I understand this email alone does not change my profile. [facts: confirmation='none', instructed_outside_portal=True]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": true}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → True (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: change, confidence 1.00 → change.
51. Classifier (jev jev-latest) on `credentials_requested`: 0.01 → False.
52. Classifier (jev jev-latest) on `joint_holder_change`: 0.04 → False.
53. Classifier (jev jev-latest) on `subject`: profile, confidence 1.00 → profile.
54. `request_type`: not known → change (by `triage`).
55. `credentials_requested`: not known → False (by `triage`).
56. `joint_holder_change`: not known → False (by `triage`).
57. `subject`: not known → profile (by `triage`).
58. State `READING` → `TRIAGED` (by `triage`).
59. Rule `route-access` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [access, profile] → true (subject=profile).
60. `next_system`: not known → access (by `route-access`).
61. Rule `change-by-email` fired: state = TRIAGED → true (state=TRIAGED); request_type = change → true (request_type=change); channel = external_message → true (channel=external_message); role != third_party → true (role=customer). An email does not change anything; the customer is pointed to the secure process.
62. State `TRIAGED` → `REDIRECT_PENDING` (by `change-by-email`).
63. Rule `do-redirect` fired: state = REDIRECT_PENDING → true (state=REDIRECT_PENDING).
64. Called `redirect_secure` (attempt 1, key banking-036-at-01:do-redirect:17).
65. Action in the world: `redirect_secure` {"to": "Mara Ellison", "channel": "external_message", "text": "Please use the secure process in your secure portal to do this; it checks your identity there. We will never ask for your password, PIN or a verification code. Nothing on your profile was changed."}.
66. `redirect_secure` found {}.
67. State `REDIRECT_PENDING` → `REDIRECTED` (by `do-redirect`).
68. The case closed in `REDIRECTED`: **redirect_secure**.
69. The agent asked for `redirect_secure` {}.
70. Refused `redirect_secure` in `REDIRECTED`: redirect-to-the-secure-process: state = TRIAGED is false (state=REDIRECTED); request_type = access is false (request_type=change); request_type = instruction is false (request_type=change).

## Model calls

3 calls, 5435 tokens in, 710 out, 7.222 s, cost $0.0136; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> I called `redirect_secure`, and the desk refused it. The case is already in the REDIRECTED state, and the request is a profile change rather than an access or instruction request. The result also says the case is closed under `redirect_secure`, so the customer has already been pointed to the secure process.
> 
> Mara Ellison is not verified and wrote in by email. The bank can't change her correspondence address from this message, which she acknowledged herself. She needs to make the change through the bank's secure, signed-in process. Nothing else is left for me to do on this case.

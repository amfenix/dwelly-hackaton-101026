# Case banking-027-at-02: how the decision was reached

Every line below is a record of the run, in order: the agent's requests, the rules that fired with the facts they saw, what checks returned, and each change of state.

1. Case opened in `READING` under policy banking-desk v1.
2. Rule `read-requester` fired: state = READING → true (state=READING).
3. Called `identify_requester` (attempt 1, key banking-027-at-02:read-requester:1).
4. Note from `read-requester`: event 2 (Mara Ellison): I’ve completed H&V’s identification checks for this call. I still can’t sign in to my profile, and I need help restoring access; I’m not sharing any password or verification code. [facts: requester='Mara Ellison', role='customer', channel='verified_call', verified=True]
5. `identify_requester` found {"requester": "Mara Ellison", "role": "customer", "channel": "verified_call", "verified": true}.
6. `requester`: not known → Mara Ellison (by `read-requester`).
7. `role`: not known → customer (by `read-requester`).
8. `channel`: not known → verified_call (by `read-requester`).
9. `verified`: not known → True (by `read-requester`).
10. Rule `read-subject` fired: state = READING → true (state=READING).
11. Called `find_subject` (attempt 1, key banking-027-at-02:read-subject:2).
12. `find_subject` found {}.
13. Rule `read-payment` fired: state = READING → true (state=READING).
14. Called `check_payment` (attempt 1, key banking-027-at-02:read-payment:3).
15. `check_payment` found {}.
16. Rule `read-incoming` fired: state = READING → true (state=READING).
17. Called `check_incoming` (attempt 1, key banking-027-at-02:read-incoming:4).
18. `check_incoming` found {}.
19. Rule `read-recurring` fired: state = READING → true (state=READING).
20. Called `check_recurring` (attempt 1, key banking-027-at-02:read-recurring:5).
21. `check_recurring` found {}.
22. Rule `read-card` fired: state = READING → true (state=READING).
23. Called `check_card` (attempt 1, key banking-027-at-02:read-card:6).
24. `check_card` found {}.
25. Rule `read-access` fired: state = READING → true (state=READING).
26. Called `check_access` (attempt 1, key banking-027-at-02:read-access:7).
27. `check_access` found {}.
28. Rule `read-business` fired: state = READING → true (state=READING).
29. Called `check_business` (attempt 1, key banking-027-at-02:read-business:8).
30. `check_business` found {}.
31. Rule `read-documents` fired: state = READING → true (state=READING).
32. Called `check_documents` (attempt 1, key banking-027-at-02:read-documents:9).
33. `check_documents` found {}.
34. Rule `read-tariff` fired: state = READING → true (state=READING).
35. Called `check_tariff` (attempt 1, key banking-027-at-02:read-tariff:10).
36. `check_tariff` found {}.
37. Rule `read-bank-actions` fired: state = READING → true (state=READING).
38. Called `check_bank_actions` (attempt 1, key banking-027-at-02:read-bank-actions:11).
39. `check_bank_actions` found {}.
40. Rule `read-registration` fired: state = READING → true (state=READING).
41. Called `check_registration` (attempt 1, key banking-027-at-02:read-registration:12).
42. `check_registration` found {}.
43. Rule `read-confirmation` fired: state = READING → true (state=READING).
44. Called `check_confirmation` (attempt 1, key banking-027-at-02:read-confirmation:13).
45. Note from `read-confirmation`: event 2 (Mara Ellison): I’ve completed H&V’s identification checks for this call. I still can’t sign in to my profile, and I need help restoring access; I’m not sharing any password or verification code. [facts: confirmation='none', instructed_outside_portal=False]
46. `check_confirmation` found {"confirmation": "none", "instructed_outside_portal": false}.
47. `confirmation`: not known → none (by `read-confirmation`).
48. `instructed_outside_portal`: not known → False (by `read-confirmation`).
49. Rule `triage` fired: state = READING → true (state=READING).
50. Classifier (jev jev-latest) on `request_type`: access, confidence 1.00 → access.
51. Classifier (jev jev-latest) on `subject`: access, confidence 1.00 → access.
52. `request_type`: not known → access (by `triage`).
53. `subject`: not known → access (by `triage`).
54. State `READING` → `TRIAGED` (by `triage`).
55. Rule `route-access` fired: state = TRIAGED → true (state=TRIAGED); next_system absent → true (next_system=not known); subject in [access, profile] → true (subject=access).
56. `next_system`: not known → access (by `route-access`).
57. The agent asked for `redirect_secure` {}.
58. Rule `redirect-to-the-secure-process` (on `redirect_secure`) fired: state = TRIAGED → true (state=TRIAGED); request_type = access → true (request_type=access).
59. State `TRIAGED` → `REDIRECT_PENDING` (by `redirect-to-the-secure-process`).
60. Rule `do-redirect` fired: state = REDIRECT_PENDING → true (state=REDIRECT_PENDING).
61. Called `redirect_secure` (attempt 1, key banking-027-at-02:do-redirect:17).
62. Action in the world: `redirect_secure` {"to": "Mara Ellison", "channel": "verified_call", "text": "Please use the secure process in your secure portal to do this; it checks your identity there. We will never ask for your password, PIN or a verification code. Nothing on your profile was changed."}.
63. `redirect_secure` found {}.
64. State `REDIRECT_PENDING` → `REDIRECTED` (by `do-redirect`).
65. The case closed in `REDIRECTED`: **redirect_secure**.

## Model calls

3 calls, 4855 tokens in, 529 out, 3.916 s, cost $0.0112; models: claude-sonnet-5-5, jev-1.13.0.

## What the agent said

> I've pointed the customer to H&V's secure recovery process to get back into their profile. The desk accepted this and the case is closed.
> 
> I didn't look up the profile in the access system first. Recovery goes through the secure process whatever the cause of the lockout. The bank never handles passwords or codes, and the customer didn't share any.

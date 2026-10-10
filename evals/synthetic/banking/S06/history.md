# Case S06 history — Supplier batch row returned by the beneficiary bank

Total events: 5

<a id="event-001"></a>
## 2025-11-06 09:00:00 UTC — event 001

- **Channel:** Business portal
- **From:** H&V secure portal
- **To:** Daniel Ferreira

Batch “Kestrel Joinery — October suppliers” — status: Processed.

<a id="event-002"></a>
## 2025-11-06 09:47:00 UTC — event 002

- **Channel:** Secure chat
- **From:** Daniel Ferreira
- **To:** H&V service agent

I’m an authorised signatory for Kestrel Joinery Ltd. The October supplier batch shows as processed, but our timber supplier on row SUP-31 says they haven’t had their money. Can you tell me whether that row was paid or not?

<a id="event-003"></a>
## 2025-11-06 10:34:00 UTC — event 003

- **Channel:** Internal note
- **From:** H&V service agent
- **To:** H&V payment journal

I am checking row SUP-31 of the processed batch “Kestrel Joinery — October suppliers” specifically, rather than inferring its status from the batch status.

<a id="event-004"></a>
## 2025-11-06 11:21:00 UTC — event 004

- **Channel:** Internal note
- **From:** H&V payment journal
- **To:** H&V service agent

SUP-31 — RETURNED by beneficiary institution (account closed), funds re-credited to the batch account.

<a id="event-005"></a>
## 2025-11-06 12:08:00 UTC — event 005

- **Channel:** Secure chat
- **From:** H&V service agent
- **To:** Daniel Ferreira

I’ve checked row SUP-31. The payment journal shows it as returned by the beneficiary institution, with the reason “account closed”, and the funds have been re-credited to the batch account. So it was not paid to the supplier’s account, and it was not rejected by H&V. I haven’t re-sent the payment or re-evaluated the other rows; a processed batch doesn’t mean every row was paid.

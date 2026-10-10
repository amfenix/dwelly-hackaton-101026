"""The banking track's policy on synthetic cases: what it decides, and what it refuses."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from desk.machine import Case, Services, load_functions
from desk.policy import load_policy
from tests.conftest import FakeClassifier

TRACK = Path(__file__).resolve().parents[1] / "track"
POLICY = load_policy(TRACK / "policy.yaml")
FUNCTIONS, _ = load_functions(TRACK / "functions.py")

CUSTOMER = "Mara Ellison"
ASK = ("Secure chat", CUSTOMER, "H&V service agent", "Has H&V sent my £420 transfer to Alder Workshop?")
TO_JOURNAL = ("Internal note", "H&V service agent", "H&V transfer journal", "Please return the transfer status.")
FROM_JOURNAL = ("Internal note", "H&V transfer journal", "H&V service agent", "Transfer status: SENT.")


class Triage(FakeClassifier):
    """Answers the triage; any other question (a reader's fallback) is not known."""

    def classify(self, text: str, questions: Any) -> Any:
        self.answers = {name: self.answers.get(name, "unknown") for name in {*self.answers, *questions}}
        return super().classify(text, questions)


def event(seq: int, channel: str, sender: str, recipient: str, text: str) -> dict[str, Any]:
    kind = "system" if channel == "Internal note" else "conversation"
    return {"seq": seq, "at": "2025-07-19T09:00:00Z", "channel": channel, "kind": kind,
            "from": sender, "to": recipient, "extra": {}, "text": text}  # fmt: skip


def started(
    *events: tuple[str, str, str, str],
    request_type: str = "question",
    subject: str = "transfer",
    role: str = "Bank customer",
) -> Case:
    case_input = {
        "id": "t",
        "title": "A question",
        "details": {"Source role": role, "Bank": "Harrow & Vale Bank plc (fictional)"},
        "request": events[0][3],
        "events": [event(i, *e) for i, e in enumerate(events, 1)],
        "attachments": [],
    }
    machine = Case(
        POLICY, FUNCTIONS, case_input, None, Services(Triage({"request_type": request_type, "subject": subject}))
    )
    machine.start()
    return machine


def acts(case: Case) -> list[str]:
    return [e.data["type"] for e in case.journal.of("action")]


def test_nothing_asked_yet_the_agent_asks_the_system_that_holds_the_answer() -> None:
    case = started(ASK)
    assert case.state == "TRIAGED" and case.fields["next_system"] == "payment"
    assert not case.send("ask_system", {"system": "card"}).accepted  # not the system the facts point to
    assert case.send("ask_system", {"system": "payment"}).accepted
    assert case.state == "ASKED" and acts(case) == ["ask_system"]
    assert not case.send("reply").accepted  # one decision per point


def test_asked_and_not_answered_waits_without_the_agent() -> None:
    case = started(ASK, TO_JOURNAL)
    assert case.state == "WAITING" and case.outcome == "wait" and acts(case) == []


def test_answered_the_reply_says_what_the_record_shows_and_no_more() -> None:
    case = started(ASK, TO_JOURNAL, FROM_JOURNAL)
    assert not case.send("ask_system", {"system": "payment"}).accepted  # already asked
    assert case.send("reply").accepted and case.state == "REPLIED"
    reply = case.journal.of("action")[-1].data["args"]
    assert reply["to"] == CUSTOMER and "sent" in reply["text"] and "does not confirm receipt" in reply["text"]


def test_no_reply_before_the_answer_is_in() -> None:
    case = started(ASK)
    refused = case.send("reply")
    assert not refused.accepted and refused.reason is not None and "payment_status present" in refused.reason


def test_with_no_subject_the_agent_names_the_system() -> None:
    case = started(("Secure chat", CUSTOMER, "H&V service agent", "Is my new tablet linked yet?"), subject="unknown")
    assert "next_system" not in {k for k, v in case.fields.items() if v is not None}
    assert case.send("ask_system", {"system": "access"}).accepted
    assert case.fields["next_system"] == "access" and case.state == "ASKED"


def test_a_role_goes_to_the_business_system() -> None:
    revoke = ("Verified call", CUSTOMER, "H&V business banking agent", "Please revoke Owen Bell's approver role.")
    case = started(revoke, request_type="instruction", subject="role")
    assert case.fields["next_system"] == "business"  # `role` the value, not the requester's `role`
    assert case.send("submit_request").accepted and case.state == "REQUESTED"


def test_what_the_bank_already_did_outranks_triage() -> None:
    correct = ("Verified call", CUSTOMER, "H&V service agent", "Please correct the spelling of my name.")
    referred = ("Internal note", "H&V service agent", "H&V data team", "I have opened a review of the name correction.")
    case = started(correct, referred, request_type="change", subject="profile")
    assert case.fields["registration_asked"] is True
    assert case.state == "WAITING"  # the review is with the data team: not sent for confirmation as a change


def test_the_bank_may_check_before_an_instruction() -> None:
    duplicate = ("Verified call", CUSTOMER, "H&V service agent", "Remove the duplicate of my £34.80 transfer.")
    case = started(duplicate, request_type="instruction")
    assert case.send("ask_system", {"system": "payment"}).accepted and case.state == "ASKED"


def test_a_fee_is_checked_against_the_tariff() -> None:
    fee = ("Secure chat", CUSTOMER, "H&V service agent", "What is the £3.20 fee on my withdrawal?")
    asked = ("Internal note", "H&V service agent", "H&V transaction records", "Check the fee against the tariff.")
    answered = (
        "Internal note",
        "H&V transaction records",
        "H&V service agent",
        "The £3.20 fee matches the applicable tariff entry.",
    )
    case = started(fee, subject="fee")
    assert case.fields["next_system"] == "tariff" and case.send("ask_system", {"system": "tariff"}).accepted
    case = started(fee, asked, answered, subject="fee")
    assert case.fields["tariff_status"] == "MATCHES" and case.send("reply").accepted and case.state == "REPLIED"


def test_a_review_is_registered_not_asked() -> None:
    case = started(ASK, request_type="register")
    assert not case.send("ask_system", {"system": "payment"}).accepted
    assert case.send("submit_request").accepted and case.state == "REQUESTED"
    assert acts(case) == ["register_request"]


def test_approval_for_someone_else_is_sent_to_that_person() -> None:
    access = ("Secure chat", "Nadia Bell", "H&V business support agent", "Please give my new colleague access.")
    case = started(access, request_type="authority", subject="role")
    assert not case.send("submit_request").accepted  # nothing is granted by the desk
    assert case.send("forward_to_authority").accepted and case.state == "FORWARDED"
    forwarded = case.journal.of("action")[-1].data
    assert (
        forwarded["type"] == "forward_to_authority" and forwarded["args"]["to"] == "the verified company administrator"
    )


def test_the_customer_is_asked_only_while_the_case_names_nothing() -> None:
    declined = ("External message", "Terminal", "Mara", "Payment not accepted. Please contact your bank.")
    case = started(declined, request_type="question", subject="card_payment")
    assert case.send("clarify", {"need": "which_card"}).accepted and case.state == "CLARIFIED"
    text = case.journal.of("action")[-1].data["args"]["text"]
    assert "which card" in text and "never ask for your password, PIN" in text
    assert not started(ASK).send("clarify", {"need": "which_transaction"}).accepted  # £420 to Alder Workshop is named


def test_sign_in_goes_through_the_secure_process() -> None:
    locked = ("Verified call", CUSTOMER, "H&V service agent", "I can't sign in to my profile.")
    assert not started(locked).send("redirect_secure").accepted  # only for access requests
    case = started(locked, request_type="access", subject="access")
    assert case.send("redirect_secure").accepted and case.state == "REDIRECTED"
    assert "secure process" in case.journal.of("action")[-1].data["args"]["text"]


def test_an_unverified_instruction_goes_to_a_person() -> None:
    block = ("External message", CUSTOMER, "Harrow & Vale Bank plc", "Block my card now.")
    case = started(block, request_type="instruction")
    assert case.state == "ESCALATED" and case.fields["reason"] == "UNVERIFIED"


def test_a_change_asked_in_chat_is_sent_for_confirmation() -> None:
    change = ("Secure chat", CUSTOMER, "H&V service agent", "Please change my standing order to £68.00.")
    case = started(change, request_type="change", subject="standing_order")
    assert case.state == "CONFIRMATION_SENT" and acts(case) == ["send_for_confirmation"]


def test_the_agent_can_hand_over() -> None:
    case = started(ASK)
    assert case.send("escalate", {"note": "the customer also disputes a fee"}).accepted
    assert case.state == "ESCALATED" and case.fields["reason"] == "AGENT_ESCALATED"

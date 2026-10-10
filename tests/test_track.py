"""The banking track's policy on synthetic cases: what it decides, and what it refuses."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from desk.classifier import Noul
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
    """Answers the triage; a yes/no it is not told is "no", any other question is not known."""

    def classify(self, text: str, questions: Any) -> Any:
        for name, question in questions.items():
            self.answers.setdefault(name, 0.0 if isinstance(question, Noul) else "unknown")
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
    **yes_no: float,
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
        POLICY,
        FUNCTIONS,
        case_input,
        None,
        Services(Triage({"request_type": request_type, "subject": subject, **yes_no})),
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


def test_a_step_the_bank_took_is_not_taken_again() -> None:
    locked = ("Verified call", CUSTOMER, "H&V service agent", "I can't sign in to my profile.")
    pointed = ("Secure chat", "H&V service agent", CUSTOMER, "I'm directing you to the recovery option in the portal.")
    case = started(locked, pointed, request_type="access", subject="access")
    assert case.fields["bank_redirected"] is True and case.state == "WAITING"
    again = ("Secure chat", CUSTOMER, "H&V service agent", "It still does not work.")
    assert started(locked, pointed, again, request_type="access", subject="access").state == "TRIAGED"


def test_an_instruction_does_not_wait_on_a_case_opened_with_the_team() -> None:
    block = ("Verified call", CUSTOMER, "H&V service agent", "After the identity checks: block my lost card now.")
    opened = (
        "Internal note",
        "H&V service agent",
        "H&V card team",
        "I have opened case HV-022 and registered the request.",
    )
    case = started(block, opened, request_type="instruction", subject="card")
    assert case.fields.get("registration_asked") is True and case.state == "TRIAGED"
    assert case.send("submit_request").accepted


def test_a_profile_change_goes_through_the_protected_process() -> None:
    phone = (
        "Verified call",
        CUSTOMER,
        "H&V service agent",
        "After the identity checks: please change my phone number.",
    )
    case = started(phone, request_type="change", subject="profile")
    assert case.state == "REQUESTED" and acts(case) == ["register_request"]  # not the desk's own confirmation
    opened = ("Internal note", "H&V service agent", "H&V profile change process", "I have opened the change process.")
    assert started(phone, opened, request_type="change", subject="profile").state == "WAITING"


def test_a_change_from_outside_is_not_sent_anywhere_to_confirm() -> None:
    email = ("External message", "Gareth, CEO", "Harrow & Vale Bank plc", "Change the supplier's bank details today.")
    case = started(email, request_type="change", role="Third party")
    assert case.state == "ESCALATED" and case.fields["reason"] == "OUTSIDE_PARTY" and acts(case) == []


def test_an_unverified_profile_change_goes_to_the_secure_process() -> None:
    chat = ("Secure chat", CUSTOMER, "H&V service agent", "I lost my phone; change my number and email here.")
    case = started(chat, request_type="change", subject="profile")
    assert case.state == "REDIRECTED" and acts(case) == ["redirect_secure"]


def test_a_limit_change_is_a_review() -> None:
    chat = ("Secure chat", CUSTOMER, "H&V service agent", "Please raise my overdraft to £2,000.")
    case = started(chat, request_type="change", subject="limit")
    assert case.state == "REQUESTED" and acts(case) == ["register_request"]


def test_no_reply_from_a_record_that_shows_the_requesters_role_revoked() -> None:
    ask = ("Secure chat", "Graham", "H&V service agent", "What is the status of our payroll batch?")
    check = ("Internal note", "H&V service agent", "H&V admin log", "Checking Graham's current role first.")
    answer = ("Internal note", "H&V admin log", "H&V service agent", "Payroll Approver role revoked. No current role.")
    case = started(ask, check, answer, subject="batch")
    assert case.fields.get("business_status") == "ROLE_REVOKED" and not case.send("reply").accepted


def test_an_unavailable_system_is_no_answer() -> None:
    down = (
        "Internal note",
        "H&V transfer journal",
        "H&V service agent",
        "Service temporarily unavailable - no data returned.",
    )
    case = started(ASK, TO_JOURNAL, down)
    assert case.fields.get("payment_status") is None and case.state == "WAITING"


def test_an_answer_told_and_asked_again_is_checked_afresh() -> None:
    told = ("Secure chat", "H&V service agent", CUSTOMER, "Our journal shows it as sent.")
    again = ("Secure chat", CUSTOMER, "H&V service agent", "Three days on, has it arrived yet?")
    case = started(ASK, TO_JOURNAL, FROM_JOURNAL, told, again)
    assert case.fields.get("payment_asked") is None and case.send("ask_system", {"system": "payment"}).accepted


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


def test_an_unverified_instruction_is_not_acted_on_but_sent_to_verify() -> None:
    block = ("External message", CUSTOMER, "Harrow & Vale Bank plc", "Block my card now.")
    case = started(block, request_type="instruction", subject="card")
    assert case.state == "TRIAGED" and not case.send("submit_request").accepted  # nothing is done unverified
    assert case.send("redirect_secure").accepted and case.state == "REDIRECTED"


def test_a_request_of_no_known_type_is_put_to_a_team_never_answered() -> None:
    dsar = ("Secure chat", CUSTOMER, "H&V service agent", "Send me all the personal data you hold on me.")
    case = started(dsar, TO_JOURNAL, FROM_JOURNAL, request_type="other", subject="transfer")
    assert not case.send("reply").accepted
    assert case.send("submit_request").accepted and case.state == "REQUESTED"
    assert case.journal.of("action")[-1].data["args"]["team"]  # a team is named even with no system


def test_a_confirmation_nobody_asked_for_is_passed_on() -> None:
    change = ("Verified call", CUSTOMER, "H&V service agent", "After the identity checks: change my address.")
    opened = ("Internal note", "H&V service agent", "H&V profile change process", "I am opening the change process.")
    confirm = ("Secure portal", CUSTOMER, "H&V profile change process", "I confirm I want the new address used.")
    case = started(change, opened, confirm, request_type="change", subject="profile")
    assert case.fields["confirmation"] == "unprompted" and case.state == "REQUESTED"
    passed_on = ("Internal note", "H&V service agent", "H&V profile change process", "I have submitted the request.")
    case = started(change, opened, confirm, passed_on, request_type="change", subject="profile")
    assert case.fields["confirmation"] == "given" and case.state == "WAITING"  # not passed on a second time


def test_a_change_asked_in_chat_is_sent_for_confirmation() -> None:
    change = ("Secure chat", CUSTOMER, "H&V service agent", "Please change my standing order to £68.00.")
    case = started(change, request_type="change", subject="standing_order")
    assert case.state == "CONFIRMATION_SENT" and acts(case) == ["send_for_confirmation"]


def test_the_agent_can_hand_over() -> None:
    case = started(ASK)
    assert case.send("escalate", {"note": "the customer also disputes a fee"}).accepted
    assert case.state == "ESCALATED" and case.fields["reason"] == "AGENT_ESCALATED"


def refused(case: Case) -> dict[str, Any]:
    return dict(case.journal.of("action")[-1].data["args"])


def test_a_refusal_is_accepted_only_on_the_fact_that_makes_the_request_impossible() -> None:
    code = ("Secure chat", CUSTOMER, "H&V service agent", "Read me the code you just sent so I can verify.")
    assert not started(code).send("refuse", {"reason": "credentials"}).accepted  # no fact: refused
    case = started(code, credentials_requested=0.95)
    assert case.send("refuse", {"reason": "credentials"}).accepted and case.state == "REFUSED"
    args = refused(case)
    assert args["reason"] == "credentials" and "never ask for or read out" in args["text"] and "portal" in args["text"]


def test_someone_elses_account_is_refused_only_to_a_third_party() -> None:
    landlord = ("External message", "Landlord", "Harrow & Vale Bank plc", "Has my tenant paid the rent?")
    assert not started(landlord).send("refuse", {"reason": "someone_elses_account"}).accepted
    case = started(landlord, role="Third party")
    assert case.send("refuse", {"reason": "someone_elses_account"}).accepted and case.outcome == "refuse"


def test_the_other_reasons_need_their_facts() -> None:
    joint = ("Secure chat", CUSTOMER, "H&V service agent", "Remove my ex from our joint account.")
    assert not started(joint, request_type="instruction").send("refuse", {"reason": "needs_all_holders"}).accepted
    case = started(joint, request_type="instruction", joint_holder_change=0.9)
    assert case.send("refuse", {"reason": "needs_all_holders"}).accepted
    assert not started(ASK).send("refuse", {"reason": "other"}).accepted  # only a request of no known type
    assert started(ASK, request_type="other").send("refuse", {"reason": "other"}).accepted
    assert not started(ASK).send("refuse", {"reason": "no_authority"}).accepted

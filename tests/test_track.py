"""The track's rules and functions: what pays, what goes to a person, and that a payment is made once."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from desk.machine import Case, Services, load_functions
from desk.policy import load_policy
from desk.runner import load_data
from tests.conftest import FakeClassifier

TRACK = Path(__file__).resolve().parents[1] / "track"
POLICY = load_policy(TRACK / "policy.yaml")
FUNCTIONS, MODULE = load_functions(TRACK / "functions.py")
WORLD = load_data(TRACK / "world.json")


def started(category: str = "payment", sender: str = "ana.lopes@example.com", **request: Any) -> Case:
    request = {"amount": "120.00", "payee": "P-ENERGY", **request}
    case_input = {"id": "t", "from": sender, "text": "x", "request": request}
    machine = Case(POLICY, FUNCTIONS, case_input, WORLD, Services(FakeClassifier({"category": category})))
    machine.start()
    return machine


def payments(case: Case) -> list[dict[str, Any]]:
    return [e.data["args"] for e in case.journal.of("action") if e.data["type"] == "payment"]


def test_a_payment_within_the_limit_is_made_once() -> None:
    case = started()
    assert case.state == "TRIAGED"
    assert case.send("pay").accepted and case.state == "DONE" and case.fields["paid"] is True
    assert not case.send("pay").accepted  # the case has moved on: a second pay is refused
    assert [(p["payee"], p["amount"]) for p in payments(case)] == [("P-ENERGY", "120.00")]


def test_over_the_limit_goes_to_a_person() -> None:
    case = started(amount="900.00")
    assert case.state == "ESCALATED" and case.fields["reason"] == "OVER_LIMIT" and not payments(case)


def test_a_payee_the_customer_does_not_have_goes_to_a_person() -> None:
    case = started(payee="P-UNKNOWN")
    assert case.state == "ESCALATED" and case.fields["reason"] == "UNKNOWN_PAYEE"


def test_a_sender_who_is_not_a_customer_goes_to_a_person() -> None:
    case = started(sender="someone@example.net")
    assert case.state == "ESCALATED" and case.fields["reason"] == "UNKNOWN_CUSTOMER"


def test_pay_is_refused_for_anything_but_a_payment() -> None:
    case = started(category="question")
    refused = case.send("pay")
    assert not refused.accepted and refused.reason is not None and "category = payment" in refused.reason
    assert case.send("escalate", {"note": "a question for a person"}).accepted
    assert case.fields["reason"] == "AGENT_ESCALATED" and not payments(case)

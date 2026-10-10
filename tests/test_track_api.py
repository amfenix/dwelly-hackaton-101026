"""Synthetic contract tests for the banking track's event readers and actions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from desk import CaseError, ModelError
from desk.calls import CallRecord, Recorder
from desk.classifier import ClaudeClassifier, JevClassifier
from desk.machine import load_functions
from tests.conftest import FakeAnthropic, FakeTypeSafe, text_reply

TRACK = Path(__file__).resolve().parents[1] / "track"
FUNCTIONS, _ = load_functions(TRACK / "functions.py")
BANKING_CASES = json.loads((TRACK / "cases.json").read_text(encoding="utf-8"))


class Probe:
    def __init__(self, case: dict[str, Any], fields: dict[str, Any] | None = None) -> None:
        self.case = case
        self.fields = fields or {}
        self.notes: list[str] = []
        self.actions: list[dict[str, Any]] = []
        self.state = "NEW"
        self.key = "test-key"

    def note(self, text: str) -> None:
        self.notes.append(text)

    def act(self, type_: str, **args: Any) -> None:
        self.actions.append({"type": type_, "args": args})


class ClassifyingProbe(Probe):
    def __init__(self, case: dict[str, Any], answer: Any) -> None:
        super().__init__(case)
        self.answer = answer
        self.classifications: list[tuple[str, dict[str, Any]]] = []

    def classify(self, text: str, questions: dict[str, Any]) -> dict[str, Any]:
        self.classifications.append((text, questions))
        return {"status": self.answer, "confirmation": self.answer}


class AdapterProbe(Probe):
    def __init__(self, case: dict[str, Any], classifier: Any) -> None:
        super().__init__(case)
        self.classifier = classifier

    def classify(self, text: str, questions: dict[str, Any]) -> dict[str, Any]:
        return self.classifier.classify(text, questions)


def event(
    seq: int,
    kind: str,
    sender: str,
    recipient: str,
    text: str,
    channel: str = "Internal note",
) -> dict[str, Any]:
    return {
        "seq": seq,
        "at": f"2025-09-{seq:02d}T09:00:00Z",
        "channel": channel,
        "kind": kind,
        "from": sender,
        "to": recipient,
        "extra": {},
        "text": text,
    }


def case(
    *events: dict[str, Any], request: str = "Please check my transfer.", attachments: list[Any] | None = None
) -> dict[str, Any]:
    return {
        "id": "synthetic-001-at-04",
        "track": "Banking & Financial Services",
        "case": "001",
        "point": len(events),
        "title": "Synthetic",
        "details": {"Source role": "Bank customer", "Bank": "Harrow & Vale Bank plc"},
        "request": request,
        "events": list(events),
        "attachments": attachments or [],
    }


def invoke(name: str, data: dict[str, Any], fields: dict[str, Any] | None = None) -> tuple[dict[str, Any], Probe]:
    probe = Probe(data, fields)
    return FUNCTIONS[name](probe), probe


def banking_point(case_id: str, point: int) -> dict[str, Any]:
    return next(item for item in BANKING_CASES if item["case"] == case_id and item["point"] == point)


@pytest.mark.parametrize(
    "name",
    [
        "identify_requester",
        "find_subject",
        "check_payment",
        "check_incoming",
        "check_recurring",
        "check_card",
        "check_access",
        "check_business",
        "check_documents",
        "check_tariff",
        "check_registration",
        "check_confirmation",
    ],
)
def test_readers_reject_a_missing_event_list(name: str) -> None:
    with pytest.raises(CaseError, match=r"case\.events"):
        FUNCTIONS[name](Probe({"request": "x"}))


def test_missing_event_text_is_a_case_error() -> None:
    with pytest.raises(CaseError, match="must have text"):
        FUNCTIONS["find_subject"](Probe(case({"seq": 1, "kind": "conversation"})))


def test_event_history_must_be_a_list() -> None:
    with pytest.raises(CaseError, match=r"case\.events"):
        FUNCTIONS["find_subject"](Probe({"events": (), "request": "x"}))


def test_requester_subject_and_channel_are_from_the_customer_conversation() -> None:
    data = case(
        event(1, "conversation", "Harrow & Vale Bank plc", "Mara Ellison", "A portal notice.", "Secure portal"),
        event(
            2,
            "conversation",
            "Mara Ellison",
            "H&V service agent",
            "I need my £420 transfer to Alder & Reed Workshop checked on 14 July 2025.",
            "Secure chat",
        ),
    )
    requester, requester_probe = invoke("identify_requester", data)
    structured, subject_probe = invoke("find_subject", data)
    assert requester == {
        "requester": "Mara Ellison",
        "role": "customer",
        "channel": "secure_chat",
        "verified": False,
    }
    assert structured == {
        "amount": "420.00",
        "counterparty": "Alder & Reed Workshop",
        "subject_date": "2025-07-14",
    }
    assert "subject" not in structured
    assert all("event 2" in note for note in requester_probe.notes + subject_probe.notes)


@pytest.mark.parametrize(
    ("text", "role"),
    [
        ("I am the company's authorised file uploader; check batch receipt.", "uploader"),
        ("I'm the company signatory for this payment; check its stage.", "signatory"),
        ("I'm authorised to view our payment limit; please confirm it.", "viewer"),
        ("I am the verified business administrator; revoke the old role.", "business_admin"),
    ],
)
def test_requester_role_uses_the_requester_self_description(text: str, role: str) -> None:
    facts, _ = invoke("identify_requester", case(event(1, "conversation", "Mara Ellison", "H&V", text, "Secure chat")))
    assert facts["role"] == role


def test_requester_uses_bank_authored_identity_check_and_source_role() -> None:
    data = case(
        event(
            1,
            "conversation",
            "H&V agent",
            "Mara Ellison",
            "I have completed H&V's identity checks in this secure chat.",
            "Secure chat",
        ),
        event(2, "conversation", "Mara Ellison", "H&V agent", "Please check the record.", "Secure chat"),
    )
    data["details"]["Source role"] = "Business administrator"
    facts, _ = invoke("identify_requester", data)
    assert facts["verified"] is True
    assert facts["role"] == "business_admin"


def test_requester_mentions_do_not_create_viewer_or_third_party_role() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "Please send the report to our viewer; a third party may read it.",
            "Secure chat",
        )
    )
    facts, _ = invoke("identify_requester", data)
    assert facts["role"] == "customer"


def test_subject_extraction_does_not_turn_references_or_dates_into_money() -> None:
    facts, _ = invoke(
        "find_subject",
        case(
            event(
                1,
                "conversation",
                "Mara Ellison",
                "H&V",
                "Please review case HV-041 dated 14 July 2025; the amount is not shown.",
                "Secure chat",
            )
        ),
    )
    assert "amount" not in facts and facts["reference"] == "HV-041" and facts["subject_date"] == "2025-07-14"


def test_subject_amount_prefers_requested_change_over_current_value() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I want to increase the standing order to £68.00; the portal still shows £42.00.",
            "Secure chat",
        )
    )
    facts, probe = invoke("find_subject", data)
    assert facts["amount"] == "68.00"
    assert any("event 1" in note for note in probe.notes)


def test_subject_evidence_uses_first_customer_request_and_initial_request_label() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "Please check my £420 payment to Alder Workshop.",
            "Secure chat",
        ),
        event(2, "conversation", "Mara Ellison", "H&V", "Any update?", "Secure chat"),
    )
    _, probe = invoke("find_subject", data)
    assert all("event 1" in note for note in probe.notes)

    initial, initial_probe = invoke("find_subject", case(request="Please check the £420 payment to Alder Workshop."))
    assert initial["amount"] == "420.00"
    assert any("initial request" in note for note in initial_probe.notes)


def test_customer_claim_does_not_create_a_payment_fact() -> None:
    data = case(event(1, "conversation", "Mara Ellison", "H&V service agent", "The transfer was sent.", "Secure chat"))
    facts, _ = invoke("check_payment", data)
    assert facts == {}


def test_payment_asked_answer_and_unknown_answer_are_sequenced() -> None:
    asked = case(event(1, "system", "H&V service agent", "H&V transfer journal", "Please check the transfer."))
    facts, probe = invoke("check_payment", asked)
    assert facts == {"payment_asked": True}
    assert "H&V transfer journal" in probe.notes[0]

    answered = case(
        event(1, "system", "H&V service agent", "H&V transfer journal", "Please check the transfer."),
        event(2, "system", "H&V transfer journal", "H&V service agent", "Transfer status: SENT."),
    )
    facts, _ = invoke("check_payment", answered)
    assert facts == {"payment_asked": True, "payment_status": "SENT"}

    other = case(
        event(1, "system", "H&V service agent", "H&V transfer journal", "Please check the transfer."),
        event(2, "system", "H&V transfer journal", "H&V service agent", "Purpose: deposit for a kiln repair."),
    )
    facts, probe = invoke("check_payment", other)
    assert facts["payment_status"] == "OTHER"
    assert any("Purpose: deposit" in note for note in probe.notes)


def test_payment_count_and_pending_are_read_from_the_same_system_answer() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V payment instruction journal", "Check the instructions."),
        event(
            2,
            "system",
            "H&V payment instruction journal",
            "H&V agent",
            "Journal match: two distinct instruction references. One instruction is Completed; the other is Pending.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts["payment_status"] == "OTHER" and facts["payment_count"] == 2


def test_multiple_transfers_are_counted() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V payment instruction journal", "Check the transfers."),
        event(2, "system", "H&V payment instruction journal", "H&V agent", "Two separate transfers were completed."),
    )
    facts, _ = invoke("check_payment", data)
    assert facts["payment_count"] == 2 and facts["payment_status"] == "COMPLETED"


def test_mixed_instruction_statuses_remain_aggregate_other() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V payment instruction journal", "Check the instructions."),
        event(
            2,
            "system",
            "H&V payment instruction journal",
            "H&V agent",
            "Two separate payment instructions: one COMPLETED and one PENDING.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts["payment_count"] == 2 and facts["payment_status"] == "OTHER"


def test_protected_instruction_process_alias_matches_instruction_log() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V protected instruction process", "Submit cancellation."),
        event(2, "system", "H&V instruction log", "H&V agent", "HV-013 — Future run cancelled."),
    )
    facts, _ = invoke("check_recurring", data)
    assert facts == {"recurring_asked": True, "recurring_status": "CANCELLED"}


def test_case_record_quote_uses_the_pending_system_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V signing log", "Check the signing queue."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-043",
            "The queue shows no second consent and no individual payment submissions.",
        ),
    )
    facts, _ = invoke("check_business", data)
    assert facts == {"business_asked": True, "business_status": "AWAITING_SECOND_SIGNATORY"}


def test_unquoted_case_record_claim_does_not_answer_a_pending_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-123",
            "Customer says the transfer was SENT; HV-123 is awaiting the journal answer.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_quoted_case_record_claim_does_not_answer_a_pending_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-123",
            "Customer says the transfer journal shows SENT; awaiting journal answer.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_case_record_result_from_another_domain_does_not_answer_the_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-123",
            "The card status record shows REJECTED for case HV-123.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_named_case_record_question_is_not_an_answer() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-123",
            "I asked the transfer journal whether the payment was sent.",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Check whether the transfer journal shows SENT.", {"payment_asked": True}),
        ("Does the transfer journal show SENT?", {"payment_asked": True}),
        ("Does the transfer journal show SENT", {"payment_asked": True}),
        ("The transfer journal shows SENT?", {"payment_asked": True}),
        (
            "Does the transfer journal show SENT? The transfer journal shows PENDING.",
            {"payment_asked": True, "payment_status": "PENDING"},
        ),
        (
            "The transfer journal shows SENT?\nThe transfer journal shows PENDING.",
            {"payment_asked": True, "payment_status": "PENDING"},
        ),
        ("The transfer journal shows SENT.", {"payment_asked": True, "payment_status": "SENT"}),
    ],
)
def test_case_record_requires_a_positive_result_attribution(text: str, expected: dict[str, Any]) -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(2, "system", "H&V agent", "H&V case record HV-123", text),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == expected


def test_shared_reference_uses_the_answer_domain_before_consuming_a_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(2, "system", "H&V agent", "H&V card journal", "Check card HV-123."),
        event(
            3,
            "system",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Card status: REJECTED. Case HV-123.",
            "Secure portal",
        ),
        event(4, "system", "H&V transfer journal", "H&V agent", "Transfer status: SENT."),
    )
    payment, _ = invoke("check_payment", data)
    card, _ = invoke("check_card", data)
    assert payment["payment_status"] == "SENT"
    assert card["card_status"] == "OTHER"


def test_card_portal_domain_does_not_consume_a_transfer_with_a_shared_reference() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(2, "system", "H&V agent", "H&V card journal", "Check card HV-123."),
        event(
            3,
            "system",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Card payment status: DECLINED. Case HV-123.",
            "Secure portal",
        ),
        event(4, "system", "H&V transfer journal", "H&V agent", "Transfer status: SENT."),
    )
    payment, _ = invoke("check_payment", data)
    card, _ = invoke("check_card", data)
    assert payment["payment_status"] == "SENT"
    assert card["card_status"] == "DECLINED"


def test_payment_portal_case_reference_is_not_registration() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(
            2,
            "system",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Payment status: SENT. Case HV-123.",
            "Secure portal",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True, "payment_status": "SENT"}


def test_conflicting_portal_status_domains_consume_neither_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check transfer HV-123."),
        event(2, "system", "H&V agent", "H&V card journal", "Check card HV-123."),
        event(
            3,
            "system",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Card status: DECLINED. Payment status: SENT. Case HV-123.",
            "Secure portal",
        ),
    )
    payment, _ = invoke("check_payment", data)
    card, _ = invoke("check_card", data)
    assert payment == {"payment_asked": True}
    assert card == {"card_asked": True}


def test_incoming_portal_status_is_not_generic_payment_status() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V incoming-payment journal", "Check incoming payment HV-123."),
        event(
            2,
            "system",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Incoming payment status: FOUND. Case HV-123.",
            "Secure portal",
        ),
    )
    facts, _ = invoke("check_incoming", data)
    assert facts == {"incoming_asked": True, "incoming_found": True}


def test_bank_portal_system_record_matches_by_requested_reference() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V import service", "Retrieve validation report HV-042."),
        event(
            2,
            "system",
            "Harrow & Vale Bank plc",
            "Nadia Fenwick",
            "Validation report validation-042.txt for batch HV-042 is available; validation FAILED.",
            "Business portal",
        ),
    )
    facts, _ = invoke("check_business", data)
    assert facts == {"business_asked": True, "business_status": "VALIDATION_FAILED"}


def test_same_bank_portal_body_as_conversation_is_not_a_system_answer() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V import service", "Retrieve validation report HV-042."),
        event(
            2,
            "conversation",
            "Harrow & Vale Bank plc",
            "Nadia Fenwick",
            "Validation report validation-042.txt for batch HV-042 is available; validation FAILED.",
            "Business portal",
        ),
    )
    facts, _ = invoke("check_business", data)
    assert facts == {"business_asked": True}


def test_generated_document_is_ready_but_name_still_requires_an_attachment() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V document service", "Generate the record."),
        event(2, "system", "H&V document service", "H&V agent", "Record HV-040 generated; status is SENT."),
    )
    facts, _ = invoke("check_documents", data)
    assert facts == {"documents_asked": True, "document_ready": True}


def test_document_not_generated_is_not_ready() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V document service", "Generate the record."),
        event(2, "system", "H&V document service", "H&V agent", "The document has not been generated."),
    )
    facts, _ = invoke("check_documents", data)
    assert facts == {"documents_asked": True, "document_ready": False}


def test_unknown_status_uses_one_choice_on_the_system_answer_and_invalid_is_other() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V card journal", "Check the card."),
        event(2, "system", "H&V card journal", "H&V agent", "The card is in a special queue."),
    )
    probe = ClassifyingProbe(data, type("Answer", (), {"value": "NOT_A_CARD_STATUS"})())
    facts = FUNCTIONS["check_card"](probe)
    assert facts["card_status"] == "OTHER"
    assert len(probe.classifications) == 1
    text, questions = probe.classifications[0]
    assert text == "The card is in a special queue." and set(questions) == {"status"}


@pytest.mark.parametrize("backend", ["jev", "claude"])
def test_unknown_status_uses_each_fake_classifier_and_replays_once(backend: str) -> None:
    if backend == "jev":
        body: dict[str, Any] = {
            "model": "jev-1.13.0",
            "usage": {"input_tokens": 1, "output_tokens": 1},
            "answers": {"status": {"type": "choice", "choice": "OTHER", "confidence": 0.9, "probabilities": {}}},
        }
        recorder = Recorder()
        classifier = JevClassifier(recorder, client=FakeTypeSafe(body))
    else:
        recorder = Recorder()
        classifier = ClaudeClassifier(recorder, client=FakeAnthropic(text_reply('{"status":"OTHER"}')))

    data = case(
        event(1, "system", "H&V agent", "H&V card journal", "Check the card."),
        event(2, "system", "H&V card journal", "H&V agent", "The card is in a special queue."),
    )
    probe = AdapterProbe(data, classifier)
    assert FUNCTIONS["check_card"](probe)["card_status"] == "OTHER"
    assert len(recorder.calls) == 1 and recorder.calls[0].kind == "classify"

    saved = [CallRecord.from_json(json.loads(json.dumps(record.to_json()))) for record in recorder.calls]
    replay_recorder = Recorder(replay=saved)
    replay_classifier = JevClassifier(replay_recorder) if backend == "jev" else ClaudeClassifier(replay_recorder)
    replay_probe = AdapterProbe(data, replay_classifier)
    assert FUNCTIONS["check_card"](replay_probe)["card_status"] == "OTHER"
    assert replay_recorder.calls[0].replayed and replay_recorder.unused() == 0


def test_classifier_rejects_an_invalid_enum_before_the_reader_can_use_it() -> None:
    client = FakeAnthropic(text_reply('{"status":"NOT_A_CARD_STATUS"}'))
    probe = AdapterProbe(
        case(
            event(1, "system", "H&V agent", "H&V card journal", "Check the card."),
            event(2, "system", "H&V card journal", "H&V agent", "The card is in a special queue."),
        ),
        ClaudeClassifier(Recorder(), client=client),
    )
    with pytest.raises(ModelError, match="not one of"):
        FUNCTIONS["check_card"](probe)


def test_an_answer_before_its_request_is_not_a_fact() -> None:
    data = case(
        event(1, "system", "H&V transfer journal", "H&V service agent", "Transfer status: SENT."),
        event(2, "system", "H&V service agent", "H&V transfer journal", "Please check the transfer."),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_negative_status_and_quoted_case_record_answer() -> None:
    not_sent = case(
        event(1, "system", "H&V service agent", "H&V transfer journal", "Check it."),
        event(2, "system", "H&V transfer journal", "H&V service agent", "The transfer was not sent."),
    )
    facts, _ = invoke("check_payment", not_sent)
    assert facts["payment_status"] == "OTHER"

    quoted = case(
        event(1, "system", "H&V agent", "H&V import journal", "Check batch receipt."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record HV-041",
            "I found an import-journal entry recording receipt of batch-041.csv.",
        ),
    )
    facts, _ = invoke("check_business", quoted)
    assert facts == {"business_asked": True, "business_status": "RECEIVED"}


def test_conversation_case_record_quote_is_not_a_system_answer() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check the transfer."),
        event(
            2,
            "conversation",
            "Mara Ellison",
            "H&V case record HV-001",
            "Transfer journal says SENT.",
            "Secure chat",
        ),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_answer_from_an_unrelated_endpoint_does_not_match_the_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V transfer journal", "Check the transfer."),
        event(2, "system", "H&V payment team", "H&V agent", "Payment completed."),
    )
    facts, _ = invoke("check_payment", data)
    assert facts == {"payment_asked": True}


def test_explicit_system_aliases_match_answers() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V incoming-payment journal", "Check the credit."),
        event(2, "system", "H&V incoming-payment system", "H&V agent", "Credit found."),
    )
    facts, _ = invoke("check_incoming", data)
    assert facts == {"incoming_asked": True, "incoming_found": True}


@pytest.mark.parametrize(
    ("name", "to", "asked"),
    [
        ("check_incoming", "H&V incoming-payment journal", "incoming_asked"),
        ("check_recurring", "H&V standing-order journal", "recurring_asked"),
        ("check_card", "H&V card journal", "card_asked"),
        ("check_access", "H&V access log", "access_asked"),
        ("check_business", "H&V signing log", "business_asked"),
        ("check_documents", "H&V document service", "documents_asked"),
    ],
)
def test_each_system_reader_reports_asked_without_an_answer(name: str, to: str, asked: str) -> None:
    facts, _ = invoke(name, case(event(1, "system", "H&V service agent", to, "Please check this record.")))
    assert facts == {asked: True}


@pytest.mark.parametrize(
    ("name", "to", "claim"),
    [
        ("check_incoming", "H&V incoming-payment journal", "I received the incoming payment."),
        ("check_recurring", "H&V standing-order journal", "The standing order is active."),
        ("check_card", "H&V card journal", "The card was dispatched."),
        ("check_access", "H&V access log", "Access was restored."),
        ("check_business", "H&V signing log", "The package is received."),
        ("check_documents", "H&V document service", "The document is available."),
    ],
)
def test_each_system_reader_ignores_a_customer_status_claim(name: str, to: str, claim: str) -> None:
    facts, _ = invoke(name, case(event(1, "conversation", "Mara Ellison", "H&V service agent", claim, "Secure chat")))
    assert facts == {}


@pytest.mark.parametrize(
    ("name", "to", "answer", "field"),
    [
        ("check_recurring", "H&V standing-order journal", "Status: unknown.", "recurring_status"),
        ("check_card", "H&V card journal", "Status: queued for a manual review.", "card_status"),
        ("check_access", "H&V access log", "The record is under manual review.", "access_status"),
        ("check_business", "H&V signing log", "Status: queued for manual review.", "business_status"),
    ],
)
def test_enum_readers_preserve_unlisted_answers_as_other(name: str, to: str, answer: str, field: str) -> None:
    data = case(
        event(1, "system", "H&V agent", to, "Please check this record."),
        event(2, "system", to, "H&V agent", answer),
    )
    facts, _ = invoke(name, data)
    assert facts[field] == "OTHER"


@pytest.mark.parametrize(
    ("name", "to", "answer", "expected"),
    [
        (
            "check_incoming",
            "H&V incoming-payment journal",
            "No identifiable incoming credit is shown.",
            {"incoming_found": False},
        ),
        (
            "check_recurring",
            "H&V standing-order journal",
            "The standing order is active; next run is 2025-09-03.",
            {"recurring_status": "ACTIVE", "next_run": "2025-09-03"},
        ),
        ("check_card", "H&V card journal", "Dispatch status: registered.", {"card_status": "DISPATCHED"}),
        ("check_access", "H&V access log", "The procedure started.", {"access_status": "PROCEDURE_STARTED"}),
        (
            "check_business",
            "H&V limit register",
            "The maximum is £20,000 per outgoing payment.",
            {"business_limit": "20000.00"},
        ),
        (
            "check_business",
            "H&V import service",
            "Validation report validation-042.txt for batch HV-042 is available; validation status: FAILED.",
            {"business_status": "VALIDATION_FAILED"},
        ),
        (
            "check_documents",
            "H&V statements service",
            "The statement is available.",
            {"document_ready": True, "document_name": "statement.pdf"},
        ),
        (
            "check_registration",
            "H&V Direct Debit team",
            "The review request is registered under HV-016.",
            {"registered": True, "registration_ref": "HV-016"},
        ),
    ],
)
def test_each_system_reader_extracts_its_answer(name: str, to: str, answer: str, expected: dict[str, Any]) -> None:
    attachments = [{"name": "statement.pdf", "path": "statement.pdf"}] if name == "check_documents" else []
    data = case(
        event(
            1,
            "system",
            "H&V agent",
            to,
            "Please register the review request." if name == "check_registration" else "Please check this record.",
        ),
        event(2, "system", to, "H&V agent", answer),
        attachments=attachments,
    )
    facts, _ = invoke(name, data)
    for key, value in expected.items():
        assert facts[key] == value


def test_registration_routing_and_confirmation_sequence() -> None:
    registration = case(
        event(1, "system", "H&V agent", "H&V data team", "I opened a protected name review."),
        event(2, "system", "H&V data team", "H&V agent", "The request was received for review."),
    )
    facts, _ = invoke("check_registration", registration)
    assert facts["registration_asked"] is True and facts["registered"] is True

    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I want to increase the standing order; chat is not authorisation.",
            "Secure chat",
        ),
        event(2, "conversation", "H&V agent", "Mara Ellison", "I sent the change for confirmation.", "Secure portal"),
        event(3, "conversation", "Mara Ellison", "H&V", "I confirm the change.", "Secure portal"),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts == {"confirmation": "given", "instructed_outside_portal": True}


@pytest.mark.parametrize(
    "text", ["I do not approve the change.", "I don't confirm it.", "The change is not yet confirmed."]
)
def test_confirmation_negation_is_not_given(text: str) -> None:
    data = case(
        event(1, "conversation", "H&V agent", "Mara Ellison", "I sent the change for confirmation.", "Secure portal"),
        event(2, "conversation", "Mara Ellison", "H&V", text, "Secure portal"),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "requested"


def test_document_name_must_be_an_available_attachment() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V document service", "Place the report."),
        event(2, "system", "H&V document service", "H&V agent", "Report report-001.pdf is available."),
    )
    facts, _ = invoke("check_documents", data)
    assert facts == {"documents_asked": True, "document_ready": True}


def test_negated_access_status_is_other() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V access log", "Check access."),
        event(2, "system", "H&V access log", "H&V agent", "Access has not been restored."),
    )
    facts, _ = invoke("check_access", data)
    assert facts["access_status"] == "OTHER"


def test_a_bank_status_notice_is_not_a_change_confirmation_request() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Harrow & Vale Bank plc",
            "Mara Ellison",
            "Transfer status: sent. This confirms the transfer status.",
            "Secure portal",
        )
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "none"


def test_briefing_contains_only_conversation_text() -> None:
    data = case(
        event(1, "conversation", "Mara Ellison", "H&V", "Please check my transfer.", "Secure chat"),
        event(2, "system", "H&V agent", "H&V transfer journal", "SECRET INTERNAL ANSWER"),
    )
    probe = Probe(data, {"subject": "transfer", "payment_status": "SENT"})
    text = FUNCTIONS["brief"](probe)
    assert "Please check my transfer." in text
    assert "SECRET INTERNAL ANSWER" not in text
    assert "payment_status" in text


@pytest.mark.parametrize(
    ("name", "fields", "action", "expected"),
    [
        (
            "ask_system",
            {"next_system": "payment", "subject": "transfer", "amount": "420.00"},
            "ask_system",
            {"system": "payment", "about": "transfer", "amount": "420.00"},
        ),
        (
            "register_request",
            {"next_system": "registration", "subject": "direct_debit", "reference": "HV-016"},
            "register_request",
            {"team": "registration", "about": "direct_debit", "reference": "HV-016"},
        ),
        (
            "send_for_confirmation",
            {"requester": "Mara", "subject": "standing_order", "amount": "68.00"},
            "send_for_confirmation",
            {"to": "Mara"},
        ),
    ],
)
def test_actions_read_fields_only(name: str, fields: dict[str, Any], action: str, expected: dict[str, Any]) -> None:
    probe = Probe(case(), fields)
    assert FUNCTIONS[name](probe) == {}
    if name == "send_for_confirmation":
        expected = {"change": "standing_order, amount=68.00", "to": "Mara"}
    assert probe.actions == [{"type": action, "args": expected}]


def test_reply_is_three_parts_and_does_not_use_agent_words() -> None:
    fields = {
        "requester": "Mara",
        "channel": "secure_portal",
        "next_system": "payment",
        "subject": "transfer",
        "amount": "420.00",
        "counterparty": "Alder & Reed Workshop",
        "payment_status": "SENT",
    }
    probe = Probe(case(), fields)
    assert FUNCTIONS["reply_customer"](probe) == {}
    text = probe.actions[0]["args"]["text"]
    assert text.count(".") >= 3
    assert "recipient bank" in text and "No new transfer was made" in text


def test_reply_dispatches_by_next_system() -> None:
    fields = {
        "requester": "Mara",
        "channel": "secure_portal",
        "next_system": "documents",
        "subject": "document",
        "document_ready": True,
        "payment_status": "SENT",
    }
    probe = Probe(case(), fields)
    FUNCTIONS["reply_customer"](probe)
    text = probe.actions[0]["args"]["text"]
    assert "document record" in text and "payment record" not in text


@pytest.mark.parametrize(
    "text",
    [
        "Please increase the standing-order amount from £42 to £68.",
        "The current amount is £42. Please set the amount to £68.",
        "I want to increase the standing order to £68. The portal still shows £42.",
    ],
)
def test_change_amount_uses_local_from_and_to_context(text: str) -> None:
    facts, _ = invoke("find_subject", case(event(1, "conversation", "Mara", "H&V", text, "Secure chat")))
    assert facts["amount"] == "68.00"


@pytest.mark.parametrize(
    ("kind", "text"),
    [
        ("system", "Identity checks have been completed."),
        ("conversation", "I\u2019ve completed H&V\u2019s identity checks in this secure chat."),
    ],
)
def test_completed_identity_check_retains_the_bank_event_as_evidence(kind: str, text: str) -> None:
    data = case(
        event(1, "conversation", "Mara", "H&V", "Please check it.", "Secure chat"),
        event(2, kind, "H&V agent", "H&V case record", text, "Secure chat"),
    )
    facts, probe = invoke("identify_requester", data)
    assert facts["verified"] is True
    assert "event 2" in probe.notes[-1]


@pytest.mark.parametrize(
    "text",
    [
        "Where is the confirmation button?",
        "How do I confirm it",
        "I confirm?",
        "Approval is pending.",
        "I confirm receipt of your message.",
    ],
)
def test_confirmation_requires_an_affirmative_statement(text: str) -> None:
    data = case(
        event(1, "conversation", "H&V agent", "Mara", "I sent the change for confirmation.", "Secure portal"),
        event(2, "conversation", "Mara", "H&V", text, "Secure portal"),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "requested"


@pytest.mark.parametrize("backend", ["jev", "claude"])
def test_confirmation_uses_a_fake_classifier_only_for_a_later_secure_portal_customer_message(backend: str) -> None:
    data = case(
        event(1, "conversation", "Mara", "H&V", "I confirm the change.", "Secure portal"),
        event(2, "conversation", "H&V agent", "Mara", "I sent the change for confirmation.", "Secure portal"),
        event(
            3,
            "conversation",
            "Mara",
            "H&V",
            "The amended amount is acceptable and authorised.",
            "Secure portal",
        ),
    )
    recorder = Recorder()
    if backend == "jev":
        client = FakeTypeSafe(
            {
                "model": "jev-1.13.0",
                "usage": {"input_tokens": 1, "output_tokens": 1},
                "answers": {
                    "confirmation": {
                        "type": "choice",
                        "choice": "GIVEN",
                        "confidence": 0.9,
                        "probabilities": {},
                    }
                },
            }
        )
        classifier = JevClassifier(recorder, client=client)
    else:
        classifier = ClaudeClassifier(
            recorder,
            client=FakeAnthropic(text_reply('{"confirmation":"GIVEN"}')),
        )
    facts = FUNCTIONS["check_confirmation"](AdapterProbe(data, classifier))
    assert facts == {"confirmation": "given", "instructed_outside_portal": False}
    assert len(recorder.calls) == 1


def test_confirmation_classifier_overrides_a_receipt_acknowledgement_fast_path() -> None:
    data = case(
        event(1, "conversation", "H&V agent", "Mara", "I sent the change for confirmation.", "Secure portal"),
        event(2, "conversation", "Mara", "H&V", "I confirm receipt of your message.", "Secure portal"),
    )
    answer = type("Answer", (), {"value": "NOT_GIVEN"})()
    probe = ClassifyingProbe(data, answer)
    facts = FUNCTIONS["check_confirmation"](probe)
    assert facts["confirmation"] == "requested"
    assert len(probe.classifications) == 1


def test_business_portal_is_not_secure_portal_change_confirmation() -> None:
    data = case(
        event(1, "conversation", "H&V agent", "Mara", "I sent the change for confirmation.", "Secure portal"),
        event(2, "conversation", "Mara", "H&V", "I confirm the change.", "Business portal"),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "requested"


def test_request_reference_and_long_date_evidence_are_preserved() -> None:
    data = case(
        event(1, "conversation", "Mara", "H&V", "Any update?", "Secure chat"),
        event(2, "conversation", "Mara", "H&V", "The transfer was on 3 September 2025.", "Secure chat"),
        request="Please check transfer HV-123.",
    )
    facts, probe = invoke("find_subject", data)
    assert facts["reference"] == "HV-123" and facts["subject_date"] == "2025-09-03"
    assert any("initial request" in note and "HV-123" in note for note in probe.notes)
    assert "event 2" in probe.notes[-1]


@pytest.mark.parametrize(
    ("subject", "field", "status"),
    [
        ("standing_order", "recurring_status", "CANCELLED"),
        ("role", "business_status", "ROLE_REVOKED"),
        ("access", "access_status", "RESTORED"),
        ("card", "card_status", "BLOCKED"),
    ],
)
def test_reply_does_not_deny_a_recorded_change(subject: str, field: str, status: str) -> None:
    system = {
        "recurring_status": "recurring",
        "business_status": "business",
        "access_status": "access",
        "card_status": "card",
    }[field]
    facts = {"requester": "Mara", "channel": "secure_portal", "next_system": system, "subject": subject, field: status}
    _, probe = invoke("reply_customer", case(), facts)
    assert "additional" in probe.actions[0]["args"]["text"]


def test_permitted_card_restriction_category_maps_to_restricted() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V card journal", "Check the permitted category."),
        event(
            2, "system", "H&V card journal", "H&V agent", "Permitted category: temporary security-related restriction."
        ),
    )
    facts, _ = invoke("check_card", data)
    assert facts["card_status"] == "RESTRICTED"


@pytest.mark.parametrize(
    ("case_id", "point", "reader", "expected"),
    [
        ("030", 4, "check_card", {"card_asked": True, "card_status": "IN_MANUFACTURE"}),
        ("032", 3, "check_documents", {"documents_asked": True, "document_ready": False}),
        ("032", 4, "check_documents", {"documents_asked": True}),  # the order placed after the archive check is pending
        ("028", 5, "check_confirmation", {"confirmation": "given", "instructed_outside_portal": True}),
        ("036", 4, "check_confirmation", {"confirmation": "unprompted", "instructed_outside_portal": True}),
        ("013", 5, "check_confirmation", {"confirmation": "given", "instructed_outside_portal": False}),
        ("046", 4, "check_business", {"business_asked": True, "business_status": "ROLE_REVOKED"}),
        ("006", 4, "check_payment", {"payment_asked": True, "payment_status": "OTHER", "payment_count": 2}),
        ("018", 4, "check_payment", {"payment_asked": True, "payment_status": "OTHER", "payment_count": 2}),
        ("034", 4, "check_tariff", {"tariff_asked": True, "tariff_status": "MATCHES"}),
    ],
)
def test_section3_regressions_on_the_public_case_points(
    case_id: str, point: int, reader: str, expected: dict[str, Any]
) -> None:
    facts, _ = invoke(reader, banking_point(case_id, point))
    assert facts == expected


@pytest.mark.parametrize("case_id", ["006", "018"])
def test_separate_instruction_answers_have_a_safe_reply_template(case_id: str) -> None:
    data = banking_point(case_id, 4)
    facts, _ = invoke("check_payment", data)
    fields = {
        **facts,
        "requester": "Mara Ellison",
        "channel": "secure_portal",
        "next_system": "payment",
        "subject": "payment",
    }
    _, probe = invoke("reply_customer", data, fields)
    text = probe.actions[0]["args"]["text"]
    assert "2 separate payment instructions" in text
    assert "No new transfer was made" in text
    assert "does not establish execution" in text


def test_agent_card_note_needs_a_direct_result_and_not_a_question() -> None:
    data = case(
        event(
            1,
            "system",
            "H&V agent",
            "H&V card journal",
            "I checked whether the card journal shows the replacement status.",
        )
    )
    facts, _ = invoke("check_card", data)
    assert facts == {"card_asked": True}


def test_confirmation_inside_an_unmatched_process_is_not_authorisation() -> None:
    data = case(
        event(
            1,
            "system",
            "H&V service agent",
            "H&V profile change process",
            "I started the approved profile change process.",
        ),
        event(
            2,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I confirm that I want the change.",
            "Secure portal",
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


@pytest.mark.parametrize(
    "start_text",
    [
        "I have not yet started the approved profile change process.",
        "I will start the approved profile change process after checking authority.",
        "If I started the profile change process, confirm securely.",
        "The customer says I started the profile change process.",
    ],
)
def test_confirmation_does_not_treat_a_planned_process_as_started(start_text: str) -> None:
    data = case(
        event(1, "system", "H&V service agent", "H&V profile change process", start_text),
        event(
            2,
            "conversation",
            "Mara Ellison",
            "H&V profile change process",
            "I confirm that I want the change.",
            "Secure portal",
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


def test_question_or_imperative_process_start_does_not_gate_confirmation() -> None:
    for text in ("Should I start the profile change?", "Please start the profile change after checking authority."):
        data = case(
            event(1, "system", "H&V service agent", "H&V profile change process", text),
            event(
                2,
                "conversation",
                "Mara Ellison",
                "H&V profile change process",
                "I confirm that I want the change.",
                "Secure portal",
            ),
        )
        facts, _ = invoke("check_confirmation", data)
        assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


def test_unrequested_portal_confirmation_needs_a_bank_record_of_adoption() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I confirm that I want the change.",
            "Secure portal",
        ),
        event(
            2,
            "system",
            "H&V agent",
            "H&V case record",
            "The portal confirmation is mentioned in the case history.",
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


@pytest.mark.parametrize(
    "processing_text",
    [
        "I am not submitting the secure-portal confirmation HV-111.",
        "Please submit the secure-portal confirmation HV-111 when checks complete.",
        "I am submitting Alice's secure-portal confirmation HV-222.",
    ],
)
def test_portal_confirmation_adoption_must_be_positive_and_for_the_same_change(processing_text: str) -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I confirm the change for reference HV-111.",
            "Secure portal",
        ),
        event(
            2,
            "system",
            "H&V agent",
            "H&V protected instruction process",
            processing_text,
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


def test_future_portal_confirmation_is_not_adopted_as_given() -> None:
    data = case(
        event(
            1,
            "conversation",
            "Mara Ellison",
            "H&V",
            "I will confirm the change for reference HV-111 later.",
            "Secure portal",
        ),
        event(
            2,
            "system",
            "H&V agent",
            "H&V protected instruction process",
            "I am submitting Mara Ellison's secure-portal confirmation HV-111.",
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "none"  # a promise to confirm later is no confirmation


def test_unbound_portal_confirmation_pronoun_is_not_adopted() -> None:
    data = case(
        event(1, "conversation", "Mara Ellison", "H&V", "I confirm the change.", "Secure portal"),
        event(
            2,
            "system",
            "H&V agent",
            "H&V protected instruction process",
            "I am submitting her secure-portal confirmation for HV-222.",
        ),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


@pytest.mark.parametrize(
    "processing_text",
    [
        (
            "Mara Ellison has an unresolved instruction. Alice Smith completed confirmation. "
            "I am submitting her secure-portal confirmation."
        ),
        "Mara Ellison and Alice Smith have unresolved instructions. I am submitting her secure-portal confirmation.",
    ],
)
def test_portal_adoption_pronoun_needs_an_immediate_unambiguous_owner(processing_text: str) -> None:
    data = case(
        event(1, "conversation", "Mara Ellison", "H&V", "I confirm the change.", "Secure portal"),
        event(2, "system", "H&V agent", "H&V protected instruction process", processing_text),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == "unprompted"  # confirmed by the customer, not adopted by the bank


@pytest.mark.parametrize(
    ("candidate", "adoption", "expected"),
    [
        (
            "I confirm the change for reference HV-111.",
            "HV-111 still awaits authority checks. I am submitting Alice's secure-portal confirmation HV-222.",
            "unprompted",
        ),
        (
            "I confirm the change for reference HV-111.",
            "I am submitting Alice's secure-portal confirmation HV-111.",
            "unprompted",
        ),
        (
            "I confirm the change for reference HV-111.",
            "I am submitting Mara Ellison's secure-portal confirmation HV-111.",
            "given",
        ),
        (
            "I confirm the change for reference HV-111.",
            "I am submitting Mara Smith's secure-portal confirmation HV-111.",
            "unprompted",
        ),
    ],
)
def test_portal_adoption_uses_the_action_clause_and_customer(candidate: str, adoption: str, expected: str) -> None:
    data = case(
        event(1, "conversation", "Mara Ellison", "H&V", candidate, "Secure portal"),
        event(2, "system", "H&V agent", "H&V protected instruction process", adoption),
    )
    facts, _ = invoke("check_confirmation", data)
    assert facts["confirmation"] == expected


def test_self_contained_card_result_matches_an_existing_card_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V card journal", "Check the replacement."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V card journal",
            "I checked the card journal. The record shows the replacement is in manufacture.",
        ),
    )
    facts, _ = invoke("check_card", data)
    assert facts == {"card_asked": True, "card_status": "IN_MANUFACTURE"}


def test_self_contained_card_note_does_not_answer_a_card_team_request() -> None:
    data = case(
        event(1, "system", "H&V agent", "H&V card team", "Please check the replacement."),
        event(
            2,
            "system",
            "H&V agent",
            "H&V card journal",
            "I checked the card journal. The record shows the replacement is in manufacture.",
        ),
    )
    facts, _ = invoke("check_card", data)
    assert facts == {"card_asked": True}


def test_tariff_mismatch_is_distinct_from_a_matching_fee() -> None:
    data = case(
        event(1, "system", "H&V service agent", "H&V transaction records", "Check the fee against the tariff."),
        event(2, "system", "H&V transaction records", "H&V service agent", "The fee does not match the tariff entry."),
    )
    facts, _ = invoke("check_tariff", data)
    assert facts == {"tariff_asked": True, "tariff_status": "MISMATCH"}


@pytest.mark.parametrize(
    "answer",
    [
        "Please check whether the fee matches the tariff entry.",
        "If the fee matches the tariff entry, reply to the customer.",
    ],
)
def test_tariff_questions_and_conditions_are_not_matches(answer: str) -> None:
    data = case(
        event(1, "system", "H&V service agent", "H&V transaction records", "Check the fee against the tariff."),
        event(2, "system", "H&V transaction records", "H&V service agent", answer),
    )
    facts, _ = invoke("check_tariff", data)
    assert facts == {"tariff_asked": True, "tariff_status": "OTHER"}


@pytest.mark.parametrize("status", ["MATCHES", "MISMATCH", "OTHER"])
def test_tariff_reply_template_is_narrow_and_safe(status: str) -> None:
    fields = {
        "requester": "Mara",
        "channel": "secure_portal",
        "next_system": "tariff",
        "subject": "fee",
        "tariff_status": status,
    }
    _, probe = invoke("reply_customer", case(), fields)
    text = probe.actions[0]["args"]["text"]
    assert "tariff review" in text and "No fee or account change was made" in text

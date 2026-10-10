"""The docs stay true: the guide's example policy loads, and every flag docs/desk.md names exists."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from desk.policy import parse_policy

ROOT = Path(__file__).resolve().parents[1]


def test_the_guide_example_policy_loads() -> None:
    guide = (ROOT / "docs" / "policy.md").read_text(encoding="utf-8")
    example = re.search(r"```yaml\n(policy:.*?)```", guide, re.DOTALL)
    assert example is not None
    policy = parse_policy(example.group(1), "docs/policy.md")
    assert policy.name == "repairs-desk" and set(policy.signals) == {"book_repair"}
    assert policy.agent.instructions == "Be brief." and policy.max_steps == 100


@pytest.mark.parametrize("doc", ["docs/desk.md", "README.md"])
def test_every_flag_a_doc_names_exists(doc: str) -> None:
    text = (ROOT / doc).read_text(encoding="utf-8")
    cli = (ROOT / "src" / "desk" / "cli.py").read_text(encoding="utf-8")
    named = set(re.findall(r"`(--[a-z-]+)", text))
    assert named
    for flag in named:
        assert f'"{flag}"' in cli, f"{doc} names {flag}, which desk does not have"


def test_every_link_in_the_readme_exists() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)#:]+)\)", readme)
    assert links
    for link in links:
        assert (ROOT / link).exists(), f"README.md links {link}, which is not in the repository"


def test_every_engine_module_in_the_desk_doc_exists() -> None:
    readme = (ROOT / "docs" / "desk.md").read_text(encoding="utf-8")
    for module in re.findall(r"`(\w+\.py)`", readme):
        assert (ROOT / "src" / "desk" / module).exists() or (ROOT / "track" / module).exists(), module

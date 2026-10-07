from app.state.state_factory import create_initial_state

from app.agents.guardrails import (
    is_action_allowed,
    validate_agent_action,
)


def test_research_can_read():

    assert is_action_allowed(
        "research",
        "read"
    ) is True


def test_research_cannot_write():

    assert is_action_allowed(
        "research",
        "write"
    ) is False


def test_analysis_cannot_execute():

    assert is_action_allowed(
        "analysis",
        "execute"
    ) is False


def test_decision_can_approve():

    assert is_action_allowed(
        "decision",
        "approve"
    ) is True


def test_unauthorized_action_is_blocked():

    state = create_initial_state(
        "Evaluate AI platform"
    )

    state = validate_agent_action(
        state,
        "research",
        "write"
    )

    assert state["status"] == "blocked"

    assert state["errors"]
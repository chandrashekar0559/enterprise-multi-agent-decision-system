from app.state.state_factory import create_initial_state
from app.agents.conflict_resolver import (
    detect_conflict,
    resolve_conflict,
)


def test_no_conflict_without_results():

    assert detect_conflict(
        [],
        []
    ) is False


def test_conflict_detected():

    assert detect_conflict(
        ["Platform provides significant benefits."],
        ["Vendor lock-in is a major concern."]
    ) is True


def test_conflict_resolution():

    state = create_initial_state(
        "Evaluate AI platform"
    )

    state = resolve_conflict(
        state,
        ["Platform provides significant benefits."],
        ["Vendor lock-in is a major concern."]
    )

    assert len(state["conflicts"]) == 1

    assert state["status"] == (
        "conflict_detected"
    )
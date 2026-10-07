from app.state.state_factory import create_initial_state


def test_initial_state():
    state = create_initial_state(
        "Evaluate whether our company should adopt a new AI platform."
    )

    assert state["task"]
    assert state["research_findings"] == []
    assert state["analysis"] == []
    assert state["risks"] == []
    assert state["recommendation"] == ""
    assert state["status"] == "started"
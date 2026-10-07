from app.state.state_factory import create_initial_state

from app.agents.communication import (
    store_research_result,
    store_analysis_result,
    store_risk_result,
    store_decision_result,
)


def test_store_research_result():
    state = create_initial_state("Evaluate AI platform")

    state = store_research_result(
        state,
        ["AI platform supports enterprise deployment."],
        ["official documentation"]
    )

    assert len(state["research_findings"]) == 1
    assert len(state["research_sources"]) == 1
    assert state["current_agent"] == "research"


def test_store_analysis_result():
    state = create_initial_state("Evaluate AI platform")

    state = store_analysis_result(
        state,
        ["Platform is suitable for enterprise workloads."]
    )

    assert len(state["analysis"]) == 1
    assert state["current_agent"] == "analysis"


def test_store_risk_result():
    state = create_initial_state("Evaluate AI platform")

    state = store_risk_result(
        state,
        ["Vendor lock-in is a potential risk."]
    )

    assert len(state["risks"]) == 1
    assert state["current_agent"] == "risk"


def test_store_decision_result():
    state = create_initial_state("Evaluate AI platform")

    state = store_decision_result(
        state,
        "Adopt the platform with appropriate safeguards."
    )

    assert state["recommendation"]
    assert state["current_agent"] == "decision"
    assert state["status"] == "completed"
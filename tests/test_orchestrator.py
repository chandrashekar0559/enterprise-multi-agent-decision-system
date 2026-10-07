from app.state.state_factory import create_initial_state

from app.orchestrator.orchestrator import get_next_agent
from app.orchestrator.router import route_agent


def test_first_agent_is_research():
    state = create_initial_state("Evaluate a new AI platform")

    assert get_next_agent(state) == "research"
    assert route_agent(state) == "research"


def test_next_agent_is_analysis():
    state = create_initial_state("Evaluate a new AI platform")

    state["research_findings"].append(
        "Platform supports enterprise deployment."
    )

    assert get_next_agent(state) == "analysis"


def test_next_agent_is_risk():
    state = create_initial_state("Evaluate a new AI platform")

    state["research_findings"].append(
        "Platform supports enterprise deployment."
    )

    state["analysis"].append(
        "Platform appears suitable."
    )

    assert get_next_agent(state) == "risk"


def test_next_agent_is_decision():
    state = create_initial_state("Evaluate a new AI platform")

    state["research_findings"].append("Research completed.")
    state["analysis"].append("Analysis completed.")
    state["risks"].append("Risk analysis completed.")

    assert get_next_agent(state) == "decision"


def test_workflow_complete():
    state = create_initial_state("Evaluate a new AI platform")

    state["research_findings"].append("Research completed.")
    state["analysis"].append("Analysis completed.")
    state["risks"].append("Risk analysis completed.")
    state["recommendation"] = "Adopt with safeguards."

    assert get_next_agent(state) is None
    assert route_agent(state) == "complete"
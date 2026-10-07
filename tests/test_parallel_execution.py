from app.state.state_factory import create_initial_state

from app.orchestrator.parallel_executor import (
    run_parallel_agents
)

from app.orchestrator.parallel_state import (
    merge_parallel_results
)


def test_parallel_agents():

    state = create_initial_state(
        "Evaluate a new AI platform"
    )

    state["research_findings"].append(
        "Platform supports enterprise deployment."
    )

    analysis_result, risk_result = run_parallel_agents(
        state
    )

    assert analysis_result["agent"] == "analysis"
    assert risk_result["agent"] == "risk"

    assert analysis_result["status"] == "completed"
    assert risk_result["status"] == "completed"


def test_merge_parallel_results():

    state = create_initial_state(
        "Evaluate a new AI platform"
    )

    analysis_result = {
        "analysis": [
            "Platform appears suitable."
        ]
    }

    risk_result = {
        "risks": [
            "Vendor lock-in is possible."
        ]
    }

    state = merge_parallel_results(
        state,
        analysis_result,
        risk_result
    )

    assert len(state["analysis"]) == 1
    assert len(state["risks"]) == 1

    assert state["current_agent"] == (
        "parallel_analysis_risk"
    )
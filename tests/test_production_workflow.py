from app.state.state_factory import create_initial_state

from app.orchestrator.production_workflow import (
    run_production_workflow
)


def test_production_workflow():

    state = create_initial_state(
        "Evaluate whether our company "
        "should adopt a new AI platform."
    )

    result = run_production_workflow(
        state
    )

    assert result["research_findings"]

    assert result["analysis"]

    assert result["risks"]

    assert result["recommendation"]

    assert result["current_agent"] == "decision"

    assert result["status"] == "completed"
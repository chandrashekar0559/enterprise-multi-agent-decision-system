from app.state.agent_state import AgentState


def merge_parallel_results(
    state: AgentState,
    analysis_result: dict,
    risk_result: dict
) -> AgentState:

    state["analysis"].extend(
        analysis_result.get("analysis", [])
    )

    state["risks"].extend(
        risk_result.get("risks", [])
    )

    state["current_agent"] = "parallel_analysis_risk"

    return state
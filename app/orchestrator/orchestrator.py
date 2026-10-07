from app.state.agent_state import AgentState


def get_next_agent(state: AgentState) -> str | None:
    if not state["research_findings"]:
        return "research"

    if not state["analysis"]:
        return "analysis"

    if not state["risks"]:
        return "risk"

    if not state["recommendation"]:
        return "decision"

    return None
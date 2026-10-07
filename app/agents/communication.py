from app.state.agent_state import AgentState


def store_research_result(
    state: AgentState,
    findings: list[str],
    sources: list[str]
) -> AgentState:
    state["research_findings"].extend(findings)
    state["research_sources"].extend(sources)
    state["current_agent"] = "research"
    return state


def store_analysis_result(
    state: AgentState,
    analysis: list[str]
) -> AgentState:
    state["analysis"].extend(analysis)
    state["current_agent"] = "analysis"
    return state


def store_risk_result(
    state: AgentState,
    risks: list[str]
) -> AgentState:
    state["risks"].extend(risks)
    state["current_agent"] = "risk"
    return state


def store_decision_result(
    state: AgentState,
    recommendation: str
) -> AgentState:
    state["recommendation"] = recommendation
    state["current_agent"] = "decision"
    state["status"] = "completed"
    return state
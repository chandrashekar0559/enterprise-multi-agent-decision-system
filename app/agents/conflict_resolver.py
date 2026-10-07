from app.state.agent_state import AgentState


def detect_conflict(
    analysis: list[str],
    risks: list[str]
) -> bool:

    return bool(analysis and risks)


def resolve_conflict(
    state: AgentState,
    analysis: list[str],
    risks: list[str]
) -> AgentState:

    if not detect_conflict(analysis, risks):
        return state

    conflict = (
        "Analysis indicates potential benefits while "
        "Risk identifies potential enterprise concerns."
    )

    state["conflicts"].append(conflict)

    state["findings"].append(
        "Conflict detected between Analysis and Risk agents."
    )

    state["status"] = "conflict_detected"

    return state
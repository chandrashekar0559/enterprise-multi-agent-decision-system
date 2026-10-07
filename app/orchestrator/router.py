from app.state.agent_state import AgentState
from app.orchestrator.orchestrator import get_next_agent


def route_agent(state: AgentState) -> str:
    next_agent = get_next_agent(state)

    if next_agent is None:
        return "complete"

    return next_agent
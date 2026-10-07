from app.state.agent_state import AgentState


def create_initial_state(task: str) -> AgentState:
    return {
        "task": task,
        "research_findings": [],
        "research_sources": [],
        "conflicts": [],
        "findings": [],
        "analysis": [],
        "risks": [],
        "recommendation": "",
        "errors": [],
        "current_agent": "",
        "status": "started",
    }
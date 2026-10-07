from app.state.agent_state import AgentState


AGENT_PERMISSIONS = {
    "research": {
        "read": True,
        "write": False,
        "execute": False,
        "approve": False,
    },
    "analysis": {
        "read": True,
        "write": False,
        "execute": False,
        "approve": False,
    },
    "risk": {
        "read": True,
        "write": False,
        "execute": False,
        "approve": False,
    },
    "decision": {
        "read": True,
        "write": False,
        "execute": False,
        "approve": True,
    },
}


def is_action_allowed(
    agent_name: str,
    action: str
) -> bool:

    permissions = AGENT_PERMISSIONS.get(
        agent_name,
        {}
    )

    return permissions.get(action, False)


def validate_agent_action(
    state: AgentState,
    agent_name: str,
    action: str
) -> AgentState:

    if not is_action_allowed(
        agent_name,
        action
    ):
        state["errors"].append(
            f"Permission denied: "
            f"{agent_name} cannot perform {action}"
        )

        state["status"] = "blocked"

    return state
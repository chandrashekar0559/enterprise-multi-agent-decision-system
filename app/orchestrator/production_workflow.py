from app.state.agent_state import AgentState

from app.agents.research_agent import research_agent
from app.agents.analysis_agent import analysis_agent
from app.agents.risk_agent import risk_agent
from app.agents.decision_agent import decision_agent

from app.agents.communication import (
    store_research_result,
    store_analysis_result,
    store_risk_result,
    store_decision_result,
)

from app.agents.conflict_resolver import resolve_conflict

from app.orchestrator.parallel_executor import (
    run_parallel_agents
)

from app.orchestrator.parallel_state import (
    merge_parallel_results
)


def run_production_workflow(
    state: AgentState
) -> AgentState:

    # -------------------------------------------------
    # 1. RESEARCH
    # -------------------------------------------------

    state["current_agent"] = "research"

    research_result = research_agent(
        state["task"]
    )

    state = store_research_result(
        state,
        research_result["findings"],
        research_result["sources"]
    )

    # -------------------------------------------------
    # 2. PARALLEL ANALYSIS + RISK
    # -------------------------------------------------

    state["current_agent"] = (
        "parallel_analysis_risk"
    )

    analysis_result, risk_result = (
        run_parallel_agents(state)
    )

    state = merge_parallel_results(
        state,
        analysis_result,
        risk_result
    )

    # -------------------------------------------------
    # 3. CONFLICT RESOLUTION
    # -------------------------------------------------

    state = resolve_conflict(
        state,
        state["analysis"],
        state["risks"]
    )

    # -------------------------------------------------
    # 4. DECISION
    # -------------------------------------------------

    state["current_agent"] = "decision"

    decision_result = decision_agent(
        state["task"],
        state["research_findings"],
        state["analysis"],
        state["risks"]
    )

    state = store_decision_result(
        state,
        decision_result["recommendation"]
    )

    state["status"] = "completed"

    return state
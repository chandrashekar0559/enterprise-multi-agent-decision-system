from concurrent.futures import ThreadPoolExecutor

from app.state.agent_state import AgentState
from app.agents.analysis_agent import analysis_agent
from app.agents.risk_agent import risk_agent


def run_parallel_agents(
    state: AgentState
) -> tuple[dict, dict]:

    research_findings = state["research_findings"]

    with ThreadPoolExecutor(max_workers=2) as executor:

        analysis_future = executor.submit(
            analysis_agent,
            state["task"],
            research_findings
        )

        risk_future = executor.submit(
            risk_agent,
            state["task"],
            research_findings
        )

        analysis_result = analysis_future.result()
        risk_result = risk_future.result()

    return analysis_result, risk_result
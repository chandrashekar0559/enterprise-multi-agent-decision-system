from typing import TypedDict


class AgentState(TypedDict):
    task: str

    research_findings: list[str]
    research_sources: list[str]

    analysis: list[str]

    risks: list[str]

    recommendation: str

    errors: list[str]

    current_agent: str
    
    conflicts: list[str]

    status: str
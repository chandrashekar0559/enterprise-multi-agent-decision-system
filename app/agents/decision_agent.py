def decision_agent(
    task: str,
    research_findings: list[str],
    analysis: list[str],
    risks: list[str]
) -> dict:

    return {
        "agent": "decision",
        "task": task,
        "recommendation": (
            "Decision agent produced a recommendation "
            "based on research, analysis and risks."
        ),
        "evidence": research_findings,
        "analysis": analysis,
        "risks": risks,
        "status": "completed",
    }
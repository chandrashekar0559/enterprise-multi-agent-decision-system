def analysis_agent(
    task: str,
    research_findings: list[str]
) -> dict:

    return {
        "agent": "analysis",
        "task": task,
        "analysis": [
            "Analysis agent evaluated the available evidence."
        ],
        "based_on": research_findings,
        "status": "completed",
    }
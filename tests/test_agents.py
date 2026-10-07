from app.agents.research_agent import research_agent
from app.agents.analysis_agent import analysis_agent
from app.agents.risk_agent import risk_agent
from app.agents.decision_agent import decision_agent


def test_research_agent():
    result = research_agent(
        "Evaluate a new technology"
    )

    assert result["agent"] == "research"
    assert result["status"] == "completed"


def test_analysis_agent():
    result = analysis_agent(
        "Analyze technology",
        ["Research finding"]
    )

    assert result["agent"] == "analysis"
    assert result["status"] == "completed"


def test_risk_agent():
    result = risk_agent(
        "Identify risks",
        ["Research finding"]
    )

    assert result["agent"] == "risk"
    assert result["status"] == "completed"


def test_decision_agent():
    result = decision_agent(
        "Make recommendation",
        ["Research finding"],
        ["Analysis finding"],
        ["Risk finding"],
    )

    assert result["agent"] == "decision"
    assert result["status"] == "completed"
    assert result["recommendation"]
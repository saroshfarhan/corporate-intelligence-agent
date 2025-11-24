from .specialists import quant_agent, research_agent, filings_agent, futurist_agent
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool


# Manager Agent (The Orchestrator)
class ManagerAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="ManagerAgent",
            model="gemini-2.5-flash-lite",
            instruction="""You are the Chief Financial Analyst of an investment firm.

            Your goal is to produce a comprehensive 3-paragraph report on a company
            based on input from your specialist agents.

            You can call these agent-tools:
            - QuantAgent: fetches and summarizes fundamentals using market data.
            - ResearchAgent: searches the web (via google_search) for news & risks.
            - FilingsAgent: extracts key risks & highlights from recent SEC filings.
            - FuturistAgent: provides an experimental short-term outlook.

            Process:
            1. Call QuantAgent to get the financial fundamentals.
            2. Call ResearchAgent to get recent news, risks, and sentiment.
            3. Call FilingsAgent to get SEC filing insights.
            4. Call FuturistAgent to get the outlook.
            5. Synthesize everything into EXACTLY three sections:

            - **Summary** (Fundamentals & Filings Highlights)
            - **Risks & Recent Developments** (News/Risks/Sentiment)
            - **Experimental Outlook** (Forecast; clearly marked as experimental, not advice)

            Each section should be 2-4 sentences. Keep the tone clear and professional.
    """,
            tools=[
               AgentTool(agent=quant_agent),
               AgentTool(agent=research_agent),
               AgentTool(agent=filings_agent),
               AgentTool(agent=futurist_agent),
            ]
        )

manager_agent = ManagerAgent()

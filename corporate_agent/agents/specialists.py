from google.adk.agents import Agent
from google.adk.tools import google_search
from ..tools.financial_tools import get_fundamentals, get_outlook, parse_sec_filing

MODEL_NAME = "gemini-2.5-flash-lite"

# 1. Quant Agent
quant_agent = Agent(
    name="QuantAgent",
    model=MODEL_NAME,
    description="A financial analyst that provides fundamental data.",
    instruction="You are a financial analyst. Use the `get_fundamentals` tool to analyze the company's financial health. Return a concise text summary of the fundamentals.",
    tools=[get_fundamentals]
)

# 2 Research Agent
research_agent = Agent(
    name = "ResearchAgent",
    model = MODEL_NAME,
    description = "A research agent that finds new, headlines, issues.",
    instruction="""You are a reasearch agent thatuses 'google_search' tool to identify the latest news, regulatory issues, investigations against the firm, scandals, analyst sentiments, user sentiments from various sorces as shown but the 'google_search' agent.
    Focus on:
        - Lawsuits and regulatory investigations
        - Major product or strategy news
        - Analyst upgrades/downgrades
        - Sentiment analysis

    Summarize the key risks and overall sentiment, with short inline citations like [1], [2].

    CRITICAL: Do not add information from your own, use the available online results from 'google_search' tool and then return a concise text summary.
    """,
    tools = [google_search]
)

filings_agent = Agent(
    name="FilingsAgent",
    model=MODEL_NAME,
    description="A specialist in SEC filings.",
    instruction="""You are an expert in analyzing SEC filings (10-K, 10-Q). 
    Use the `parse_sec_filing` tool to extract key risks and financial highlights from the latest reports.
    Summarize the top 3 critical insights.""",
    tools=[parse_sec_filing]
)

# 4. Futurist Agent
futurist_agent = Agent(
    name="FuturistAgent",
    model=MODEL_NAME,
    description="A market futurist that provides an experimental short-term outlook.",
    instruction="You are a market futurist. Use the `get_outlook` tool to provide an experimental forecast. Return a concise text summary of the outlook.",
    tools=[get_outlook]
)

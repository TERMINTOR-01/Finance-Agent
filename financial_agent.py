from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo  # Web search
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
# Web search agent
websearch_agent = Agent(
    name="web search Agent",
    role="Search The web for the information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Financial agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use Tables To Display The Data"],
    show_tool_calls=True,
    markdown=True,
)

#multi mode agent websearch+finance agent
multi_ai_agents=Agent(
    team=[websearch_agent,finance_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include sources","Use Table to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agents.print_response("summarizes analyst recommendation and share the latest news for the NVDA",stream=False)
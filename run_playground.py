from phi.agent import Agent
import os
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()
os.environ["PHI_API_KEY"] = os.getenv("PHI_API_KEY")

# Agents setup
websearch_agent = Agent(
    name="web search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
#VA
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
            
        )
    ],
    instructions=["Use Tables To Display The Data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agents = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id="llama3-70b-8192"),
    instructions=["Always include sources", "Use Table to display the data"],
    show_tool_calls=True,
    markdown=True
)
#VA
# Launch Playground
app = Playground(agents=[finance_agent, websearch_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("run_playground:app", reload=True)

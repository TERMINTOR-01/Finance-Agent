Financial AI Agent - One Page Overview
Overview:
This project combines AI agents for real-time financial analysis and web search using the Groq LLaMA3 model via
PhiData. It provides stock data, analyst ratings, and news through YFinance and DuckDuckGo tools.
Main Features:
- Real-time stock fundamentals & recommendations (YFinance)
- Web search for latest news (DuckDuckGo)
- Combined agent output using markdown and tables
- FastAPI UI playground for interactive testing
Setup Instructions:
1. Clone the repo & install dependencies:
pip install -r requirements.txt
2. Create a `.env` file with keys:
PHI_API_KEY=...
GROQ_API_KEY=...
OPENAI_API_KEY=...

"""Yahoo Finance News Tool Module.

This module provides a tool for fetching the latest financial news from Yahoo Finance.
It wraps the YahooFinanceNewsTool from LangChain community tools, providing
access to up-to-date financial news, stock information, and market data.

Examples:
    >>> from haive.tools.tools.yfinance_tool import yfinance_news_tool
    >>> result = yfinance_news_tool.run("AAPL")
    >>> print(result)  # Returns latest news about Apple Inc.
"""

from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool

# Initialize the Yahoo Finance news tool
# This provides capabilities to fetch financial news from Yahoo Finance
yfinance_news_tool = YahooFinanceNewsTool()

# Example usage in an agent:
# agent = initialize_agent([yfinance_news_tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# agent.run("What's the latest news about Tesla?")

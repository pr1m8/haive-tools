"""Alpha Vantage Toolkit Module

This module provides a toolkit for accessing financial market data through the Alpha Vantage API.
It offers tools for retrieving stock market data, currency exchange rates, market sentiment analysis,
and other financial information.

The toolkit integrates with Alpha Vantage's comprehensive financial data API, providing access to:
- Real-time and historical stock data
- Foreign exchange rates
- Company information and symbol search
- Market sentiment analysis
- Market movers (top gainers, losers, and most active stocks)

An Alpha Vantage API key is required to use these tools. You can obtain a free API key from:
https://www.alphavantage.co/support/#api-key

Required Environment Variables:
    - ALPHAVANTAGE_API_KEY: Your Alpha Vantage API key

Examples:
    >>> from haive.tools.toolkits.alpha_vantage import alpha_vantage_toolkit
    >>> # Use the toolkit directly
    >>> daily_stock_data = alpha_vantage_toolkit[1].run("AAPL")

    >>> # Or with a custom API key
    >>> from haive.tools.toolkits.alpha_vantage import AlphaVantageConfig, get_alpha_vantage_tools
    >>> config = AlphaVantageConfig(api_key="your_api_key_here")
    >>> tools = get_alpha_vantage_tools(config)
"""

import os

from dotenv import load_dotenv
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from langchain_core.tools import Tool
from pydantic import BaseModel, Field

load_dotenv(".env")


class AlphaVantageConfig(BaseModel):
    """Configuration for Alpha Vantage API access.

    This model manages the API key and client configuration for accessing
    the Alpha Vantage financial data API.

    Attributes:
        api_key (Optional[str]): Alpha Vantage API key. If not provided, will use
            the ALPHAVANTAGE_API_KEY environment variable.
    """

    api_key: str | None = Field(
        default=os.getenv("ALPHAVANTAGE_API_KEY"),
        description="Alpha Vantage API key for accessing financial data services",
    )

    def get_client(self) -> AlphaVantageAPIWrapper:
        """Initialize and return an Alpha Vantage API client.

        Returns:
            AlphaVantageAPIWrapper: An initialized Alpha Vantage API wrapper.

        Raises:
            ValueError: If no API key is available (neither provided nor in environment).
        """
        return AlphaVantageAPIWrapper()


def get_alpha_vantage_tools(config: AlphaVantageConfig) -> list[Tool]:
    """Create a list of Alpha Vantage financial data tools.

    This function creates a set of tools for accessing various financial data
    endpoints from the Alpha Vantage API, including stock data, exchange rates,
    market sentiment, and market movers.

    Args:
        config (AlphaVantageConfig): Configuration with API key and settings.

    Returns:
        List[Tool]: A list of tools for interacting with Alpha Vantage API.

    Raises:
        ValueError: If the API client cannot be initialized due to missing credentials.
    """
    client = config.get_client()

    return [
        Tool.from_function(
            func=client.run,
            name="alpha_vantage_exchange_rate",
            description="Get real-time currency exchange rate from one currency to another. Input is a string: 'USD,JPY'.",
        ),
        Tool.from_function(
            func=client._get_time_series_daily,
            name="alpha_vantage_daily_stock_data",
            description="Get daily stock time series data for a given symbol. Input is a string symbol (e.g., 'IBM').",
        ),
        Tool.from_function(
            func=client._get_time_series_weekly,
            name="alpha_vantage_weekly_stock_data",
            description="Get weekly stock time series data for a given symbol. Input is a string symbol (e.g., 'IBM').",
        ),
        Tool.from_function(
            func=client._get_quote_endpoint,
            name="alpha_vantage_quote",
            description="Get real-time quote data (price, volume) for a given symbol. Input is a string symbol (e.g., 'IBM').",
        ),
        Tool.from_function(
            func=client.search_symbols,
            name="alpha_vantage_search_symbol",
            description="Search for matching company symbols by input string (e.g., 'Tesla', 'IBM').",
        ),
        Tool.from_function(
            func=client._get_market_news_sentiment,
            name="alpha_vantage_market_sentiment",
            description="Get market news sentiment for a given symbol.",
        ),
        Tool.from_function(
            func=client._get_top_gainers_losers,
            name="alpha_vantage_market_movers",
            description="Get top 20 gainers, losers, and most active stocks in the US market.",
        ),
    ]


# Create a default toolkit instance for easy importing
alpha_vantage_toolkit = get_alpha_vantage_tools(AlphaVantageConfig())

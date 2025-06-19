"""
Polygon.io Toolkit Module

This module provides a toolkit for accessing financial market data through the Polygon.io API.
It offers tools for retrieving stock market data, options data, crypto data, forex data,
and market reference data.

The Polygon.io API provides access to:
- Real-time and historical stock data
- Options market data
- Cryptocurrency market data
- Forex (currency) market data
- Reference data (tickers, splits, dividends, etc.)
- Market aggregates and indicators

A Polygon.io API key is required to use these tools. You can obtain an API key from:
https://polygon.io/

Required Environment Variables:
    - POLYGON_API_KEY: Your Polygon.io API key

Examples:
    >>> from haive.tools.toolkits.polygon_toolkit import polygon_toolkit
    >>> # Use the toolkit directly
    >>> tools = polygon_toolkit.get_tools()
    >>> ticker_news = tools[0].run("AAPL")

    >>> # Or create a custom instance with your own API key
    >>> import os
    >>> os.environ["POLYGON_API_KEY"] = "your_api_key_here"
    >>> from haive.tools.toolkits.polygon_toolkit import create_polygon_toolkit
    >>> custom_toolkit = create_polygon_toolkit()
"""

import os
from typing import Optional

from dotenv import load_dotenv
from langchain_community.agent_toolkits.polygon.toolkit import PolygonToolkit
from langchain_community.utilities.polygon import PolygonAPIWrapper

# Load environment variables from .env file if it exists
load_dotenv(".env")


def create_polygon_toolkit(api_key: Optional[str] = None) -> PolygonToolkit:
    """
    Create a Polygon.io toolkit instance with the provided or environment API key.

    This function initializes a Polygon.io API wrapper and creates a toolkit with
    tools for accessing various financial data endpoints from the Polygon.io API.

    Args:
        api_key (Optional[str]): Polygon.io API key. If not provided, will use
            the POLYGON_API_KEY environment variable.

    Returns:
        PolygonToolkit: A toolkit containing tools for interacting with Polygon.io API.

    Raises:
        ValueError: If no API key is available (neither provided nor in environment).
    """
    if api_key:
        os.environ["POLYGON_API_KEY"] = api_key

    if not os.getenv("POLYGON_API_KEY"):
        raise ValueError(
            "Polygon.io API key is required. Set POLYGON_API_KEY environment variable or provide api_key parameter."
        )

    polygon_wrapper = PolygonAPIWrapper()
    return PolygonToolkit.from_polygon_api_wrapper(polygon_wrapper)


# Create a default toolkit instance for easy importing
try:
    polygon_toolkit = create_polygon_toolkit()
except ValueError as e:
    import warnings

    warnings.warn(
        f"Polygon toolkit initialization failed: {e}. Set POLYGON_API_KEY environment variable."
    )
    # Create an empty object that will raise proper errors if accessed
    polygon_toolkit = None

"""Google Finance Tool Module.

This module provides a tool for retrieving financial information from Google Finance.
It leverages LangChain's GoogleFinanceQueryRun to query financial data like stock prices,
market trends, and company financial information.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key

Examples:
    >>> from haive.tools.tools.google.google_finance import google_finance_tool
    >>> result = google_finance_tool[0].invoke("AAPL stock price")
    >>> print(result)
    ['Apple Inc. (AAPL) stock is currently trading at $XXX.XX...']

"""

import os

from dotenv import load_dotenv
from langchain.agents import load_tools
from pydantic import BaseModel, Field


class GoogleFinanceResult(BaseModel):
    """Response model for Google Finance search results.

    Attributes:
        results (List[str]): A list of financial information snippets from Google Finance.

    """

    results: list[str] = Field(
        ..., description="List of financial information snippets from Google Finance"
    )


def initialize_google_finance():
    """Initialize the Google Finance API wrapper with credentials from environment.
    variables.

    This function loads environment variables and configures the Google Finance API client.

    Returns:
        list: A list containing the Google Finance tool.

    Raises:
        ValueError: If required environment variables are not set.

    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Google Finance requires GOOGLE_API_KEY environment variable")

    # Load the Google Finance tool
    return load_tools(["google-finance"])


# Initialize the Google Finance tool with error handling
try:
    google_finance_tool = initialize_google_finance()
except (ImportError, ValueError) as e:
    # If initialization fails, create a dummy tool that raises an error when used
    import logging

    logging.warning(f"Failed to initialize Google Finance tool: {e}")

    def _dummy_google_finance(*args, **kwargs):
        raise RuntimeError(
            "Google Finance tool is not available. "
            "Please install google-search-results and set GOOGLE_API_KEY."
        )

    google_finance_tool = [_dummy_google_finance]

"""Google Trends Tool Module.

This module provides a tool for retrieving trend data from Google Trends.
It leverages LangChain's GoogleTrendsQueryRun to fetch information about trending search terms,
relative popularity of search terms over time, and related queries.

Note:
    This tool may require Google API credentials to be set in environment variables,
    though many Google Trends queries can work without authentication.

Examples:
    >>> from haive.tools.tools.google.google_trends import google_trends_tool
    >>> result = google_trends_tool[0].invoke("blockchain technology")
    >>> print(result)
    ['The interest in blockchain technology has increased by 120% over the past year...']

"""

from dotenv import load_dotenv
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
from pydantic import BaseModel, Field


class GoogleTrendsResult(BaseModel):
    """Response model for Google Trends search results.

    Attributes:
        results (List[str]): A list of trend information from Google Trends.

    """

    results: list[str] = Field(
        ..., description="List of trend information from Google Trends"
    )


def initialize_google_trends():
    """Initialize the Google Trends API wrapper.

    This function loads environment variables and configures the Google Trends API client.

    Returns:
        list: A list containing the Google Trends search tool.

    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Initialize the Google Trends tool
    return [GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())]


# Initialize the Google Trends tool with error handling
try:
    google_trends_tool = initialize_google_trends()
except (ImportError, ValueError) as e:
    # If initialization fails, create a dummy tool that raises an error when used
    import logging
    logging.warning(f"Failed to initialize Google Trends tool: {e}")
    
    def _dummy_google_trends(*args, **kwargs):
        raise RuntimeError(
            "Google Trends tool is not available. "
            "Please install google-search-results and set GOOGLE_API_KEY."
        )
    
    google_trends_tool = [_dummy_google_trends]

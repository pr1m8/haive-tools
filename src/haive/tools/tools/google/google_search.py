"""Google Search Tool Module.

This module provides a tool for searching the web using Google's Custom Search API.
It leverages LangChain's GoogleSearchAPIWrapper to perform searches and return relevant results.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key
    - GOOGLE_CSE_ID: Your Custom Search Engine ID

Examples:
    >>> from haive.tools.tools.google.google_search import google_search_tool
    >>> result = google_search_tool[0].invoke("quantum computing advances")
    >>> print(result)
    ['Recent advances in quantum computing include...']
"""

import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from pydantic import BaseModel, Field


class GoogleSearchResult(BaseModel):
    """Response model for Google Search results.

    Attributes:
        results (List[str]): A list of search result snippets from Google.
    """

    results: list[str] = Field(
        ..., description="List of search result snippets from Google"
    )


def initialize_google_search():
    """Initialize the Google Search API wrapper with credentials from environment variables.

    This function loads environment variables and configures the Google Search API client.

    Returns:
        list: A list containing the Google Search tool.

    Raises:
        ValueError: If required environment variables are not set.
    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY") or not os.getenv("GOOGLE_CSE_ID"):
        raise ValueError(
            "Google Search requires GOOGLE_API_KEY and GOOGLE_CSE_ID environment variables"
        )

    # Load the Google Search tool
    return load_tools(["google-search"])


# Initialize the Google Search tool
google_search_tool = initialize_google_search()

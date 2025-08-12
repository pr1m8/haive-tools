"""Google Scholar Tool Module.

This module provides a tool for searching academic papers using Google Scholar.
It leverages LangChain's GoogleScholarAPIWrapper to perform searches and return relevant academic results.

Note:
    This tool requires SerpAPI credentials to be set in environment variables:
    - SERP_API_KEY: Your SerpAPI key

Examples:
    >>> from haive.tools.tools.google.google_scholar import google_scholar_tool
    >>> result = google_scholar_tool[0].invoke("quantum computing advances")
    >>> print(result)
    ['Smith, J. (2023). Recent advances in quantum computing...']

"""

import os

from dotenv import load_dotenv
from langchain.agents import load_tools
from pydantic import BaseModel, Field


class GoogleScholarResult(BaseModel):
    """Response model for Google Scholar search results.

    Attributes:
        results (List[str]): A list of academic paper snippets from Google Scholar.

    """

    results: list[str] = Field(
        ..., description="List of academic paper snippets from Google Scholar"
    )


def initialize_google_scholar():
    """Initialize the Google Scholar API wrapper with credentials from environment.
    variables.

    This function loads environment variables and configures the Google Scholar API client.

    Returns:
        list: A list containing the Google Scholar tool.

    Raises:
        ValueError: If required environment variables are not set.

    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("SERP_API_KEY"):
        raise ValueError("Google Scholar requires SERP_API_KEY environment variable")

    # Load the Google Scholar tool
    return load_tools(["google-scholar"])


# Initialize the Google Scholar tool with error handling
try:
    google_scholar_tool = initialize_google_scholar()
except (ImportError, ValueError) as e:
    # If initialization fails, create a dummy tool that raises an error when used
    import logging

    logging.warning(f"Failed to initialize Google Scholar tool: {e}")

    def _dummy_google_scholar(*args, **kwargs):
        raise RuntimeError(
            "Google Scholar tool is not available. "
            "Please install google-search-results and set SERP_API_KEY."
        )

    google_scholar_tool = [_dummy_google_scholar]

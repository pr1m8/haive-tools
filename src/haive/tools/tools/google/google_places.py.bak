"""Google Places Tool Module.

This module provides a tool for searching and retrieving information about places using Google Places API.
It leverages LangChain's GooglePlacesTool to search for locations, businesses, points of interest,
and retrieve detailed information about them.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key
    - GOOGLE_CSE_ID: Your Custom Search Engine ID (for some functionality)

Examples:
    >>> from haive.tools.tools.google.google_places import google_places_tool
    >>> result = google_places_tool[0].invoke("coffee shops in Seattle")
    >>> print(result)
    ['Starbucks at Pike Place Market, Seattle...']

"""

import os
from typing import Any

from dotenv import load_dotenv
from langchain_google_community import GooglePlacesTool
from pydantic import BaseModel, Field


class GooglePlacesResult(BaseModel):
    """Response model for Google Places search results.

    Attributes:
        results (List[Dict[str, Any]]): A list of place information from Google Places API.

    """

    results: list[dict[str, Any]] = Field(
        ..., description="List of place information from Google Places API"
    )


def initialize_google_places():
    """Initialize the Google Places API wrapper with credentials from environment
    variables.

    This function loads environment variables and configures the Google Places API client.

    Returns:
        list: A list containing the Google Places search tool.

    Raises:
        ValueError: If required environment variables are not set.

    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Google Places requires GOOGLE_API_KEY environment variable")

    # Initialize the Google Places tool
    return [GooglePlacesTool()]


# Initialize the Google Places tool with error handling
try:
    google_places_tool = initialize_google_places()
except (ImportError, ValueError) as e:
    # If initialization fails, create a dummy tool that raises an error when used
    import logging

    logging.warning(f"Failed to initialize Google Places tool: {e}")

    def _dummy_google_places(*args, **kwargs):
        raise RuntimeError(
            "Google Places tool is not available. "
            "Please install google-search-results and set GOOGLE_API_KEY."
        )

    google_places_tool = [_dummy_google_places]

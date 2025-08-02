"""Google Lens Tool Module.

This module provides a tool for visual search and image recognition using Google Lens API.
It leverages LangChain's GoogleLensAPIWrapper to analyze images, identify objects, text,
and provide information about the content in images.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key
    - GOOGLE_LENS_API_KEY: Your Google Lens API key (if different)

Examples:
    >>> from haive.tools.tools.google.google_lens import google_lens_tool
    >>> result = google_lens_tool[0].invoke({"image_url": "https://example.com/image.jpg"})
    >>> print(result)
    ['The image shows a Siberian Husky dog in a snowy environment...']

"""

import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from pydantic import BaseModel, Field


class GoogleLensResult(BaseModel):
    """Response model for Google Lens image analysis results.

    Attributes:
        results (List[str]): A list of image analysis information from Google Lens.

    """

    results: list[str] = Field(
        ..., description="List of image analysis information from Google Lens"
    )


class GoogleLensInput(BaseModel):
    """Input model for Google Lens image analysis.

    Attributes:
        image_url (str): URL of the image to analyze.

    """

    image_url: str = Field(
        ..., description="URL of the image to analyze with Google Lens"
    )


def initialize_google_lens():
    """Initialize the Google Lens API wrapper with credentials from environment
    variables.

    This function loads environment variables and configures the Google Lens API client.

    Returns:
        list: A list containing the Google Lens tool.

    Raises:
        ValueError: If required environment variables are not set.

    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Google Lens requires GOOGLE_API_KEY environment variable")

    # Load the Google Lens tool
    return load_tools(["google-lens"])


# Initialize the Google Lens tool with error handling
try:
    google_lens_tool = initialize_google_lens()
except (ImportError, ValueError) as e:
    # If initialization fails, create a dummy tool that raises an error when used
    import logging
    logging.warning(f"Failed to initialize Google Lens tool: {e}")
    
    def _dummy_google_lens(*args, **kwargs):
        raise RuntimeError(
            "Google Lens tool is not available. "
            "Please install google-search-results and set GOOGLE_API_KEY."
        )
    
    google_lens_tool = [_dummy_google_lens]

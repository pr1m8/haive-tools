"""Google Jobs Tool Module.

This module provides a tool for searching job listings using Google Jobs API.
It leverages LangChain's GoogleJobsQueryRun to search for job postings, retrieve job details,
and find employment opportunities based on various criteria like location, title, and company.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key
    - GOOGLE_CSE_ID: Your Custom Search Engine ID

Examples:
    >>> from haive.tools.tools.google.google_jobs import google_job_search_tool
    >>> result = google_job_search_tool[0].invoke("software engineer positions in San Francisco")
    >>> print(result)
    ['Senior Software Engineer at Tech Co. - San Francisco, CA...']
"""

import os
from typing import Any

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from pydantic import BaseModel, Field


class GoogleJobsResult(BaseModel):
    """Response model for Google Jobs search results.

    Attributes:
        results (List[Dict[str, Any]]): A list of job listings from Google Jobs API.
    """

    results: list[dict[str, Any]] = Field(
        ..., description="List of job listings from Google Jobs API"
    )


class GoogleJobsInput(BaseModel):
    """Input model for Google Jobs search.

    Attributes:
        query (str): The job search query string.
    """

    query: str = Field(
        ..., description="Job search query, e.g., 'software engineer in New York'"
    )


def initialize_google_jobs():
    """Initialize the Google Jobs API wrapper with credentials from environment variables.

    This function loads environment variables and configures the Google Jobs API client.

    Returns:
        list: A list containing the Google Jobs search tool.

    Raises:
        ValueError: If required environment variables are not set.
    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY") or not os.getenv("GOOGLE_CSE_ID"):
        raise ValueError(
            "Google Jobs requires GOOGLE_API_KEY and GOOGLE_CSE_ID environment variables"
        )

    # Load the Google Jobs tool
    return load_tools(["google-jobs"])


# Initialize the Google Jobs tool
google_job_search_tool = initialize_google_jobs()

"""
Google Books Tool Module

This module provides a tool for searching and retrieving information from Google Books.
It leverages LangChain's GoogleBooksQueryRun to perform searches on the Google Books database
and retrieve relevant book information.

Note:
    This tool requires Google API credentials to be set in environment variables:
    - GOOGLE_API_KEY: Your Google API key

Examples:
    >>> from haive.tools.tools.google.google_books import google_books_tool
    >>> result = google_books_tool[0].invoke("quantum physics introductions")
    >>> print(result)
    ['Introduction to Quantum Physics by John Doe...']
"""

import os
from typing import List

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools.google_books import GoogleBooksQueryRun
from langchain_community.utilities.google_books import GoogleBooksAPIWrapper
from pydantic import BaseModel, Field


class GoogleBooksResult(BaseModel):
    """
    Response model for Google Books search results.

    Attributes:
        results (List[str]): A list of book information snippets from Google Books.
    """

    results: List[str] = Field(
        ..., description="List of book information snippets from Google Books"
    )


def initialize_google_books():
    """
    Initialize the Google Books API wrapper with credentials from environment variables.

    This function loads environment variables and configures the Google Books API client.

    Returns:
        list: A list containing the Google Books search tool.

    Raises:
        ValueError: If required environment variables are not set.
    """
    # Load environment variables from the .env file
    load_dotenv(".env")

    # Check if required environment variables are set
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Google Books requires GOOGLE_API_KEY environment variable")

    # Load the Google Books tool
    return load_tools(["google-books"])


# Initialize the Google Books tool
google_books_tool = initialize_google_books()

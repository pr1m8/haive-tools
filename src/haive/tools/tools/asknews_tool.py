"""AskNews Search Tool Module.

This module provides a tool for searching news using the AskNewsSearch API from
langchain_community. It loads necessary environment variables for authentication
and creates a ready-to-use news search tool.

Example:
    >>> from haive.tools.tools.asknews_tool import asknews_search_tool
    >>> result = asknews_search_tool[0].run("Latest AI developments")

Note:
    Make sure to set up a .env file with required API credentials.

"""

import os

from dotenv import load_dotenv
from langchain_community.tools.asknews import AskNewsSearch

# Load environment variables from .env file
load_dotenv(".env")


def get_asknews_search_tool():
    """Get AskNewsSearch tool with proper error handling for missing credentials.

    Returns:
        list: List containing AskNewsSearch tool if credentials are available,
              empty list otherwise.
    """
    try:
        return [AskNewsSearch()]
    except Exception as e:
        # Return empty list if credentials are missing or other issues occur
        print(f"Warning: AskNewsSearch tool unavailable: {e}")
        return []


# Initialize the AskNewsSearch tool only if credentials are available
asknews_search_tool = get_asknews_search_tool()

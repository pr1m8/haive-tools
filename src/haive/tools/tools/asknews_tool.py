"""
AskNews Search Tool Module.

This module provides a tool for searching news using the AskNewsSearch API from
langchain_community. It loads necessary environment variables for authentication
and creates a ready-to-use news search tool.

Example:
    >>> from haive.tools.tools.asknews_tool import asknews_search_tool
    >>> result = asknews_search_tool[0].run("Latest AI developments")

Note:
    Make sure to set up a .env file with required API credentials.
"""

import getpass
import os

from dotenv import load_dotenv
from haive.config.config import Config
from langchain_community.tools.asknews import AskNewsSearch

# Load environment variables from .env file
load_dotenv(".env")

# Initialize the AskNewsSearch tool
asknews_search_tool = [AskNewsSearch()]

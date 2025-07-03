"""Brave Search Tool Module.

This module provides access to Brave Search functionality through langchain's
BraveSearchWrapper utility. It creates a pre-configured tool for performing web
searches using the Brave search engine API.

The module uses the langchain_community agent_toolkits to load a preconfigured
Brave Search tool that can be used directly in agent workflows.

Example:
    >>> from haive.tools.tools.brave_search import brave_search_tool
    >>> results = brave_search_tool[0].run("quantum computing advancements 2025")

Note:
    Requires a Brave Search API key in your environment or configuration.
    See: https://python.langchain.com/api_reference/_modules/langchain_community/utilities/brave_search.html#BraveSearchWrapper
"""

from langchain_community.agent_toolkits import load_tools

# Initialize the Brave Search tool
brave_search_tool = load_tools(["brave-search"])

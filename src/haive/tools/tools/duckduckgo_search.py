"""
DuckDuckGo Search Tools Module

This module provides tools for performing web searches using the DuckDuckGo search engine.
It includes tools for both getting formatted text results and structured search results.

These tools use DuckDuckGo's search API to provide privacy-focused web search capabilities
without requiring API keys or authentication.

Features:
- Text-based search results for simple queries
- Structured search results with metadata (URL, title, snippet)
- No API key required
- Privacy-focused search provider

Examples:
    >>> from haive.tools.tools.duckduckgo_search import duckduckgo_search_tool
    >>> results = duckduckgo_search_tool.run("latest AI research papers")
    >>> print(results)

    >>> from haive.tools.tools.duckduckgo_search import duckduckgo_search_results
    >>> structured_results = duckduckgo_search_results.run("python programming")
    >>> for result in structured_results:
    ...     print(f"Title: {result['title']}\nURL: {result['link']}")
"""

from typing import Any, Dict, List

from langchain_community.tools import DuckDuckGoSearchResults, DuckDuckGoSearchRun

# Initialize the text-based search tool
duckduckgo_search_tool = DuckDuckGoSearchRun()
duckduckgo_search_tool.name = "duckduckgo_search"
duckduckgo_search_tool.description = (
    "Search the web using DuckDuckGo and get summarized results as text."
)

# Initialize the structured search results tool
duckduckgo_search_results = DuckDuckGoSearchResults()
duckduckgo_search_results.name = "duckduckgo_search_results"
duckduckgo_search_results.description = "Search the web using DuckDuckGo and get structured results with URLs, titles, and snippets."

# Combine tools into a toolkit
duckduckgo_search_tools = [duckduckgo_search_tool, duckduckgo_search_results]

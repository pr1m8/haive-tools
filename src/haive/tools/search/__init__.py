"""Search tools module for backward compatibility.

This module re-exports search tools from their actual locations for documentation compatibility.
"""

# Re-export search tools from their actual locations
from haive.tools.tools.duckduckgo_search import (
    duckduckgo_search_results,
    duckduckgo_search_tool,
)
from haive.tools.tools.google.google_search import google_search_tool
from haive.tools.tools.search_tools import (
    scrape_webpages,
    tavily_extract,
    tavily_qna,
    tavily_search_context,
    tavily_search_tool,
)

# Alias for documentation compatibility
WebSearchTool = tavily_search_tool
SearchConfig = dict  # Placeholder type

__all__ = [
    "duckduckgo_search_results",
    "duckduckgo_search_tool",
    "google_search_tool",
    "tavily_search_tool",
    "tavily_search_context",
    "tavily_qna",
    "tavily_extract",
    "scrape_webpages",
    "WebSearchTool",
    "SearchConfig",
]

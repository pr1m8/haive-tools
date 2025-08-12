
:py:mod:`tools.tools.duckduckgo_search`
=======================================

.. py:module:: tools.tools.duckduckgo_search

DuckDuckGo Search Tools Module.

This module provides tools for performing web searches using the DuckDuckGo search engine.
It includes tools for both getting formatted text results and structured search results.

These tools use DuckDuckGo's search API to provide privacy-focused web search capabilities
without requiring API keys or authentication.

Features:
- Text-based search results for simple queries
- Structured search results with metadata (URL, title, snippet)
- No API key required
- Privacy-focused search provider

.. rubric:: Examples

>>> from haive.tools.tools.duckduckgo_search import duckduckgo_search_tool
>>> results = duckduckgo_search_tool.run("latest AI research papers")
>>> print(results)

>>> from haive.tools.tools.duckduckgo_search import duckduckgo_search_results
>>> structured_results = duckduckgo_search_results.run("python programming")
>>> for result in structured_results:
...     print(f"Title: {result['title']}\nURL: {result['link']}")


.. autolink-examples:: tools.tools.duckduckgo_search
   :collapse:





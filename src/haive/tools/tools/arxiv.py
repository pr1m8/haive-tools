"""ArXiv Research Tool Module

This module provides a tool for searching and accessing research papers from arXiv.org,
a popular open-access repository for academic papers in fields such as physics, mathematics,
computer science, and more. The tool is loaded from LangChain's community tools.

Examples:
    >>> from haive.tools.tools.arxiv import arxiv_query_tool
    >>> result = arxiv_query_tool[0].run("quantum computing")
    >>> print(result)  # Returns summaries of relevant quantum computing papers
"""

from langchain_community.agent_toolkits.load_tools import load_tools

# Load ArXiv tool from LangChain community tools
# This provides capabilities to search and retrieve papers from arXiv.org
arxiv_query_tool = load_tools(
    ["arxiv"],
)

"""ArXiv Research Tool Module.

This module provides a tool for searching and accessing research papers from arXiv.org,
a popular open-access repository for academic papers in fields such as physics, mathematics,
computer science, and more. The tool is loaded from LangChain's community tools.

Examples:
    >>> from haive.tools.tools.arxiv import arxiv_query_tool
    >>> result = arxiv_query_tool[0].run("quantum computing")
    >>> print(result)  # Returns summaries of relevant quantum computing papers

"""

from langchain.agents import load_tools


def get_arxiv_query_tool():
    """Get ArXiv query tool with proper error handling for missing dependencies.

    Returns:
        list: List containing ArXiv query tool if available,
              empty list otherwise.
    """
    try:
        return load_tools(["arxiv"])
    except Exception as e:
        # Return empty list if dependencies are missing or other issues occur
        print(f"Warning: ArXiv query tool unavailable: {e}")
        return []


# Load ArXiv tool from LangChain community tools
# This provides capabilities to search and retrieve papers from arXiv.org
arxiv_query_tool = get_arxiv_query_tool()

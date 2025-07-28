"""Search Tools Module.

This module provides various search tools powered by the Tavily API and web scraping capabilities.
It offers tools for question answering, web content extraction, context generation for RAG applications,
and comprehensive search functionality with configurable parameters.

Examples:
    >>> from haive.tools.tools.search_tools import tavily_search_tool
    >>> results = tavily_search_tool(query="What is quantum computing?")
    >>> print(results)
"""

from collections.abc import Sequence
from typing import Literal

from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv(dotenv_path=".env")
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def tavily_qna(
    query: str,
    max_results: int = 5,
    include_answer: bool = True,
    search_depth: Literal["basic", "advanced"] = "advanced",
    verbose: bool = False,
    topic: Literal["general", "news", "finance"] = "general",
    days: int = 3,
    include_domains: Sequence[str] = [],
    exclude_domains: Sequence[str] = [],
) -> str:
    """Search tool for getting a quick answer to a specific question using Tavily's QnA search.

    This tool queries the Tavily API with a question and returns a direct answer along
    with supporting information from web search results.

    Args:
        query (str): The search query or question to be answered.
        max_results (int): Maximum number of results to return. Default is 5.
        include_answer (bool): Include short answer in response. Default is True.
        search_depth (Literal["basic", "advanced"]): Search depth, either 'basic' or 'advanced'.
            Default is 'advanced'.
        verbose (bool): Log the tool's progress. Default is False.
        topic (Literal["general", "news", "finance"]): Topic category for search context.
            Default is 'general'.
        days (int): How recent the information should be in days. Default is 3.
        include_domains (Sequence[str]): Specific domains to include in search. Default is empty list.
        exclude_domains (Sequence[str]): Specific domains to exclude from search. Default is empty list.

    Returns:
        str: The search results with a direct answer to the question.

    Raises:
        Exception: If the Tavily API request fails.
    """
    response = client.qna_search(
        query=query,
        search_depth=search_depth,
        topic=topic,
        days=days,
        max_results=max_results,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
    )
    return response


@tool
def tavily_extract(urls: list[str], **kwargs) -> dict:
    """Extract raw content from a list of websites using the Tavily Extract API.

    This tool retrieves the content from specified URLs, which is useful for data collection,
    content analysis, and research. It can be combined with search methods to first find
    relevant documents and then extract detailed information from them.

    Args:
        urls (List[str]): The list of URLs to extract content from.
        **kwargs: Additional arguments to pass to the Tavily Extract API.

    Returns:
        Dict: The extracted content from the specified URLs in a structured format.

    Raises:
        Exception: If the URL extraction fails or if the API request encounters an error.
    """
    response = client.extract(urls=urls, **kwargs)
    return response


@tool
def tavily_search_context(
    query: str,
    search_depth: Literal["basic", "advanced"] = "basic",
    topic: Literal["general", "news"] = "general",
    days: int = 3,
    max_results: int = 5,
    include_domains: Sequence[str] = [],
    exclude_domains: Sequence[str] = [],
    max_tokens: int = 4000,
    **kwargs,  # Accept custom arguments
) -> str:
    """Generate search context for Retrieval Augmented Generation (RAG) applications.

    This tool retrieves relevant context information from the web based on a search query,
    specifically formatted for use in RAG applications. It provides more comprehensive
    context than standard search responses.

    Args:
        query (str): The search query string.
        search_depth (Literal["basic", "advanced"]): Search depth, either 'basic' or 'advanced'.
            Default is 'basic'.
        topic (Literal["general", "news"]): The topic category for search context.
            Default is 'general'.
        days (int): How recent the information should be in days. Default is 3.
        max_results (int): Maximum number of results to return. Default is 5.
        include_domains (Sequence[str]): Specific domains to include in search.
            Default is empty list.
        exclude_domains (Sequence[str]): Specific domains to exclude from search.
            Default is empty list.
        max_tokens (int): Maximum number of tokens to return in the context. Default is 4000.
        **kwargs: Additional arguments to pass to the Tavily API.

    Returns:
        str: The search context formatted for RAG applications.

    Raises:
        Exception: If the API request fails.
    """
    response = client.get_search_context(
        query=query,
        search_depth=search_depth,
        topic=topic,
        days=days,
        max_results=max_results,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
        max_tokens=max_tokens,
        **kwargs,
    )
    return response


@tool
def tavily_search_tool(
    query: str,
    max_results: int | None = 5,
    include_answer: bool | None = True,
    include_raw_content: bool | None = False,
    include_images: bool | None = False,
    search_depth: str | None = "advanced",
    include_domains: list[str] | None = [],
    exclude_domains: list[str] | None = [],
    verbose: bool | None = False,
) -> dict:
    """Query Tavily Search API with full configurability for comprehensive search results.

    This tool provides complete access to all Tavily search options and returns structured
    search results with customizable content types and filtering options.

    Args:
        query (str): The search query string.
        max_results (Optional[int]): Maximum number of results to return. Default is 5.
        include_answer (Optional[bool]): Include short answer in response. Default is True.
        include_raw_content (Optional[bool]): Include raw content of the search results.
            Default is False.
        include_images (Optional[bool]): Include images in the response. Default is False.
        search_depth (Optional[str]): Search depth, either 'basic' or 'advanced'.
            Default is 'advanced'.
        include_domains (Optional[List[str]]): Specific domains to include in search.
            Default is empty list.
        exclude_domains (Optional[List[str]]): Specific domains to exclude in search.
            Default is empty list.
        verbose (Optional[bool]): Log the tool's progress. Default is False.

    Returns:
        Dict: The search results in a structured format including titles, URLs, and optionally
            raw content, images, and direct answers.

    Raises:
        Exception: If the API request fails or if invalid parameters are provided.
    """
    # Initialize TavilySearchResults with provided parameters
    tavily_tool = TavilySearchResults(
        max_results=max_results,
        include_answer=include_answer,
        include_raw_content=include_raw_content,
        include_images=include_images,
        search_depth=search_depth,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
        verbose=verbose,
    )

    # Execute the query and return results
    return tavily_tool.invoke({"query": query})


@tool
def scrape_webpages(urls: list[str]) -> str:
    """Scrape web pages using WebBaseLoader to extract detailed content information.

    This tool uses langchain's WebBaseLoader to fetch and parse content from specified URLs,
    returning the extracted content in a formatted document structure.

    Args:
        urls (List[str]): The list of URLs to scrape for content.

    Returns:
        str: The scraped content from all URLs in a structured format with document titles.

    Raises:
        Exception: If URL scraping fails due to network issues, invalid URLs, or access restrictions.
    """
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return "\n\n".join(
        [
            f'<Document name="{doc.metadata.get("title", "")}">\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )

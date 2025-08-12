
:py:mod:`tools.tools.search_tools`
==================================

.. py:module:: tools.tools.search_tools

Search Tools Module.

This module provides various search tools powered by the Tavily API and web scraping capabilities.
It offers tools for question answering, web content extraction, context generation for RAG applications,
and comprehensive search functionality with configurable parameters.

.. rubric:: Examples

>>> from haive.tools.tools.search_tools import tavily_search_tool
>>> results = tavily_search_tool(query="What is quantum computing?")
>>> print(results)


.. autolink-examples:: tools.tools.search_tools
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.search_tools._get_tavily_client
   tools.tools.search_tools.scrape_webpages
   tools.tools.search_tools.tavily_extract
   tools.tools.search_tools.tavily_qna
   tools.tools.search_tools.tavily_search_context
   tools.tools.search_tools.tavily_search_tool

.. py:function:: _get_tavily_client()

   Get Tavily client, initializing it lazily to avoid import-time API key errors.


   .. autolink-examples:: _get_tavily_client
      :collapse:

.. py:function:: scrape_webpages(urls: list[str]) -> str

   Scrape web pages using WebBaseLoader to extract detailed content information.

   This tool uses langchain's WebBaseLoader to fetch and parse content from specified URLs,
   returning the extracted content in a formatted document structure.

   :param urls: The list of URLs to scrape for content.
   :type urls: List[str]

   :returns: The scraped content from all URLs in a structured format with document titles.
   :rtype: str

   :raises Exception: If URL scraping fails due to network issues, invalid URLs, or access restrictions.


   .. autolink-examples:: scrape_webpages
      :collapse:

.. py:function:: tavily_extract(urls: list[str], **kwargs) -> dict

   Extract raw content from a list of websites using the Tavily Extract API.

   This tool retrieves the content from specified URLs, which is useful for data collection,
   content analysis, and research. It can be combined with search methods to first find
   relevant documents and then extract detailed information from them.

   :param urls: The list of URLs to extract content from.
   :type urls: List[str]
   :param \*\*kwargs: Additional arguments to pass to the Tavily Extract API.

   :returns: The extracted content from the specified URLs in a structured format.
   :rtype: Dict

   :raises Exception: If the URL extraction fails or if the API request encounters an error.


   .. autolink-examples:: tavily_extract
      :collapse:

.. py:function:: tavily_qna(query: str, max_results: int = 5, include_answer: bool = True, search_depth: Literal['basic', 'advanced'] = 'advanced', verbose: bool = False, topic: Literal['general', 'news', 'finance'] = 'general', days: int = 3, include_domains: collections.abc.Sequence[str] = [], exclude_domains: collections.abc.Sequence[str] = []) -> str

   Search tool for getting a quick answer to a specific question using Tavily's QnA.
   search.

   This tool queries the Tavily API with a question and returns a direct answer along
   with supporting information from web search results.

   :param query: The search query or question to be answered.
   :type query: str
   :param max_results: Maximum number of results to return. Default is 5.
   :type max_results: int
   :param include_answer: Include short answer in response. Default is True.
   :type include_answer: bool
   :param search_depth: Search depth, either 'basic' or 'advanced'.
                        Default is 'advanced'.
   :type search_depth: Literal["basic", "advanced"]
   :param verbose: Log the tool's progress. Default is False.
   :type verbose: bool
   :param topic: Topic category for search context.
                 Default is 'general'.
   :type topic: Literal["general", "news", "finance"]
   :param days: How recent the information should be in days. Default is 3.
   :type days: int
   :param include_domains: Specific domains to include in search. Default is empty list.
   :type include_domains: Sequence[str]
   :param exclude_domains: Specific domains to exclude from search. Default is empty list.
   :type exclude_domains: Sequence[str]

   :returns: The search results with a direct answer to the question.
   :rtype: str

   :raises Exception: If the Tavily API request fails.


   .. autolink-examples:: tavily_qna
      :collapse:

.. py:function:: tavily_search_context(query: str, search_depth: Literal['basic', 'advanced'] = 'basic', topic: Literal['general', 'news'] = 'general', days: int = 3, max_results: int = 5, include_domains: collections.abc.Sequence[str] = [], exclude_domains: collections.abc.Sequence[str] = [], max_tokens: int = 4000, **kwargs) -> str

   Generate search context for Retrieval Augmented Generation (RAG) applications.

   This tool retrieves relevant context information from the web based on a search query,
   specifically formatted for use in RAG applications. It provides more comprehensive
   context than standard search responses.

   :param query: The search query string.
   :type query: str
   :param search_depth: Search depth, either 'basic' or 'advanced'.
                        Default is 'basic'.
   :type search_depth: Literal["basic", "advanced"]
   :param topic: The topic category for search context.
                 Default is 'general'.
   :type topic: Literal["general", "news"]
   :param days: How recent the information should be in days. Default is 3.
   :type days: int
   :param max_results: Maximum number of results to return. Default is 5.
   :type max_results: int
   :param include_domains: Specific domains to include in search.
                           Default is empty list.
   :type include_domains: Sequence[str]
   :param exclude_domains: Specific domains to exclude from search.
                           Default is empty list.
   :type exclude_domains: Sequence[str]
   :param max_tokens: Maximum number of tokens to return in the context. Default is 4000.
   :type max_tokens: int
   :param \*\*kwargs: Additional arguments to pass to the Tavily API.

   :returns: The search context formatted for RAG applications.
   :rtype: str

   :raises Exception: If the API request fails.


   .. autolink-examples:: tavily_search_context
      :collapse:

.. py:function:: tavily_search_tool(query: str, max_results: int | None = 5, include_answer: bool | None = True, include_raw_content: bool | None = False, include_images: bool | None = False, search_depth: str | None = 'advanced', include_domains: list[str] | None = None, exclude_domains: list[str] | None = None, verbose: bool | None = False) -> dict

   Query Tavily Search API with full configurability for comprehensive search.
   results.

   This tool provides complete access to all Tavily search options and returns structured
   search results with customizable content types and filtering options.

   :param query: The search query string.
   :type query: str
   :param max_results: Maximum number of results to return. Default is 5.
   :type max_results: Optional[int]
   :param include_answer: Include short answer in response. Default is True.
   :type include_answer: Optional[bool]
   :param include_raw_content: Include raw content of the search results.
                               Default is False.
   :type include_raw_content: Optional[bool]
   :param include_images: Include images in the response. Default is False.
   :type include_images: Optional[bool]
   :param search_depth: Search depth, either 'basic' or 'advanced'.
                        Default is 'advanced'.
   :type search_depth: Optional[str]
   :param include_domains: Specific domains to include in search.
                           Default is empty list.
   :type include_domains: Optional[List[str]]
   :param exclude_domains: Specific domains to exclude in search.
                           Default is empty list.
   :type exclude_domains: Optional[List[str]]
   :param verbose: Log the tool's progress. Default is False.
   :type verbose: Optional[bool]

   :returns:

             The search results in a structured format including titles, URLs, and optionally
                 raw content, images, and direct answers.
   :rtype: Dict

   :raises Exception: If the API request fails or if invalid parameters are provided.


   .. autolink-examples:: tavily_search_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.search_tools
   :collapse:
   
.. autolink-skip:: next

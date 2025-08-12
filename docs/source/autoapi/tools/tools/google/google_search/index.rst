
:py:mod:`tools.tools.google.google_search`
==========================================

.. py:module:: tools.tools.google.google_search

Google Search Tool Module.

This module provides a tool for searching the web using Google's Custom Search API.
It leverages LangChain's GoogleSearchAPIWrapper to perform searches and return relevant results.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key
   - GOOGLE_CSE_ID: Your Custom Search Engine ID

.. rubric:: Examples

>>> from haive.tools.tools.google.google_search import google_search_tool
>>> result = google_search_tool[0].invoke("quantum computing advances")
>>> print(result)
['Recent advances in quantum computing include...']


.. autolink-examples:: tools.tools.google.google_search
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_search.GoogleSearchResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleSearchResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleSearchResult {
        node [shape=record];
        "GoogleSearchResult" [label="GoogleSearchResult"];
        "pydantic.BaseModel" -> "GoogleSearchResult";
      }

.. autopydantic_model:: tools.tools.google.google_search.GoogleSearchResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   tools.tools.google.google_search.initialize_google_search

.. py:function:: initialize_google_search()

   Initialize the Google Search API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Search API client.

   :returns: A list containing the Google Search tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_search
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_search
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.brave_search`
==================================

.. py:module:: tools.tools.brave_search

Brave Search Tool Module.

This module provides access to Brave Search functionality through langchain's
BraveSearchWrapper utility. It creates a pre-configured tool for performing web
searches using the Brave search engine API.

The module uses the langchain_community agent_toolkits to load a preconfigured
Brave Search tool that can be used directly in agent workflows.

.. rubric:: Example

>>> from haive.tools.tools.brave_search import brave_search_tool
>>> results = brave_search_tool[0].run("quantum computing advancements 2025")

.. note::

   Requires a Brave Search API key in your environment or configuration.
   See: https://python.langchain.com/api_reference/_modules/langchain_community/utilities/brave_search.html#BraveSearchWrapper


.. autolink-examples:: tools.tools.brave_search
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.brave_search.get_brave_search_tool

.. py:function:: get_brave_search_tool()

   Get Brave Search tool with proper error handling for missing credentials.

   :returns:

             List containing Brave Search tool if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_brave_search_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.brave_search
   :collapse:
   
.. autolink-skip:: next

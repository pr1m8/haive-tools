
:py:mod:`tools.tools.dataforseo_tool`
=====================================

.. py:module:: tools.tools.dataforseo_tool

DataForSEO API integration tools for SEO and search engine data.

This module provides integration with DataForSEO's API services through the LangChain
tools interface. DataForSEO offers various API endpoints for SEO analytics, search engine
results, key research, competitor analysis, and more.

The module configures and initializes the DataForSEO API wrapper and loads the corresponding
tools for use in agent workflows. It requires valid DataForSEO API credentials to be
configured in the environment or the Config object.

Requires:
    - DataForSEO account with API access
    - Valid credentials (login and pass
    - API usage is subject to DataForSEO's terms of service and rate limits
    - Documentation for the DataForSEO API integration in LangChain is available at:
      https://python.langchain.com/docs/integrations/tools/dataforseo/


.. autolink-examples:: tools.tools.dataforseo_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.dataforseo_tool.get_dataforseo_tools

.. py:function:: get_dataforseo_tools()

   Get DataForSEO tools with proper error handling for missing credentials.

   :returns:

             List containing DataForSEO tools if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_dataforseo_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.dataforseo_tool
   :collapse:
   
.. autolink-skip:: next

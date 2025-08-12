
:py:mod:`tools.tools.asknews_tool`
==================================

.. py:module:: tools.tools.asknews_tool

AskNews Search Tool Module.

This module provides a tool for searching news using the AskNewsSearch API from
langchain_community. It loads necessary environment variables for authentication
and creates a ready-to-use news search tool.

.. rubric:: Example

>>> from haive.tools.tools.asknews_tool import asknews_search_tool
>>> result = asknews_search_tool[0].run("Latest AI developments")

.. note:: Make sure to set up a .env file with required API credentials.


.. autolink-examples:: tools.tools.asknews_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.asknews_tool.get_asknews_search_tool

.. py:function:: get_asknews_search_tool()

   Get AskNewsSearch tool with proper error handling for missing credentials.

   :returns:

             List containing AskNewsSearch tool if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_asknews_search_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.asknews_tool
   :collapse:
   
.. autolink-skip:: next

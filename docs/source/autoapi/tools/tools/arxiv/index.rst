
:py:mod:`tools.tools.arxiv`
===========================

.. py:module:: tools.tools.arxiv

ArXiv Research Tool Module.

This module provides a tool for searching and accessing research papers from arXiv.org,
a popular open-access repository for academic papers in fields such as physics, mathematics,
computer science, and more. The tool is loaded from LangChain's community tools.

.. rubric:: Examples

>>> from haive.tools.tools.arxiv import arxiv_query_tool
>>> result = arxiv_query_tool[0].run("quantum computing")
>>> print(result)  # Returns summaries of relevant quantum computing papers


.. autolink-examples:: tools.tools.arxiv
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.arxiv.get_arxiv_query_tool

.. py:function:: get_arxiv_query_tool()

   Get ArXiv query tool with proper error handling for missing dependencies.

   :returns:

             List containing ArXiv query tool if available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_arxiv_query_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.arxiv
   :collapse:
   
.. autolink-skip:: next

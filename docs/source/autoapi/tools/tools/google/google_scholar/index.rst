
:py:mod:`tools.tools.google.google_scholar`
===========================================

.. py:module:: tools.tools.google.google_scholar

Google Scholar Tool Module.

This module provides a tool for searching academic papers using Google Scholar.
It leverages LangChain's GoogleScholarAPIWrapper to perform searches and return relevant academic results.

.. note::

   This tool requires SerpAPI credentials to be set in environment variables:
   - SERP_API_KEY: Your SerpAPI key

.. rubric:: Examples

>>> from haive.tools.tools.google.google_scholar import google_scholar_tool
>>> result = google_scholar_tool[0].invoke("quantum computing advances")
>>> print(result)
['Smith, J. (2023). Recent advances in quantum computing...']


.. autolink-examples:: tools.tools.google.google_scholar
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_scholar.GoogleScholarResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleScholarResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleScholarResult {
        node [shape=record];
        "GoogleScholarResult" [label="GoogleScholarResult"];
        "pydantic.BaseModel" -> "GoogleScholarResult";
      }

.. autopydantic_model:: tools.tools.google.google_scholar.GoogleScholarResult
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

   tools.tools.google.google_scholar.initialize_google_scholar

.. py:function:: initialize_google_scholar()

   Initialize the Google Scholar API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Scholar API client.

   :returns: A list containing the Google Scholar tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_scholar
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_scholar
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.google.google_trends`
==========================================

.. py:module:: tools.tools.google.google_trends

Google Trends Tool Module.

This module provides a tool for retrieving trend data from Google Trends.
It leverages LangChain's GoogleTrendsQueryRun to fetch information about trending search terms,
relative popularity of search terms over time, and related queries.

.. note::

   This tool may require Google API credentials to be set in environment variables,
   though many Google Trends queries can work without authentication.

.. rubric:: Examples

>>> from haive.tools.tools.google.google_trends import google_trends_tool
>>> result = google_trends_tool[0].invoke("blockchain technology")
>>> print(result)
['The interest in blockchain technology has increased by 120% over the past year...']


.. autolink-examples:: tools.tools.google.google_trends
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_trends.GoogleTrendsResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleTrendsResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleTrendsResult {
        node [shape=record];
        "GoogleTrendsResult" [label="GoogleTrendsResult"];
        "pydantic.BaseModel" -> "GoogleTrendsResult";
      }

.. autopydantic_model:: tools.tools.google.google_trends.GoogleTrendsResult
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

   tools.tools.google.google_trends.initialize_google_trends

.. py:function:: initialize_google_trends()

   Initialize the Google Trends API wrapper.

   This function loads environment variables and configures the Google Trends API client.

   :returns: A list containing the Google Trends search tool.
   :rtype: list


   .. autolink-examples:: initialize_google_trends
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_trends
   :collapse:
   
.. autolink-skip:: next

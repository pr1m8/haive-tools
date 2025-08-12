
:py:mod:`tools.tools.google.google_finance`
===========================================

.. py:module:: tools.tools.google.google_finance

Google Finance Tool Module.

This module provides a tool for retrieving financial information from Google Finance.
It leverages LangChain's GoogleFinanceQueryRun to query financial data like stock prices,
market trends, and company financial information.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key

.. rubric:: Examples

>>> from haive.tools.tools.google.google_finance import google_finance_tool
>>> result = google_finance_tool[0].invoke("AAPL stock price")
>>> print(result)
['Apple Inc. (AAPL) stock is currently trading at $XXX.XX...']


.. autolink-examples:: tools.tools.google.google_finance
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_finance.GoogleFinanceResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleFinanceResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleFinanceResult {
        node [shape=record];
        "GoogleFinanceResult" [label="GoogleFinanceResult"];
        "pydantic.BaseModel" -> "GoogleFinanceResult";
      }

.. autopydantic_model:: tools.tools.google.google_finance.GoogleFinanceResult
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

   tools.tools.google.google_finance.initialize_google_finance

.. py:function:: initialize_google_finance()

   Initialize the Google Finance API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Finance API client.

   :returns: A list containing the Google Finance tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_finance
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_finance
   :collapse:
   
.. autolink-skip:: next

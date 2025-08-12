
:py:mod:`tools.tools.toolkits.alpha_vantage`
============================================

.. py:module:: tools.tools.toolkits.alpha_vantage

Alpha Vantage Toolkit Module.

This module provides a toolkit for accessing financial market data through the Alpha Vantage API.
It offers tools for retrieving stock market data, currency exchange rates, market sentiment analysis,
and other financial information.

The toolkit integrates with Alpha Vantage's comprehensive financial data API, providing access to:
- Real-time and historical stock data
- Foreign exchange rates
- Company information and symbol search
- Market sentiment analysis
- Market movers (top gainers, losers, and most active stocks)

An Alpha Vantage API key is required to use these tools. You can obtain a free API key from:
https://www.alphavantage.co/support/#api-key

Required Environment Variables:
    - ALPHAVANTAGE_API_KEY: Your Alpha Vantage API key

.. rubric:: Examples

>>> from haive.tools.toolkits.alpha_vantage import alpha_vantage_toolkit
>>> # Use the toolkit directly
>>> daily_stock_data = alpha_vantage_toolkit[1].run("AAPL")

>>> # Or with a custom API key
>>> from haive.tools.toolkits.alpha_vantage import AlphaVantageConfig, get_alpha_vantage_tools
>>> config = AlphaVantageConfig(api_key="your_api_key_here")
>>> tools = get_alpha_vantage_tools(config)


.. autolink-examples:: tools.tools.toolkits.alpha_vantage
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.alpha_vantage.AlphaVantageConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AlphaVantageConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AlphaVantageConfig {
        node [shape=record];
        "AlphaVantageConfig" [label="AlphaVantageConfig"];
        "pydantic.BaseModel" -> "AlphaVantageConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.alpha_vantage.AlphaVantageConfig
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

   tools.tools.toolkits.alpha_vantage.get_alpha_vantage_tools

.. py:function:: get_alpha_vantage_tools(config: AlphaVantageConfig) -> list[langchain_core.tools.Tool]

   Create a list of Alpha Vantage financial data tools.

   This function creates a set of tools for accessing various financial data
   endpoints from the Alpha Vantage API, including stock data, exchange rates,
   market sentiment, and market movers.

   :param config: Configuration with API key and settings.
   :type config: AlphaVantageConfig

   :returns: A list of tools for interacting with Alpha Vantage API.
   :rtype: List[Tool]

   :raises ValueError: If the API client cannot be initialized due to missing credentials.


   .. autolink-examples:: get_alpha_vantage_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.alpha_vantage
   :collapse:
   
.. autolink-skip:: next

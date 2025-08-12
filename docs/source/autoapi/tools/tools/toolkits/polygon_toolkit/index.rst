
:py:mod:`tools.tools.toolkits.polygon_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.polygon_toolkit

Polygon.io Toolkit Module.

This module provides a toolkit for accessing financial market data through the Polygon.io API.
It offers tools for retrieving stock market data, options data, crypto data, forex data,
and market reference data.

The Polygon.io API provides access to:
- Real-time and historical stock data
- Options market data
- Cryptocurrency market data
- Forex (currency) market data
- Reference data (tickers, splits, dividends, etc.)
- Market aggregates and indicators

A Polygon.io API key is required to use these tools. You can obtain an API key from:
https://polygon.io/

Required Environment Variables:
    - POLYGON_API_KEY: Your Polygon.io API key

.. rubric:: Examples

>>> from haive.tools.toolkits.polygon_toolkit import polygon_toolkit
>>> # Use the toolkit directly
>>> tools = polygon_toolkit.get_tools()
>>> ticker_news = tools[0].run("AAPL")

>>> # Or create a custom instance with your own API key
>>> import os
>>> os.environ["POLYGON_API_KEY"] = "your_api_key_here"
>>> from haive.tools.toolkits.polygon_toolkit import create_polygon_toolkit
>>> custom_toolkit = create_polygon_toolkit()


.. autolink-examples:: tools.tools.toolkits.polygon_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.polygon_toolkit.create_polygon_toolkit

.. py:function:: create_polygon_toolkit(api_key: str | None = None) -> langchain_community.agent_toolkits.polygon.toolkit.PolygonToolkit

   Create a Polygon.io toolkit instance with the provided or environment API key.

   This function initializes a Polygon.io API wrapper and creates a toolkit with
   tools for accessing various financial data endpoints from the Polygon.io API.

   :param api_key: Polygon.io API key. If not provided, will use
                   the POLYGON_API_KEY environment variable.
   :type api_key: Optional[str]

   :returns: A toolkit containing tools for interacting with Polygon.io API.
   :rtype: PolygonToolkit

   :raises ValueError: If no API key is available (neither provided nor in environment).


   .. autolink-examples:: create_polygon_toolkit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.polygon_toolkit
   :collapse:
   
.. autolink-skip:: next

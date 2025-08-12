
:py:mod:`tools.tools.yfinance_tool`
===================================

.. py:module:: tools.tools.yfinance_tool

Yahoo Finance News Tool Module.

This module provides a tool for fetching the latest financial news from Yahoo Finance.
It wraps the YahooFinanceNewsTool from LangChain community tools, providing
access to up-to-date financial news, stock information, and market data.

.. rubric:: Examples

>>> from haive.tools.tools.yfinance_tool import yfinance_news_tool
>>> result = yfinance_news_tool.run("AAPL")
>>> print(result)  # Returns latest news about Apple Inc.


.. autolink-examples:: tools.tools.yfinance_tool
   :collapse:





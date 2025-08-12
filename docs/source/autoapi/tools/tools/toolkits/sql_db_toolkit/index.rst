
:py:mod:`tools.tools.toolkits.sql_db_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.sql_db_toolkit

SQL Database Toolkit Module.

This module provides a toolkit for interacting with SQL databases through LangChain's
SQL Database Toolkit. It initializes a connection to a SQLite database and creates
a toolkit that can be used by agents to query and manipulate the database.

The module leverages LangChain's utilities and agent toolkits to provide a comprehensive
set of tools for SQL operations, including schema inspection, query generation,
and data retrieval.

.. rubric:: Example

>>> from haive.tools.toolkits.sql_db_toolkit import toolkit
>>> from langchain.agents import create_sql_agent
>>> agent = create_sql_agent(toolkit=toolkit, llm=llm)
>>> agent.run("How many tracks are in the database?")

.. note::

   This module is configured to use a SQLite database named "Chinook.db" by default.
   You can modify the database URI to connect to other SQL database types.


.. autolink-examples:: tools.tools.toolkits.sql_db_toolkit
   :collapse:





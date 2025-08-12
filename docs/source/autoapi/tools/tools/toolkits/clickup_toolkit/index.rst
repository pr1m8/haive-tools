
:py:mod:`tools.tools.toolkits.clickup_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.clickup_toolkit

ClickUp Toolkit Module.

This module provides a toolkit for interacting with ClickUp's API through LangChain's
agent toolkit interface. It creates a wrapper around the ClickUp API that can be used
by agents to manage tasks, lists, folders, and other ClickUp resources.

The module exports a function that initializes and returns a configured ClickUp
toolkit using credentials from the application's configuration.

.. rubric:: Example

>>> from haive.tools.toolkits.clickup_toolkit import get_clickup_toolkit
>>> from langchain.agents import initialize_agent, AgentType
>>> toolkit = get_clickup_toolkit()
>>> agent = initialize_agent(
>>>     tools=toolkit.get_tools(),
>>>     llm=llm,
>>>     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
>>>     verbose=True
>>> )
>>> agent.run("Create a new task called 'Document code' in my workspace")

.. note::

   Requires ClickUp API credentials to be set in the application configuration.
   You'll need a valid API key, client ID, client secret, and redirect URI.


.. autolink-examples:: tools.tools.toolkits.clickup_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.clickup_toolkit.get_clickup_toolkit

.. py:function:: get_clickup_toolkit() -> langchain_community.agent_toolkits.clickup.toolkit.ClickupToolkit

   Initialize and return a ClickUp toolkit with configured API credentials.

   This function creates a ClickupAPIWrapper using credentials from the
   application configuration, then uses that wrapper to initialize a
   ClickupToolkit that can be used by LangChain agents.

   :returns: A toolkit containing ClickUp API tools ready for use in agents
   :rtype: ClickupToolkit

   :raises ValueError: If required ClickUp credentials are missing from configuration


   .. autolink-examples:: get_clickup_toolkit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.clickup_toolkit
   :collapse:
   
.. autolink-skip:: next

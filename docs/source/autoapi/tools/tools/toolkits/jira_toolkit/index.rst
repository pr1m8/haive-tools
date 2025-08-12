
:py:mod:`tools.tools.toolkits.jira_toolkit`
===========================================

.. py:module:: tools.tools.toolkits.jira_toolkit

Jira Integration Toolkit Module.

This module provides a comprehensive toolkit for interacting with Jira instances via the
atlassian-python-api library. It enables agents to perform operations such as searching for issues
using JQL queries, creating new issues, retrieving project information, and making custom API
calls to the Jira API.

The toolkit includes tools for:
- Searching issues with JQL (Jira Query Language)
- Retrieving all accessible projects
- Creating new issues with customizable fields
- A "catch-all" tool for accessing any Jira API functionality
- Creating Confluence pages

Required Environment Variables:
    - JIRA_API_TOKEN: Your Jira API token
    - JIRA_USERNAME: Your Jira username (typically email)
    - JIRA_INSTANCE_URL: URL of your Jira instance
    - JIRA_CLOUD: Set to "True" for cloud instances

.. rubric:: Examples

>>> from langchain_community.utilities.jira import JiraAPIWrapper
>>> from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
>>> jira = JiraAPIWrapper()
>>> toolkit = JiraToolkit.from_jira_api_wrapper(jira)
>>> tools = toolkit.get_tools()
>>> # Use tools with an agent framework
>>> from langchain.agents import initialize_agent, AgentType
>>> from langchain_openai import OpenAI
>>> llm = OpenAI(temperature=0)
>>> agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
>>> agent.run("Create a task in project XYZ to remind me about the quarterly report")


.. autolink-examples:: tools.tools.toolkits.jira_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.jira_toolkit.JiraToolManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for JiraToolManager:

   .. graphviz::
      :align: center

      digraph inheritance_JiraToolManager {
        node [shape=record];
        "JiraToolManager" [label="JiraToolManager"];
      }

.. autoclass:: tools.tools.toolkits.jira_toolkit.JiraToolManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.jira_toolkit
   :collapse:
   
.. autolink-skip:: next

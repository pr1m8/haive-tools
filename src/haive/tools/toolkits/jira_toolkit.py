"""
Jira Integration Toolkit Module

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

Examples:
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
"""

import os
from typing import Any, Dict, List, Optional

from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from langchain_community.utilities.jira import JiraAPIWrapper
from langchain_openai import OpenAI


class JiraToolManager:
    """
    Manager class for Jira tools integration.

    This class provides a simplified interface for initializing and using the Jira toolkit
    with LangChain agents.

    Attributes:
        jira_api (JiraAPIWrapper): The wrapped Jira API client.
        toolkit (JiraToolkit): The Jira toolkit containing all tools.
        tools (List): The list of individual tools from the toolkit.
    """

    def __init__(
        self,
        api_token: Optional[str] = None,
        username: Optional[str] = None,
        instance_url: Optional[str] = None,
        is_cloud: bool = True,
    ):
        """
        Initialize the Jira Tool Manager.

        Args:
            api_token (Optional[str]): Jira API token. If not provided, will use JIRA_API_TOKEN env var.
            username (Optional[str]): Jira username. If not provided, will use JIRA_USERNAME env var.
            instance_url (Optional[str]): Jira instance URL. If not provided, will use JIRA_INSTANCE_URL env var.
            is_cloud (bool): Whether the Jira instance is cloud-based. Defaults to True.
        """
        # Set environment variables if provided
        if api_token:
            os.environ["JIRA_API_TOKEN"] = api_token
        if username:
            os.environ["JIRA_USERNAME"] = username
        if instance_url:
            os.environ["JIRA_INSTANCE_URL"] = instance_url
        os.environ["JIRA_CLOUD"] = str(is_cloud)

        # Initialize the API wrapper and toolkit
        self.jira_api = JiraAPIWrapper()
        self.toolkit = JiraToolkit.from_jira_api_wrapper(self.jira_api)
        self.tools = self.toolkit.get_tools()

    def create_agent(self, llm=None, verbose: bool = False) -> Any:
        """
        Create an agent with the Jira toolkit.

        Args:
            llm: Language model to use. If None, initializes an OpenAI model.
            verbose (bool): Whether to enable verbose output. Defaults to False.

        Returns:
            Any: The initialized agent that can be used with agent.run()
        """
        if llm is None:
            llm = OpenAI(temperature=0)

        return initialize_agent(
            self.tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=verbose,
        )

    def get_projects(self) -> List[Dict[str, Any]]:
        """
        Get all projects the user has access to.

        Returns:
            List[Dict[str, Any]]: List of project dictionaries.
        """
        return self.jira_api.projects()

    def create_issue(
        self,
        summary: str,
        description: str,
        project_key: str,
        issue_type: str = "Task",
        priority: str = "Medium",
    ) -> Dict[str, Any]:
        """
        Create a new Jira issue directly.

        Args:
            summary (str): Issue summary/title.
            description (str): Issue description.
            project_key (str): Project key (e.g. "ABC").
            issue_type (str): Issue type name. Defaults to "Task".
            priority (str): Priority name. Defaults to "Medium".

        Returns:
            Dict[str, Any]: Response from Jira API containing the created issue details.
        """
        issue_dict = {
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
            "priority": {"name": priority},
            "project": {"key": project_key},
        }
        return self.jira_api.create_issue(issue_dict)

    def jql_search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for issues using JQL (Jira Query Language).

        Args:
            query (str): JQL query string (e.g. "project = ABC AND status = 'In Progress'").

        Returns:
            List[Dict[str, Any]]: List of matching issues.
        """
        return self.jira_api.jql_query(query)


# Make the tools directly accessible
JiraTools = JiraToolkit.from_jira_api_wrapper(JiraAPIWrapper()).get_tools()

"""ClickUp Toolkit Module.

This module provides a toolkit for interacting with ClickUp's API through LangChain's
agent toolkit interface. It creates a wrapper around the ClickUp API that can be used
by agents to manage tasks, lists, folders, and other ClickUp resources.

The module exports a function that initializes and returns a configured ClickUp
toolkit using credentials from the application's configuration.

Example:
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

Note:
    Requires ClickUp API credentials to be set in the application configuration.
    You'll need a valid API key, client ID, client secret, and redirect URI.

"""

from langchain_community.agent_toolkits.clickup.toolkit import ClickupToolkit
from langchain_community.utilities.clickup import ClickupAPIWrapper

from haive.config.config import Config


def get_clickup_toolkit() -> ClickupToolkit:
    """Initialize and return a ClickUp toolkit with configured API credentials.

    This function creates a ClickupAPIWrapper using credentials from the
    application configuration, then uses that wrapper to initialize a
    ClickupToolkit that can be used by LangChain agents.

    Returns:
        ClickupToolkit: A toolkit containing ClickUp API tools ready for use in agents

    Raises:
        ValueError: If required ClickUp credentials are missing from configuration

    """
    clickup_api_wrapper = ClickupAPIWrapper(
        api_key=Config.CLICKUP_API_KEY,
        redirect_uri=Config.CLICKUP_REDIRECT_URI,
        client_id=Config.CLICKUP_CLIENT_ID,
        client_secret=Config.CLICKUP_CLIENT_SECRET,
    )

    return ClickupToolkit(api_wrapper=clickup_api_wrapper)

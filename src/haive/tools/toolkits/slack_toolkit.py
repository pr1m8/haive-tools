"""Slack toolkit for interacting with Slack workspaces.

This module provides tools for interacting with Slack workspaces, including
sending messages, reading channels, and managing content. The toolkit leverages
LangChain's SlackToolkit to interact with the Slack API.

To use this toolkit, you need to have a Slack user token set in your environment
variables as SLACK_USER_TOKEN. If not set, the module will prompt for the token
when imported. You can obtain a token from https://api.slack.com/apps.

The toolkit includes tools for:
- Sending messages to channels or users
- Reading messages from channels
- Searching for messages
- Managing channels and users

Typical usage:
    from haive.tools.toolkits.slack_toolkit import slack_toolkit

    # Use in an agent
    agent = Agent(tools=slack_toolkit)
    agent.run("Send a message to the general channel")
"""

import getpass
import os
from typing import List

from haive.config.config import Config
from langchain_community.agent_toolkits import SlackToolkit
from langchain_core.tools import BaseTool


def get_slack_tools() -> List[BaseTool]:
    """Get tools for interacting with Slack.

    This function creates and returns tools for interacting with Slack workspaces
    using the Slack API. If the SLACK_USER_TOKEN is not set in the environment,
    it will prompt the user to enter it.

    Returns:
        A list of BaseTool instances for interacting with Slack.

    Raises:
        ValueError: If the Slack API returns an error or if authentication fails.
    """
    # Ensure we have a Slack token
    if not Config.SLACK_USER_TOKEN:
        os.environ["SLACK_USER_TOKEN"] = getpass.getpass(
            "Enter your Slack user token: "
        )

    # Create the toolkit and get the tools
    toolkit = SlackToolkit()
    return toolkit.get_tools()


# Export the tools for easy access
slack_toolkit = get_slack_tools()

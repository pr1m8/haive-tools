
:py:mod:`tools.tools.toolkits.slack_toolkit`
============================================

.. py:module:: tools.tools.toolkits.slack_toolkit

Slack toolkit for interacting with Slack workspaces.

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


.. autolink-examples:: tools.tools.toolkits.slack_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.slack_toolkit.get_slack_tools

.. py:function:: get_slack_tools() -> list[langchain_core.tools.BaseTool]

   Get tools for interacting with Slack.

   This function creates and returns tools for interacting with Slack workspaces
   using the Slack API. If the SLACK_USER_TOKEN is not set in the environment,
   it will prompt the user to enter it.

   :returns: A list of BaseTool instances for interacting with Slack.

   :raises ValueError: If the Slack API returns an error or if authentication fails.


   .. autolink-examples:: get_slack_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.slack_toolkit
   :collapse:
   
.. autolink-skip:: next

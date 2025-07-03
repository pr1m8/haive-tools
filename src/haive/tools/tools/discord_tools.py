"""Discord integration toolkit for Haive agents.

This module provides a toolkit for interacting with Discord through the LangChain
Discord integration. It allows agents to perform various Discord operations like
sending messages, reading channels, and managing server content.

The module loads necessary environment variables from a .env file and initializes
the Discord toolkit, making it available for use in agent workflows.

Requires:
    - Discord bot token and permissions set in environment variables
    - langchain_discord_shikenso package
    - python-dotenv package
    - Proper Discord application setup with API access

Example:
    To use the Discord tools in an agent:
    ```python
    from haive.tools.tools.discord_tools import discord_tools

    # Add to your agent's toolkit
    agent = Agent(tools=discord_tools)
    ```
"""

from dotenv import load_dotenv
from langchain_discord_shikenso.toolkits import DiscordToolkit

# Load environment variables from .env file
load_dotenv(".env")

# Initialize the Discord toolkit
discord_toolkit = DiscordToolkit()

# Get all available Discord tools
discord_tools = discord_toolkit.get_tools()

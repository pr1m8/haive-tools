"""Steam Toolkit Module

This toolkit provides integration with the Steam Web API, enabling access to
information about Steam games, players, achievements, and other related data.
It wraps the LangChain SteamToolkit to provide seamless integration with Haive's
toolkit system.

The Steam Web API requires an API key which should be stored in environment variables
or configuration. See https://steamcommunity.com/dev to obtain a Steam API key.

Examples:
    >>> from haive.tools.toolkits.steam_toolkit import steam_toolkit
    >>> tools = steam_toolkit.get_tools()
    >>> # Get information about a Steam game
    >>> game_info = tools[0].invoke({"app_id": 440})  # Team Fortress 2
    >>> print(game_info["name"])
    'Team Fortress 2'

    >>> # Get news about a game
    >>> news = tools[1].invoke({"app_id": 570, "count": 3})  # Dota 2
    >>> print(news["newsitems"][0]["title"])
    'Dota 2 Update - June 15, 2023'
"""

import getpass
import os

from dotenv import load_dotenv
from haive.config.config import Config
from langchain_community.agent_toolkits.steam.toolkit import SteamToolkit
from langchain_community.utilities.steam import SteamWebAPIWrapper

# Load environment variables from .env file if it exists
load_dotenv(".env")


# Initialize the Steam Web API wrapper
Steam = SteamWebAPIWrapper()

# Create the Steam toolkit from the API wrapper
steam_toolkit = SteamToolkit.from_steam_api_wrapper(Steam)

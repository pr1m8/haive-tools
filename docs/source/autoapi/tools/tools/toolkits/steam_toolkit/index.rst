
:py:mod:`tools.tools.toolkits.steam_toolkit`
============================================

.. py:module:: tools.tools.toolkits.steam_toolkit

Steam Toolkit Module.

This toolkit provides integration with the Steam Web API, enabling access to
information about Steam games, players, achievements, and other related data.
It wraps the LangChain SteamToolkit to provide seamless integration with Haive's
toolkit system.

The Steam Web API requires an API key which should be stored in environment variables
or configuration. See https://steamcommunity.com/dev to obtain a Steam API key.

.. rubric:: Examples

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


.. autolink-examples:: tools.tools.toolkits.steam_toolkit
   :collapse:





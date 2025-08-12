
:py:mod:`tools.tools.toolkits.free_to_game_toolkit`
===================================================

.. py:module:: tools.tools.toolkits.free_to_game_toolkit

Free-To-Game Toolkit Module.

This toolkit provides a collection of tools to interact with the Free-To-Game API,
allowing users to search, filter, and retrieve information about free-to-play games
across different platforms and categories. The API is provided by https://www.freetogame.com/api.

.. rubric:: Examples

>>> from haive.tools.toolkits.free_to_game_toolkit import FreeToGameToolkit
>>> toolkit = FreeToGameToolkit()
>>> tools = toolkit.get_tools()
>>> # Get all games with category 'shooter' sorted by popularity
>>> games = tools[0].invoke({"category": "shooter", "sort_by": "popularity"})
>>> print(games[0]["title"])
'Valorant'

>>> # Get details for a specific game
>>> game_details = tools[1].invoke({"game_id": 452})
>>> print(game_details["title"])
'Call of Duty: Warzone'

>>> # Filter games by multiple tags
>>> filtered_games = tools[2].invoke({"tag": "mmorpg.fantasy", "platform": "pc"})
>>> print(filtered_games[0]["title"])
'World of Warcraft'


.. autolink-examples:: tools.tools.toolkits.free_to_game_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.free_to_game_toolkit.FilterGamesByTagsInput
   tools.tools.toolkits.free_to_game_toolkit.FreeToGameToolkit
   tools.tools.toolkits.free_to_game_toolkit.GetAllGamesInput
   tools.tools.toolkits.free_to_game_toolkit.GetGameDetailsInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FilterGamesByTagsInput:

   .. graphviz::
      :align: center

      digraph inheritance_FilterGamesByTagsInput {
        node [shape=record];
        "FilterGamesByTagsInput" [label="FilterGamesByTagsInput"];
        "pydantic.BaseModel" -> "FilterGamesByTagsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.free_to_game_toolkit.FilterGamesByTagsInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FreeToGameToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_FreeToGameToolkit {
        node [shape=record];
        "FreeToGameToolkit" [label="FreeToGameToolkit"];
        "langchain_core.tools.BaseToolkit" -> "FreeToGameToolkit";
      }

.. autoclass:: tools.tools.toolkits.free_to_game_toolkit.FreeToGameToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetAllGamesInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetAllGamesInput {
        node [shape=record];
        "GetAllGamesInput" [label="GetAllGamesInput"];
        "pydantic.BaseModel" -> "GetAllGamesInput";
      }

.. autopydantic_model:: tools.tools.toolkits.free_to_game_toolkit.GetAllGamesInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetGameDetailsInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetGameDetailsInput {
        node [shape=record];
        "GetGameDetailsInput" [label="GetGameDetailsInput"];
        "pydantic.BaseModel" -> "GetGameDetailsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.free_to_game_toolkit.GetGameDetailsInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   tools.tools.toolkits.free_to_game_toolkit.filter_games_by_tags
   tools.tools.toolkits.free_to_game_toolkit.get_all_games
   tools.tools.toolkits.free_to_game_toolkit.get_game_details

.. py:function:: filter_games_by_tags(input: FilterGamesByTagsInput) -> list[dict]

   Filter games by multiple tags (dot-separated) and optional platform.

   :param input: Input parameters containing tags and optional platform.
   :type input: FilterGamesByTagsInput

   :returns: A list of game objects matching the specified tags and platform.
   :rtype: List[dict]

   :raises requests.RequestException: If the API request fails or the tags are invalid.


   .. autolink-examples:: filter_games_by_tags
      :collapse:

.. py:function:: get_all_games(input: GetAllGamesInput) -> list[dict]

   Retrieve all free-to-play games with optional filtering by platform, category,.
   and sort order.

   :param input: Input parameters for filtering and sorting games.
   :type input: GetAllGamesInput

   :returns: A list of game objects matching the specified criteria.
   :rtype: List[dict]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_all_games
      :collapse:

.. py:function:: get_game_details(input: GetGameDetailsInput) -> dict

   Get detailed information about a specific game by its ID.

   :param input: Input parameters containing the game ID.
   :type input: GetGameDetailsInput

   :returns: Detailed information about the requested game.
   :rtype: dict

   :raises requests.RequestException: If the API request fails or the game ID is invalid.


   .. autolink-examples:: get_game_details
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.free_to_game_toolkit
   :collapse:
   
.. autolink-skip:: next

"""Free-To-Game Toolkit Module.

This toolkit provides a collection of tools to interact with the Free-To-Game API,
allowing users to search, filter, and retrieve information about free-to-play games
across different platforms and categories. The API is provided by https://www.freetogame.com/api.

Examples:
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

"""

import requests
from langchain_core.tools import BaseToolkit, StructuredTool
from pydantic import BaseModel, Field

BASE_URL = "https://www.freetogame.com/api"


class GetAllGamesInput(BaseModel):
    """Input model for retrieving all free-to-play games with optional filtering
    parameters.

    Attributes:
        platform (Optional[str]): Filter games by platform (pc or browser).
        category (Optional[str]): Filter games by category or genre.
        sort_by (Optional[str]): Sort results by specified criteria.

    """

    platform: str | None = Field(
        None, description="Platform name, e.g. 'pc', 'browser'"
    )
    category: str | None = Field(
        None, description="Category/tag, e.g. 'shooter', 'mmorpg', 'racing', 'social'"
    )
    sort_by: str | None = Field(
        None,
        description="Sort by one of: 'release-date', 'popularity', 'alphabetical', 'relevance'",
    )


def get_all_games(input: GetAllGamesInput) -> list[dict]:
    """Retrieve all free-to-play games with optional filtering by platform, category,
    and sort order.

    Args:
        input (GetAllGamesInput): Input parameters for filtering and sorting games.

    Returns:
        List[dict]: A list of game objects matching the specified criteria.

    Raises:
        requests.RequestException: If the API request fails.

    """
    params = {}
    if input.platform:
        params["platform"] = input.platform
    if input.category:
        params["category"] = input.category
    if input.sort_by:
        params["sort-by"] = input.sort_by
    response = requests.get(f"{BASE_URL}/games", params=params)
    response.raise_for_status()
    return response.json()


class GetGameDetailsInput(BaseModel):
    """Input model for retrieving detailed information about a specific game.

    Attributes:
        game_id (int): The unique identifier for the game to retrieve details for.

    """

    game_id: int = Field(..., description="The game ID to retrieve.")


def get_game_details(input: GetGameDetailsInput) -> dict:
    """Get detailed information about a specific game by its ID.

    Args:
        input (GetGameDetailsInput): Input parameters containing the game ID.

    Returns:
        dict: Detailed information about the requested game.

    Raises:
        requests.RequestException: If the API request fails or the game ID is invalid.

    """
    response = requests.get(f"{BASE_URL}/game", params={"id": input.game_id})
    response.raise_for_status()
    return response.json()


class FilterGamesByTagsInput(BaseModel):
    """Input model for filtering games by multiple tags and optional platform.

    Attributes:
        tag (str): Dot-separated tag filter to match games with specific features.
        platform (Optional[str]): Optional platform filter (pc or browser).

    """

    tag: str = Field(
        ..., description="Dot-separated tag filter, e.g. '3d.mmorpg.fantasy.pvp'"
    )
    platform: str | None = Field(
        None, description="Platform name, e.g. 'pc', 'browser'"
    )


def filter_games_by_tags(input: FilterGamesByTagsInput) -> list[dict]:
    """Filter games by multiple tags (dot-separated) and optional platform.

    Args:
        input (FilterGamesByTagsInput): Input parameters containing tags and optional platform.

    Returns:
        List[dict]: A list of game objects matching the specified tags and platform.

    Raises:
        requests.RequestException: If the API request fails or the tags are invalid.

    """
    params = {"tag": input.tag}
    if input.platform:
        params["platform"] = input.platform
    response = requests.get(f"{BASE_URL}/filter", params=params)
    response.raise_for_status()
    return response.json()


class FreeToGameToolkit(BaseToolkit):
    """LangChain toolkit for the FreeToGame API (Free-To-Play Games Database).

    This toolkit provides structured tools for interacting with the FreeToGame API,
    allowing agents to search, filter, and retrieve information about free-to-play games.

    Attributes:
        None

    """

    def get_tools(self) -> list[StructuredTool]:
        """Get the list of tools provided by this toolkit.

        Returns:
            List[StructuredTool]: A list of structured tools for working with the FreeToGame API.

        """
        return [
            StructuredTool.from_function(get_all_games),
            StructuredTool.from_function(get_game_details),
            StructuredTool.from_function(filter_games_by_tags),
        ]

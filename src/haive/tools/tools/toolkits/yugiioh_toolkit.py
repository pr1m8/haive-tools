"""Yu-Gi-Oh! API Toolkit Module.

This toolkit provides a collection of tools to interact with the Yu-Gi-Oh! API,
allowing users to search for cards, get card details, retrieve information about
card sets, archetypes, and more. The API is provided by https://db.ygoprodeck.com/api/v7/.

Examples:
    >>> from haive.tools.toolkits.yugiioh_toolkit import yugioh_api_toolkit
    >>> # Get information about a specific card by name
    >>> card_info = yugioh_api_toolkit[0].invoke({"name": "Dark Magician"})
    >>> print(card_info['data'][0]['name'])
    'Dark Magician'

    >>> # Get all card sets
    >>> card_sets = yugioh_api_toolkit[1].invoke()
    >>> print(card_sets[0]['set_name'])
    'Legend of Blue Eyes White Dragon'

    >>> # Get a random card
    >>> random_card = yugioh_api_toolkit[3].invoke()
    >>> print(random_card['name'])
    'Blue-Eyes White Dragon'

"""

import requests
from langchain.agents import Tool
from langchain_core.tools import StructuredTool
from pydantic.v1 import BaseModel, Field


# Schema for querying card info
class GetCardInfoInput(BaseModel):
    """Input model for querying Yu-Gi-Oh! card information with various filters.

    Attributes:
        name (Optional[str]): Filter by exact card name.
        fname (Optional[str]): Fuzzy search by name fragment.
        archetype (Optional[str]): Filter by card archetype.
        attribute (Optional[str]): Filter by card attribute (DARK, LIGHT, etc).
        race (Optional[str]): Filter by card race/type (Warrior, Dragon, etc).
        level (Optional[int]): Filter by card level or rank.
        cardset (Optional[str]): Filter by card set name.
        format (Optional[str]): Filter by card format (TCG, OCG, Speed Duel, etc).
        misc (Optional[bool]): Include additional metadata in the response.

    """

    name: str | None = Field(None, description="Exact card name")
    fname: str | None = Field(None, description="Fuzzy search by name fragment")
    archetype: str | None = Field(None, description="Card archetype, e.g. Blue-Eyes")
    attribute: str | None = Field(None, description="Card attribute, e.g. DARK, LIGHT")
    race: str | None = Field(None, description="Card race/type, e.g. Warrior, Dragon")
    level: int | None = Field(None, description="Level or rank of the card")
    cardset: str | None = Field(None, description="Card set, e.g. Metal Raiders")
    format: str | None = Field(None, description="Card format, e.g. TCG, Speed Duel")
    misc: bool | None = Field(
        False, description="Whether to include additional metadata"
    )


def get_card_info(input_data: GetCardInfoInput) -> dict:
    """Retrieve Yu-Gi-Oh! card information based on the provided filters.

    Args:
        input_data (GetCardInfoInput): Input parameters for filtering card results.

    Returns:
        dict: A dictionary containing card information matching the specified filters.

    Raises:
        requests.RequestException: If the API request fails or the parameters are invalid.

    """
    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    params = {k: v for k, v in input_data.dict().items() if v is not None}
    if input_data.misc:
        params["misc"] = "yes"
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


# Main card lookup tool
card_info_tool = StructuredTool.from_function(
    name="get_yugioh_card_info",
    description="Retrieve detailed Yu-Gi-Oh! card info using name, archetype, attribute, level, etc.",
    args_schema=GetCardInfoInput,
    func=get_card_info,
)


# Simple REST endpoints
def get_card_sets() -> list[dict]:
    """Get a list of all Yu-Gi-Oh! card sets.

    Returns:
        List[dict]: A list of card set objects containing set information.

    Raises:
        requests.RequestException: If the API request fails.

    """
    return requests.get("https://db.ygoprodeck.com/api/v7/cardsets.php").json()


def get_archetypes() -> list[dict]:
    """Get a list of all Yu-Gi-Oh! archetypes.

    Returns:
        List[dict]: A list of archetype objects.

    Raises:
        requests.RequestException: If the API request fails.

    """
    return requests.get("https://db.ygoprodeck.com/api/v7/archetypes.php").json()


def get_random_card() -> dict:
    """Get information about a random Yu-Gi-Oh! card.

    Returns:
        dict: Detailed information about a randomly selected card.

    Raises:
        requests.RequestException: If the API request fails.

    """
    return requests.get("https://db.ygoprodeck.com/api/v7/randomcard.php").json()


def get_database_version() -> dict:
    """Check the current version of the Yu-Gi-Oh! database.

    Returns:
        dict: Information about the current database version.

    Raises:
        requests.RequestException: If the API request fails.

    """
    return requests.get("https://db.ygoprodeck.com/api/v7/checkDBVer.php").json()


# Toolkit
yugioh_api_toolkit = [
    card_info_tool,
    Tool(
        name="get_yugioh_card_sets",
        func=get_card_sets,
        description="Get all Yu-Gi-Oh! card sets",
    ),
    Tool(
        name="get_yugioh_archetypes",
        func=get_archetypes,
        description="Get all Yu-Gi-Oh! archetypes",
    ),
    Tool(
        name="get_random_yugioh_card",
        func=get_random_card,
        description="Get a random Yu-Gi-Oh! card",
    ),
    Tool(
        name="get_yugioh_database_version",
        func=get_database_version,
        description="Check the Yu-Gi-Oh! database version",
    ),
]


# Note: This module does not use the BaseToolkit pattern like other toolkits
# Instead, it directly exports a list of tools as yugioh_api_toolkit

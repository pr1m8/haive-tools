from typing import Any

from langchain_core.tools import BaseToolkit, StructuredTool
from pydantic import BaseModel, Field
import requests

r"""Rick and Morty API Toolkit Module.

This toolkit provides tools for accessing data from the Rick and Morty TV show via
the official Rick and Morty API. It offers both REST and GraphQL endpoints for retrieving
information about characters, locations, and episodes from the show.

The toolkit includes tools for:
- Getting specific characters by ID
- Filtering characters by various attributes
- Performing GraphQL queries for more complex data retrieval
- Getting location information

No authentication or API keys are required to use this API.

Examples:
    >>> from haive.tools.toolkits.rick_and_morty_toolkit import get_character_by_id
    >>> # Get information about Rick (ID: 1)
    >>> rick_info = get_character_by_id(1)
    >>> print(f"Name: {rick_info['name']}\nSpecies: {rick_info['species']}")
    Name: Rick Sanchez
    Species: Human

    >>> # Filter characters
    >>> from haive.tools.toolkits.rick_and_morty_toolkit import filter_characters
    >>> aliens = filter_characters(species="Alien", status="Alive")
    >>> print(f"Found {aliens['info']['count']} living aliens")
"""


# API endpoints
GRAPHQL_ENDPOINT = "https://rickandmortyapi.com/graphql"
REST_BASE_URL = "https://rickandmortyapi.com/api"


# --------------------- REST Tools ---------------------


class GetCharacterByIDInput(BaseModel):
    """Input schema for getting a Rick and Morty character by ID.

    Attributes:
        id (int): The unique identifier of the character to retrieve.

    """

    id: int = Field(..., description="The ID of the character.")


def get_character_by_id(id: int) -> dict[str, Any]:
    """Get detailed information about a specific Rick and Morty character by ID.

    This function retrieves a character's complete information including their
    status, species, gender, origin, location, and episode appearances.

    Args:
        id (int): The unique identifier of the character to retrieve.

    Returns:
        Dict[str, Any]: Character data including name, status, species, gender,
            origin, location, and episode appearances.

    Raises:
        requests.RequestException: If the API request fails.

    """
    url = f"{REST_BASE_URL}/character/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


get_character_tool = StructuredTool.from_function(
    name="get_rick_and_morty_character_by_id",
    description="Get Rick and Morty character by ID using the REST API.",
    func=get_character_by_id,
    args_schema=GetCharacterByIDInput,
)


class FilterCharactersInput(BaseModel):
    """Input schema for filtering Rick and Morty characters.

    This model defines optional parameters that can be used to filter
    the characters returned by the Rick and Morty API.

    Attributes:
        name (Optional[str]): Filter by character name (case-insensitive, partial matches).
        status (Optional[str]): Filter by character status ("alive", "dead", or "unknown").
        species (Optional[str]): Filter by character species (e.g., "Human", "Alien").
        gender (Optional[str]): Filter by character gender ("male", "female", "genderless", "unknown").

    """

    name: str | None = Field(None, description="Filter characters by name.")
    status: str | None = Field(None, description="alive, dead, or unknown")
    species: str | None = Field(None, description="Filter characters by species.")
    gender: str | None = Field(None, description="male, female, genderless, unknown")


def filter_characters(
    name: str | None = None,
    status: str | None = None,
    species: str | None = None,
    gender: str | None = None,
) -> dict[str, Any]:
    """Filter Rick and Morty characters by various attributes.

    This function allows filtering characters by name, status, species, and gender.
    Filters can be combined to narrow down results.

    Args:
        name (Optional[str], optional): Filter by character name. Defaults to None.
        status (Optional[str], optional): Filter by character status. Defaults to None.
            Valid values: "alive", "dead", "unknown".
        species (Optional[str], optional): Filter by character species. Defaults to None.
        gender (Optional[str], optional): Filter by character gender. Defaults to None.
            Valid values: "male", "female", "genderless", "unknown".

    Returns:
        Dict[str, Any]: Dictionary containing filtered character results and pagination info.

    Raises:
        requests.RequestException: If the API request fails.

    """
    params = {"name": name, "status": status, "species": species, "gendef": gender}
    params = {k: v for k, v in params.items() if v}
    url = f"{REST_BASE_URL}/character"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


filter_characters_tool = StructuredTool.from_function(
    name="filter_rick_and_morty_characters",
    description="Filter Rick and Morty characters using the REST API with optional parameters.",
    func=filter_characters,
    args_schema=FilterCharactersInput,
)


# --------------------- GraphQL Tools ---------------------


class GraphQLCharactersQueryInput(BaseModel):
    """Input schema for the GraphQL character query.

    This model defines the parameters that can be passed to the GraphQL API
    when querying for Rick and Morty characters.

    Attributes:
        name (Optional[str]): Character name to filter results by.
        page (Optional[int]): Page number for paginated results.

    """

    name: str | None = Field(None, description="Character name to filter")
    page: int | None = Field(None, description="Page number")


def graphql_characters_query(
    name: str | None = None, page: int | None = None
) -> dict[str, Any]:
    """Query Rick and Morty characters using the GraphQL API.

    This function sends a GraphQL query to retrieve character information
    with optional filtering by name and pagination support.

    Args:
        name (Optional[str], optional): Character name to filter by. Defaults to None.
        page (Optional[int], optional): Page number for paginated results. Defaults to None.

    Returns:
        Dict[str, Any]: GraphQL response containing character data and metadata.

    Raises:
        requests.RequestException: If the API request fails.

    """
    query = """
    query ($page: Int, $name: String) {
      characters(page: $page, filter: { name: $name }) {
        info {
          count
          pages
          next
          prev
        }
        results {
          id
          name
          status
          species
          gender
        }
      }
    }
    """
    variables = {"page": page, "name": name}
    response = requests.post(
        GRAPHQL_ENDPOINT, json={"query": query, "variables": variables}
    )
    response.raise_for_status()
    return response.json()


graphql_characters_tool = StructuredTool.from_function(
    name="graphql_query_rick_and_morty_characters",
    description="Query Rick and Morty characters using GraphQL endpoint with optional page and name filter.",
    func=graphql_characters_query,
    args_schema=GraphQLCharactersQueryInput,
)


class GraphQLLocationByIDInput(BaseModel):
    """Input schema for the GraphQL location query by ID.

    Attributes:
        id (int): The unique identifier of the location to retrieve.

    """

    id: int = Field(..., description="Location ID")


def graphql_location_by_id(id: int) -> dict[str, Any]:
    """Get detailed information about a specific location by ID using GraphQL.

    This function retrieves information about a location from the Rick and Morty
    universe, including its name, type, and dimension.

    Args:
        id (int): The unique identifier of the location to retrieve.

    Returns:
        Dict[str, Any]: GraphQL response containing location data.

    Raises:
        requests.RequestException: If the API request fails.

    """
    query = """
    query ($id: ID!) {
      location(id: $id) {
        id
        name
        type
        dimension
      }
    }
    """
    response = requests.post(
        GRAPHQL_ENDPOINT, json={"query": query, "variables": {"id": id}}
    )
    response.raise_for_status()
    return response.json()


graphql_location_tool = StructuredTool.from_function(
    name="graphql_query_rick_and_morty_location",
    description="Query a specific location by ID from the Rick and Morty GraphQL API.",
    func=graphql_location_by_id,
    args_schema=GraphQLLocationByIDInput,
)


# --------------------- Toolkit ---------------------


class RickAndMortyToolkit(BaseToolkit):
    """Toolkit for accessing the Rick and Morty API.

    This toolkit provides a collection of tools for retrieving information about
    characters, locations, and episodes from the Rick and Morty TV show using both REST
    and GraphQL endpoints.

    The toolkit includes tools for getting specific characters, filtering characters by
    attributes, and performing more complex queries using GraphQL.

    """

    def get_tools(self) -> list[StructuredTool]:
        """Get all tools in the Rick and Morty toolkit.

        Returns:
            List[StructuredTool]: A list of tools for interacting with the Rick and Morty API.

        """
        return [
            get_character_tool,
            filter_characters_tool,
            graphql_characters_tool,
            graphql_location_tool,
        ]

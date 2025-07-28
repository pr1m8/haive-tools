"""Rock-Paper-Scissors 101 Toolkit Module.

This toolkit provides a collection of tools to interact with the RPS-101 API,
allowing users to access the expanded version of Rock-Paper-Scissors that includes 101
different objects. The API provides information about all objects, their winning outcomes,
and match results between any two objects. The API is provided by https://rps101.pythonanywhere.com/.

Examples:
    >>> from haive.tools.toolkits.rps_101_toolkit import RPS101Toolkit
    >>> toolkit = RPS101Toolkit()
    >>> tools = toolkit.get_tools()
    >>> # Get all RPS-101 objects
    >>> objects = tools[0].invoke()
    >>> print(objects[:3])  # First three objects
    ['Dynamite', 'Tornado', 'Quicksand']

    >>> # Get winning outcomes for an object
    >>> outcomes = tools[1].invoke({"object_name": "rock"})
    >>> print(outcomes["defeats"][0])
    {'name': 'fire', 'outcome': 'extinguishes'}

    >>> # Get the result of a match between two objects
    >>> match = tools[2].invoke({"object_one": "paper", "object_two": "rock"})
    >>> print(f"{match['winner']} {match['outcome']} {match['loser']}")
    'paper covers rock'
"""

import requests
from langchain_core.tools import BaseToolkit, StructuredTool
from pydantic import BaseModel, Field

BASE_URL = "https://rps101.pythonanywhere.com/api/v1"


# Tool 1: Get All RPS-101 Objects
def _get_all_rps101_objects() -> list[str]:
    """Get a list of all 101 objects in the RPS-101 game.

    Returns:
        List[str]: A list of all object names in the RPS-101 game.

    Raises:
        requests.RequestException: If the API request fails.
    """
    response = requests.get(f"{BASE_URL}/objects/all")
    response.raise_for_status()
    return response.json()


get_all_rps101_objects = StructuredTool.from_function(
    name="get_all_rps101_objects",
    description="Get a list of all RPS-101 objects (e.g. Rock, Paper, Scissors, Nuke, etc).",
    func=_get_all_rps101_objects,
)


# Tool 2: Get Outcomes for an Object
class ObjectNameInput(BaseModel):
    """Input model for retrieving outcome information about a specific RPS-101 object.

    Attributes:
        object_name (str): The name of the RPS-101 object to get information about.
    """

    object_name: str = Field(
        ...,
        description="The name of the RPS-101 object to get winning outcomes for (e.g. 'nuke')",
    )


def _get_rps101_object_outcomes(object_name: str) -> dict:
    """Get detailed information about a specific RPS-101 object, including what it defeats.

    Args:
        object_name (str): The name of the RPS-101 object to get information about.

    Returns:
        dict: A dictionary containing information about the object and what it defeats.
            Format: {"name": str, "defeats": List[{"name": str, "outcome": str}]}

    Raises:
        requests.RequestException: If the API request fails or the object name is invalid.
    """
    response = requests.get(f"{BASE_URL}/objects/{object_name}")
    response.raise_for_status()
    return response.json()


get_rps101_object_outcomes = StructuredTool.from_function(
    name="get_rps101_object_outcomes",
    description="Get the winning outcomes for a given RPS-101 object. Returns what that object defeats and how.",
    func=_get_rps101_object_outcomes,
    args_schema=ObjectNameInput,
)


# Tool 3: Match Two RPS-101 Objects
class RPSMatchInput(BaseModel):
    """Input model for simulating a match between two RPS-101 objects.

    Attributes:
        object_one (str): The name of the first object in the match.
        object_two (str): The name of the second object in the match.
    """

    object_one: str = Field(
        ..., description="The first object in the match (e.g. 'nuke')"
    )
    object_two: str = Field(
        ..., description="The second object in the match (e.g. 'tank')"
    )


def _get_rps101_match_result(object_one: str, object_two: str) -> dict:
    """Get the result of a match between two RPS-101 objects.

    Args:
        object_one (str): The name of the first object in the match.
        object_two (str): The name of the second object in the match.

    Returns:
        dict: A dictionary containing the match result information.
            Format: {"winner": str, "loser": str, "outcome": str}

    Raises:
        requests.RequestException: If the API request fails or the object names are invalid.
    """
    response = requests.get(
        f"{BASE_URL}/match", params={"object_one": object_one, "object_two": object_two}
    )
    response.raise_for_status()
    return response.json()


get_rps101_match_result = StructuredTool.from_function(
    name="get_rps101_match_result",
    description="Get the result of a match between two RPS-101 objects.",
    func=_get_rps101_match_result,
    args_schema=RPSMatchInput,
)


# Toolkit
class RPS101Toolkit(BaseToolkit):
    """LangChain toolkit for the RPS-101 API (Rock-Paper-Scissors with 101 objects).

    This toolkit provides structured tools for interacting with the RPS-101 API,
    allowing agents to explore the 101 objects, understand their relationships,
    and simulate matches between any two objects.

    Attributes:
        None
    """

    def get_tools(self) -> list[StructuredTool]:
        """Get the list of tools provided by this toolkit.

        Returns:
            List[StructuredTool]: A list of structured tools for working with the RPS-101 API.
        """
        return [
            get_all_rps101_objects,
            get_rps101_object_outcomes,
            get_rps101_match_result,
        ]

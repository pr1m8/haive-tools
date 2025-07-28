"""Geek Jokes API Tool Module.

This module provides a tool for fetching random geek and programming-related jokes from
the Geek Jokes API. These jokes are oriented toward programmers, computer enthusiasts,
and tech culture, making them suitable for adding humor to technical conversations.

Examples:
    >>> from haive.tools.tools.geek_jokes_tool import get_geek_joke, GetGeekJokeInput
    >>> joke = get_geek_joke(GetGeekJokeInput())
    >>> print(joke)
    'Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25'
"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class GetGeekJokeInput(BaseModel):
    """Input model for the get_geek_joke function.

    This is an empty input model that exists for compatibility with the LangChain
    structured tool interface. The Geek Jokes API doesn't require any parameters.

    Attributes:
        dummy (Optional[str]): An unused field that maintains compatibility with
            LangChain's requirement for an input schema.
    """

    dummy: str | None = Field(
        None, description="Unused input; the joke requires no input."
    )


def get_geek_joke(_: GetGeekJokeInput) -> str:
    """Fetch a random geek or programming-related joke from the Geek Jokes API.

    This function makes a request to the Geek Jokes API and returns a random
    joke related to geek culture, programming, or technology.

    Args:
        _ (GetGeekJokeInput): Empty input model (not used, but required for
            LangChain compatibility).

    Returns:
        str: A random geek or programming joke as a string.

    Raises:
        requests.RequestException: If the API request fails.
    """
    url = "https://geek-jokes.sameerkumar.website/api?format=json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("joke", "No joke found.")


get_geek_joke_tool = StructuredTool.from_function(
    name="get_geek_joke",
    description="Fetch a random geek or programming-related joke from the Geek Jokes API",
    func=get_geek_joke,
    args_schema=GetGeekJokeInput,
)

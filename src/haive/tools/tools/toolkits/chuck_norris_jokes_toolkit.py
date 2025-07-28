"""Chuck Norris Jokes Toolkit Module.

This toolkit provides a collection of tools to interact with the Chuck Norris Jokes API,
allowing users to retrieve, search, and filter Chuck Norris jokes across different categories.
The API is provided by https://api.chucknorris.io/.

Examples:
    >>> from haive.tools.toolkits.chuck_norris_jokes_toolkit import get_random_joke
    >>> joke = get_random_joke()
    >>> print(joke.value)
    'Chuck Norris can divide by zero.'

    >>> from haive.tools.toolkits.chuck_norris_jokes_toolkit import get_available_categories
    >>> categories = get_available_categories()
    >>> print(categories)
    ['animal', 'career', 'celebrity', ...]
"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class Joke(BaseModel):
    """Response model for Chuck Norris Jokes API.

    Attributes:
        id (str): Unique identifier for the joke.
        icon_url (str): URL to the Chuck Norris icon image.
        value (str): The actual joke text content.
        url (Optional[str]): Optional URL to the joke on the Chuck Norris API website.
    """

    id: str = Field(..., description="Unique identifier for the joke")
    icon_url: str = Field(..., description="URL to the Chuck Norris icon image")
    value: str = Field(..., description="The actual joke text content")
    url: str | None = Field(None, description="Optional URL to the joke on the website")


def get_random_joke() -> Joke:
    """Fetch a random Chuck Norris joke from the API.

    Returns:
        Joke: A random Chuck Norris joke object.

    Raises:
        requests.RequestException: If the API request fails.
    """
    res = requests.get("https://api.chucknorris.io/jokes/random")
    res.raise_for_status()
    return Joke(**res.json())


def get_random_joke_by_category(category: str) -> Joke:
    """Fetch a random Chuck Norris joke from a specific category.

    Args:
        category (str): The joke category to filter by (use get_available_categories
            to see available options).

    Returns:
        Joke: A random Chuck Norris joke from the specified category.

    Raises:
        requests.RequestException: If the API request fails or the category is invalid.
    """
    res = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
    res.raise_for_status()
    return Joke(**res.json())


def get_available_categories() -> list[str]:
    """Get a list of all available joke categories from the Chuck Norris API.

    Returns:
        List[str]: A list of category names as strings.

    Raises:
        requests.RequestException: If the API request fails.
    """
    res = requests.get("https://api.chucknorris.io/jokes/categories")
    res.raise_for_status()
    return res.json()


def search_jokes(query: str) -> list[Joke]:
    """Search for Chuck Norris jokes containing the specified query string.

    Args:
        query (str): The search term to look for in jokes.

    Returns:
        List[Joke]: A list of joke objects matching the search query.

    Raises:
        requests.RequestException: If the API request fails.
    """
    res = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
    res.raise_for_status()
    data = res.json()
    return [Joke(**joke) for joke in data.get("result", [])]


ChuckNorrisToolkit = [
    StructuredTool.from_function(
        func=get_random_joke,
        name="get_random_chuck_joke",
        description="Get a random Chuck Norris joke",
    ),
    StructuredTool.from_function(
        func=get_random_joke_by_category,
        name="get_chuck_joke_by_category",
        description="Get a random Chuck Norris joke from a specified category",
    ),
    StructuredTool.from_function(
        func=get_available_categories,
        name="get_chuck_joke_categories",
        description="Get a list of all available joke categories",
    ),
    StructuredTool.from_function(
        func=search_jokes,
        name="search_chuck_jokes",
        description="Search for Chuck Norris jokes matching a text query",
    ),
]

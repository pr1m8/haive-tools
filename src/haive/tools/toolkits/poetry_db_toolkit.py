"""PoetryDB Toolkit for accessing poetry data from the PoetryDB API.

This toolkit provides tools for interacting with the PoetryDB API,
allowing agents to search for poems by author, title, or content,
and retrieve random poems. It simplifies the process of finding and
analyzing poetry from a variety of sources.

Example:
    ```python
    tools = get_poetry_toolkit()
    ```

Attributes:
    BASE_URL: The base URL for the PoetryDB API
"""

from typing import List, Optional

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

BASE_URL = "https://poetrydb.org"


### --- Tool 1: Search Poems by Author --- ###
class AuthorSearchInput(BaseModel):
    """Input schema for searching poems by author name.

    Args:
        author: Name of the poet to search for
    """

    author: str = Field(..., description="Name of the poet to search for")


def search_poems_by_author(author: str) -> List[dict]:
    """Searches for poems by a specific author or poet.

    Args:
        author: Name of the poet to search for

    Returns:
        List[dict]: Up to 5 poems by the specified author

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    url = f"{BASE_URL}/author/{author}"
    res = requests.get(url)
    res.raise_for_status()
    poems = res.json()
    return poems[:5]  # Return first 5 results


search_poems_by_author_tool = StructuredTool.from_function(
    func=search_poems_by_author,
    name="search_poems_by_author",
    description="Search for poems by a specific poet",
    args_schema=AuthorSearchInput,
)


### --- Tool 2: Search Poem by Title --- ###
class TitleSearchInput(BaseModel):
    """Input schema for searching a poem by its title.

    Args:
        title: Title of the poem to search for
    """

    title: str = Field(..., description="Title of the poem")


def search_poem_by_title(title: str) -> dict:
    """Searches for a poem using its title.

    Args:
        title: Title of the poem to search for

    Returns:
        dict: The first poem matching the given title

    Raises:
        HTTPError: If the request fails or returns an error status code
        IndexError: If no poems match the given title
    """
    url = f"{BASE_URL}/title/{title}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()[0]  # Return first match


search_poem_by_title_tool = StructuredTool.from_function(
    func=search_poem_by_title,
    name="search_poem_by_title",
    description="Search for a poem using its title",
    args_schema=TitleSearchInput,
)


### --- Tool 3: Get Random Poems --- ###
class RandomPoemInput(BaseModel):
    """Input schema for fetching random poems.

    Args:
        count: Number of random poems to retrieve
    """

    count: int = Field(..., description="Number of random poems to fetch")


def get_random_poems(count: int) -> List[dict]:
    """Fetches a specified number of random poems.

    Args:
        count: Number of random poems to retrieve

    Returns:
        List[dict]: The requested number of random poems

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    url = f"{BASE_URL}/random/{count}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


get_random_poems_tool = StructuredTool.from_function(
    func=get_random_poems,
    name="get_random_poems",
    description="Get a number of random poems",
    args_schema=RandomPoemInput,
)


### --- Tool 4: Search Poems by Line Fragment --- ###
class LineSearchInput(BaseModel):
    """Input schema for searching poems containing a specific phrase or line.

    Args:
        phrase: Line or text fragment to search for in poems
    """

    phrase: str = Field(..., description="Line or phrase to search for in poems")


def search_by_line_fragment(phrase: str) -> List[dict]:
    """Searches for poems containing a specific line or text fragment.

    Args:
        phrase: Line or text fragment to search for in poems

    Returns:
        List[dict]: Up to 3 poems containing the specified phrase

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    url = f"{BASE_URL}/lines/{phrase}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()[:3]


search_by_line_tool = StructuredTool.from_function(
    func=search_by_line_fragment,
    name="search_poems_by_line",
    description="Search for poems that contain a specific line or phrase",
    args_schema=LineSearchInput,
)


### --- Toolkit Wrapper --- ###
def get_poetry_toolkit() -> List[StructuredTool]:
    """Gets a list of tools for interacting with the PoetryDB API.

    Returns:
        List[StructuredTool]: A list of tools for searching and retrieving poetry
    """
    return [
        search_poems_by_author_tool,
        search_poem_by_title_tool,
        get_random_poems_tool,
        search_by_line_tool,
    ]

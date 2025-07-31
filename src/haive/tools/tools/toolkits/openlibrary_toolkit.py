"""OpenLibrary toolkit for searching books, authors, and retrieving cover images.

This module provides a set of tools for interacting with the OpenLibrary API
(https://openlibrary.org). These tools allow users to search for books by title
or key, search for authors by name, and retrieve cover images.

The module includes three main tools:
1. search_books_tool: Search for books by title, keywords, or other query terms
2. search_authors_tool: Search for authors by name
3. get_cover_image_tool: Get the URL for a book or author cover image

Typical usage:
    from haive.tools.toolkits.openlibrary_toolkit import open_library_tools

    # Use in an agent
    agent = Agent(tools=open_library_tools)
    agent.run("Find books by J.K. Rowling")

"""

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
import requests


BASE_URL = "https://openlibrary.org"


class BookSearchInput(BaseModel):
    """Input schema for the book search tool.

    Attributes:
        query: The book title, keywords, or search query to use.
        page: Page number of results to retrieve, starting from 1.

    """

    query: str = Field(..., description="The book title, keywords, or search query")
    page: int = Field(default=1, description="Page number of results")


def search_books(query: str, page: int = 1) -> dict:
    """Search for books on OpenLibrary by title, key, or subject.

    This function queries the OpenLibrary search API and returns a list of
    matching books with their details.

    Args:
        query: The book title, keywords, or search query.
        page: The page number of results to retrieve (default: 1).

    Returns:
        A dictionary containing the number of results and a list of books with
        their title, author, first publish year, and OpenLibrary ID.

    Raises:
        requests.HTTPError: If the API request fails.

    """
    url = f"{BASE_URL}/search.json"
    params = {"q": query, "page": page}
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()
    return {
        "num_results": data.get("numFound"),
        "books": [
            {
                "title": doc.get("title"),
                "author": ", ".join(doc.get("author_name", [])),
                "first_publish_year": doc.get("first_publish_year"),
                "olid": doc.get("key").split("/")[-1] if doc.get("key") else None,
            }
            for doc in data.get("docs", [])[:5]
        ],
    }


search_books_tool = StructuredTool.from_function(
    func=search_books,
    name="search_books_openlibrary",
    description="Search for books by title, key, or subject using OpenLibrary",
    args_schema=BookSearchInput,
)


class AuthorSearchInput(BaseModel):
    """Input schema for the author search tool.

    Attributes:
        name: Name of the author to search for.

    """

    name: str = Field(..., description="Name of the author to search for")


def search_authors(name: str) -> dict:
    """Search for authors on OpenLibrary by name.

    This function queries the OpenLibrary author search API and returns a list of
    matching authors with their details.

    Args:
        name: The name of the author to search for.

    Returns:
        A dictionary containing a list of authors with their name, birth date,
        top work, work count, and OpenLibrary ID.

    Raises:
        requests.HTTPError: If the API request fails.

    """
    url = f"{BASE_URL}/search/authors.json"
    params = {"q": name}
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()
    return {
        "authors": [
            {
                "name": doc.get("name"),
                "birth_date": doc.get("birth_date"),
                "top_work": doc.get("top_work"),
                "work_count": doc.get("work_count"),
                "olid": doc.get("key").split("/")[-1] if doc.get("key") else None,
            }
            for doc in data.get("docs", [])[:5]
        ]
    }


search_authors_tool = StructuredTool.from_function(
    func=search_authors,
    name="search_authors_openlibrary",
    description="Search for authors by name using OpenLibrary",
    args_schema=AuthorSearchInput,
)


class CoverInput(BaseModel):
    """Input schema for the cover image retrieval tool.

    Attributes:
        olid: The OpenLibrary ID for a book or author.
        is_author: Boolean flag indicating if the OLID is for an author.

    """

    olid: str = Field(..., description="The OpenLibrary ID for a book or author")
    is_author: bool = Field(
        default=False, description="Set to true if the OLID is for an author"
    )


def get_cover_image_url(olid: str, is_author: bool = False) -> str:
    """Get the cover image URL for a book or author.

    This function constructs the URL for an OpenLibrary cover image based on
    the provided OpenLibrary ID.

    Args:
        olid: The OpenLibrary ID for a book or author.
        is_author: Boolean indicating if the OLID is for an author (default: False).

    Returns:
        A URL string for the medium-sized cover image.

    """
    prefix = "a" if is_author else "b"
    return f"https://covers.openlibrary.org/{prefix}/olid/{olid}-M.jpg"


get_cover_image_tool = StructuredTool.from_function(
    func=get_cover_image_url,
    name="get_openlibrary_cover_image",
    description="Get the cover image URL from an OpenLibrary ID (for book or author)",
    args_schema=CoverInput,
)

# Export all tools as a list for easy access
open_library_tools = [search_books_tool, search_authors_tool, get_cover_image_tool]

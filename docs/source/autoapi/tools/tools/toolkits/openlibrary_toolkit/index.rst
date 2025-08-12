
:py:mod:`tools.tools.toolkits.openlibrary_toolkit`
==================================================

.. py:module:: tools.tools.toolkits.openlibrary_toolkit

OpenLibrary toolkit for searching books, authors, and retrieving cover images.

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


.. autolink-examples:: tools.tools.toolkits.openlibrary_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.openlibrary_toolkit.AuthorSearchInput
   tools.tools.toolkits.openlibrary_toolkit.BookSearchInput
   tools.tools.toolkits.openlibrary_toolkit.CoverInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AuthorSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_AuthorSearchInput {
        node [shape=record];
        "AuthorSearchInput" [label="AuthorSearchInput"];
        "pydantic.BaseModel" -> "AuthorSearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.openlibrary_toolkit.AuthorSearchInput
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

   Inheritance diagram for BookSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_BookSearchInput {
        node [shape=record];
        "BookSearchInput" [label="BookSearchInput"];
        "pydantic.BaseModel" -> "BookSearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.openlibrary_toolkit.BookSearchInput
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

   Inheritance diagram for CoverInput:

   .. graphviz::
      :align: center

      digraph inheritance_CoverInput {
        node [shape=record];
        "CoverInput" [label="CoverInput"];
        "pydantic.BaseModel" -> "CoverInput";
      }

.. autopydantic_model:: tools.tools.toolkits.openlibrary_toolkit.CoverInput
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

   tools.tools.toolkits.openlibrary_toolkit.get_cover_image_url
   tools.tools.toolkits.openlibrary_toolkit.search_authors
   tools.tools.toolkits.openlibrary_toolkit.search_books

.. py:function:: get_cover_image_url(olid: str, is_author: bool = False) -> str

   Get the cover image URL for a book or author.

   This function constructs the URL for an OpenLibrary cover image based on
   the provided OpenLibrary ID.

   :param olid: The OpenLibrary ID for a book or author.
   :param is_author: Boolean indicating if the OLID is for an author (default: False).

   :returns: A URL string for the medium-sized cover image.


   .. autolink-examples:: get_cover_image_url
      :collapse:

.. py:function:: search_authors(name: str) -> dict

   Search for authors on OpenLibrary by name.

   This function queries the OpenLibrary author search API and returns a list of
   matching authors with their details.

   :param name: The name of the author to search for.

   :returns: A dictionary containing a list of authors with their name, birth date,
             top work, work count, and OpenLibrary ID.

   :raises requests.HTTPError: If the API request fails.


   .. autolink-examples:: search_authors
      :collapse:

.. py:function:: search_books(query: str, page: int = 1) -> dict

   Search for books on OpenLibrary by title, key, or subject.

   This function queries the OpenLibrary search API and returns a list of
   matching books with their details.

   :param query: The book title, keywords, or search query.
   :param page: The page number of results to retrieve (default: 1).

   :returns: A dictionary containing the number of results and a list of books with
             their title, author, first publish year, and OpenLibrary ID.

   :raises requests.HTTPError: If the API request fails.


   .. autolink-examples:: search_books
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.openlibrary_toolkit
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.toolkits.poetry_db_toolkit`
================================================

.. py:module:: tools.tools.toolkits.poetry_db_toolkit

PoetryDB Toolkit for accessing poetry data from the PoetryDB API.

This toolkit provides tools for interacting with the PoetryDB API,
allowing agents to search for poems by author, title, or content,
and retrieve random poems. It simplifies the process of finding and
analyzing poetry from a variety of sources.

.. rubric:: Example

```python
tools = get_poetry_toolkit()
```

.. attribute:: BASE_URL

   The base URL for the PoetryDB API


.. autolink-examples:: tools.tools.toolkits.poetry_db_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.poetry_db_toolkit.AuthorSearchInput
   tools.tools.toolkits.poetry_db_toolkit.LineSearchInput
   tools.tools.toolkits.poetry_db_toolkit.RandomPoemInput
   tools.tools.toolkits.poetry_db_toolkit.TitleSearchInput


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

.. autopydantic_model:: tools.tools.toolkits.poetry_db_toolkit.AuthorSearchInput
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

   Inheritance diagram for LineSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_LineSearchInput {
        node [shape=record];
        "LineSearchInput" [label="LineSearchInput"];
        "pydantic.BaseModel" -> "LineSearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.poetry_db_toolkit.LineSearchInput
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

   Inheritance diagram for RandomPoemInput:

   .. graphviz::
      :align: center

      digraph inheritance_RandomPoemInput {
        node [shape=record];
        "RandomPoemInput" [label="RandomPoemInput"];
        "pydantic.BaseModel" -> "RandomPoemInput";
      }

.. autopydantic_model:: tools.tools.toolkits.poetry_db_toolkit.RandomPoemInput
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

   Inheritance diagram for TitleSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_TitleSearchInput {
        node [shape=record];
        "TitleSearchInput" [label="TitleSearchInput"];
        "pydantic.BaseModel" -> "TitleSearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.poetry_db_toolkit.TitleSearchInput
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

   tools.tools.toolkits.poetry_db_toolkit.get_poetry_toolkit
   tools.tools.toolkits.poetry_db_toolkit.get_random_poems
   tools.tools.toolkits.poetry_db_toolkit.search_by_line_fragment
   tools.tools.toolkits.poetry_db_toolkit.search_poem_by_title
   tools.tools.toolkits.poetry_db_toolkit.search_poems_by_author

.. py:function:: get_poetry_toolkit() -> list[langchain_core.tools.StructuredTool]

   Gets a list of tools for interacting with the PoetryDB API.

   :returns: A list of tools for searching and retrieving poetry
   :rtype: List[StructuredTool]


   .. autolink-examples:: get_poetry_toolkit
      :collapse:

.. py:function:: get_random_poems(count: int) -> list[dict]

   Fetches a specified number of random poems.

   :param count: Number of random poems to retrieve

   :returns: The requested number of random poems
   :rtype: List[dict]

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: get_random_poems
      :collapse:

.. py:function:: search_by_line_fragment(phrase: str) -> list[dict]

   Searches for poems containing a specific line or text fragment.

   :param phrase: Line or text fragment to search for in poems

   :returns: Up to 3 poems containing the specified phrase
   :rtype: List[dict]

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: search_by_line_fragment
      :collapse:

.. py:function:: search_poem_by_title(title: str) -> dict

   Searches for a poem using its title.

   :param title: Title of the poem to search for

   :returns: The first poem matching the given title
   :rtype: dict

   :raises HTTPError: If the request fails or returns an error status code
   :raises IndexError: If no poems match the given title


   .. autolink-examples:: search_poem_by_title
      :collapse:

.. py:function:: search_poems_by_author(author: str) -> list[dict]

   Searches for poems by a specific author or poet.

   :param author: Name of the poet to search for

   :returns: Up to 5 poems by the specified author
   :rtype: List[dict]

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: search_poems_by_author
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.poetry_db_toolkit
   :collapse:
   
.. autolink-skip:: next

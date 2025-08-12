
:py:mod:`tools.tools.toolkits.chuck_norris_jokes_toolkit`
=========================================================

.. py:module:: tools.tools.toolkits.chuck_norris_jokes_toolkit

Chuck Norris Jokes Toolkit Module.

This toolkit provides a collection of tools to interact with the Chuck Norris Jokes API,
allowing users to retrieve, search, and filter Chuck Norris jokes across different categories.
The API is provided by https://api.chucknorris.io/.

.. rubric:: Examples

>>> from haive.tools.toolkits.chuck_norris_jokes_toolkit import get_random_joke
>>> joke = get_random_joke()
>>> print(joke.value)
'Chuck Norris can divide by zero.'

>>> from haive.tools.toolkits.chuck_norris_jokes_toolkit import get_available_categories
>>> categories = get_available_categories()
>>> print(categories)
['animal', 'career', 'celebrity', ...]


.. autolink-examples:: tools.tools.toolkits.chuck_norris_jokes_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.chuck_norris_jokes_toolkit.Joke


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Joke:

   .. graphviz::
      :align: center

      digraph inheritance_Joke {
        node [shape=record];
        "Joke" [label="Joke"];
        "pydantic.BaseModel" -> "Joke";
      }

.. autopydantic_model:: tools.tools.toolkits.chuck_norris_jokes_toolkit.Joke
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

   tools.tools.toolkits.chuck_norris_jokes_toolkit.get_available_categories
   tools.tools.toolkits.chuck_norris_jokes_toolkit.get_random_joke
   tools.tools.toolkits.chuck_norris_jokes_toolkit.get_random_joke_by_category
   tools.tools.toolkits.chuck_norris_jokes_toolkit.search_jokes

.. py:function:: get_available_categories() -> list[str]

   Get a list of all available joke categories from the Chuck Norris API.

   :returns: A list of category names as strings.
   :rtype: List[str]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_available_categories
      :collapse:

.. py:function:: get_random_joke() -> Joke

   Fetch a random Chuck Norris joke from the API.

   :returns: A random Chuck Norris joke object.
   :rtype: Joke

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_random_joke
      :collapse:

.. py:function:: get_random_joke_by_category(category: str) -> Joke

   Fetch a random Chuck Norris joke from a specific category.

   :param category: The joke category to filter by (use get_available_categories
                    to see available options).
   :type category: str

   :returns: A random Chuck Norris joke from the specified category.
   :rtype: Joke

   :raises requests.RequestException: If the API request fails or the category is invalid.


   .. autolink-examples:: get_random_joke_by_category
      :collapse:

.. py:function:: search_jokes(query: str) -> list[Joke]

   Search for Chuck Norris jokes containing the specified query string.

   :param query: The search term to look for in jokes.
   :type query: str

   :returns: A list of joke objects matching the search query.
   :rtype: List[Joke]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: search_jokes
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.chuck_norris_jokes_toolkit
   :collapse:
   
.. autolink-skip:: next

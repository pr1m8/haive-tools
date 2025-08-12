
:py:mod:`tools.tools.geek_jokes_tool`
=====================================

.. py:module:: tools.tools.geek_jokes_tool

Geek Jokes API Tool Module.

This module provides a tool for fetching random geek and programming-related jokes from
the Geek Jokes API. These jokes are oriented toward programmers, computer enthusiasts,
and tech culture, making them suitable for adding humor to technical conversations.

.. rubric:: Examples

>>> from haive.tools.tools.geek_jokes_tool import get_geek_joke, GetGeekJokeInput
>>> joke = get_geek_joke(GetGeekJokeInput())
>>> print(joke)
'Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25'


.. autolink-examples:: tools.tools.geek_jokes_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.geek_jokes_tool.GetGeekJokeInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetGeekJokeInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetGeekJokeInput {
        node [shape=record];
        "GetGeekJokeInput" [label="GetGeekJokeInput"];
        "pydantic.BaseModel" -> "GetGeekJokeInput";
      }

.. autopydantic_model:: tools.tools.geek_jokes_tool.GetGeekJokeInput
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

   tools.tools.geek_jokes_tool.get_geek_joke

.. py:function:: get_geek_joke(_: GetGeekJokeInput) -> str

   Fetch a random geek or programming-related joke from the Geek Jokes API.

   This function makes a request to the Geek Jokes API and returns a random
   joke related to geek culture, programming, or technology.

   :param _: Empty input model (not used, but required for
             LangChain compatibility).
   :type _: GetGeekJokeInput

   :returns: A random geek or programming joke as a string.
   :rtype: str

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_geek_joke
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.geek_jokes_tool
   :collapse:
   
.. autolink-skip:: next

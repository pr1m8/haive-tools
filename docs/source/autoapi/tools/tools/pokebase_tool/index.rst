
:py:mod:`tools.tools.pokebase_tool`
===================================

.. py:module:: tools.tools.pokebase_tool

Pokebase Tool Module.

This module provides a tool for accessing Pokémon data from the PokéAPI using the pokebase
library. It allows querying various Pokémon resources including Pokémon species, moves,
abilities, items, berries, locations, and types.

The PokéAPI is a comprehensive RESTful API providing data about the Pokémon video game series,
and pokebase is a Python wrapper that simplifies interaction with this API.

.. rubric:: Examples

>>> from haive.tools.tools.pokebase_tool import query_pokebase_resource, PokeBaseQueryInput
>>> input_data = PokeBaseQueryInput(resource_type="pokemon", identifier="pikachu")
>>> result = query_pokebase_resource(input_data)
>>> print(result["name"])  # Outputs: pikachu


.. autolink-examples:: tools.tools.pokebase_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.pokebase_tool.PokeBaseQueryInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokeBaseQueryInput:

   .. graphviz::
      :align: center

      digraph inheritance_PokeBaseQueryInput {
        node [shape=record];
        "PokeBaseQueryInput" [label="PokeBaseQueryInput"];
        "pydantic.BaseModel" -> "PokeBaseQueryInput";
      }

.. autopydantic_model:: tools.tools.pokebase_tool.PokeBaseQueryInput
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

   tools.tools.pokebase_tool.query_pokebase_resource

.. py:function:: query_pokebase_resource(query_input: PokeBaseQueryInput) -> dict

   Query a PokéAPI resource using the pokebase library.

   This function retrieves data for a specified Pokémon-related resource
   from the PokéAPI using the pokebase library and returns the data as
   a dictionary.

   :param query_input: The input parameters specifying the resource
                       type and identifier to query.
   :type query_input: PokeBaseQueryInput

   :returns:

             A dictionary containing the requested resource data with attributes
                 such as name, ID, and resource-specific properties. Returns an error
                 dictionary if the query fails.
   :rtype: dict

   :raises AttributeError: If an invalid resource_type is provided.
   :raises ValueError: If the resource cannot be found with the given identifier.


   .. autolink-examples:: query_pokebase_resource
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.pokebase_tool
   :collapse:
   
.. autolink-skip:: next

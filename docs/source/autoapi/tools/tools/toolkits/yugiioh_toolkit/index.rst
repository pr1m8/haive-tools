
:py:mod:`tools.tools.toolkits.yugiioh_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.yugiioh_toolkit

Yu-Gi-Oh! API Toolkit Module.

This toolkit provides a collection of tools to interact with the Yu-Gi-Oh! API,
allowing users to search for cards, get card details, retrieve information about
card sets, archetypes, and more. The API is provided by https://db.ygoprodeck.com/api/v7/.

.. rubric:: Examples

>>> from haive.tools.toolkits.yugiioh_toolkit import yugioh_api_toolkit
>>> # Get information about a specific card by name
>>> card_info = yugioh_api_toolkit[0].invoke({"name": "Dark Magician"})
>>> print(card_info['data'][0]['name'])
'Dark Magician'

>>> # Get all card sets
>>> card_sets = yugioh_api_toolkit[1].invoke()
>>> print(card_sets[0]['set_name'])
'Legend of Blue Eyes White Dragon'

>>> # Get a random card
>>> random_card = yugioh_api_toolkit[3].invoke()
>>> print(random_card['name'])
'Blue-Eyes White Dragon'


.. autolink-examples:: tools.tools.toolkits.yugiioh_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.yugiioh_toolkit.GetCardInfoInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetCardInfoInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetCardInfoInput {
        node [shape=record];
        "GetCardInfoInput" [label="GetCardInfoInput"];
        "pydantic.v1.BaseModel" -> "GetCardInfoInput";
      }

.. autopydantic_model:: tools.tools.toolkits.yugiioh_toolkit.GetCardInfoInput
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

   tools.tools.toolkits.yugiioh_toolkit.get_archetypes
   tools.tools.toolkits.yugiioh_toolkit.get_card_info
   tools.tools.toolkits.yugiioh_toolkit.get_card_sets
   tools.tools.toolkits.yugiioh_toolkit.get_database_version
   tools.tools.toolkits.yugiioh_toolkit.get_random_card

.. py:function:: get_archetypes() -> list[dict]

   Get a list of all Yu-Gi-Oh! archetypes.

   :returns: A list of archetype objects.
   :rtype: List[dict]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_archetypes
      :collapse:

.. py:function:: get_card_info(input_data: GetCardInfoInput) -> dict

   Retrieve Yu-Gi-Oh! card information based on the provided filters.

   :param input_data: Input parameters for filtering card results.
   :type input_data: GetCardInfoInput

   :returns: A dictionary containing card information matching the specified filters.
   :rtype: dict

   :raises requests.RequestException: If the API request fails or the parameters are invalid.


   .. autolink-examples:: get_card_info
      :collapse:

.. py:function:: get_card_sets() -> list[dict]

   Get a list of all Yu-Gi-Oh! card sets.

   :returns: A list of card set objects containing set information.
   :rtype: List[dict]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_card_sets
      :collapse:

.. py:function:: get_database_version() -> dict

   Check the current version of the Yu-Gi-Oh! database.

   :returns: Information about the current database version.
   :rtype: dict

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_database_version
      :collapse:

.. py:function:: get_random_card() -> dict

   Get information about a random Yu-Gi-Oh! card.

   :returns: Detailed information about a randomly selected card.
   :rtype: dict

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_random_card
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.yugiioh_toolkit
   :collapse:
   
.. autolink-skip:: next

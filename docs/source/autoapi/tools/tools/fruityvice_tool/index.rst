
:py:mod:`tools.tools.fruityvice_tool`
=====================================

.. py:module:: tools.tools.fruityvice_tool

Fruityvice API Tool Module.

This module provides a tool for accessing the Fruityvice API, which offers comprehensive
nutritional information and details about various fruits. It allows users to query
fruit data by name and retrieve detailed nutritional facts.

.. rubric:: Examples

>>> from haive.tools.tools.fruityvice_tool import get_fruit_info, FruitNameInput
>>> input = FruitNameInput(name="banana")
>>> result = get_fruit_info(input)
>>> print(result["name"])
'Banana'


.. autolink-examples:: tools.tools.fruityvice_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.fruityvice_tool.FruitNameInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FruitNameInput:

   .. graphviz::
      :align: center

      digraph inheritance_FruitNameInput {
        node [shape=record];
        "FruitNameInput" [label="FruitNameInput"];
        "pydantic.BaseModel" -> "FruitNameInput";
      }

.. autopydantic_model:: tools.tools.fruityvice_tool.FruitNameInput
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

   tools.tools.fruityvice_tool.get_fruit_info

.. py:function:: get_fruit_info(fruit_input: FruitNameInput) -> dict[str, Any]

   Fetch detailed information about a specific fruit from the Fruityvice API.

   The information returned typically includes nutritional data (calories, fat, sugar, etc.),
   family, genus, and other taxonomic details.

   :param fruit_input: Object containing the name of the fruit to look up.
   :type fruit_input: FruitNameInput

   :returns: A dictionary containing the fruit's details and nutritional information.
             If the fruit is not found, returns a dictionary with an error message.
   :rtype: Dict[str, Any]

   :raises requests.HTTPError: If the API request fails for reasons other than a 404.


   .. autolink-examples:: get_fruit_info
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.fruityvice_tool
   :collapse:
   
.. autolink-skip:: next

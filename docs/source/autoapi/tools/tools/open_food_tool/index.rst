
:py:mod:`tools.tools.open_food_tool`
====================================

.. py:module:: tools.tools.open_food_tool

Open Food Facts Tool Module.

This module provides a tool for retrieving product information from the
Open Food Facts database using barcodes. It creates a structured tool that
can be integrated into LangChain-based agents to get nutrition facts, ingredients,
and other product data.

The module uses the Open Food Facts API (https://world.openfoodfacts.org/api/v2/)
to look up product information by barcode.

.. rubric:: Example

>>> from haive.tools.tools.open_food_tool import open_food_facts_tool
>>> result = open_food_facts_tool.invoke({"barcode": "3017620422003"})
>>> print(f"Product: {result.get('product_name')}")

.. note::

   No API key is required for usage, but rate limits may apply.
   See https://world.openfoodfacts.org/api/v2/ for API details.


.. autolink-examples:: tools.tools.open_food_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.open_food_tool.GetProductInfoInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetProductInfoInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetProductInfoInput {
        node [shape=record];
        "GetProductInfoInput" [label="GetProductInfoInput"];
        "pydantic.BaseModel" -> "GetProductInfoInput";
      }

.. autopydantic_model:: tools.tools.open_food_tool.GetProductInfoInput
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

   tools.tools.open_food_tool.get_product_info

.. py:function:: get_product_info(barcode: str) -> dict

   Retrieve product information from Open Food Facts by barcode.

   :param barcode: The barcode of the product to look up (EAN, UPC, etc.)

   :returns: Product information including name, ingredients, nutrition facts, etc.
   :rtype: dict

   :raises ValueError: If the API request fails or no product is found


   .. autolink-examples:: get_product_info
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.open_food_tool
   :collapse:
   
.. autolink-skip:: next

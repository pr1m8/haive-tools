
:py:mod:`tools.tools.toolkits.lcbo_toolkit`
===========================================

.. py:module:: tools.tools.toolkits.lcbo_toolkit

LCBO API Toolkit for accessing data from the Liquor Control Board of Ontario.

This toolkit provides tools to interact with the LCBO API, allowing agents to
search for products and retrieve detailed product information from the Liquor
Control Board of Ontario's product database.

.. rubric:: Example

```python
toolkit = LCBOApiToolkit()
tools = toolkit.get_tools()
```

.. attribute:: None

   


.. autolink-examples:: tools.tools.toolkits.lcbo_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.lcbo_toolkit.GetLCBOProductInput
   tools.tools.toolkits.lcbo_toolkit.LCBOApiToolkit
   tools.tools.toolkits.lcbo_toolkit.SearchLCBOProductsInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetLCBOProductInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetLCBOProductInput {
        node [shape=record];
        "GetLCBOProductInput" [label="GetLCBOProductInput"];
        "pydantic.BaseModel" -> "GetLCBOProductInput";
      }

.. autopydantic_model:: tools.tools.toolkits.lcbo_toolkit.GetLCBOProductInput
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

   Inheritance diagram for LCBOApiToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_LCBOApiToolkit {
        node [shape=record];
        "LCBOApiToolkit" [label="LCBOApiToolkit"];
        "langchain_core.tools.BaseToolkit" -> "LCBOApiToolkit";
      }

.. autoclass:: tools.tools.toolkits.lcbo_toolkit.LCBOApiToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SearchLCBOProductsInput:

   .. graphviz::
      :align: center

      digraph inheritance_SearchLCBOProductsInput {
        node [shape=record];
        "SearchLCBOProductsInput" [label="SearchLCBOProductsInput"];
        "pydantic.BaseModel" -> "SearchLCBOProductsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.lcbo_toolkit.SearchLCBOProductsInput
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

   tools.tools.toolkits.lcbo_toolkit.get_lcbo_product
   tools.tools.toolkits.lcbo_toolkit.search_lcbo_products

.. py:function:: get_lcbo_product(product_id: int) -> dict

   Fetches detailed information for a specific LCBO product.

   :param product_id: The unique LCBO product identifier

   :returns: JSON response containing detailed product information
   :rtype: dict

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: get_lcbo_product
      :collapse:

.. py:function:: search_lcbo_products(query: str, page: int = 1, per_page: int = 10) -> dict

   Searches for LCBO products based on a query string.

   :param query: The search terms to find matching products
   :param page: Page number for paginated results (default: 1)
   :param per_page: Number of results to return per page (default: 10)

   :returns: JSON response containing the search results
   :rtype: dict

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: search_lcbo_products
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.lcbo_toolkit
   :collapse:
   
.. autolink-skip:: next

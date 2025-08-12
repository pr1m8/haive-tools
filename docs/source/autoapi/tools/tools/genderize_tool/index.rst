
:py:mod:`tools.tools.genderize_tool`
====================================

.. py:module:: tools.tools.genderize_tool

Genderize Tool Module.

This module provides a tool for predicting gender from first names using the
Genderize.io API. It creates a structured tool that can be integrated into
LangChain-based agents to predict gender based on provided names, with optional
country context.

The module includes a Pydantic model for the API response and a function to
interact with the Genderize.io API directly.

.. rubric:: Example

>>> from haive.tools.tools.genderize_tool import genderize_tool
>>> result = genderize_tool.invoke({"name": "Alex", "country_id": "US"})
>>> print(f"Predicted gender: {result.gender} with {result.probability} probability")

.. note::

   No API key is required for basic usage, but rate limits apply.
   See https://genderize.io/ for more information.


.. autolink-examples:: tools.tools.genderize_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.genderize_tool.GenderizeResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GenderizeResponse:

   .. graphviz::
      :align: center

      digraph inheritance_GenderizeResponse {
        node [shape=record];
        "GenderizeResponse" [label="GenderizeResponse"];
        "pydantic.BaseModel" -> "GenderizeResponse";
      }

.. autopydantic_model:: tools.tools.genderize_tool.GenderizeResponse
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

   tools.tools.genderize_tool.predict_gender

.. py:function:: predict_gender(name: str, country_id: str | None = None) -> GenderizeResponse

   Predict gender from a first name using the Genderize.io API.

   :param name: The first name to predict gender for
   :param country_id: Optional two-letter country code (ISO 3166-1 alpha-2)
                      to scope the search to a specific country

   :returns:

             An object containing the predicted gender, probability,
                 and other metadata from the API
   :rtype: GenderizeResponse

   :raises requests.exceptions.HTTPError: If the API request fails


   .. autolink-examples:: predict_gender
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.genderize_tool
   :collapse:
   
.. autolink-skip:: next

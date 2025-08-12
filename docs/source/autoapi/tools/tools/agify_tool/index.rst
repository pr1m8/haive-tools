
:py:mod:`tools.tools.agify_tool`
================================

.. py:module:: tools.tools.agify_tool

Agify Name Age Estimation Tool Module.

This module provides a tool for estimating the average age of a person based on their first name
using the Agify.io API. The tool can optionally filter age estimations by country.

Agify.io analyzes name data across different countries to predict the likely age of a person
based solely on their first name.

.. rubric:: Examples

>>> from haive.tools.tools.agify_tool import estimate_age
>>> result = estimate_age("John")
>>> print(f"The estimated age for John is {result.age} years old")
The estimated age for John is 61 years old

>>> # With country filter
>>> result = estimate_age("John", country_id="US")
>>> print(f"The estimated age for John in the US is {result.age} years old")
The estimated age for John in the US is 69 years old


.. autolink-examples:: tools.tools.agify_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.agify_tool.AgifyResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgifyResponse:

   .. graphviz::
      :align: center

      digraph inheritance_AgifyResponse {
        node [shape=record];
        "AgifyResponse" [label="AgifyResponse"];
        "pydantic.BaseModel" -> "AgifyResponse";
      }

.. autopydantic_model:: tools.tools.agify_tool.AgifyResponse
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

   tools.tools.agify_tool.estimate_age

.. py:function:: estimate_age(name: str, country_id: str | None = None) -> AgifyResponse

   Estimate the average age of a person based on their first name.

   This function queries the Agify.io API to get an age estimation based on the provided
   first name. The estimation can be optionally filtered by country.

   :param name: The first name to estimate age for.
   :type name: str
   :param country_id: Two-letter country code (ISO 3166-1 alpha-2)
                      to filter results by country. Defaults to None (worldwide data).
   :type country_id: Optional[str], optional

   :returns: Object containing the age estimation and related metadata.
   :rtype: AgifyResponse

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: estimate_age
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.agify_tool
   :collapse:
   
.. autolink-skip:: next

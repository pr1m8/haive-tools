
:py:mod:`tools.tools.toolkits.citydsk_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.citydsk_toolkit

CitySDK Toolkit for accessing city-related data from various sources.

This toolkit provides tools for interacting with the CitySDK APIs,
including the Linked Data API for SPARQL queries and the Tourism API
for points of interest information. These tools help agents find and
process structured city information.

.. rubric:: Example

```python
toolkit = CitySDKToolkit()
tools = toolkit.get_tools()
```

.. attribute:: None

   


.. autolink-examples:: tools.tools.toolkits.citydsk_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.citydsk_toolkit.CitySDKLinkedDataQueryInput
   tools.tools.toolkits.citydsk_toolkit.CitySDKToolkit
   tools.tools.toolkits.citydsk_toolkit.CitySDKTourismPOIInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CitySDKLinkedDataQueryInput:

   .. graphviz::
      :align: center

      digraph inheritance_CitySDKLinkedDataQueryInput {
        node [shape=record];
        "CitySDKLinkedDataQueryInput" [label="CitySDKLinkedDataQueryInput"];
        "pydantic.BaseModel" -> "CitySDKLinkedDataQueryInput";
      }

.. autopydantic_model:: tools.tools.toolkits.citydsk_toolkit.CitySDKLinkedDataQueryInput
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

   Inheritance diagram for CitySDKToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_CitySDKToolkit {
        node [shape=record];
        "CitySDKToolkit" [label="CitySDKToolkit"];
        "langchain_core.tools.base.BaseToolkit" -> "CitySDKToolkit";
      }

.. autoclass:: tools.tools.toolkits.citydsk_toolkit.CitySDKToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CitySDKTourismPOIInput:

   .. graphviz::
      :align: center

      digraph inheritance_CitySDKTourismPOIInput {
        node [shape=record];
        "CitySDKTourismPOIInput" [label="CitySDKTourismPOIInput"];
        "pydantic.BaseModel" -> "CitySDKTourismPOIInput";
      }

.. autopydantic_model:: tools.tools.toolkits.citydsk_toolkit.CitySDKTourismPOIInput
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

   tools.tools.toolkits.citydsk_toolkit.get_tourism_pois
   tools.tools.toolkits.citydsk_toolkit.run_citysdk_linkeddata_query

.. py:function:: get_tourism_pois(bbox: str | None = None, city: str | None = None) -> dict

   Fetches Points of Interest data from the CitySDK Tourism API.

   :param bbox: Optional bounding box to filter POIs geographically
   :param city: Optional city name to filter POIs

   :returns: JSON response containing the POI data
   :rtype: dict

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: get_tourism_pois
      :collapse:

.. py:function:: run_citysdk_linkeddata_query(query: str) -> dict

   Executes a SPARQL query against the CitySDK Linked Data endpoint.

   :param query: A valid SPARQL query string

   :returns: JSON response containing the query results
   :rtype: dict

   :raises HTTPError: If the request fails or returns an error status code


   .. autolink-examples:: run_citysdk_linkeddata_query
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.citydsk_toolkit
   :collapse:
   
.. autolink-skip:: next

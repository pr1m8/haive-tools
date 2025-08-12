
:py:mod:`tools.tools.google.google_places`
==========================================

.. py:module:: tools.tools.google.google_places

Google Places Tool Module.

This module provides a tool for searching and retrieving information about places using Google Places API.
It leverages LangChain's GooglePlacesTool to search for locations, businesses, points of interest,
and retrieve detailed information about them.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key
   - GOOGLE_CSE_ID: Your Custom Search Engine ID (for some functionality)

.. rubric:: Examples

>>> from haive.tools.tools.google.google_places import google_places_tool
>>> result = google_places_tool[0].invoke("coffee shops in Seattle")
>>> print(result)
['Starbucks at Pike Place Market, Seattle...']


.. autolink-examples:: tools.tools.google.google_places
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_places.GooglePlacesResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GooglePlacesResult:

   .. graphviz::
      :align: center

      digraph inheritance_GooglePlacesResult {
        node [shape=record];
        "GooglePlacesResult" [label="GooglePlacesResult"];
        "pydantic.BaseModel" -> "GooglePlacesResult";
      }

.. autopydantic_model:: tools.tools.google.google_places.GooglePlacesResult
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

   tools.tools.google.google_places.initialize_google_places

.. py:function:: initialize_google_places()

   Initialize the Google Places API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Places API client.

   :returns: A list containing the Google Places search tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_places
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_places
   :collapse:
   
.. autolink-skip:: next

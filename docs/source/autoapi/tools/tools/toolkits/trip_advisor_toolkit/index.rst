
:py:mod:`tools.tools.toolkits.trip_advisor_toolkit`
===================================================

.. py:module:: tools.tools.toolkits.trip_advisor_toolkit

TripAdvisor Toolkit.

This module provides tools to interact with the TripAdvisor Content API. It allows
querying for location details, photos, reviews, and searching for locations by various
criteria.

Requires a TripAdvisor API key set as TRIPADVISOR_API_KEY in environment variables or
.env file.


.. autolink-examples:: tools.tools.toolkits.trip_advisor_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.trip_advisor_toolkit.LocationDetailsInput
   tools.tools.toolkits.trip_advisor_toolkit.LocationPhotosInput
   tools.tools.toolkits.trip_advisor_toolkit.LocationReviewsInput
   tools.tools.toolkits.trip_advisor_toolkit.LocationSearchInput
   tools.tools.toolkits.trip_advisor_toolkit.NearbySearchInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LocationDetailsInput:

   .. graphviz::
      :align: center

      digraph inheritance_LocationDetailsInput {
        node [shape=record];
        "LocationDetailsInput" [label="LocationDetailsInput"];
        "pydantic.BaseModel" -> "LocationDetailsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.trip_advisor_toolkit.LocationDetailsInput
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

   Inheritance diagram for LocationPhotosInput:

   .. graphviz::
      :align: center

      digraph inheritance_LocationPhotosInput {
        node [shape=record];
        "LocationPhotosInput" [label="LocationPhotosInput"];
        "pydantic.BaseModel" -> "LocationPhotosInput";
      }

.. autopydantic_model:: tools.tools.toolkits.trip_advisor_toolkit.LocationPhotosInput
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

   Inheritance diagram for LocationReviewsInput:

   .. graphviz::
      :align: center

      digraph inheritance_LocationReviewsInput {
        node [shape=record];
        "LocationReviewsInput" [label="LocationReviewsInput"];
        "pydantic.BaseModel" -> "LocationReviewsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.trip_advisor_toolkit.LocationReviewsInput
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

   Inheritance diagram for LocationSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_LocationSearchInput {
        node [shape=record];
        "LocationSearchInput" [label="LocationSearchInput"];
        "pydantic.BaseModel" -> "LocationSearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.trip_advisor_toolkit.LocationSearchInput
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

   Inheritance diagram for NearbySearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_NearbySearchInput {
        node [shape=record];
        "NearbySearchInput" [label="NearbySearchInput"];
        "pydantic.BaseModel" -> "NearbySearchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.trip_advisor_toolkit.NearbySearchInput
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

   tools.tools.toolkits.trip_advisor_toolkit.get_location_details
   tools.tools.toolkits.trip_advisor_toolkit.get_location_photos
   tools.tools.toolkits.trip_advisor_toolkit.get_location_reviews
   tools.tools.toolkits.trip_advisor_toolkit.nearby_search
   tools.tools.toolkits.trip_advisor_toolkit.search_locations
   tools.tools.toolkits.trip_advisor_toolkit.tripadvisor_get

.. py:function:: get_location_details(location_id: int, language: str = 'en', currency: str = 'USD')

   Get details about a location by ID.

   Retrieves comprehensive information about a specific TripAdvisor location
   such as a hotel, restaurant, or attraction.

   :param location_id: The unique identifier for a TripAdvisor location.
   :param language: The language code for the response content (ISO 639-1).
   :param currency: The currency code for price values (ISO 4217).

   :returns: Location details including name, address, rating, etc.
   :rtype: dict


   .. autolink-examples:: get_location_details
      :collapse:

.. py:function:: get_location_photos(location_id: int, language: str = 'en', limit: int = 5, offset: int = 0, source: str | None = None)

   Get high-quality photos for a location.

   Retrieves photos from TripAdvisor for a specific location.

   :param location_id: The unique identifier for a TripAdvisor location.
   :param language: The language code for the response content (ISO 639-1).
   :param limit: Maximum number of photos to return (1-100).
   :param offset: Number of photos to skip for pagination.
   :param source: Filter photos by source (tripadvisor, management).

   :returns: Collection of photo objects with URLs and metadata.
   :rtype: dict


   .. autolink-examples:: get_location_photos
      :collapse:

.. py:function:: get_location_reviews(location_id: int, language: str = 'en', limit: int = 5, offset: int = 0)

   Get recent reviews for a location.

   Retrieves user reviews for a specific TripAdvisor location.

   :param location_id: The unique identifier for a TripAdvisor location.
   :param language: The language code for the response content (ISO 639-1).
   :param limit: Maximum number of reviews to return (1-50).
   :param offset: Number of reviews to skip for pagination.

   :returns: Collection of review objects with ratings, text, and metadata.
   :rtype: dict


   .. autolink-examples:: get_location_reviews
      :collapse:

.. py:function:: nearby_search(**kwargs)

   Search for nearby locations using a lat/long pair.

   Finds TripAdvisor locations near a specific geographical point.

   :param \*\*kwargs: Key arguments matching the NearbySearchInput model.
                      latLong: Latitude,longitude pair (e.g., '42.3455,-71.0983').
                      category: Filter by category (hotels, attractions, restaurants).
                      phone: Filter by phone number.
                      address: Filter by street address.
                      radius: Search radius from the specified coordinates.
                      radius_unit: Unit for radius (km, mi, m).
                      language: The language code for the response content (ISO 639-1).

   :returns: Search results with nearby location data.
   :rtype: dict


   .. autolink-examples:: nearby_search
      :collapse:

.. py:function:: search_locations(**kwargs)

   Search for TripAdvisor locations by name, address, lat/long, etc.

   Performs a general search for TripAdvisor locations using various filters.

   :param \*\*kwargs: Key arguments matching the LocationSearchInput model.
                      searchQuery: Text to search for (e.g., hotel name, restaurant name).
                      category: Filter by category (hotels, attractions, restaurants).
                      phone: Search by phone number.
                      address: Search by street address.
                      latLong: Latitude,longitude pair (e.g., '42.3455,-71.0983').
                      radius: Search radius from the specified coordinates.
                      radius_unit: Unit for radius (km, mi, m).
                      language: The language code for the response content (ISO 639-1).

   :returns: Search results with location data.
   :rtype: dict


   .. autolink-examples:: search_locations
      :collapse:

.. py:function:: tripadvisor_get(endpoint: str, params: dict)

   Make a GET request to the TripAdvisor API.

   :param endpoint: The API endpoint to call.
   :param params: Query parameters for the request.

   :returns: JSON response from the API.
   :rtype: dict

   :raises requests.HTTPError: If the request fails.


   .. autolink-examples:: tripadvisor_get
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.trip_advisor_toolkit
   :collapse:
   
.. autolink-skip:: next

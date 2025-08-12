
:py:mod:`tools.tools.openaq_tool`
=================================

.. py:module:: tools.tools.openaq_tool

OpenAQ API Tool Module.

This module provides tools for accessing air quality data from the OpenAQ API.
It currently supports retrieving detailed information about specific air quality
monitoring locations by their ID.

The OpenAQ platform aggregates air quality data from public data sources worldwide,
providing standardized access to air quality measurements including particulate matter,
ozone, nitrogen dioxide, sulfur dioxide, and carbon monoxide.

.. rubric:: Examples

>>> from haive.tools.tools.openaq_tool import get_openaq_location
>>> location_data = get_openaq_location(location_id=12345, api_key="your_api_key")
>>> print(location_data['name'])


.. autolink-examples:: tools.tools.openaq_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.openaq_tool.get_openaq_location

.. py:function:: get_openaq_location(location_id: int, api_key: str | None = None) -> dict

   Fetch detailed information about an air quality monitoring location from OpenAQ.

   This function retrieves comprehensive metadata about a specific air quality
   monitoring station identified by its location ID, including its coordinates,
   available parameters, and other attributes.

   :param location_id: The OpenAQ location ID to fetch data for.
   :type location_id: int
   :param api_key: The OpenAQ API key. If not provided, will look for
                   OPENAQ_API_KEY in environment variables.
   :type api_key: Optional[str]

   :returns:

             A dictionary containing detailed information about the location,
                 including geographical coordinates, available parameters, and metadata.
   :rtype: dict

   :raises ValueError: If no API key is provided or found in environment variables.
   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_openaq_location
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.openaq_tool
   :collapse:
   
.. autolink-skip:: next

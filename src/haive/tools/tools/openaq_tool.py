"""OpenAQ API Tool Module.

This module provides tools for accessing air quality data from the OpenAQ API.
It currently supports retrieving detailed information about specific air quality
monitoring locations by their ID.

The OpenAQ platform aggregates air quality data from public data sources worldwide,
providing standardized access to air quality measurements including particulate matter,
ozone, nitrogen dioxide, sulfur dioxide, and carbon monoxide.

Examples:
    >>> from haive.tools.tools.openaq_tool import get_openaq_location
    >>> location_data = get_openaq_location(location_id=12345, api_key="your_api_key")
    >>> print(location_data['name'])

"""

import os

from langchain_core.tools import StructuredTool
import requests


def get_openaq_location(location_id: int, api_key: str | None = None) -> dict:
    """Fetch detailed information about an air quality monitoring location from OpenAQ.

    This function retrieves comprehensive metadata about a specific air quality
    monitoring station identified by its location ID, including its coordinates,
    available parameters, and other attributes.

    Args:
        location_id (int): The OpenAQ location ID to fetch data for.
        api_key (Optional[str]): The OpenAQ API key. If not provided, will look for
            OPENAQ_API_KEY in environment variables.

    Returns:
        dict: A dictionary containing detailed information about the location,
            including geographical coordinates, available parameters, and metadata.

    Raises:
        ValueError: If no API key is provided or found in environment variables.
        requests.RequestException: If the API request fails.

    """
    api_key = api_key or os.getenv("OPENAQ_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OpenAQ API key. Set OPENAQ_API_KEY env variable or pass explicitly."
        )

    url = f"https://api.openaq.org/v3/locations/{location_id}"
    headers = {"X-API-Key": api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


openaq_location_tool = StructuredTool.from_function(
    name="get_openaq_location_by_id",
    description="Fetch air quality station details from OpenAQ by location ID. Requires an API key.",
    func=get_openaq_location,
)

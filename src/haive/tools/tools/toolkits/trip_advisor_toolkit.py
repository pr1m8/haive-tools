"""TripAdvisor Toolkit.

This module provides tools to interact with the TripAdvisor Content API.
It allows querying for location details, photos, reviews, and searching
for locations by various criteria.

Requires a TripAdvisor API key set as TRIPADVISOR_API_KEY in environment
variables or .env file.
"""

import os

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from pydantic import BaseModel, Field

load_dotenv()
TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY")
BASE_URL = "https://api.content.tripadvisor.com/api/v1"


def tripadvisor_get(endpoint: str, params: dict):
    """Make a GET request to the TripAdvisor API.

    Args:
        endpoint: The API endpoint to call.
        params: Query parameters for the request.

    Returns:
        dict: JSON response from the API.

    Raises:
        requests.HTTPError: If the request fails.
    """
    headers = {"accept": "application/json"}
    params["key"] = TRIPADVISOR_API_KEY
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()


class LocationDetailsInput(BaseModel):
    """Input parameters for retrieving location details."""

    location_id: int = Field(
        ..., description="The unique identifier for a TripAdvisor location."
    )
    language: str | None = Field(
        "en", description="The language code for the response content (ISO 639-1)."
    )
    currency: str | None = Field(
        "USD", description="The currency code for price values (ISO 4217)."
    )


@tool(args_schema=LocationDetailsInput)
def get_location_details(location_id: int, language: str = "en", currency: str = "USD"):
    """Get details about a location by ID.

    Retrieves comprehensive information about a specific TripAdvisor location
    such as a hotel, restaurant, or attraction.

    Args:
        location_id: The unique identifier for a TripAdvisor location.
        language: The language code for the response content (ISO 639-1).
        currency: The currency code for price values (ISO 4217).

    Returns:
        dict: Location details including name, address, rating, etc.
    """
    return tripadvisor_get(
        f"/location/{location_id}/details",
        {
            "language": language,
            "currency": currency,
        },
    )


class LocationPhotosInput(BaseModel):
    """Input parameters for retrieving location photos."""

    location_id: int = Field(
        ..., description="The unique identifier for a TripAdvisor location."
    )
    language: str | None = Field(
        "en", description="The language code for the response content (ISO 639-1)."
    )
    limit: int | None = Field(
        5, description="Maximum number of photos to return (1-100)."
    )
    offset: int | None = Field(
        0, description="Number of photos to skip for pagination."
    )
    source: str | None = Field(
        None, description="Filter photos by source (tripadvisor, management)."
    )


@tool(args_schema=LocationPhotosInput)
def get_location_photos(
    location_id: int,
    language: str = "en",
    limit: int = 5,
    offset: int = 0,
    source: str | None = None,
):
    """Get high-quality photos for a location.

    Retrieves photos from TripAdvisor for a specific location.

    Args:
        location_id: The unique identifier for a TripAdvisor location.
        language: The language code for the response content (ISO 639-1).
        limit: Maximum number of photos to return (1-100).
        offset: Number of photos to skip for pagination.
        source: Filter photos by source (tripadvisor, management).

    Returns:
        dict: Collection of photo objects with URLs and metadata.
    """
    params = {"language": language, "limit": limit, "offset": offset}
    if source:
        params["source"] = source
    return tripadvisor_get(f"/location/{location_id}/photos", params)


class LocationReviewsInput(BaseModel):
    """Input parameters for retrieving location reviews."""

    location_id: int = Field(
        ..., description="The unique identifier for a TripAdvisor location."
    )
    language: str | None = Field(
        "en", description="The language code for the response content (ISO 639-1)."
    )
    limit: int | None = Field(
        5, description="Maximum number of reviews to return (1-50)."
    )
    offset: int | None = Field(
        0, description="Number of reviews to skip for pagination."
    )


@tool(args_schema=LocationReviewsInput)
def get_location_reviews(
    location_id: int, language: str = "en", limit: int = 5, offset: int = 0
):
    """Get recent reviews for a location.

    Retrieves user reviews for a specific TripAdvisor location.

    Args:
        location_id: The unique identifier for a TripAdvisor location.
        language: The language code for the response content (ISO 639-1).
        limit: Maximum number of reviews to return (1-50).
        offset: Number of reviews to skip for pagination.

    Returns:
        dict: Collection of review objects with ratings, text, and metadata.
    """
    return tripadvisor_get(
        f"/location/{location_id}/reviews",
        {"language": language, "limit": limit, "offset": offset},
    )


class LocationSearchInput(BaseModel):
    """Input parameters for searching locations."""

    search_query: str = Field(
        ...,
        alias="searchQuery",
        description="Text to search for (e.g., hotel name, restaurant name).",
    )
    category: str | None = Field(
        None, description="Filter by category (hotels, attractions, restaurants)."
    )
    phone: str | None = Field(None, description="Search by phone number.")
    address: str | None = Field(None, description="Search by street address.")
    lat_long: str | None = Field(
        None,
        alias="latLong",
        description="Latitude,longitude pair (e.g., '42.3455,-71.0983').",
    )
    radius: int | None = Field(
        None, description="Search radius from the specified coordinates."
    )
    radius_unit: str | None = Field(None, description="Unit for radius (km, mi, m).")
    language: str | None = Field(
        "en", description="The language code for the response content (ISO 639-1)."
    )


@tool(args_schema=LocationSearchInput)
def search_locations(**kwargs):
    """Search for TripAdvisor locations by name, address, lat/long, etc.

    Performs a general search for TripAdvisor locations using various filters.

    Args:
        **kwargs: Key arguments matching the LocationSearchInput model.
            searchQuery: Text to search for (e.g., hotel name, restaurant name).
            category: Filter by category (hotels, attractions, restaurants).
            phone: Search by phone number.
            address: Search by street address.
            latLong: Latitude,longitude pair (e.g., '42.3455,-71.0983').
            radius: Search radius from the specified coordinates.
            radius_unit: Unit for radius (km, mi, m).
            language: The language code for the response content (ISO 639-1).

    Returns:
        dict: Search results with location data.
    """
    kwargs["key"] = TRIPADVISOR_API_KEY
    return tripadvisor_get("/location/search", kwargs)


class NearbySearchInput(BaseModel):
    """Input parameters for searching nearby locations."""

    lat_long: str = Field(
        ...,
        alias="latLong",
        description="Latitude,longitude pair (e.g., '42.3455,-71.0983').",
    )
    category: str | None = Field(
        None, description="Filter by category (hotels, attractions, restaurants)."
    )
    phone: str | None = Field(None, description="Filter by phone number.")
    address: str | None = Field(None, description="Filter by street address.")
    radius: int | None = Field(
        None, description="Search radius from the specified coordinates."
    )
    radius_unit: str | None = Field(None, description="Unit for radius (km, mi, m).")
    language: str | None = Field(
        "en", description="The language code for the response content (ISO 639-1)."
    )


@tool(args_schema=NearbySearchInput)
def nearby_search(**kwargs):
    """Search for nearby locations using a lat/long pair.

    Finds TripAdvisor locations near a specific geographical point.

    Args:
        **kwargs: Key arguments matching the NearbySearchInput model.
            latLong: Latitude,longitude pair (e.g., '42.3455,-71.0983').
            category: Filter by category (hotels, attractions, restaurants).
            phone: Filter by phone number.
            address: Filter by street address.
            radius: Search radius from the specified coordinates.
            radius_unit: Unit for radius (km, mi, m).
            language: The language code for the response content (ISO 639-1).

    Returns:
        dict: Search results with nearby location data.
    """
    kwargs["key"] = TRIPADVISOR_API_KEY
    return tripadvisor_get("/location/nearby_search", kwargs)

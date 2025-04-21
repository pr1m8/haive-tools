import os

import requests
from dotenv import load_dotenv
from langchain.tools import tool
from pydantic import BaseModel, Field

load_dotenv()
TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY")
BASE_URL = "https://api.content.tripadvisor.com/api/v1"

def tripadvisor_get(endpoint: str, params: dict):
    headers = {"accept": "application/json"}
    params["key"] = TRIPADVISOR_API_KEY
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

class LocationDetailsInput(BaseModel):
    location_id: int
    language: str | None = "en"
    currency: str | None = "USD"

@tool(args_schema=LocationDetailsInput)
def get_location_details(location_id: int, language: str = "en", currency: str = "USD"):
    """Get details about a location by ID (hotel, restaurant, attraction)."""
    return tripadvisor_get(f"/location/{location_id}/details", {
        "language": language,
        "currency": currency,
    })

class LocationPhotosInput(BaseModel):
    location_id: int
    language: str | None = "en"
    limit: int | None = 5
    offset: int | None = 0
    source: str | None = None

@tool(args_schema=LocationPhotosInput)
def get_location_photos(location_id: int, language: str = "en", limit: int = 5, offset: int = 0, source: str | None = None):
    """Get high-quality photos for a location."""
    params = {
        "language": language,
        "limit": limit,
        "offset": offset
    }
    if source:
        params["source"] = source
    return tripadvisor_get(f"/location/{location_id}/photos", params)

class LocationReviewsInput(BaseModel):
    location_id: int
    language: str | None = "en"
    limit: int | None = 5
    offset: int | None = 0

@tool(args_schema=LocationReviewsInput)
def get_location_reviews(location_id: int, language: str = "en", limit: int = 5, offset: int = 0):
    """Get recent reviews for a location."""
    return tripadvisor_get(f"/location/{location_id}/reviews", {
        "language": language,
        "limit": limit,
        "offset": offset
    })

class LocationSearchInput(BaseModel):
    search_query: str = Field(..., alias="searchQuery")
    category: str | None = None
    phone: str | None = None
    address: str | None = None
    lat_long: str | None = Field(None, alias="latLong")
    radius: int | None = None
    radius_unit: str | None = None
    language: str | None = "en"

@tool(args_schema=LocationSearchInput)
def search_locations(**kwargs):
    """Search for TripAdvisor locations by name, address, lat/long, etc."""
    kwargs["key"] = TRIPADVISOR_API_KEY
    return tripadvisor_get("/location/search", kwargs)

class NearbySearchInput(BaseModel):
    lat_long: str = Field(..., alias="latLong")
    category: str | None = None
    phone: str | None = None
    address: str | None = None
    radius: int | None = None
    radius_unit: str | None = None
    language: str | None = "en"

@tool(args_schema=NearbySearchInput)
def nearby_search(**kwargs):
    """Search for nearby locations using a lat/long pair."""
    kwargs["key"] = TRIPADVISOR_API_KEY
    return tripadvisor_get("/location/nearby_search", kwargs)

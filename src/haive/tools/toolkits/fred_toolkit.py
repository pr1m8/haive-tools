"""
Federal Reserve Economic Data (FRED) Toolkit Module

This toolkit provides tools for accessing economic data from the Federal Reserve Bank of St. Louis
FRED API. It allows retrieval of economic time series data, categories, and related metadata.

FRED is a comprehensive database containing hundreds of thousands of economic time series
from dozens of national, international, public, and private sources.

Required Environment Variables:
    - FRED_API_KEY: Your FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html

Examples:
    >>> from haive.tools.toolkits.fred_toolkit import get_series
    >>> # Get information about GDP series
    >>> gdp_info = get_series("GDP")
    >>> print(f"Series title: {gdp_info['seriess'][0]['title']}")
    Series title: Gross Domestic Product

    >>> from haive.tools.toolkits.fred_toolkit import get_series_observations
    >>> # Get GDP values for 2020-2022
    >>> gdp_data = get_series_observations("GDP", "2020-01-01", "2022-12-31")
    >>> for obs in gdp_data['observations'][:3]:
    ...     print(f"Date: {obs['date']}, Value: ${obs['value']} billion")
    Date: 2020-01-01, Value: $21477.597 billion
"""

import os
from typing import Any, Dict, List, Optional

import requests
from langchain_core.tools import BaseToolkit, StructuredTool
from pydantic import BaseModel, Field

# Environment configuration
FRED_API_KEY = os.getenv("FRED_API_KEY")
BASE_URL = "https://api.stlouisfed.org/fred"


def fred_get(endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Helper function to call the FRED API with proper authentication and formatting.

    This function adds the API key and sets the response format to JSON before
    making the request to the specified FRED API endpoint.

    Args:
        endpoint (str): The FRED API endpoint to call (e.g., "series", "category").
        params (Dict[str, Any]): Parameters to include in the API request.

    Returns:
        Dict[str, Any]: The JSON response from the FRED API.

    Raises:
        requests.RequestException: If the API request fails.
        ValueError: If FRED_API_KEY is not set in the environment.
    """
    if not FRED_API_KEY:
        raise ValueError("FRED_API_KEY environment variable must be set")

    params["api_key"] = FRED_API_KEY
    params["file_type"] = "json"
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params)
    response.raise_for_status()
    return response.json()


# Input schemas for FRED API endpoints
class CategoryInput(BaseModel):
    """Input schema for FRED category queries."""

    category_id: int = Field(
        ..., description="The FRED category ID to fetch (e.g., 0 for root)"
    )


class SeriesInput(BaseModel):
    """Input schema for FRED series queries."""

    series_id: str = Field(
        ..., description="The FRED series ID to fetch (e.g., 'GDP', 'UNRATE')"
    )


class SeriesObservationsInput(BaseModel):
    """Input schema for FRED series observations queries."""

    series_id: str = Field(
        ..., description="The FRED series ID to fetch observations for"
    )
    start_date: Optional[str] = Field(
        None, description="Start date in YYYY-MM-DD format"
    )
    end_date: Optional[str] = Field(None, description="End date in YYYY-MM-DD format")


# Core endpoint functions
def get_category(category_id: int) -> Dict[str, Any]:
    """
    Get information about a FRED category by its ID.

    Categories in FRED organize data series into groups like 'Money, Banking, & Finance',
    'Population, Employment, & Labor Markets', etc.

    Args:
        category_id (int): The FRED category ID to fetch (e.g., 0 for root category).

    Returns:
        Dict[str, Any]: Category information including name and notes.

    Raises:
        requests.RequestException: If the API request fails.
    """
    return fred_get("category", {"category_id": category_id})


def get_category_children(category_id: int) -> Dict[str, Any]:
    """
    Get the child categories of a specified FRED category.

    This function retrieves subcategories for a given parent category,
    allowing exploration of the FRED category hierarchy.

    Args:
        category_id (int): The parent category ID to get children for.

    Returns:
        Dict[str, Any]: List of child categories with their IDs and names.

    Raises:
        requests.RequestException: If the API request fails.
    """
    return fred_get("category/children", {"category_id": category_id})


def get_category_series(category_id: int) -> Dict[str, Any]:
    """
    Get all series belonging to a specified FRED category.

    This function retrieves the economic data series that are classified under
    the specified category.

    Args:
        category_id (int): The category ID to get series for.

    Returns:
        Dict[str, Any]: List of series in the category with metadata.

    Raises:
        requests.RequestException: If the API request fails.
    """
    return fred_get("category/series", {"category_id": category_id})


def get_series(series_id: str) -> Dict[str, Any]:
    """
    Get metadata about a specific FRED data series.

    This function retrieves detailed information about an economic data series,
    including its title, units, frequency, seasonal adjustment, and more.

    Args:
        series_id (str): The FRED series ID (e.g., 'GDP', 'UNRATE', 'CPIAUCSL').

    Returns:
        Dict[str, Any]: Detailed metadata about the requested series.

    Raises:
        requests.RequestException: If the API request fails.
    """
    return fred_get("series", {"series_id": series_id})


def get_series_observations(
    series_id: str, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get the actual data values (observations) for a FRED time series.

    This function retrieves the time series data points for a specified economic indicator,
    with optional date range filtering.

    Args:
        series_id (str): The FRED series ID to fetch observations for.
        start_date (Optional[str], optional): Start date in YYYY-MM-DD format. Defaults to None.
        end_date (Optional[str], optional): End date in YYYY-MM-DD format. Defaults to None.

    Returns:
        Dict[str, Any]: Series observations with dates and values.

    Raises:
        requests.RequestException: If the API request fails.
    """
    params = {"series_id": series_id}
    if start_date:
        params["observation_start"] = start_date
    if end_date:
        params["observation_end"] = end_date
    return fred_get("series/observations", params)


class FREDToolkit(BaseToolkit):
    """
    Toolkit for accessing Federal Reserve Economic Data (FRED).

    This toolkit provides a collection of tools for interacting with the FRED API
    to retrieve economic data series, categories, and related information.

    The Federal Reserve Economic Data (FRED) database contains hundreds of thousands
    of economic time series from dozens of national, international, public, and private sources.
    """

    def get_tools(self) -> List[StructuredTool]:
        """
        Get all tools in the FRED toolkit.

        Returns:
            List[StructuredTool]: A list of tools for interacting with the FRED API.
        """
        return [
            StructuredTool.from_function(
                func=get_category,
                name="get_fred_category",
                description="Get a FRED category by ID",
                args_schema=CategoryInput,
            ),
            StructuredTool.from_function(
                func=get_category_children,
                name="get_fred_category_children",
                description="Get child categories for a FRED category",
                args_schema=CategoryInput,
            ),
            StructuredTool.from_function(
                func=get_category_series,
                name="get_fred_category_series",
                description="List economic data series in a FRED category",
                args_schema=CategoryInput,
            ),
            StructuredTool.from_function(
                func=get_series,
                name="get_fred_series",
                description="Retrieve metadata for a FRED economic data series",
                args_schema=SeriesInput,
            ),
            StructuredTool.from_function(
                func=get_series_observations,
                name="get_fred_series_observations",
                description="Get FRED series observations (actual data values) with optional date range filtering",
                args_schema=SeriesObservationsInput,
            ),
        ]


# Initialize the toolkit for easy import
fred_toolkit = FREDToolkit()
fred_tools = fred_toolkit.get_tools()

"""CitySDK Toolkit for accessing city-related data from various sources.

This toolkit provides tools for interacting with the CitySDK APIs,
including the Linked Data API for SPARQL queries and the Tourism API
for points of interest information. These tools help agents find and
process structured city information.

Example:
    ```python
    toolkit = CitySDKToolkit()
    tools = toolkit.get_tools()
    ```

Attributes:
    None
"""

import requests
from langchain_core.tools import StructuredTool
from langchain_core.tools.base import BaseToolkit
from pydantic import BaseModel, Field

# --- Linked Data Tool ---


class CitySDKLinkedDataQueryInput(BaseModel):
    """Input schema for the CitySDK Linked Data SPARQL query tool.

    Args:
        query: SPARQL query to execute against the CitySDK Linked Data endpoint
    """

    query: str = Field(
        ..., description="SPARQL query to send to the CitySDK Linked Data endpoint."
    )


def run_citysdk_linkeddata_query(query: str) -> dict:
    """Executes a SPARQL query against the CitySDK Linked Data endpoint.

    Args:
        query: A valid SPARQL query string

    Returns:
        dict: JSON response containing the query results

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    endpoint = "https://citysdk.dm.fhnw.ch/sparql"
    headers = {"Accept": "application/sparql-results+json"}
    response = requests.get(endpoint, params={"query": query}, headers=headers)
    response.raise_for_status()
    return response.json()


citysdk_linked_data_tool = StructuredTool.from_function(
    func=run_citysdk_linkeddata_query,
    name="citysdk_linked_data_query",
    description="Send a SPARQL query to the CitySDK Linked Data API to retrieve structured city information.",
    args_schema=CitySDKLinkedDataQueryInput,
)

# --- Tourism Tool ---


class CitySDKTourismPOIInput(BaseModel):
    """Input schema for querying Points of Interest from the CitySDK Tourism API.

    Args:
        bbox: Bounding box coordinates to filter POIs geographically
        city: City name to filter POIs by location
    """

    bbox: str | None = Field(
        None,
        description="Bounding box (e.g., '24.9384,60.1695,24.9500,60.1750') to filter POIs geographically.",
    )
    city: str | None = Field(None, description="Optional city to filter POIs.")


def get_tourism_pois(bbox: str | None = None, city: str | None = None) -> dict:
    """Fetches Points of Interest data from the CitySDK Tourism API.

    Args:
        bbox: Optional bounding box to filter POIs geographically
        city: Optional city name to filter POIs

    Returns:
        dict: JSON response containing the POI data

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    endpoint = "https://tourism-api.citysdk.cm-lisboa.pt/resources/pois"
    params = {}
    if bbox:
        params["bbox"] = bbox
    if city:
        params["city"] = city
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()


citysdk_tourism_poi_tool = StructuredTool.from_function(
    func=get_tourism_pois,
    name="citysdk_tourism_poi_query",
    description="Retrieve Points of Interest from the CitySDK Tourism API using a bounding box or city filter.",
    args_schema=CitySDKTourismPOIInput,
)

# --- Toolkit ---


class CitySDKToolkit(BaseToolkit):
    """Toolkit for accessing CitySDK APIs for city-related data.

    This toolkit provides tools for working with different CitySDK APIs,
    including SPARQL queries for linked data and tourism POI information.
    """

    def get_tools(self) -> list[StructuredTool]:
        """Gets the list of available CitySDK tools.

        Returns:
            List[StructuredTool]: A list of tools for working with CitySDK APIs
        """
        return [citysdk_linked_data_tool, citysdk_tourism_poi_tool]

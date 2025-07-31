"""Agify Name Age Estimation Tool Module.

This module provides a tool for estimating the average age of a person based on their first name
using the Agify.io API. The tool can optionally filter age estimations by country.

Agify.io analyzes name data across different countries to predict the likely age of a person
based solely on their first name.

Examples:
    >>> from haive.tools.tools.agify_tool import estimate_age
    >>> result = estimate_age("John")
    >>> print(f"The estimated age for John is {result.age} years old")
    The estimated age for John is 61 years old

    >>> # With country filter
    >>> result = estimate_age("John", country_id="US")
    >>> print(f"The estimated age for John in the US is {result.age} years old")
    The estimated age for John in the US is 69 years old

"""

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
import requests


class AgifyResponse(BaseModel):
    """Response model from the Agify API containing age estimation details.

    This model represents the structured response from the Agify.io API,
    including the estimated age for a name and additional metadata.

    Attributes:
        name (str): The first name that was queried.
        age (int): The estimated average age for people with this name.
        count (int): The number of people with this name in the dataset.
        country_id (Optional[str]): The country code used to filter results, if provided.

    """

    name: str = Field(description="The name to estimate age for")
    age: int = Field(description="The estimated age of the name")
    count: int = Field(description="The number of people with the name in the country")
    country_id: str | None = Field(None, description="The country code of the name")


def estimate_age(name: str, country_id: str | None = None) -> AgifyResponse:
    """Estimate the average age of a person based on their first name.

    This function queries the Agify.io API to get an age estimation based on the provided
    first name. The estimation can be optionally filtered by country.

    Args:
        name (str): The first name to estimate age for.
        country_id (Optional[str], optional): Two-letter country code (ISO 3166-1 alpha-2)
            to filter results by country. Defaults to None (worldwide data).

    Returns:
        AgifyResponse: Object containing the age estimation and related metadata.

    Raises:
        requests.RequestException: If the API request fails.

    """
    url = "https://api.agify.io"
    params = {"name": name}
    if country_id:
        params["country_id"] = country_id
    response = requests.get(url, params=params)
    response.raise_for_status()
    return AgifyResponse(**response.json())


AgifyToolkit = [
    StructuredTool.from_function(
        func=estimate_age,
        name="estimate_age",
        description="Estimate the average age of a person based on their first name, with optional country filtering.",
    )
]

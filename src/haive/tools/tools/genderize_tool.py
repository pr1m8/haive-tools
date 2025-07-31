"""Genderize Tool Module.

This module provides a tool for predicting gender from first names using the
Genderize.io API. It creates a structured tool that can be integrated into
LangChain-based agents to predict gender based on provided names, with optional
country context.

The module includes a Pydantic model for the API response and a function to
interact with the Genderize.io API directly.

Example:
    >>> from haive.tools.tools.genderize_tool import genderize_tool
    >>> result = genderize_tool.invoke({"name": "Alex", "country_id": "US"})
    >>> print(f"Predicted gender: {result.gender} with {result.probability} probability")

Note:
    No API key is required for basic usage, but rate limits apply.
    See https://genderize.io/ for more information.

"""

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
import requests


class GenderizeResponse(BaseModel):
    """Response from the Genderize API.

    Attributes:
        name: The name to predict gender for
        gender: The predicted gender of the name
        probability: The probability of the predicted gender
        count: The number of people with the name in the country
        country_id: The country code of the name

    """

    name: str = Field(description="The name to predict gender for")
    gender: str | None = Field(description="The predicted gender of the name")
    probability: float | None = Field(
        description="The probability of the predicted gender"
    )
    count: int = Field(description="The number of people with the name in the country")
    country_id: str | None = Field(description="The country code of the name")


def predict_gender(name: str, country_id: str | None = None) -> GenderizeResponse:
    """Predict gender from a first name using the Genderize.io API.

    Args:
        name: The first name to predict gender for
        country_id: Optional two-letter country code (ISO 3166-1 alpha-2)
            to scope the search to a specific country

    Returns:
        GenderizeResponse: An object containing the predicted gender, probability,
            and other metadata from the API

    Raises:
        requests.exceptions.HTTPError: If the API request fails

    """
    url = "https://api.genderize.io"
    params = {"name": name}
    if country_id:
        params["country_id"] = country_id
    res = requests.get(url, params=params)
    res.raise_for_status()
    return GenderizeResponse(**res.json())


genderize_tool = StructuredTool.from_function(
    func=predict_gender,
    name="predict_gender",
    description="Predict gender from a single first name, with optional country scope.",
)

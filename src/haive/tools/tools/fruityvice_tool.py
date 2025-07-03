"""Fruityvice API Tool Module

This module provides a tool for accessing the Fruityvice API, which offers comprehensive
nutritional information and details about various fruits. It allows users to query
fruit data by name and retrieve detailed nutritional facts.

Examples:
    >>> from haive.tools.tools.fruityvice_tool import get_fruit_info, FruitNameInput
    >>> input = FruitNameInput(name="banana")
    >>> result = get_fruit_info(input)
    >>> print(result["name"])
    'Banana'
"""

from typing import Any

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class FruitNameInput(BaseModel):
    """Input model for fruit lookup requests.

    Attributes:
        name (str): The name of the fruit to retrieve data for.
    """

    name: str = Field(..., description="Name of the fruit to retrieve data for")


def get_fruit_info(input: FruitNameInput) -> dict[str, Any]:
    """Fetch detailed information about a specific fruit from the Fruityvice API.

    The information returned typically includes nutritional data (calories, fat, sugar, etc.),
    family, genus, and other taxonomic details.

    Args:
        input (FruitNameInput): Object containing the name of the fruit to look up.

    Returns:
        Dict[str, Any]: A dictionary containing the fruit's details and nutritional information.
        If the fruit is not found, returns a dictionary with an error message.

    Raises:
        requests.HTTPError: If the API request fails for reasons other than a 404.
    """
    response = requests.get(
        f"https://www.fruityvice.com/api/fruit/{input.name.lower()}"
    )
    if response.status_code == 404:
        return {"error": f"Fruit '{input.name}' not found"}
    response.raise_for_status()
    return response.json()


fruit_lookup_tool = StructuredTool.from_function(
    name="get_fruit_info",
    description="Fetch nutrition and detailed information about a specific fruit using its name from the Fruityvice API",
    func=get_fruit_info,
)

# Export the tool in a list for easy import
FruityviceTools = [fruit_lookup_tool]

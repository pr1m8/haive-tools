"""
Open Food Facts Tool Module.

This module provides a tool for retrieving product information from the
Open Food Facts database using barcodes. It creates a structured tool that
can be integrated into LangChain-based agents to get nutrition facts, ingredients,
and other product data.

The module uses the Open Food Facts API (https://world.openfoodfacts.org/api/v2/)
to look up product information by barcode.

Example:
    >>> from haive.tools.tools.open_food_tool import open_food_facts_tool
    >>> result = open_food_facts_tool.invoke({"barcode": "3017620422003"})
    >>> print(f"Product: {result.get('product_name')}")

Note:
    No API key is required for usage, but rate limits may apply.
    See https://world.openfoodfacts.org/api/v2/ for API details.
"""

from typing import Optional

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class GetProductInfoInput(BaseModel):
    """Input schema for the Open Food Facts product lookup.

    Attributes:
        barcode: The barcode of the product to look up
    """

    barcode: str = Field(..., description="The barcode of the product to look up.")


def get_product_info(barcode: str) -> dict:
    """
    Retrieve product information from Open Food Facts by barcode.

    Args:
        barcode: The barcode of the product to look up (EAN, UPC, etc.)

    Returns:
        dict: Product information including name, ingredients, nutrition facts, etc.

    Raises:
        ValueError: If the API request fails or no product is found
    """
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching product data: {response.status_code}")
    data = response.json()
    if "product" not in data:
        raise ValueError("No product data found.")
    return data["product"]


open_food_facts_tool = StructuredTool.from_function(
    func=get_product_info,
    name="get_open_food_facts_product",
    description="Use this tool to retrieve product data using a barcode from Open Food Facts.",
    args_schema=GetProductInfoInput,
)

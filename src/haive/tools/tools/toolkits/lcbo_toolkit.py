"""LCBO API Toolkit for accessing data from the Liquor Control Board of Ontario.

This toolkit provides tools to interact with the LCBO API, allowing agents to
search for products and retrieve detailed product information from the Liquor
Control Board of Ontario's product database.

Example:
    ```python
    toolkit = LCBOApiToolkit()
    tools = toolkit.get_tools()
    ```

Attributes:
    None
"""

import requests
from langchain_core.tools import BaseToolkit, StructuredTool
from pydantic import BaseModel, Field


# --- Tool to fetch a product by ID ---
class GetLCBOProductInput(BaseModel):
    """Input schema for fetching a product by ID from the LCBO API.

    Args:
        product_id: The unique LCBO product identifier
    """

    product_id: int = Field(..., description="LCBO product ID")


def get_lcbo_product(product_id: int) -> dict:
    """Fetches detailed information for a specific LCBO product.

    Args:
        product_id: The unique LCBO product identifier

    Returns:
        dict: JSON response containing detailed product information

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    url = f"https://lcboapi.com/products/{product_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


get_product_tool = StructuredTool.from_function(
    name="get_lcbo_product_by_id",
    description="Fetch detailed info for a product using its LCBO product ID",
    func=get_lcbo_product,
    args_schema=GetLCBOProductInput,
)


# --- Tool to search products ---
class SearchLCBOProductsInput(BaseModel):
    """Input schema for searching LCBO products.

    Args:
        query: The search terms to find matching products
        page: Page number for paginated results
        per_page: Number of results to return per page
    """

    query: str = Field(..., description="Search query string")
    page: int | None = Field(1, description="Page number of results")
    per_page: int | None = Field(10, description="Number of results per page")


def search_lcbo_products(query: str, page: int = 1, per_page: int = 10) -> dict:
    """Searches for LCBO products based on a query string.

    Args:
        query: The search terms to find matching products
        page: Page number for paginated results (default: 1)
        per_page: Number of results to return per page (default: 10)

    Returns:
        dict: JSON response containing the search results

    Raises:
        HTTPError: If the request fails or returns an error status code
    """
    url = "https://lcboapi.com/products"
    params = {"q": query, "page": page, "per_page": per_page}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


search_products_tool = StructuredTool.from_function(
    name="search_lcbo_products",
    description="Search for LCBO products by keyword, name, etc.",
    func=search_lcbo_products,
    args_schema=SearchLCBOProductsInput,
)


# --- Toolkit wrapper ---
class LCBOApiToolkit(BaseToolkit):
    """Toolkit for interacting with the LCBO API.

    This toolkit provides tools for searching LCBO's product database
    and retrieving detailed information about specific products.
    """

    def get_tools(self) -> list[StructuredTool]:
        """Gets the list of available LCBO API tools.

        Returns:
            List[StructuredTool]: A list of tools for working with the LCBO API
        """
        return [get_product_tool, search_products_tool]

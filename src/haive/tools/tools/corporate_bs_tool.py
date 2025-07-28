"""Corporate Buzzword Generator Tool Module.

This module provides a tool for generating random corporate business jargon and buzzwords
using the Corporate BS Generator API. Useful for satirical purposes or demonstrating
overly complex business language.

Examples:
    >>> from haive.tools.tools.corporate_bs_tool import get_random_corporate_bs
    >>> result = get_random_corporate_bs()
    >>> print(result.phrase)
    'synergize scalable paradigms'
"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class CorporateBS(BaseModel):
    """Response model for Corporate BS Generator API.

    Attributes:
        phrase (str): A randomly generated corporate buzzword phrase.
    """

    phrase: str = Field(..., description="Randomly generated corporate buzzword phrase")


def get_random_corporate_bs() -> CorporateBS:
    """Fetch a random corporate buzzword phrase from the Corporate BS Generator API.

    Returns:
        CorporateBS: An object containing the randomly generated corporate phrase.

    Raises:
        requests.RequestException: If the API request fails.
    """
    res = requests.get("https://corporatebs-generator.sameerkumar.website/")
    res.raise_for_status()
    data = res.json()
    return CorporateBS(phrase=data["phrase"])


CorporateBSToolkit = [
    StructuredTool.from_function(
        func=get_random_corporate_bs,
        name="get_random_corporate_bs",
        description="Generate a random corporate buzzword phrase for satirical purposes",
    )
]

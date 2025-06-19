"""
Useless Facts Toolkit Module.

This module provides a toolkit for retrieving random and daily useless facts.
It leverages the Useless Facts API (https://uselessfacts.jsph.pl/) to provide
fun, trivial information that can be used for entertainment purposes.

The module offers structured tools for:
1. Getting a random useless fact
2. Getting today's useless fact

Both tools support language selection (English or German) and are packaged as
LangChain-compatible structured tools for use in agent workflows.

Example:
    >>> from haive.tools.toolkits.useless_facts_toolkit import useless_facts_toolkit
    >>> random_fact_tool = useless_facts_toolkit[0]
    >>> fact = random_fact_tool.invoke({"language": "en"})
    >>> print(f"Random fact: {fact}")

Note:
    No API key is required for the Useless Facts API, though rate limits may apply.
"""

from typing import Optional

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

# Base URL for the Useless Facts API
BASE_URL = "https://uselessfacts.jsph.pl/api/v2/facts"


class FactInput(BaseModel):
    """Input schema for the useless facts tools.

    Attributes:
        language: Language code for the fact (en or de)
    """

    language: Optional[str] = Field(
        default="en", description="Language of the fact. Supports 'en' or 'de'."
    )


def get_random_fact(language: Optional[str] = "en") -> str:
    """
    Retrieve a random useless fact from the API.

    Args:
        language: Language code, either 'en' for English or 'de' for German

    Returns:
        str: A random useless fact in the specified language

    Raises:
        requests.exceptions.HTTPError: If the API request fails
    """
    res = requests.get(
        f"{BASE_URL}/random",
        params={"language": language},
        headers={"Accept": "application/json"},
    )
    res.raise_for_status()
    return res.json().get("text", "No fact found.")


def get_todays_fact(language: Optional[str] = "en") -> str:
    """
    Retrieve today's useless fact from the API.

    Args:
        language: Language code, either 'en' for English or 'de' for German

    Returns:
        str: Today's useless fact in the specified language

    Raises:
        requests.exceptions.HTTPError: If the API request fails
    """
    res = requests.get(
        f"{BASE_URL}/today",
        params={"language": language},
        headers={"Accept": "application/json"},
    )
    res.raise_for_status()
    return res.json().get("text", "No fact found for today.")


# Create structured tools for use in LangChain agents
get_random_fact_tool = StructuredTool.from_function(
    name="get_random_useless_fact",
    description="Get a random useless fact. Optionally specify the language ('en' or 'de').",
    func=get_random_fact,
    args_schema=FactInput,
)

get_todays_fact_tool = StructuredTool.from_function(
    name="get_todays_useless_fact",
    description="Get today's useless fact. Optionally specify the language ('en' or 'de').",
    func=get_todays_fact,
    args_schema=FactInput,
)

# Export both tools as a toolkit
useless_facts_toolkit = [get_random_fact_tool, get_todays_fact_tool]

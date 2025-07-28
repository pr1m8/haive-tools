"""Techy Phrase Generator Tool Module.

This module provides tools for generating random technology-related phrases using the Techy API.
It offers functionality to retrieve phrases in both plain text and structured JSON formats,
which can be used to add technical flavor to conversations or generate mock tech content.

Examples:
    >>> from haive.tools.tools.techy_phrase_tool import get_techy_phrase_text
    >>> phrase = get_techy_phrase_text()
    >>> print(phrase)
    'We need to back up the wireless SSL driver!'

    >>> from haive.tools.tools.techy_phrase_tool import get_techy_phrase_json
    >>> phrase_data = get_techy_phrase_json()
    >>> print(phrase_data['text'])
    'Try to quantify the EXE application, maybe it will index the multi-byte port!'
"""

import requests
from langchain_core.tools import Tool


def get_techy_phrase_text() -> str:
    """Fetch a random technology-related phrase in plain text format.

    This function retrieves a randomly generated tech-sounding phrase from the
    Techy API in simple text format.

    Returns:
        str: A randomly generated tech phrase as a string.

    Raises:
        requests.RequestException: If the API request fails.
    """
    return requests.get("https://techy-api.vercel.app/api/text").text.strip()


def get_techy_phrase_json() -> dict:
    """Fetch a random technology-related phrase in structured JSON format.

    This function retrieves a randomly generated tech-sounding phrase from the
    Techy API in JSON format, which includes additional metadata.

    Returns:
        dict: A dictionary containing the tech phrase and possibly other metadata.

    Raises:
        requests.RequestException: If the API request fails.
        ValueError: If the response cannot be parsed as JSON.
    """
    return requests.get("https://techy-api.vercel.app/api/json").json()


techy_text_tool = Tool(
    name="techy_phrase_text",
    description="Get a random tech phrase in plain text",
    func=lambda x: get_techy_phrase_text(),
)

techy_json_tool = Tool(
    name="techy_phrase_json",
    description="Get a random tech phrase in structured JSON format",
    func=lambda x: get_techy_phrase_json(),
)

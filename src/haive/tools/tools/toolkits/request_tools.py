"""HTTP request tools for interacting with web APIs.

This module provides tools for making HTTP requests to external APIs and services.
It leverages the LangChain Requests integration to provide a robust and secure way
to interact with web services.

The module includes tools for:
- Making GET requests to fetch data
- Making POST requests to submit data
- Making general HTTP requests with custom methods, headers, and payloads

For detailed documentation on the underlying implementation, see:
https://python.langchain.com/docs/integrations/tools/requests/

Typical usage::

    from haive.tools.toolkits.request_tools import requests_get, requests_post

    # Make a GET request
    response = requests_get.invoke({"url": "https://api.example.com/data"})

    # Make a POST request
    response = requests_post.invoke({
        "url": "https://api.example.com/submit",
        "data": {"key": "value"}
    })

"""

from typing import Any

from langchain_community.tools.requests.tool import RequestsGetTool, RequestsPostTool
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class RequestsGetInput(BaseModel):
    """Input schema for the RequestsGet tool."""

    url: str = Field(..., description="The URL to make a GET request to")
    params: dict[str, str] | None = Field(
        None, description="URL parameters to include in the request"
    )
    headers: dict[str, str] | None = Field(
        None, description="Headers to include in the request"
    )


class RequestsPostInput(BaseModel):
    """Input schema for the RequestsPost tool."""

    url: str = Field(..., description="The URL to make a POST request to")
    data: dict[str, Any] | None = Field(
        None, description="JSON data to send in the request body"
    )
    params: dict[str, str] | None = Field(
        None, description="URL parameters to include in the request"
    )
    headers: dict[str, str] | None = Field(
        None, description="Headers to include in the request"
    )


# Create structured tools from the LangChain implementations
requests_get = StructuredTool.from_function(
    func=RequestsGetTool().invoke,
    name="requests_get",
    description="Make a GET request to the specified URL and get the response",
    args_schema=RequestsGetInput,
)

requests_post = StructuredTool.from_function(
    func=RequestsPostTool().invoke,
    name="requests_post",
    description="Make a POST request to the specified URL with the given data and get the response",
    args_schema=RequestsPostInput,
)

# Export the tools as a list for easy access
requests_tools = [requests_get, requests_post]

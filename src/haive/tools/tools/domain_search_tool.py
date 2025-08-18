"""Domain search tool for querying registered domain names.

This module provides a tool for searching registered domain names based on keywords
using the domainsdb.info API. It allows users to find existing domains containing
specific keywords, which can be useful for domain availability research, brand protection,
or competitive analysis.

The tool returns a list of registered domain names matching the provided key,
limited to the top 10 results to avoid overwhelming responses.

Examples:
            from haive.tools.tools.domain_search_tool import domain_search_tool

            # Add to your agent's toolkit
            agent = Agent(tools=[domain_search_tool])

            # Example use in an agent
            response = agent.run("Find domains related to 'python'")

Note:
    - The domainsdb.info API has usage limits and may throttle requests
    - Results are limited to the top 10 matches to keep responses manageable
    - No authentication is required for basic lookups

"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import AnyUrl, BaseModel, Field


class DomainSearchInput(BaseModel):
    """Input model for the domain search tool.

    Attributes:
        domain: A domain key to search for. This can be any term that might appear
               in registered domain names, such as a brand name, generic term, or
               specific word of interest.

    """

    domain: AnyUrl = Field(
        description="A key to search for, e.g., 'facebook', 'ai', 'nasa', etc."
    )


def search_registered_domains(domain: str) -> str:
    """Search for registered domain names using a key.

    Queries the domainsdb.info API to find registered domain names containing the
    specified key. Returns up to 10 matching domain names.

    Args:
        domain: A key to search for in domain names.

    Returns:
        str: A newline-separated list of domain names matching the search criteria,
             limited to 10 results, or an error message if the search fails or no
             results are found.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    """
    url = f"https://api.domainsdb.info/v1/domains/search?domain={domain}"
    response = requests.get(url)
    if not response.ok:
        return f"Error {response.status_code}: {response.text}"

    data = response.json()
    domains = data.get("domains", [])
    if not domains:
        return f"No results found for '{domain}'"

    return "\n".join([d["domain"] for d in domains[:10]])


# Create a structured tool from the search_registered_domains function
domain_search_tool = StructuredTool.from_function(
    func=search_registered_domains,
    name="search_registered_domains",
    description="Search for registered domain names using a key",
    args_schema=DomainSearchInput,
)

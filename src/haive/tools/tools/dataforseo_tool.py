"""DataForSEO API integration tools for SEO and search engine data.

This module provides integration with DataForSEO's API services through the LangChain
tools interface. DataForSEO offers various API endpoints for SEO analytics, search engine
results, key research, competitor analysis, and more.

The module configures and initializes the DataForSEO API wrapper and loads the corresponding
tools for use in agent workflows. It requires valid DataForSEO API credentials to be
configured in the environment or the Config object.

Requires:
    - DataForSEO account with API access
    - Valid credentials (login and pass
    - API usage is subject to DataForSEO's terms of service and rate limits
    - Documentation for the DataForSEO API integration in LangChain is available at:
      https://python.langchain.com/docs/integrations/tools/dataforseo/

"""

from haive.config.config import Config
from langchain.agents import load_tools
from langchain_community.utilities.dataforseo_api_search import DataForSeoAPIWrapper


def get_dataforseo_tools():
    """Get DataForSEO tools with proper error handling for missing credentials.

    Returns:
        list: List containing DataForSEO tools if credentials are available,
              empty list otherwise.
    """
    try:
        if not Config.DATAFORSEO_LOGIN or not Config.DATAFORSEO_PASSWORD:
            raise ValueError("DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD must be set")

        # Initialize the DataForSEO API wrapper
        dataforseo = DataForSeoAPIWrapper()

        # Test the DataForSEO API wrapper with a sample query
        result = dataforseo.run(
            "https://python.langchain.com/docs/integrations/tools/dataforseo/"
        )

        # Load the DataForSEO tools
        return load_tools(["dataforseo-api"])
    except Exception as e:
        # Return empty list if credentials are missing or other issues occur
        print(f"Warning: DataForSEO tools unavailable: {e}")
        return []


# Load the DataForSEO tools
dataforseo_tools = get_dataforseo_tools()

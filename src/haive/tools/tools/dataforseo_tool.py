"""DataForSEO API integration tools for SEO and search engine data.

This module provides integration with DataForSEO's API services through the LangChain
tools interface. DataForSEO offers various API endpoints for SEO analytics, search engine
results, keyword research, competitor analysis, and more.

The module configures and initializes the DataForSEO API wrapper and loads the corresponding
tools for use in agent workflows. It requires valid DataForSEO API credentials to be
configured in the environment or the Config object.

Requires:
    - DataForSEO account with API access
    - Valid credentials (login and password) set in Config.DATAFORSEO_LOGIN and Config.DATAFORSEO_PASSWORD
    - langchain_community package with DataForSEO integration

Example:
    To use the DataForSEO tools in an agent:
    ```python
    from haive.tools.tools.dataforseo_tool import dataforseo_tools

    # Add to your agent's toolkit
    agent = Agent(tools=dataforseo_tools)
    ```

Note:
    - DataForSEO is a paid service with various pricing tiers
    - API usage is subject to DataForSEO's terms of service and rate limits
    - Documentation for the DataForSEO API integration in LangChain is available at:
      https://python.langchain.com/docs/integrations/tools/dataforseo/
"""

from haive.config.config import Config

if not Config.DATAFORSEO_LOGIN or not Config.DATAFORSEO_PASSWORD:
    raise ValueError("DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD must be set")

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities.dataforseo_api_search import DataForSeoAPIWrapper

# Initialize the DataForSEO API wrapper
dataforseo = DataForSeoAPIWrapper()

# Test the DataForSEO API wrapper with a sample query
result = dataforseo.run(
    "https://python.langchain.com/docs/integrations/tools/dataforseo/"
)
print(result)

# Load the DataForSEO tools
dataforseo_tools = load_tools(["dataforseo-api"])
print(dataforseo_tools)

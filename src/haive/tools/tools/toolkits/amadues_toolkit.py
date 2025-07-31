from __future__ import annotations

import os

from amadeus import Client
from dotenv import load_dotenv
from haive.core.models.llm.base import AzureLLMConfig, LLMConfig
from langchain_community.tools.amadeus.closest_airport import AmadeusClosestAirport
from langchain_community.tools.amadeus.flight_search import AmadeusFlightSearch
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import BaseModel, ConfigDict, Field

"""Amadeus Travel API Toolkit for accessing flight information and travel data.

This toolkit provides a Langchain-compatible interface to the Amadeus Travel APIs,
allowing agents to search for flights and find nearby airports. It simplifies
the process of authenticating with Amadeus and configuring the necessary tools.

Example:
    ```python
    config = AmadeusToolkitConfig(
        client_id=os.getenv("AMADEUS_CLIENT_ID"),
        client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
    )
    toolkit = AmadeusToolkit.from_config(config)
    tools = toolkit.get_tools()
    ```

Attributes:
    None
"""


# Load environment variables
load_dotenv(".env")

# Import your LLM config wrapper


# -----------------------------
# 🔧 Amadeus Config (Serializable)
# -----------------------------
class AmadeusToolkitConfig(BaseModel):
    """JSON-serializable config for instantiating the Amadeus toolkit and its
    dependencies.

    This configuration class holds the authentication credentials for the Amadeus API
    and optionally an LLM configuration for tools that require language model support.

    Args:
        client_id: The Amadeus API client ID for authentication
        client_secret: The Amadeus API client secret for authentication
        llm_config: Optional configuration for a language model that some tools may require

    """

    client_id: str = Field(
        default_factory=lambda: os.getenv("AMADEUS_CLIENT_ID", ""),
        description="Amadeus API client ID.",
    )
    client_secret: str = Field(
        default_factory=lambda: os.getenv("AMADEUS_CLIENT_SECRET", ""),
        description="Amadeus API client secret.",
    )
    llm_config: LLMConfig | None = Field(
        default=AzureLLMConfig(),
        description="LLM configuration dict, passed to LLMConfig",
    )

    def create_client(self) -> Client:
        """Creates an authenticated Amadeus Client instance.

        Returns:
            Client: An initialized Amadeus API client

        Raises:
            ValueError: If client credentials are invalid

        """
        return Client(client_id=self.client_id, client_secret=self.client_secret)

    def create_llm(self) -> BaseLanguageModel | None:
        """Creates a language model instance from the config if provided.

        Returns:
            Optional[BaseLanguageModel]: An initialized language model or None if not configured

        """
        if self.llm_config:
            return self.llm_config.instantiate()
        return None


# -----------------------------
# 🧰 Amadeus Toolkit (LangChain-compatible)
# -----------------------------
class AmadeusToolkit(BaseToolkit):
    """LangChain-compatible toolkit for interacting with Amadeus APIs.

    This toolkit provides a collection of tools for travel-related operations,
    including finding the closest airport to coordinates and searching for flights.

    Args:
        config: Configuration for Amadeus API authentication and LLM settings
        client: An authenticated Amadeus API client instance
        llm: Optional language model for tools that require LLM capabilities

    """

    config: AmadeusToolkitConfig
    client: Client
    llm: BaseLanguageModel | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_tools(self) -> list[BaseTool]:
        """Gets the list of available Amadeus API tools.

        Returns:
            List[BaseTool]: A list of LangChain tools for working with Amadeus APIs

        """
        # Required model rebuilds for Pydantic v2
        AmadeusClosestAirport.model_rebuild()
        AmadeusFlightSearch.model_rebuild()

        return [
            AmadeusClosestAirport(llm=self.llm),
            AmadeusFlightSearch(),
        ]

    @classmethod
    def from_config(cls, config: AmadeusToolkitConfig) -> AmadeusToolkit:
        """Creates a toolkit instance from a configuration object.

        Args:
            config: The configuration with Amadeus credentials and LLM settings

        Returns:
            AmadeusToolkit: An initialized toolkit instance

        Raises:
            ValueError: If client creation fails due to invalid credentials

        """
        return cls(
            config=config, client=config.create_client(), llm=config.create_llm()
        )


# -----------------------------
# 🧪 Test CLI
# -----------------------------
if __name__ == "__main__":
    config = AmadeusToolkitConfig(
        client_id=os.getenv("AMADEUS_CLIENT_ID", ""),
        client_secret=os.getenv("AMADEUS_CLIENT_SECRET", ""),
    )

    toolkit = AmadeusToolkit.from_config(config)
    tools = toolkit.get_tools()

    for _tool in tools:
        pass

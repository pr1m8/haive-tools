from __future__ import annotations

import os

from dotenv import load_dotenv
from haive.core.models.llm.base import AzureLLMConfig, LLMConfig
from langchain_community.agent_toolkits.nla.toolkit import NLAToolkit as RawNLAToolkit
from langchain_community.utilities.requests import Requests
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import BaseModel, ConfigDict, Field

"""Natural Language API (NLA) Toolkit for interacting with OpenAPI specifications.

This module provides a toolkit for creating tools from OpenAPI specifications or AI plugin
manifests. It leverages LangChain's NLA toolkit to automatically create tools from
API specifications, which can then be used by agents to interact with external services.

The NLA toolkit allows agents to perform Natural Language API (NLA) operations by:
1. Parsing OpenAPI specifications or AI plugin manifests
2. Creating appropriate tools for each endpoint
3. Allowing agents to interact with the API through natural language

Typical usage:
    from haive.tools.toolkits.nla_toolkit import NLAToolkitConfig, StructuredNLAToolkit

    # Configure and create the toolkit
    config = NLAToolkitConfig(
        url="https://example.com/openapi.json",
        llm_config=AzureLLMConfig(deployment_name="my-model")
    )

    # Create the toolkit and get tools
    toolkit = StructuredNLAToolkit.from_config(config)
    tools = toolkit.get_tools()

    # Use the tools in an agent
    agent = create_structured_chat_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
"""


# -----------------------------
# 📦 Load Environment
# -----------------------------
load_dotenv(".env")


# -----------------------------
# 🔧 Config Schema
# -----------------------------
class NLAToolkitConfig(BaseModel):
    """Configuration for instantiating the NLA Toolkit.

    This configuration class contains all the parameters needed to create
    an NLA toolkit instance. It includes the URL of the OpenAPI specification
    and the configuration for the language model to be used.

    Attributes:
        url: URL of the OpenAPI spec or AI plugin manifest.
        llm_config: LLM configuration for the model to use with the toolkit.
            Defaults to an AzureLLMConfig instance.

    """

    url: str = Field(..., description="URL of the OpenAPI spec or AI plugin manifest.")
    llm_config: LLMConfig | None = Field(
        default_factory=AzureLLMConfig, description="LLM configuration."
    )

    def create_llm(self) -> BaseLanguageModel | None:
        """Create a language model instance from the configuration.

        Returns:
            An instantiated language model, or None if no llm_config is provided.

        """
        if self.llm_config:
            return self.llm_config.instantiate()
        return None


# -----------------------------
# 🧰 Structured NLA Toolkit
# -----------------------------
class StructuredNLAToolkit(BaseToolkit):
    """Structured toolkit for Natural Language APIs.

    This toolkit creates tools from OpenAPI specifications or AI plugin manifests,
    allowing agents to interact with external services through natural language.

    Attributes:
        config: The configuration for this toolkit.
        llm: The language model to use for parsing and understanding the API.
        url: The URL of the OpenAPI specification or AI plugin manifest.

    """

    config: NLAToolkitConfig
    llm: BaseLanguageModel | None = None
    url: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_tools(self) -> list[BaseTool]:
        """Get the list of tools created from the OpenAPI specification.

        This method parses the OpenAPI specification and creates appropriate
        tools for each endpoint.

        Returns:
            A list of tools that can be used to interact with the API.

        Raises:
            ValueError: If the LLM is not initialized.

        """
        if not self.llm:
            raise ValueError("LLM must be initialized before using the NLA toolkit.")
        raw_toolkit = RawNLAToolkit.from_llm_and_url(
            llm=self.llm, open_api_url=self.url, requests=Requests()
        )
        return raw_toolkit.get_tools()

    @classmethod
    def from_config(cls, config: NLAToolkitConfig) -> StructuredNLAToolkit:
        """Create a toolkit instance from a configuration.

        Args:
            config: The configuration to use for creating the toolkit.

        Returns:
            A new instance of the StructuredNLAToolkit.

        """
        return cls(
            config=config,
            llm=config.create_llm(),
            url=config.url,
        )


# -----------------------------
# 🧪 CLI Test
# -----------------------------
if __name__ == "__main__":
    config = NLAToolkitConfig(
        url=os.getenv(
            "NLA_URL", "https://www.klarna.com/us/shopping/openai/v0/api-docs/"
        ),
    )

    toolkit = StructuredNLAToolkit.from_config(config)
    tools = toolkit.get_tools()

    for _tool in tools:
        pass

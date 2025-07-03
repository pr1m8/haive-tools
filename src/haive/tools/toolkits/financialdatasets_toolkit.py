"""Financial Datasets Toolkit Module

This module provides a toolkit for accessing comprehensive financial data through the Financial Datasets API.
It offers tools for retrieving financial statements, market data, and other financial information for
approximately 16,000+ tickers spanning over 30 years of historical data.

The toolkit provides access to:
- Income statements
- Balance sheets
- Cash flow statements
- Company financial metrics
- Historical financial data

Required Environment Variables:
    - FINANCIAL_DATASETS_API_KEY: Your Financial Datasets API key from financialdatasets.ai
    - OPENAI_API_KEY: An OpenAI API key for agent functionality

Examples:
    >>> from haive.tools.toolkits.financialdatasets_toolkit import get_financial_datasets_tools
    >>> tools = get_financial_datasets_tools()
    >>> # Use tools with an agent framework
    >>> from langchain.agents import AgentExecutor, create_tool_calling_agent
    >>> from langchain_openai import ChatOpenAI
    >>> from langchain_core.prompts import ChatPromptTemplate
    >>> model = ChatOpenAI(model="gpt-4o")
    >>> prompt = ChatPromptTemplate.from_messages([
    ...     ("system", system_prompt),
    ...     ("human", "{input}"),
    ...     ("placeholder", "{agent_scratchpad}"),
    ... ])
    >>> agent = create_tool_calling_agent(model, tools, prompt)
    >>> agent_executor = AgentExecutor(agent=agent, tools=tools)
    >>> agent_executor.invoke({"input": "What was AAPL's revenue in 2023?"})
"""

import os

from langchain_community.agent_toolkits.financial_datasets.toolkit import (
    FinancialDatasetsToolkit,
)
from langchain_community.utilities.financial_datasets import FinancialDatasetsAPIWrapper
from langchain_core.tools import Tool
from pydantic import BaseModel, Field


class FinancialDatasetsConfig(BaseModel):
    """Configuration for Financial Datasets API access.

    This model manages the API keys and client configuration for accessing
    the Financial Datasets API.

    Attributes:
        api_key (Optional[str]): Financial Datasets API key. If not provided, will use
            the FINANCIAL_DATASETS_API_KEY environment variable.
    """

    api_key: str | None = Field(
        default=os.getenv("FINANCIAL_DATASETS_API_KEY"),
        description="Financial Datasets API key for accessing financial statement data",
    )

    def get_client(self) -> FinancialDatasetsAPIWrapper:
        """Initialize and return a Financial Datasets API client.

        Returns:
            FinancialDatasetsAPIWrapper: An initialized Financial Datasets API wrapper.

        Raises:
            ValueError: If no API key is available (neither provided nor in environment).
        """
        if not self.api_key:
            raise ValueError(
                "Financial Datasets API key is required. Set FINANCIAL_DATASETS_API_KEY environment variable or provide api_key parameter."
            )

        return FinancialDatasetsAPIWrapper(financial_datasets_api_key=self.api_key)


def get_financial_datasets_tools(
    config: FinancialDatasetsConfig | None = None,
) -> list[Tool]:
    """Create a list of Financial Datasets tools.

    This function creates a set of tools for accessing various financial data
    endpoints from the Financial Datasets API, including income statements,
    balance sheets, and cash flow statements.

    Args:
        config (Optional[FinancialDatasetsConfig]): Configuration with API key and settings.
            If not provided, will create a default config using environment variables.

    Returns:
        List[Tool]: A list of tools for interacting with Financial Datasets API.

    Raises:
        ValueError: If the API client cannot be initialized due to missing credentials.
    """
    if config is None:
        config = FinancialDatasetsConfig()

    api_wrapper = config.get_client()
    toolkit = FinancialDatasetsToolkit(api_wrapper=api_wrapper)
    return toolkit.get_tools()


# Create a default toolkit instance for easy importing
try:
    financial_datasets_toolkit = get_financial_datasets_tools()
except ValueError as e:
    import warnings

    warnings.warn(
        f"Financial Datasets toolkit initialization failed: {e}. Set FINANCIAL_DATASETS_API_KEY environment variable."
    )
    financial_datasets_toolkit = []

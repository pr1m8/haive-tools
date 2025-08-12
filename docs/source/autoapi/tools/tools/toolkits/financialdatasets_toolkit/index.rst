
:py:mod:`tools.tools.toolkits.financialdatasets_toolkit`
========================================================

.. py:module:: tools.tools.toolkits.financialdatasets_toolkit

Financial Datasets Toolkit Module.

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

.. rubric:: Examples

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


.. autolink-examples:: tools.tools.toolkits.financialdatasets_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.financialdatasets_toolkit.FinancialDatasetsConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FinancialDatasetsConfig:

   .. graphviz::
      :align: center

      digraph inheritance_FinancialDatasetsConfig {
        node [shape=record];
        "FinancialDatasetsConfig" [label="FinancialDatasetsConfig"];
        "pydantic.BaseModel" -> "FinancialDatasetsConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.financialdatasets_toolkit.FinancialDatasetsConfig
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   tools.tools.toolkits.financialdatasets_toolkit.get_financial_datasets_tools

.. py:function:: get_financial_datasets_tools(config: FinancialDatasetsConfig | None = None) -> list[langchain_core.tools.Tool]

   Create a list of Financial Datasets tools.

   This function creates a set of tools for accessing various financial data
   endpoints from the Financial Datasets API, including income statements,
   balance sheets, and cash flow statements.

   :param config: Configuration with API key and settings.
                  If not provided, will create a default config using environment variables.
   :type config: Optional[FinancialDatasetsConfig]

   :returns: A list of tools for interacting with Financial Datasets API.
   :rtype: List[Tool]

   :raises ValueError: If the API client cannot be initialized due to missing credentials.


   .. autolink-examples:: get_financial_datasets_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.financialdatasets_toolkit
   :collapse:
   
.. autolink-skip:: next

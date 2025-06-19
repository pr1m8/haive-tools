"""
PubMed research tool for medical and scientific literature.

This module provides integration with the PubMed database through the LangChain
tools interface. PubMed is a free search engine accessing primarily the MEDLINE
database of references and abstracts on life sciences and biomedical topics
maintained by the United States National Library of Medicine.

The module initializes the PubMed query tools, making them available for use
in agent workflows for retrieving scientific and medical research information.

Requires:
    - langchain_community package with PubMed integration
    - Internet access to query the PubMed API

Example:
    To use the PubMed tools in an agent:
    ```python
    from haive.tools.tools.pubmed import pubmed_tools

    # Add to your agent's toolkit
    agent = Agent(tools=pubmed_tools)

    # Example use in an agent
    response = agent.run("Find recent research on COVID-19 vaccines")
    ```

Note:
    - PubMed API has usage limits and rate restrictions
    - Results may be limited to avoid overwhelming responses
    - Queries should be specific to get the most relevant research papers
"""

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools.pubmed.tool import PubmedQueryRun

# Load PubMed tools from LangChain's available tools
pubmed_tools = load_tools(["pubmed"])

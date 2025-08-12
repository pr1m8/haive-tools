"""StackExchange toolkit for querying Stack Exchange sites including Stack Overflow.

This module provides tools for querying Stack Exchange sites, such as Stack Overflow,
to retrieve answers to programming and technical questions. The toolkit leverages
LangChain's StackExchangeAPIWrapper to interact with the Stack Exchange API.

To use this toolkit, you need to have a Stack Exchange API key set in your
environment variables as STACKEXCHANGE_API_KEY. You can obtain a key from
https://stackapps.com/apps/oauth/register.

Typical usage:
    from haive.tools.toolkits.stack_exchange_toolkit import stackexchange_tools

    # Use in an agent
    agent = Agent(tools=stackexchange_tools)
    agent.run("How do I parse JSON in Python?")

"""

from langchain.agents import load_tools
from langchain_core.tools import BaseTool


def get_stackexchange_tools() -> list[BaseTool]:
    """Get Stack Exchange tools for querying Stack Exchange sites.

    This function loads and returns tools for querying Stack Exchange sites,
    particularly Stack Overflow, to find answers to technical questions.

    Returns:
        A list of BaseTool instances for interacting with Stack Exchange,
        empty list if credentials are missing or other issues occur.

    """
    try:
        return load_tools(["stackexchange"])
    except Exception as e:
        # Return empty list if credentials are missing or other issues occur
        print(f"Warning: Stack Exchange tools unavailable: {e}")
        return []


# Export the tools for easy access
stackexchange_tools = get_stackexchange_tools()


:py:mod:`tools.tools.toolkits.stack_exchange_toolkit`
=====================================================

.. py:module:: tools.tools.toolkits.stack_exchange_toolkit

StackExchange toolkit for querying Stack Exchange sites including Stack Overflow.

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


.. autolink-examples:: tools.tools.toolkits.stack_exchange_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.stack_exchange_toolkit.get_stackexchange_tools

.. py:function:: get_stackexchange_tools() -> list[langchain_core.tools.BaseTool]

   Get Stack Exchange tools for querying Stack Exchange sites.

   This function loads and returns tools for querying Stack Exchange sites,
   particularly Stack Overflow, to find answers to technical questions.

   :returns: A list of BaseTool instances for interacting with Stack Exchange,
             empty list if credentials are missing or other issues occur.


   .. autolink-examples:: get_stackexchange_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.stack_exchange_toolkit
   :collapse:
   
.. autolink-skip:: next

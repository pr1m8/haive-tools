
:py:mod:`tools.tools.merriam_webster`
=====================================

.. py:module:: tools.tools.merriam_webster

Merriam-Webster dictionary API integration tools.

This module provides integration with Merriam-Webster's dictionary APIs through
the LangChain tools interface. It allows for querying word definitions, synonyms,
antonyms, examples, and other lexical information from Merriam-Webster's extensive
dictionary and thesaurus services.

The module requires a valid Merriam-Webster API key and configures the necessary
tools for looking up word information.

Requires:
    - Merriam-Webster API key set in environment variables
    - langchain_community package with Merriam-Webster integration
    - requests package

.. rubric:: Example

To use the Merriam-Webster dictionary tools in an agent:
```python
from haive.tools.tools.merriam_webster import merriam_webster_tools

# Add to your agent's toolkit
agent = Agent(tools=merriam_webster_tools)
```

.. note::

   - Merriam-Webster API requires registration for an API key
   - Usage is subject to Merriam-Webster's terms of service and rate limits
   - Documentation for the Merriam-Webster API is available at:
     https://dictionaryapi.com/products/api-collegiate-dictionary


.. autolink-examples:: tools.tools.merriam_webster
   :collapse:





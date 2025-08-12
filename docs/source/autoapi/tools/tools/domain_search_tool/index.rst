
:py:mod:`tools.tools.domain_search_tool`
========================================

.. py:module:: tools.tools.domain_search_tool

Domain search tool for querying registered domain names.

This module provides a tool for searching registered domain names based on keywords
using the domainsdb.info API. It allows users to find existing domains containing
specific keywords, which can be useful for domain availability research, brand protection,
or competitive analysis.

The tool returns a list of registered domain names matching the provided key,
limited to the top 10 results to avoid overwhelming responses.

.. rubric:: Example

```python
from haive.tools.tools.domain_search_tool import domain_search_tool

# Add to your agent's toolkit
agent = Agent(tools=[domain_search_tool])

# Example use in an agent
response = agent.run("Find domains related to 'python'")
```

.. note::

   - The domainsdb.info API has usage limits and may throttle requests
   - Results are limited to the top 10 matches to keep responses manageable
   - No authentication is required for basic lookups


.. autolink-examples:: tools.tools.domain_search_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.domain_search_tool.DomainSearchInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DomainSearchInput:

   .. graphviz::
      :align: center

      digraph inheritance_DomainSearchInput {
        node [shape=record];
        "DomainSearchInput" [label="DomainSearchInput"];
        "pydantic.BaseModel" -> "DomainSearchInput";
      }

.. autopydantic_model:: tools.tools.domain_search_tool.DomainSearchInput
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

   tools.tools.domain_search_tool.search_registered_domains

.. py:function:: search_registered_domains(domain: str) -> str

   Search for registered domain names using a key.

   Queries the domainsdb.info API to find registered domain names containing the
   specified key. Returns up to 10 matching domain names.

   :param domain: A key to search for in domain names.

   :returns:

             A newline-separated list of domain names matching the search criteria,
                  limited to 10 results, or an error message if the search fails or no
                  results are found.
   :rtype: str

   :raises requests.exceptions.RequestException: If the API request fails.


   .. autolink-examples:: search_registered_domains
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.domain_search_tool
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.toolkits.request_tools`
============================================

.. py:module:: tools.tools.toolkits.request_tools

HTTP request tools for interacting with web APIs.

This module provides tools for making HTTP requests to external APIs and services.
It leverages the LangChain Requests integration to provide a robust and secure way
to interact with web services.

The module includes tools for:
- Making GET requests to fetch data
- Making POST requests to submit data
- Making general HTTP requests with custom methods, headers, and payloads

For detailed documentation on the underlying implementation, see:
https://python.langchain.com/docs/integrations/tools/requests/

Typical usage::

    from haive.tools.toolkits.request_tools import requests_get, requests_post

    # Make a GET request
    response = requests_get.invoke({"url": "https://api.example.com/data"})

    # Make a POST request
    response = requests_post.invoke({
        "url": "https://api.example.com/submit",
        "data": {"key": "value"}
    })


.. autolink-examples:: tools.tools.toolkits.request_tools
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.request_tools.RequestsGetInput
   tools.tools.toolkits.request_tools.RequestsPostInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RequestsGetInput:

   .. graphviz::
      :align: center

      digraph inheritance_RequestsGetInput {
        node [shape=record];
        "RequestsGetInput" [label="RequestsGetInput"];
        "pydantic.BaseModel" -> "RequestsGetInput";
      }

.. autopydantic_model:: tools.tools.toolkits.request_tools.RequestsGetInput
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RequestsPostInput:

   .. graphviz::
      :align: center

      digraph inheritance_RequestsPostInput {
        node [shape=record];
        "RequestsPostInput" [label="RequestsPostInput"];
        "pydantic.BaseModel" -> "RequestsPostInput";
      }

.. autopydantic_model:: tools.tools.toolkits.request_tools.RequestsPostInput
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





.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.request_tools
   :collapse:
   
.. autolink-skip:: next

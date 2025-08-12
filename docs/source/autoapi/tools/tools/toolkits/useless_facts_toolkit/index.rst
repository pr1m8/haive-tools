
:py:mod:`tools.tools.toolkits.useless_facts_toolkit`
====================================================

.. py:module:: tools.tools.toolkits.useless_facts_toolkit

Useless Facts Toolkit Module.

This module provides a toolkit for retrieving random and daily useless facts.
It leverages the Useless Facts API (https://uselessfacts.jsph.pl/) to provide
fun, trivial information that can be used for entertainment purposes.

The module offers structured tools for:
1. Getting a random useless fact
2. Getting today's useless fact

Both tools support language selection (English or German) and are packaged as
LangChain-compatible structured tools for use in agent workflows.

.. rubric:: Example

>>> from haive.tools.toolkits.useless_facts_toolkit import useless_facts_toolkit
>>> random_fact_tool = useless_facts_toolkit[0]
>>> fact = random_fact_tool.invoke({"language": "en"})
>>> print(f"Random fact: {fact}")

.. note:: No API key is required for the Useless Facts API, though rate limits may apply.


.. autolink-examples:: tools.tools.toolkits.useless_facts_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.useless_facts_toolkit.FactInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FactInput:

   .. graphviz::
      :align: center

      digraph inheritance_FactInput {
        node [shape=record];
        "FactInput" [label="FactInput"];
        "pydantic.BaseModel" -> "FactInput";
      }

.. autopydantic_model:: tools.tools.toolkits.useless_facts_toolkit.FactInput
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

   tools.tools.toolkits.useless_facts_toolkit.get_random_fact
   tools.tools.toolkits.useless_facts_toolkit.get_todays_fact

.. py:function:: get_random_fact(language: str | None = 'en') -> str

   Retrieve a random useless fact from the API.

   :param language: Language code, either 'en' for English or 'de' for German

   :returns: A random useless fact in the specified language
   :rtype: str

   :raises requests.exceptions.HTTPError: If the API request fails


   .. autolink-examples:: get_random_fact
      :collapse:

.. py:function:: get_todays_fact(language: str | None = 'en') -> str

   Retrieve today's useless fact from the API.

   :param language: Language code, either 'en' for English or 'de' for German

   :returns: Today's useless fact in the specified language
   :rtype: str

   :raises requests.exceptions.HTTPError: If the API request fails


   .. autolink-examples:: get_todays_fact
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.useless_facts_toolkit
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.translate_tools`
=====================================

.. py:module:: tools.tools.translate_tools

Translation Tools Module.

This module provides a tool for translating text between languages using the
DeepL API. It creates a LangChain-compatible structured tool that can be
integrated into agents to perform high-quality translations between multiple
languages.

The module defines the DeepLTranslateTool class which implements a BaseTool
interface for integrating with LangChain's agent frameworks. It supports both
DeepL's free and pro API modes, and includes validation for language codes.

.. rubric:: Example

>>> from haive.tools.tools.translate_tools import DeepLTranslateTool
>>> translate_tool = DeepLTranslateTool(
>>>     target_lang="EN-US",
>>>     source_lang="FR",
>>>     api_key="your_deepl_api_key"
>>> )
>>> translation = translate_tool.run("Bonjour le monde")

.. note::

   Requires a DeepL API key, which can be obtained from https://www.deepl.com/pro#developer
   The API key should be available in your .env file or environment variables.


.. autolink-examples:: tools.tools.translate_tools
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.translate_tools.DeepLInput
   tools.tools.translate_tools.DeepLTranslateTool


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DeepLInput:

   .. graphviz::
      :align: center

      digraph inheritance_DeepLInput {
        node [shape=record];
        "DeepLInput" [label="DeepLInput"];
        "pydantic.BaseModel" -> "DeepLInput";
      }

.. autopydantic_model:: tools.tools.translate_tools.DeepLInput
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

   Inheritance diagram for DeepLTranslateTool:

   .. graphviz::
      :align: center

      digraph inheritance_DeepLTranslateTool {
        node [shape=record];
        "DeepLTranslateTool" [label="DeepLTranslateTool"];
        "langchain_core.tools.BaseTool" -> "DeepLTranslateTool";
      }

.. autoclass:: tools.tools.translate_tools.DeepLTranslateTool
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: tools.tools.translate_tools
   :collapse:
   
.. autolink-skip:: next

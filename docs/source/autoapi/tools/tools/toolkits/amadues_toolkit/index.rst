
:py:mod:`tools.tools.toolkits.amadues_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.amadues_toolkit


Classes
-------

.. autoapisummary::

   tools.tools.toolkits.amadues_toolkit.AmadeusToolkit
   tools.tools.toolkits.amadues_toolkit.AmadeusToolkitConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmadeusToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_AmadeusToolkit {
        node [shape=record];
        "AmadeusToolkit" [label="AmadeusToolkit"];
        "langchain_core.tools.BaseToolkit" -> "AmadeusToolkit";
      }

.. autoclass:: tools.tools.toolkits.amadues_toolkit.AmadeusToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmadeusToolkitConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AmadeusToolkitConfig {
        node [shape=record];
        "AmadeusToolkitConfig" [label="AmadeusToolkitConfig"];
        "pydantic.BaseModel" -> "AmadeusToolkitConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.amadues_toolkit.AmadeusToolkitConfig
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

   tools.tools.toolkits.amadues_toolkit.create_client
   tools.tools.toolkits.amadues_toolkit.create_llm
   tools.tools.toolkits.amadues_toolkit.from_config
   tools.tools.toolkits.amadues_toolkit.get_tools

.. py:function:: create_client(config: AmadeusToolkitConfig) -> amadeus.Client

   Create an Amadeus client from config.


   .. autolink-examples:: create_client
      :collapse:

.. py:function:: create_llm(config: AmadeusToolkitConfig) -> langchain_core.language_models.BaseLanguageModel | None

   Create an LLM from config.


   .. autolink-examples:: create_llm
      :collapse:

.. py:function:: from_config(config: AmadeusToolkitConfig) -> AmadeusToolkit

   Create an AmadeusToolkit from config.


   .. autolink-examples:: from_config
      :collapse:

.. py:function:: get_tools(toolkit: AmadeusToolkit) -> list[langchain_core.tools.BaseTool]

   Get tools from toolkit.


   .. autolink-examples:: get_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.amadues_toolkit
   :collapse:
   
.. autolink-skip:: next

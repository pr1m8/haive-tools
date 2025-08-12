
:py:mod:`tools.tools.toolkits.base`
===================================

.. py:module:: tools.tools.toolkits.base

Base module for all toolkit implementations.

This module defines common interfaces and functionality shared across all toolkits.
It provides abstract base classes and utility functions for creating consistent
toolkit implementations.

Toolkits are collections of related tools that can be used together to perform
complex tasks. For example, a database toolkit might include tools for querying,
inserting, updating, and deleting data.

Typical usage:
    from haive.tools.toolkits.base import BaseToolkit

    class MyCustomToolkit(BaseToolkit):
        # Implementation details...


.. autolink-examples:: tools.tools.toolkits.base
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.base.HaiveToolkit
   tools.tools.toolkits.base.HaiveToolkitConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HaiveToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_HaiveToolkit {
        node [shape=record];
        "HaiveToolkit" [label="HaiveToolkit"];
        "langchain_core.tools.BaseToolkit" -> "HaiveToolkit";
        "abc.ABC" -> "HaiveToolkit";
      }

.. autoclass:: tools.tools.toolkits.base.HaiveToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HaiveToolkitConfig:

   .. graphviz::
      :align: center

      digraph inheritance_HaiveToolkitConfig {
        node [shape=record];
        "HaiveToolkitConfig" [label="HaiveToolkitConfig"];
        "pydantic.BaseModel" -> "HaiveToolkitConfig";
      }

.. autopydantic_model:: tools.tools.toolkits.base.HaiveToolkitConfig
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

.. autolink-examples:: tools.tools.toolkits.base
   :collapse:
   
.. autolink-skip:: next


:py:mod:`import_consolidator`
=============================

.. py:module:: import_consolidator

Import Consolidator Module.

This module provides functionality to consolidate and deduplicate import statements
in Python files using LibCST. It identifies duplicate imports and merges them into
single, cleaner import statements.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.import_consolidator import clean_imports
>>> clean_imports("/path/to/file.py")


.. autolink-examples:: import_consolidator
   :collapse:

Classes
-------

.. autoapisummary::

   import_consolidator.ImportConsolidator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImportConsolidator:

   .. graphviz::
      :align: center

      digraph inheritance_ImportConsolidator {
        node [shape=record];
        "ImportConsolidator" [label="ImportConsolidator"];
        "libcst.CSTTransformer" -> "ImportConsolidator";
      }

.. autoclass:: import_consolidator.ImportConsolidator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   import_consolidator.clean_imports

.. py:function:: clean_imports(filepath: str)

   Merge duplicate imports in a Python file.

   Reads a Python file, identifies duplicate imports, consolidates them,
   and writes the updated code back to the file.

   :param filepath: Path to the Python file to process
   :type filepath: str

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from or writing to the file


   .. autolink-examples:: clean_imports
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: import_consolidator
   :collapse:
   
.. autolink-skip:: next

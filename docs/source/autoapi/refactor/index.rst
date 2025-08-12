
:py:mod:`refactor`
==================

.. py:module:: refactor

Refactoring Transformers Module.

This module provides transformers for refactoring Python code using LibCST.
It includes functionality to rename functions, classes, and variables
while preserving the code structure.

.. rubric:: Example

>>> import libcst as cst
>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.refactor import RenameTransformer
>>>
>>> # Read and parse source code
>>> with open("script.py", "f") as f:
>>>     tree = cst.parse_module(f.read())
>>>
>>> # Create a rename mapping
>>> rename_map = {"old_function": "new_function", "OldClass": "NewClass"}
>>>
>>> # Apply transformations
>>> modified_tree = tree.visit(RenameTransformer(rename_map))
>>>
>>> # Write updated code back to file
>>> with open("script.py", "w") as f:
>>>     f.write(modified_tree.code)


.. autolink-examples:: refactor
   :collapse:

Classes
-------

.. autoapisummary::

   refactor.RenameTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RenameTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_RenameTransformer {
        node [shape=record];
        "RenameTransformer" [label="RenameTransformer"];
        "libcst.CSTTransformer" -> "RenameTransformer";
      }

.. autoclass:: refactor.RenameTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: refactor
   :collapse:
   
.. autolink-skip:: next

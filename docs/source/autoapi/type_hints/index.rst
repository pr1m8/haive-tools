
:py:mod:`type_hints`
====================

.. py:module:: type_hints

Type Hints Transformer Module.

This module provides functionality to add type hints to function parameters and
return types in Python code using LibCST. It allows for automated type annotation
of existing code to improve type safety and code documentation.

.. rubric:: Example

>>> import libcst as cst
>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.type_hints import TypeHintTransformer
>>>
>>> # Read and parse source code
>>> with open("script.py", "f") as f:
>>>     tree = cst.parse_module(f.read())
>>>
>>> # Define type mapping
>>> type_map = {
>>>     "name": "str",
>>>     "age": "int",
>>>     "return": "bool"
>>> }
>>>
>>> # Apply type hints
>>> modified_tree = tree.visit(TypeHintTransformer(type_map))
>>>
>>> # Write updated code back to file
>>> with open("script.py", "w") as f:
>>>     f.write(modified_tree.code)


.. autolink-examples:: type_hints
   :collapse:

Classes
-------

.. autoapisummary::

   type_hints.TypeHintTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TypeHintTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_TypeHintTransformer {
        node [shape=record];
        "TypeHintTransformer" [label="TypeHintTransformer"];
        "libcst.CSTTransformer" -> "TypeHintTransformer";
      }

.. autoclass:: type_hints.TypeHintTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: type_hints
   :collapse:
   
.. autolink-skip:: next

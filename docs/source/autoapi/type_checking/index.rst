
:py:mod:`type_checking`
=======================

.. py:module:: type_checking

Type Checking Visitor Module.

This module provides functionality to analyze Python code for type annotation issues
using LibCST. It identifies functions missing type hints and incorrect return type
annotations, helping to improve type safety in codebases.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.type_checking import check_types
>>> check_types("/path/to/file.py")
⚠️ Functions missing type hints: ['process_data', 'calculate_total']
❌ Incorrect return type in `format_result`: Expected str, got int


.. autolink-examples:: type_checking
   :collapse:

Classes
-------

.. autoapisummary::

   type_checking.TypeChecker


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TypeChecker:

   .. graphviz::
      :align: center

      digraph inheritance_TypeChecker {
        node [shape=record];
        "TypeChecker" [label="TypeChecker"];
        "libcst.CSTVisitor" -> "TypeChecker";
      }

.. autoclass:: type_checking.TypeChecker
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   type_checking.check_types

.. py:function:: check_types(filepath: str) -> None

   Check a Python file for type annotation issues.

   This function analyzes a Python file to identify functions missing type annotations
   and functions with incorrect return type annotations, and prints a report of the issues.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: check_types
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: type_checking
   :collapse:
   
.. autolink-skip:: next

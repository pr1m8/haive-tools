
:py:mod:`function_call_analyzer`
================================

.. py:module:: function_call_analyzer

Function Call Analyzer Module.

This module provides functionality to analyze function definitions and calls
in Python code using LibCST. It helps identify unused functions and analyze
function call patterns in a codebase.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.function_call_analyzer import analyze_function_calls
>>> analyze_function_calls("/path/to/file.py")
Unused Functions: ['initialize_config', 'cleanup_resources']


.. autolink-examples:: function_call_analyzer
   :collapse:

Classes
-------

.. autoapisummary::

   function_call_analyzer.FunctionCallAnalyzer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FunctionCallAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_FunctionCallAnalyzer {
        node [shape=record];
        "FunctionCallAnalyzer" [label="FunctionCallAnalyzer"];
        "libcst.CSTVisitor" -> "FunctionCallAnalyzer";
      }

.. autoclass:: function_call_analyzer.FunctionCallAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   function_call_analyzer.analyze_function_calls

.. py:function:: analyze_function_calls(filepath: str) -> dict[str, list[str]]

   Analyze function definitions and calls in a Python file.

   This function parses a Python file, analyzes function definitions and calls,
   and reports various metrics including unused functions.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :returns: Dictionary with analysis results, including 'unused_functions'
   :rtype: Dict[str, List[str]]

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: analyze_function_calls
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: function_call_analyzer
   :collapse:
   
.. autolink-skip:: next

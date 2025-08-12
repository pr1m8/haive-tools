
:py:mod:`code_smell_detector`
=============================

.. py:module:: code_smell_detector

Code Smell Detector Module.

This module provides functionality to detect code smells and bad practices
in Python code using LibCST. It identifies potential issues such as deeply
nested loops that can make code harder to understand and maintain.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.code_smell_detector import detect_code_smells
>>> detect_code_smells("/path/to/file.py")
⚠️ Deeply nested loop detected at line 42


.. autolink-examples:: code_smell_detector
   :collapse:

Classes
-------

.. autoapisummary::

   code_smell_detector.CodeSmellDetector


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CodeSmellDetector:

   .. graphviz::
      :align: center

      digraph inheritance_CodeSmellDetector {
        node [shape=record];
        "CodeSmellDetector" [label="CodeSmellDetector"];
        "libcst.CSTVisitor" -> "CodeSmellDetector";
      }

.. autoclass:: code_smell_detector.CodeSmellDetector
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   code_smell_detector.detect_code_smells

.. py:function:: detect_code_smells(filepath: str) -> list[dict]

   Detect code smells in a Python file.

   This function analyzes a Python file to identify potential code smells
   and bad practices that could impact code quality and maintainability.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :returns: List of detected code smells with details
   :rtype: List[Dict]

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: detect_code_smells
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: code_smell_detector
   :collapse:
   
.. autolink-skip:: next

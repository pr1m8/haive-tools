
:py:mod:`complexity_analyzer`
=============================

.. py:module:: complexity_analyzer

Complexity Analyzer Module.

This module provides a LibCST visitor that analyzes the cyclomatic complexity
of functions in Python code. Cyclomatic complexity is a quantitative measure of
the number of linearly independent paths through a program's source code, which
can help identify functions that may be overly complex and difficult to maintain.

The analyzer tracks complexity by counting decision points (if statements, loops, etc.)
within each function and provides a report with complexity scores, which can be used
to identify functions that might benefit from refactoring.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.complexity_analyzer import analyze_complexity
>>> analyze_complexity("path/to/your_script.py")
🔍 function_name complexity score: 5


.. autolink-examples:: complexity_analyzer
   :collapse:

Classes
-------

.. autoapisummary::

   complexity_analyzer.ComplexityAnalyzer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ComplexityAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_ComplexityAnalyzer {
        node [shape=record];
        "ComplexityAnalyzer" [label="ComplexityAnalyzer"];
        "libcst.CSTVisitor" -> "ComplexityAnalyzer";
      }

.. autoclass:: complexity_analyzer.ComplexityAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   complexity_analyzer.analyze_complexity

.. py:function:: analyze_complexity(filepath: str, threshold: int | None = None) -> dict[str, int]

   Analyze the cyclomatic complexity of functions in a Python file.

   :param filepath: Path to the Python file to analyze.
   :param threshold: Optional complexity threshold for reporting high-complexity functions.
                     If provided, only functions exceeding this threshold will be reported.

   :returns: Dictionary mapping function names to complexity scores.

   :raises FileNotFoundError: If the specified file does not exist.
   :raises SyntaxError: If the file contains invalid Python syntax.


   .. autolink-examples:: analyze_complexity
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: complexity_analyzer
   :collapse:
   
.. autolink-skip:: next


:py:mod:`import_analyzer`
=========================

.. py:module:: import_analyzer

Import Analyzer Module.

This module provides functionality to analyze import statements in Python code
using LibCST. It helps identify unused imports, import conflicts, and other import-related
issues that can affect code quality and maintainability.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.import_analyzer import analyze_imports
>>> analyze_imports("/path/to/file.py")
📌 **Import Analysis Report**
✅ Used Imports: {'os', 'sys', 'pandas'}
🛑 Unused Imports: {'numpy', 'matplotlib'}
⚠️ Conflict: DataFrame is imported from multiple sources: {'pandas', 'pyspark.sql'}


.. autolink-examples:: import_analyzer
   :collapse:

Classes
-------

.. autoapisummary::

   import_analyzer.ImportAnalyzer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImportAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_ImportAnalyzer {
        node [shape=record];
        "ImportAnalyzer" [label="ImportAnalyzer"];
        "libcst.CSTVisitor" -> "ImportAnalyzer";
      }

.. autoclass:: import_analyzer.ImportAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   import_analyzer.analyze_imports

.. py:function:: analyze_imports(filepath: str) -> dict[str, list]

   Analyze import statements in a Python file.

   This function parses a Python file and analyzes its import statements to identify
   unused imports, import conflicts, and other import-related issues.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :returns:

             Dictionary containing analysis results, including
                 'unused_imports', 'import_conflicts', and 'all_imports'
   :rtype: Dict[str, List]

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: analyze_imports
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: import_analyzer
   :collapse:
   
.. autolink-skip:: next

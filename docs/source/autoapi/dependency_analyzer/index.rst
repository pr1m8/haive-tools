
:py:mod:`dependency_analyzer`
=============================

.. py:module:: dependency_analyzer

Dependency Analyzer Module.

This module provides functionality to analyze import statements and track
dependencies between modules in Python projects using LibCST. It helps identify
the external libraries and internal modules that a Python file depends on.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.dependency_analyzer import analyze_dependencies
>>> analyze_dependencies("/path/to/file.py")
Dependencies in /path/to/file.py: {'os', 'sys', 'pandas', 'numpy', 'myproject.utils'}


.. autolink-examples:: dependency_analyzer
   :collapse:

Classes
-------

.. autoapisummary::

   dependency_analyzer.DependencyAnalyzer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DependencyAnalyzer:

   .. graphviz::
      :align: center

      digraph inheritance_DependencyAnalyzer {
        node [shape=record];
        "DependencyAnalyzer" [label="DependencyAnalyzer"];
        "libcst.CSTVisitor" -> "DependencyAnalyzer";
      }

.. autoclass:: dependency_analyzer.DependencyAnalyzer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   dependency_analyzer.analyze_dependencies

.. py:function:: analyze_dependencies(filepath: str) -> set[str]

   Analyze import dependencies in a Python file.

   This function parses a Python file and identifies all the modules it imports,
   returning a set of dependency module names.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :returns: Set of module names imported in the file
   :rtype: Set[str]

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: analyze_dependencies
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: dependency_analyzer
   :collapse:
   
.. autolink-skip:: next

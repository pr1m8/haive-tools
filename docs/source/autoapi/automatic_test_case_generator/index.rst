
:py:mod:`automatic_test_case_generator`
=======================================

.. py:module:: automatic_test_case_generator

Automatic Test Case Generator Module.

This module provides functionality to automatically generate test case templates
for Python functions using LibCST. It analyzes function definitions and generates
test function skeletons that can be used as starting points for unit tests.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.automatic_test_case_generator import generate_tests
>>> generate_tests("/path/to/file.py")
def test_calculate_total():
    # TODO: Add assertions
    assert calculate_total(amount, tax_rate) is not None

def test_format_currency():
    # TODO: Add assertions
    assert format_currency(value, currency_symbol) is not None


.. autolink-examples:: automatic_test_case_generator
   :collapse:

Classes
-------

.. autoapisummary::

   automatic_test_case_generator.TestGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TestGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_TestGenerator {
        node [shape=record];
        "TestGenerator" [label="TestGenerator"];
        "libcst.CSTVisitor" -> "TestGenerator";
      }

.. autoclass:: automatic_test_case_generator.TestGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   automatic_test_case_generator.generate_tests

.. py:function:: generate_tests(filepath: str) -> str

   Generate test case templates for functions in a Python file.

   This function analyzes a Python file, identifies all function definitions,
   and generates test function templates that can be used as starting points
   for unit tests.

   :param filepath: Path to the Python file to analyze
   :type filepath: str

   :returns: String containing all generated test function templates
   :rtype: str

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from the file


   .. autolink-examples:: generate_tests
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: automatic_test_case_generator
   :collapse:
   
.. autolink-skip:: next

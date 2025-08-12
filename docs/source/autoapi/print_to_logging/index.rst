
:py:mod:`print_to_logging`
==========================

.. py:module:: print_to_logging

Print to Logging Transformer Module.

This module provides functionality to convert print statements to logging calls
in Python files using LibCST. It automatically transforms print() calls to
logging.info() calls for better production-ready code.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.print_to_logging import replace_print_with_logging
>>> replace_print_with_logging("/path/to/file.py")

Before:
    print("Hello, world!")

After:
    logging.info("Hello, world!")


.. autolink-examples:: print_to_logging
   :collapse:

Classes
-------

.. autoapisummary::

   print_to_logging.PrintToLoggingTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PrintToLoggingTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_PrintToLoggingTransformer {
        node [shape=record];
        "PrintToLoggingTransformer" [label="PrintToLoggingTransformer"];
        "libcst.CSTTransformer" -> "PrintToLoggingTransformer";
      }

.. autoclass:: print_to_logging.PrintToLoggingTransformer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   print_to_logging.replace_print_with_logging

.. py:function:: replace_print_with_logging(filepath: str)

   Replaces all print() calls with logging.info() calls in a Python file.

   This function reads a Python file, converts all print() function calls to
   logging.info() calls, and writes the updated code back to the file. It does not
   automatically add the import statement for the logging module.

   :param filepath: Path to the Python file to process
   :type filepath: str

   :raises FileNotFoundError: If the specified file does not exist
   :raises IOError: If there are issues reading from or writing to the file


   .. autolink-examples:: replace_print_with_logging
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: print_to_logging
   :collapse:
   
.. autolink-skip:: next

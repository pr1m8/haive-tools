
:py:mod:`function_logging_transformer`
======================================

.. py:module:: function_logging_transformer

Function Logging Transformer Module.

This module provides a LibCST transformer that automatically adds logging statements
to functions in Python code. It can be used to instrument code for debugging,
performance monitoring, or audit trail generation without manually modifying
every function.

The transformer injects a print statement at the beginning of each function body
that logs the function name when it is executed, making it easy to trace function
calls during program execution.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.function_logging_transformer import add_logging
>>> add_logging("path/to/your_script.py")
# This will modify the file, adding logging to all functions


.. autolink-examples:: function_logging_transformer
   :collapse:

Classes
-------

.. autoapisummary::

   function_logging_transformer.FunctionLoggingTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FunctionLoggingTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_FunctionLoggingTransformer {
        node [shape=record];
        "FunctionLoggingTransformer" [label="FunctionLoggingTransformer"];
        "libcst.CSTTransformer" -> "FunctionLoggingTransformer";
      }

.. autoclass:: function_logging_transformer.FunctionLoggingTransformer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   function_logging_transformer.add_logging

.. py:function:: add_logging(filepath: str, log_format: str = 'Executing {name}', exclude_methods: list[str] | None = None) -> None

   Inject logging into functions in a Python file.

   This function parses a Python file, adds logging statements to the beginning of
   each function definition, and writes the modified code back to the file.

   :param filepath: Path to the Python file to modify.
   :param log_format: Format string for the log message, with {name} as placeholder.
   :param exclude_methods: List of method names to exclude from logging.

   :raises FileNotFoundError: If the specified file does not exist.
   :raises PermissionError: If the file cannot be read or written.
   :raises SyntaxError: If the file contains invalid Python syntax.


   .. autolink-examples:: add_logging
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: function_logging_transformer
   :collapse:
   
.. autolink-skip:: next

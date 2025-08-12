
:py:mod:`multi_file_rename`
===========================

.. py:module:: multi_file_rename

Multi-File Rename Module.

This module provides functionality to rename functions across multiple Python files
using LibCST. It identifies both function definitions and function calls and renames
them to maintain consistency throughout a codebase.

.. rubric:: Example

>>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.multi_file_rename import rename_function_in_files
>>> rename_function_in_files("/path/to/directory", "old_function_name", "new_function_name")


.. autolink-examples:: multi_file_rename
   :collapse:

Classes
-------

.. autoapisummary::

   multi_file_rename.MultiFileRenameTransformer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiFileRenameTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_MultiFileRenameTransformer {
        node [shape=record];
        "MultiFileRenameTransformer" [label="MultiFileRenameTransformer"];
        "libcst.CSTTransformer" -> "MultiFileRenameTransformer";
      }

.. autoclass:: multi_file_rename.MultiFileRenameTransformer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   multi_file_rename.rename_function_in_files

.. py:function:: rename_function_in_files(directory: str, old_name: str, new_name: str)

   Renames a function across all `.py` files in a directory recursively.

   This function walks through all Python files in a directory and its subdirectories,
   renames both function definitions and function calls, and writes the updated code
   back to the files.

   :param directory: Path to the directory containing Python files
   :type directory: str
   :param old_name: Current name of the function to rename
   :type old_name: str
   :param new_name: New name to give the function
   :type new_name: str

   :raises FileNotFoundError: If the specified directory does not exist
   :raises IOError: If there are issues reading from or writing to the files


   .. autolink-examples:: rename_function_in_files
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: multi_file_rename
   :collapse:
   
.. autolink-skip:: next

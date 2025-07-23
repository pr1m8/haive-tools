"""Multi-File Rename Module

This module provides functionality to rename functions across multiple Python files
using LibCST. It identifies both function definitions and function calls and renames
them to maintain consistency throughout a codebase.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.multi_file_rename import rename_function_in_files
    >>> rename_function_in_files("/path/to/directory", "old_function_name", "new_function_name")
"""

import os

import libcst as cst
from libcst import Call, MetadataWrapper, Name


class MultiFileRenameTransformer(cst.CSTTransformer):
    """Renames a function across multiple files.

    This transformer identifies and renames both function definitions and
    function calls to maintain consistency throughout a codebase.

    Attributes:
        old_name (str): The current name of the function to rename
        new_name (str): The new name to give the function
    """

    def __init__(self, old_name: str, new_name: str):
        """Initialize the multi-file rename transformer.

        Args:
            old_name (str): The current name of the function to rename
            new_name (str): The new name to give the function
        """
        self.old_name = old_name
        self.new_name = new_name

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ):
        """Rename function definitions during the AST traversal.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The function definition with the updated name if it matches
                the target function, otherwise the original node
        """
        if original_node.name.value == self.old_name:
            return updated_node.with_changes(name=cst.Name(value=self.new_name))
        return updated_node

    def leave_Call(self, original_node: Call, updated_node: Call):
        """Rename function calls during the AST traversal.

        Args:
            original_node (cst.Call): The original function call node
            updated_node (cst.Call): The updated function call node

        Returns:
            cst.Call: The function call with the updated name if it matches
                the target function, otherwise the original node
        """
        if (
            isinstance(original_node.func, Name)
            and original_node.func.value == self.old_name
        ):
            return updated_node.with_changes(func=cst.Name(value=self.new_name))
        return updated_node


def rename_function_in_files(directory: str, old_name: str, new_name: str):
    """Renames a function across all `.py` files in a directory recursively.

    This function walks through all Python files in a directory and its subdirectories,
    renames both function definitions and function calls, and writes the updated code
    back to the files.

    Args:
        directory (str): Path to the directory containing Python files
        old_name (str): Current name of the function to rename
        new_name (str): New name to give the function

    Raises:
        FileNotFoundError: If the specified directory does not exist
        IOError: If there are issues reading from or writing to the files
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path) as f:
                    tree = cst.parse_module(f.read())

                wrapper = MetadataWrapper(tree)
                modified_tree = wrapper.visit(
                    MultiFileRenameTransformer(old_name, new_name)
                )

                with open(path, "w") as f:
                    f.write(modified_tree.code)


# Example usage:
# rename_function_in_files("src/", "old_func", "new_func")  # ✅ Rename function globally

"""
Refactoring Transformers Module

This module provides transformers for refactoring Python code using LibCST.
It includes functionality to rename functions, classes, and variables
while preserving the code structure.

Example:
    >>> import libcst as cst
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.refactor import RenameTransformer
    >>>
    >>> # Read and parse source code
    >>> with open("script.py", "r") as f:
    >>>     tree = cst.parse_module(f.read())
    >>>
    >>> # Create a rename mapping
    >>> rename_map = {"old_function": "new_function", "OldClass": "NewClass"}
    >>>
    >>> # Apply transformations
    >>> modified_tree = tree.visit(RenameTransformer(rename_map))
    >>>
    >>> # Write updated code back to file
    >>> with open("script.py", "w") as f:
    >>>     f.write(modified_tree.code)
"""

import libcst as cst


class RenameTransformer(cst.CSTTransformer):
    """
    Renames functions, classes, and variables in Python code.

    This transformer finds and renames identifiers throughout the code
    based on a provided mapping, maintaining the structure and semantics
    of the original code.

    Attributes:
        rename_map (dict): A dictionary mapping old names to new names
    """

    def __init__(self, rename_map):
        """
        Initialize the rename transformer with a mapping of names.

        Args:
            rename_map (dict): A dictionary mapping old names to new names
                in the format {old_name: new_name}
        """
        super().__init__()
        self.rename_map = rename_map  # {old_name: new_name}

    def leave_FunctionDef(self, original_node, updated_node):
        """
        Rename function definitions during the AST traversal.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The function definition with the updated name if it's in
                the rename map, otherwise the original node
        """
        if original_node.name.value in self.rename_map:
            return updated_node.with_changes(
                name=cst.Name(self.rename_map[original_node.name.value])
            )
        return updated_node

    def leave_ClassDef(self, original_node, updated_node):
        """
        Rename class definitions during the AST traversal.

        Args:
            original_node (cst.ClassDef): The original class definition node
            updated_node (cst.ClassDef): The updated class definition node

        Returns:
            cst.ClassDef: The class definition with the updated name if it's in
                the rename map, otherwise the original node
        """
        if original_node.name.value in self.rename_map:
            return updated_node.with_changes(
                name=cst.Name(self.rename_map[original_node.name.value])
            )
        return updated_node

    def leave_Name(self, original_node, updated_node):
        """
        Rename variable and reference names during the AST traversal.

        Args:
            original_node (cst.Name): The original name node
            updated_node (cst.Name): The updated name node

        Returns:
            cst.Name: The name node with the updated value if it's in
                the rename map, otherwise the original node
        """
        if original_node.value in self.rename_map:
            return updated_node.with_changes(value=self.rename_map[original_node.value])
        return updated_node

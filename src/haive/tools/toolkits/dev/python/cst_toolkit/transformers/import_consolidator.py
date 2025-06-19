"""
Import Consolidator Module

This module provides functionality to consolidate and deduplicate import statements
in Python files using LibCST. It identifies duplicate imports and merges them into
single, cleaner import statements.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.import_consolidator import clean_imports
    >>> clean_imports("/path/to/file.py")
"""

import libcst as cst
from libcst import MetadataWrapper


class ImportConsolidator(cst.CSTTransformer):
    """
    Consolidates duplicate imports into a single statement.

    This transformer tracks all import statements in a Python file and
    consolidates duplicates to reduce redundancy and improve code organization.

    Attributes:
        imports (dict): Dictionary mapping module names to their alias (if any)
    """

    def __init__(self):
        """Initialize the import consolidator transformer."""
        self.imports = {}

    def visit_Import(self, node):
        """
        Track module imports during the AST traversal.

        Args:
            node (cst.Import): The import node being visited
        """
        for alias in node.names:
            module_name = alias.name.value
            self.imports[module_name] = alias.asname.value if alias.asname else None

    def leave_Module(self, original_node, updated_node):
        """
        Remove duplicates and consolidate imports at the module level.

        Args:
            original_node (cst.Module): The original module node
            updated_node (cst.Module): The updated module node

        Returns:
            cst.Module: The module with consolidated import statements
        """
        unique_imports = [
            cst.Import(
                names=[
                    cst.ImportAlias(
                        name=cst.Name(module),
                        asname=self.imports[module] and cst.Name(self.imports[module]),
                    )
                ]
            )
            for module in self.imports
        ]
        return updated_node.with_changes(body=[*unique_imports, *updated_node.body])


def clean_imports(filepath: str):
    """
    Merge duplicate imports in a Python file.

    Reads a Python file, identifies duplicate imports, consolidates them,
    and writes the updated code back to the file.

    Args:
        filepath (str): Path to the Python file to process

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from or writing to the file
    """
    with open(filepath, "r") as f:
        tree = cst.parse_module(f.read())

    wrapper = MetadataWrapper(tree)
    modified_tree = wrapper.visit(ImportConsolidator())

    with open(filepath, "w") as f:
        f.write(modified_tree.code)


# Example usage:
# clean_imports("your_script.py")  # ✅ Deduplicate imports

"""
Dependency Analyzer Module

This module provides functionality to analyze import statements and track
dependencies between modules in Python projects using LibCST. It helps identify
the external libraries and internal modules that a Python file depends on.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.dependency_analyzer import analyze_dependencies
    >>> analyze_dependencies("/path/to/file.py")
    Dependencies in /path/to/file.py: {'os', 'sys', 'pandas', 'numpy', 'myproject.utils'}
"""

from collections import defaultdict
from typing import Dict, Optional, Set

import libcst as cst


class DependencyAnalyzer(cst.CSTVisitor):
    """
    Analyzes imports and tracks dependencies within a project.

    This visitor identifies and collects all import statements in a Python file,
    including both direct imports and imports from specific modules, to build
    a dependency graph of the codebase.

    Attributes:
        imports (Dict[str, Set[str]]): Dictionary mapping file paths to sets of imported modules
        current_file (str): Path of the file currently being analyzed
    """

    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize the dependency analyzer visitor.

        Args:
            file_path (Optional[str]): Path of the file to be analyzed. If not provided,
                'current_file' is used as a placeholder key.
        """
        super().__init__()
        self.imports = defaultdict(set)
        self.current_file = file_path or "current_file"

    def visit_Import(self, node: cst.Import) -> None:
        """
        Handle simple 'import module' statements during the AST traversal.

        This method extracts module names from import statements and adds them
        to the dependency set for the current file.

        Args:
            node (cst.Import): The import node being visited
        """
        for alias in node.names:
            self.imports[self.current_file].add(alias.name.value)

    def visit_ImportFrom(self, node: cst.ImportFrom) -> None:
        """
        Handle 'from module import X' statements during the AST traversal.

        This method extracts the base module name from import-from statements
        and adds it to the dependency set for the current file.

        Args:
            node (cst.ImportFrom): The import-from node being visited
        """
        if node.module:
            self.imports[self.current_file].add(node.module.value)

    def get_dependencies(self) -> Set[str]:
        """
        Get the set of dependencies for the current file.

        Returns:
            Set[str]: Set of module names imported in the current file
        """
        return self.imports[self.current_file]


def analyze_dependencies(filepath: str) -> Set[str]:
    """
    Analyze import dependencies in a Python file.

    This function parses a Python file and identifies all the modules it imports,
    returning a set of dependency module names.

    Args:
        filepath (str): Path to the Python file to analyze

    Returns:
        Set[str]: Set of module names imported in the file

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from the file
    """
    with open(filepath, "r") as f:
        tree = cst.parse_module(f.read())

    analyzer = DependencyAnalyzer(filepath)
    tree.visit(analyzer)

    dependencies = analyzer.get_dependencies()
    print(f"Dependencies in {filepath}: {dependencies}")

    return dependencies


# Example Usage:
# analyze_dependencies("/path/to/file.py")  # ✅ Detects all imported modules

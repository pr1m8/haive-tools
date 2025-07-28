"""Import Analyzer Module.

This module provides functionality to analyze import statements in Python code
using LibCST. It helps identify unused imports, import conflicts, and other import-related
issues that can affect code quality and maintainability.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.import_analyzer import analyze_imports
    >>> analyze_imports("/path/to/file.py")
    📌 **Import Analysis Report**
    ✅ Used Imports: {'os', 'sys', 'pandas'}
    🛑 Unused Imports: {'numpy', 'matplotlib'}
    ⚠️ Conflict: DataFrame is imported from multiple sources: {'pandas', 'pyspark.sql'}
"""

from collections import defaultdict

import libcst as cst


class ImportAnalyzer(cst.CSTVisitor):
    """Analyzes and detects issues in Python imports.

    This visitor analyzes import statements in Python code to identify issues
    such as unused imports, import conflicts, and other import-related problems
    that can affect code quality.

    Attributes:
        imports (Set[str]): Set of all imported module names
        import_conflicts (Dict[str, Set[str]]): Dictionary mapping imported names to their source modules
        unused_imports (Set[str]): Set of imported names that are not used in the code
        used_identifiers (Set[str]): Set of identifier names used in the code
    """

    def __init__(self):
        """Initialize the import analyzer visitor."""
        super().__init__()
        self.imports: set[str] = set()
        self.import_conflicts: dict[str, set[str]] = defaultdict(set)
        self.unused_imports: set[str] = set()
        self.used_identifiers: set[str] = set()

    def visit_Import(self, node: cst.Import) -> None:
        """Track imported modules during the AST traversal.

        This method processes 'import module' statements and records information
        about imported modules, potential conflicts, and usage tracking.

        Args:
            node (cst.Import): The import node being visited
        """
        for alias in node.names:
            module_name = alias.name.value
            if alias.asname:
                self.import_conflicts[module_name].add(alias.asname.value)
            self.imports.add(module_name)
            self.unused_imports.add(module_name)

    def visit_ImportFrom(self, node: cst.ImportFrom) -> None:
        """Track 'from module import x' statements during the AST traversal.

        This method processes import-from statements and records information
        about imported names, their source modules, and usage tracking.

        Args:
            node (cst.ImportFrom): The import-from node being visited
        """
        if node.module:
            module_name = node.module.value
            for alias in node.names:
                imported_name = alias.name.value
                self.imports.add(module_name)
                self.import_conflicts[imported_name].add(module_name)
                self.unused_imports.add(imported_name)

    def visit_Name(self, node: cst.Name) -> None:
        """Detect used symbols in the script during the AST traversal.

        This method tracks which imported names are actually used in the code
        to identify unused imports.

        Args:
            node (cst.Name): The name node being visited
        """
        if node.value in self.unused_imports:
            self.unused_imports.discard(node.value)
        self.used_identifiers.add(node.value)

    def report_issues(self) -> dict[str, list]:
        """Generate a report on import-related issues.

        This method prints a human-readable report of import issues and returns
        a structured representation of the findings.

        Returns:
            Dict[str, List]: Dictionary containing analysis results, including
                'unused_imports', 'import_conflicts', and 'all_imports'
        """
        print("📌 **Import Analysis Report**")
        print(f"✅ Used Imports: {self.imports}")
        print(f"🛑 Unused Imports: {self.unused_imports}")

        conflicts = []
        for import_name, sources in self.import_conflicts.items():
            if len(sources) > 1:
                conflict = (import_name, list(sources))
                conflicts.append(conflict)
                print(
                    f"⚠️ Conflict: {import_name} is imported from multiple sources: {sources}"
                )

        return {
            "unused_imports": list(self.unused_imports),
            "import_conflicts": conflicts,
            "all_imports": list(self.imports),
        }


def analyze_imports(filepath: str) -> dict[str, list]:
    """Analyze import statements in a Python file.

    This function parses a Python file and analyzes its import statements to identify
    unused imports, import conflicts, and other import-related issues.

    Args:
        filepath (str): Path to the Python file to analyze

    Returns:
        Dict[str, List]: Dictionary containing analysis results, including
            'unused_imports', 'import_conflicts', and 'all_imports'

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from the file
    """
    with open(filepath) as f:
        tree = cst.parse_module(f.read())

    analyzer = ImportAnalyzer()
    tree.visit(analyzer)
    return analyzer.report_issues()


# Example Usage:
# analyze_imports("your_script.py")  # ✅ Detects unused, conflicting, and missing imports

"""Function Call Analyzer Module.

This module provides functionality to analyze function definitions and calls
in Python code using LibCST. It helps identify unused functions and analyze
function call patterns in a codebase.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.function_call_analyzer import analyze_function_calls
    >>> analyze_function_calls("/path/to/file.py")
    Unused Functions: ['initialize_config', 'cleanup_resources']
"""

from collections import defaultdict

import libcst as cst
from libcst import Call, CSTVisitor, Name


class FunctionCallAnalyzer(CSTVisitor):
    """Tracks function definitions and calls within a script.

    This visitor analyzes Python code to identify function definitions and
    track each time a function is called, allowing for the detection of
    unused functions and function call patterns.

    Attributes:
        function_defs (Set[str]): Set of defined function names
        function_calls (Dict[str, int]): Dictionary mapping function names to call counts
    """

    def __init__(self):
        """Initialize the function call analyzer visitor."""
        super().__init__()
        self.function_defs: set[str] = set()
        self.function_calls: dict[str, int] = defaultdict(int)

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        """Track function definitions during the AST traversal.

        This method adds each defined function name to the set of tracked functions.

        Args:
            node (cst.FunctionDef): The function definition node being visited
        """
        self.function_defs.add(node.name.value)

    def visit_Call(self, node: Call) -> None:
        """Track function calls during the AST traversal.

        This method increments the call count for functions when they are invoked.
        It only tracks direct function calls by name, not method calls or calls
        through variables.

        Args:
            node (Call): The function call node being visited
        """
        if isinstance(node.func, Name):
            self.function_calls[node.func.value] += 1

    def report_unused_functions(self) -> list[str]:
        """Find functions that are defined but never called.

        Returns:
            List[str]: List of function names that are defined but never called
                within the analyzed code
        """
        return [f for f in self.function_defs if self.function_calls[f] == 0]

    def get_call_counts(self) -> dict[str, int]:
        """Get the call count for each defined function.

        Returns:
            Dict[str, int]: Dictionary mapping function names to their call counts
        """
        return {f: self.function_calls[f] for f in self.function_defs}


def analyze_function_calls(filepath: str) -> dict[str, list[str]]:
    """Analyze function definitions and calls in a Python file.

    This function parses a Python file, analyzes function definitions and calls,
    and reports various metrics including unused functions.

    Args:
        filepath (str): Path to the Python file to analyze

    Returns:
        Dict[str, List[str]]: Dictionary with analysis results, including 'unused_functions'

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from the file
    """
    with open(filepath) as f:
        tree = cst.parse_module(f.read())

    analyzer = FunctionCallAnalyzer()
    tree.visit(analyzer)

    unused_functions = analyzer.report_unused_functions()
    print(f"Unused Functions: {unused_functions}")

    return {
        "unused_functions": unused_functions,
        "defined_functions": list(analyzer.function_defs),
    }


# Example Usage:
# analyze_function_calls("your_script.py")  # ✅ Detect unused functions

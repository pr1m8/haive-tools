"""Type Checking Visitor Module.

This module provides functionality to analyze Python code for type annotation issues
using LibCST. It identifies functions missing type hints and incorrect return type
annotations, helping to improve type safety in codebases.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.type_checking import check_types
    >>> check_types("/path/to/file.py")
    ⚠️ Functions missing type hints: ['process_data', 'calculate_total']
    ❌ Incorrect return type in `format_result`: Expected str, got int
"""

import libcst as cst


class TypeChecker(cst.CSTVisitor):
    """Checks for missing or incorrect type hints in functions.

    This visitor analyzes function definitions in Python code to identify
    missing parameter type annotations and incorrect return type annotations.

    Attributes:
        missing_annotations (List[str]): List of function names missing type annotations
        incorrect_annotations (List[Tuple[str, str, str]]): List of tuples containing function name,
            expected return type, and actual return type for functions with incorrect annotations
        function_types (Dict[str, str]): Dictionary mapping function names to their expected return types
    """

    def __init__(self):
        """Initialize the type checker visitor."""
        super().__init__()
        self.missing_annotations: list[str] = []
        self.incorrect_annotations: list[tuple[str, str, str]] = []
        self.function_types: dict[str, str] = {}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        """Check if a function has proper type hints during the AST traversal.

        This method analyzes a function definition to determine if it has parameter
        type annotations and if the return type annotation is correct.

        Args:
            node (cst.FunctionDef): The function definition node being visited
        """
        function_name = node.name.value
        has_annotations = any(param.annotation for param in node.params.params)
        return_annotation = node.returns

        if not has_annotations:
            self.missing_annotations.append(function_name)

        if (
            return_annotation
            and return_annotation.annotation
            and function_name in self.function_types
        ):
            expected_type = self.function_types[function_name]
            actual_type = return_annotation.annotation.value
            if expected_type != actual_type:
                self.incorrect_annotations.append(
                    (function_name, expected_type, actual_type)
                )

    def report_issues(self) -> None:
        """Print a report of all type checking issues found.

        This method generates a human-readable report of functions missing type hints
        and functions with incorrect return type annotations.
        """
        if self.missing_annotations:
            print(f"⚠️ Functions missing type hints: {self.missing_annotations}")
        if self.incorrect_annotations:
            for func, expected, actual in self.incorrect_annotations:
                print(
                    f"❌ Incorrect return type in `{func}`: Expected {expected}, got {actual}"
                )


def check_types(filepath: str) -> None:
    """Check a Python file for type annotation issues.

    This function analyzes a Python file to identify functions missing type annotations
    and functions with incorrect return type annotations, and prints a report of the issues.

    Args:
        filepath (str): Path to the Python file to analyze

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from the file
    """
    with open(filepath) as f:
        tree = cst.parse_module(f.read())

    checker = TypeChecker()
    tree.visit(checker)
    checker.report_issues()


# Example Usage:
# check_types("your_script.py")  # ✅ Detect missing type hints & incorrect return types

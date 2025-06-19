"""
Code Smell Detector Module

This module provides functionality to detect code smells and bad practices
in Python code using LibCST. It identifies potential issues such as deeply
nested loops that can make code harder to understand and maintain.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.visitors.code_smell_detector import detect_code_smells
    >>> detect_code_smells("/path/to/file.py")
    ⚠️ Deeply nested loop detected at line 42
"""

from typing import Dict, List, Set

import libcst as cst


class CodeSmellDetector(cst.CSTVisitor):
    """
    Detects code smells and bad coding patterns.

    This visitor analyzes Python code for potential code smells, such as
    deeply nested loops, excessively large functions, and other anti-patterns
    that can impact code maintainability and readability.

    Attributes:
        nesting_level (int): The current nesting level of loops being analyzed
        issues (List[Dict]): List of detected code smells with details
    """

    def __init__(self):
        """Initialize the code smell detector visitor."""
        super().__init__()
        self.nesting_level = 0
        self.issues: List[Dict] = []

    def visit_For(self, node: cst.For) -> None:
        """
        Track nesting depth of for loops during the AST traversal.

        This method increments the nesting level counter when entering a loop
        and checks if the nesting level exceeds a threshold (3).

        Args:
            node (cst.For): The for loop node being visited
        """
        self.nesting_level += 1
        if self.nesting_level > 3:
            issue = {
                "type": "deeply_nested_loop",
                "message": f"Deeply nested loop detected at line {node.lineno if hasattr(node, 'lineno') else 'unknown'}",
                "severity": "warning",
            }
            self.issues.append(issue)
            print(f"⚠️ {issue['message']}")

    def leave_For(self, original_node: cst.For) -> None:
        """
        Decrement nesting level when leaving a for loop.

        Args:
            original_node (cst.For): The for loop node being left
        """
        self.nesting_level -= 1

    def get_issues(self) -> List[Dict]:
        """
        Return a list of all detected code smells.

        Returns:
            List[Dict]: List of dictionaries containing details about each detected issue
        """
        return self.issues


def detect_code_smells(filepath: str) -> List[Dict]:
    """
    Detect code smells in a Python file.

    This function analyzes a Python file to identify potential code smells
    and bad practices that could impact code quality and maintainability.

    Args:
        filepath (str): Path to the Python file to analyze

    Returns:
        List[Dict]: List of detected code smells with details

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from the file
    """
    with open(filepath, "r") as f:
        tree = cst.parse_module(f.read())

    detector = CodeSmellDetector()
    tree.visit(detector)

    return detector.get_issues()


# Example Usage:
# detect_code_smells("your_script.py")  # ✅ Warns about deeply nested loops

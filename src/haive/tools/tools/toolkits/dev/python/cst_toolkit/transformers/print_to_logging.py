"""Print to Logging Transformer Module.

This module provides functionality to convert print statements to logging calls
in Python files using LibCST. It automatically transforms print() calls to
logging.info() calls for better production-ready code.

Example:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.print_to_logging import replace_print_with_logging
    >>> replace_print_with_logging("/path/to/file.py")

Before:
    print("Hello, world!")

After:
    logging.info("Hello, world!")

"""

import libcst as cst


class PrintToLoggingTransformer(cst.CSTTransformer):
    """Replaces print statements with logging.info calls.

    This transformer identifies print() function calls in Python code and
    replaces them with equivalent logging.info() calls for better production-ready code.

    Attributes:
        None

    """

    def leave_Expr(self, original_node: cst.Expr, updated_node: cst.Expr):
        """Replace print calls with logging.info() during the AST traversal.

        Args:
            original_node (cst.Expr): The original expression node
            updated_node (cst.Expr): The updated expression node

        Returns:
            cst.Expr: The transformed expression with logging.info() if it was a print call,
                otherwise the original node

        """
        if (
            isinstance(original_node.value, cst.Call)
            and isinstance(original_node.value.func, cst.Name)
            and original_node.value.func.value == "print"
        ):
            return updated_node.with_changes(
                value=cst.Call(
                    func=cst.parse_expression("logging.info"),
                    args=original_node.value.args,
                )
            )
        return updated_node


def replace_print_with_logging(filepath: str):
    """Replaces all print() calls with logging.info() calls in a Python file.

    This function reads a Python file, converts all print() function calls to
    logging.info() calls, and writes the updated code back to the file. It does not
    automatically add the import statement for the logging module.

    Args:
        filepath (str): Path to the Python file to process

    Raises:
        FileNotFoundError: If the specified file does not exist
        IOError: If there are issues reading from or writing to the file

    """
    with open(filepath) as f:
        tree = cst.parse_module(f.read())

    modified_tree = tree.visit(PrintToLoggingTransformer())

    with open(filepath, "w") as f:
        f.write(modified_tree.code)


# Example Usage:
# replace_print_with_logging("your_script.py")  # ✅ Auto-fixes `print()`

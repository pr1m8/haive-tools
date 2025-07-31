"""Function Logging Transformer Module.

This module provides a LibCST transformer that automatically adds logging statements
to functions in Python code. It can be used to instrument code for debugging,
performance monitoring, or audit trail generation without manually modifying
every function.

The transformer injects a print statement at the beginning of each function body
that logs the function name when it is executed, making it easy to trace function
calls during program execution.

Examples:
    >>> from haive.tools.toolkits.dev.python.cst_toolkit.transformers.function_logging_transformer import add_logging
    >>> add_logging("path/to/your_script.py")
    # This will modify the file, adding logging to all functions

"""

import os

import libcst as cst
from libcst import MetadataWrapper


class FunctionLoggingTransformer(cst.CSTTransformer):
    """Adds logging to function definitions.

    This transformer visits each function definition in the code and adds
    a print statement at the beginning of the function body that logs
    the function name when it is executed.

    Attributes:
        log_format: Format string for the log message, with {name} as placeholder.
        exclude_methods: List of method names to exclude from logging.

    """

    def __init__(
        self, log_format: str = "Executing {name}", exclude_methods: list[str] = None
    ):
        """Initialize the function logging transformer.

        Args:
            log_format: Format string for the log message, with {name} as placeholder.
            exclude_methods: List of method names to exclude from logging.

        """
        super().__init__()
        self.log_format = log_format
        self.exclude_methods = exclude_methods or []

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """Inject logging at the start of every function.

        This method is called by the CST visitor when it leaves a function definition.
        It adds a print statement at the beginning of the function body.

        Args:
            original_node: The original function definition node from the CST.
            updated_node: The potentially modified function definition node.

        Returns:
            A modified function definition with logging injected.

        """
        # Skip if the function name is in the exclude list
        if original_node.name.value in self.exclude_methods:
            return updated_node

        # Create a print statement with the function name
        log_msg = self.log_format.format(name=original_node.name.value)
        log_statement = cst.parse_statement(f'print("{log_msg}")')

        # Add the log statement at the beginning of the function body
        new_body = [log_statement, *updated_node.body.body]
        return updated_node.with_changes(
            body=updated_node.body.with_changes(body=new_body)
        )


def add_logging(
    filepath: str,
    log_format: str = "Executing {name}",
    exclude_methods: list[str] = None,
) -> None:
    """Inject logging into functions in a Python file.

    This function parses a Python file, adds logging statements to the beginning of
    each function definition, and writes the modified code back to the file.

    Args:
        filepath: Path to the Python file to modify.
        log_format: Format string for the log message, with {name} as placeholder.
        exclude_methods: List of method names to exclude from logging.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the file cannot be read or written.
        SyntaxError: If the file contains invalid Python syntax.

    """
    # Check if file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # Read the file
    with open(filepath) as f:
        source_code = f.read()

    # Parse the code
    try:
        tree = cst.parse_module(source_code)
    except Exception as e:
        raise SyntaxError(f"Failed to parse {filepath}: {e!s}")

    # Apply the transformer
    wrapper = MetadataWrapper(tree)
    transformer = FunctionLoggingTransformer(log_format, exclude_methods)
    modified_tree = wrapper.visit(transformer)

    # Write the modified code back to the file
    with open(filepath, "w") as f:
        f.write(modified_tree.code)

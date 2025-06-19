import difflib
import json
import logging
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

import libcst as cst
from haive.core.engine.aug_llm import AugLLMConfig, compose_runnable
from haive.core.models.llm.base import AzureLLMConfig, LLMProvider
from langchain_core.tools import BaseTool, StructuredTool
from libcst import matchers as m
from libcst.metadata import MetadataWrapper, PositionProvider
from pydantic import BaseModel, Field

"""
Development toolkit for code editing, quality assurance, and Git operations.

This module provides a set of tools for automated code manipulation, including:
- AST-based code transformations (renaming, docstring addition, etc.)
- Code quality checks and automatic fixes
- Git operations and commit management
- Code summarization and analysis

The toolkit uses LibCST for safe, reliable code transformations and provides
a structured interface for common development tasks.
"""

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================
# Enums and Constants
# =============================================


class EditType(str, Enum):
    """
    Types of AST edits that can be performed.

    Defines the supported code transformation operations for the AST-based
    code editor tools.
    """

    RENAME_FUNCTION = "rename_function"
    RENAME_CLASS = "rename_class"
    RENAME_VARIABLE = "rename_variable"
    ADD_DOCSTRING = "add_docstring"
    ADD_TYPE_HINTS = "add_type_hints"
    ADD_LOGGING = "add_logging"
    EXTRACT_FUNCTION = "extract_function"
    REFACTOR_LOOP = "refactor_loop"
    ADD_ERROR_HANDLING = "add_error_handling"
    ADD_PARAMETER = "add_parameter"
    REMOVE_PARAMETER = "remove_parameter"
    RENAME_PARAMETER = "rename_parameter"
    CUSTOM_TRANSFORM = "custom_transform"


class GitOperation(str, Enum):
    """
    Types of Git operations.

    Defines the supported Git operations that can be performed
    through the Git operation tools.
    """

    DIFF = "diff"
    COMMIT = "commit"
    STAGE = "stage"
    STATUS = "status"
    LOG = "log"
    BRANCH = "branch"
    CHECKOUT = "checkout"
    RESET = "reset"


class CodeQualityTool(str, Enum):
    """
    Code quality tools that can be used.

    Defines the supported code quality and formatting tools
    that can be executed on Python code.
    """

    BLACK = "black"
    FLAKE8 = "flake8"
    PYLINT = "pylint"
    MYPY = "mypy"
    ISORT = "isort"
    AUTOFLAKE = "autoflake"


# =============================================
# Schema Models
# =============================================


class ASTEditConfig(BaseModel):
    """
    Configuration for AST-based code edits.

    Defines the parameters needed to perform Abstract Syntax Tree
    transformations on Python code, including the edit type and
    various operation-specific parameters.
    """

    file_path: str = Field(
        ..., description="Absolute path to the Python file to modify"
    )
    edit_type: EditType = Field(
        ..., description="Type of AST edit operation to perform"
    )

    # Common parameters (used by multiple edit types)
    target_name: Optional[str] = Field(
        None, description="Name of the function, class, or variable to modify"
    )
    new_name: Optional[str] = Field(
        None, description="New name for the function, class, or variable being renamed"
    )
    docstring: Optional[str] = Field(
        None, description="Content of the docstring to add or replace"
    )

    # Rename parameters
    scope: Optional[str] = Field(
        None, description="Scope for variable renaming (function or class name)"
    )

    # Function extraction parameters
    start_line: Optional[int] = Field(
        None, description="Starting line number for code to be extracted"
    )
    end_line: Optional[int] = Field(
        None, description="Ending line number for code to be extracted"
    )
    extracted_function_name: Optional[str] = Field(
        None, description="Name to give to the newly extracted function"
    )
    parameters: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="Parameters for the extracted function, including name, type, and default value",
    )

    # Type hint parameters
    type_annotations: Optional[Dict[str, str]] = Field(
        None, description="Dictionary mapping parameter names to their type annotations"
    )
    infer_types: Optional[bool] = Field(
        False, description="Whether to attempt automatic type inference for parameters"
    )

    # Error handling parameters
    exception_type: Optional[str] = Field(
        None, description="Exception type to catch in added error handling blocks"
    )
    error_message: Optional[str] = Field(
        None, description="Error message to log when exceptions are caught"
    )

    # Logging parameters
    log_points: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="Points in the code to add logging statements, with position and message",
    )
    log_level: Optional[str] = Field(
        "info",
        description="Logging level to use for added logging statements (info, debug, warning, error)",
    )

    # Parameter modifications
    param_name: Optional[str] = Field(
        None, description="Name of the parameter to add, remove, or rename"
    )
    param_type: Optional[str] = Field(
        None, description="Type annotation for the parameter being added or modified"
    )
    param_default: Optional[str] = Field(
        None, description="Default value for the parameter being added or modified"
    )

    # Custom transformation
    transform_code: Optional[str] = Field(
        None,
        description="Python code defining a custom transformer class for specialized edits",
    )
    transform_args: Optional[Dict[str, Any]] = Field(
        None, description="Arguments to pass to the custom transformer"
    )

    # Backup options
    create_backup: bool = Field(
        True, description="Whether to create a backup of the file before editing"
    )
    backup_suffix: str = Field(
        ".bak", description="Suffix to add to the filename when creating a backup"
    )


class CodeQualityConfig(BaseModel):
    """
    Configuration for code quality checks.

    Defines the parameters for running code quality tools on Python files,
    including which tools to run and their configuration options.
    """

    file_path: str = Field(
        ..., description="Absolute path to the Python file to check for quality issues"
    )
    tools: List[CodeQualityTool] = Field(
        default=[CodeQualityTool.BLACK, CodeQualityTool.FLAKE8],
        description="List of code quality tools to run on the file",
    )
    fix: bool = Field(
        True, description="Whether to automatically fix issues when possible"
    )
    ignore_errors: List[str] = Field(
        default_factory=list,
        description="List of error codes to ignore during quality checks",
    )
    config_path: Optional[str] = Field(
        None, description="Path to a configuration file for the quality tools"
    )
    line_length: Optional[int] = Field(
        None, description="Maximum line length for formatting tools"
    )
    aggressive: Optional[int] = Field(
        None,
        description="Aggression level for autoflake (0-3, higher means more aggressive)",
    )
    mypy_options: Optional[List[str]] = Field(
        None, description="Additional command-line options to pass to mypy"
    )
    show_diff: bool = Field(
        True, description="Whether to show a diff of changes made by formatting tools"
    )


class GitOperationConfig(BaseModel):
    """
    Configuration for Git operations.

    Defines the parameters needed to perform Git operations on files,
    including the operation type and various operation-specific options.
    """

    file_paths: Union[str, List[str]] = Field(
        ..., description="Absolute path(s) to the file(s) for the Git operation"
    )
    operation: GitOperation = Field(..., description="Type of Git operation to perform")

    # Commit options
    commit_message: Optional[str] = Field(
        None, description="Message to use for Git commit operations"
    )
    generate_message: bool = Field(
        False,
        description="Whether to automatically generate a commit message based on changes",
    )
    commit_author: Optional[str] = Field(
        None,
        description="Author name and email for the commit in 'Name <email>' format",
    )

    # Branch options
    branch_name: Optional[str] = Field(
        None,
        description="Branch name for branch creation, checkout, or deletion operations",
    )

    # Diff options
    staged: bool = Field(
        False, description="Whether to show only staged changes in diff operations"
    )
    context_lines: int = Field(
        3, description="Number of context lines to include in diff output"
    )

    # Reset options
    reset_mode: Optional[str] = Field(
        "mixed",
        description="Reset mode to use: soft (keep changes staged), mixed (default, unstage changes), or hard (discard changes)",
    )

    # Log options
    log_count: Optional[int] = Field(
        5, description="Number of recent commits to show in log operations"
    )
    log_format: Optional[str] = Field(
        None, description="Format string for Git log output"
    )


class CodeSummarizeConfig(BaseModel):
    """
    Configuration for code summarization.

    Defines the parameters for summarizing a Python file, including
    which elements to include in the summary.
    """

    file_path: str = Field(
        ..., description="Absolute path to the Python file to summarize"
    )
    include_docstrings: bool = Field(
        True, description="Whether to extract and include docstrings in the summary"
    )
    include_class_names: bool = Field(
        True, description="Whether to include class definitions in the summary"
    )
    include_function_names: bool = Field(
        True, description="Whether to include function definitions in the summary"
    )
    include_imports: bool = Field(
        True, description="Whether to include import statements in the summary"
    )
    include_global_vars: bool = Field(
        True,
        description="Whether to include global variable declarations in the summary",
    )
    output_format: str = Field(
        "text", description="Format for the summary output: text, json, or markdown"
    )


# =============================================
# Result Models
# =============================================


class EditResult(BaseModel):
    """
    Result of a code edit operation.

    Contains information about the result of an AST-based code edit,
    including whether it was successful and details of the changes made.
    """

    success: bool = Field(
        ..., description="Whether the edit operation completed successfully"
    )
    file_path: str = Field(..., description="Path to the file that was modified")
    edit_type: str = Field(..., description="Type of edit operation that was performed")
    message: str = Field(
        ..., description="Human-readable message describing the result"
    )
    changes: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of detailed changes made during the edit",
    )
    error: Optional[str] = Field(
        None, description="Error message if the operation failed"
    )
    diff: Optional[str] = Field(
        None, description="Unified diff showing the changes made to the file"
    )
    backup_path: Optional[str] = Field(
        None, description="Path to the backup file if one was created"
    )


class QualityResult(BaseModel):
    """
    Result of code quality checks.

    Contains information about the result of running code quality tools,
    including any issues found and fixes applied.
    """

    success: bool = Field(..., description="Whether all quality checks passed")
    file_path: str = Field(..., description="Path to the file that was checked")
    tool_results: Dict[str, Dict[str, Any]] = Field(
        ..., description="Detailed results from each quality tool that was run"
    )
    issues_count: int = Field(
        ..., description="Total number of quality issues found across all tools"
    )
    fixed_count: int = Field(
        0, description="Number of issues that were automatically fixed"
    )
    diff: Optional[str] = Field(
        None, description="Unified diff showing any changes made by formatting tools"
    )
    error: Optional[str] = Field(
        None, description="Error message if any of the quality checks failed"
    )


class GitResult(BaseModel):
    """
    Result of a Git operation.

    Contains information about the result of a Git operation,
    including the command output and any errors.
    """

    success: bool = Field(
        ..., description="Whether the Git operation completed successfully"
    )
    operation: str = Field(..., description="Type of Git operation that was performed")
    file_paths: List[str] = Field(
        ..., description="Paths to the files affected by the operation"
    )
    output: str = Field(
        ..., description="Output from the Git command that was executed"
    )
    error: Optional[str] = Field(
        None, description="Error message if the operation failed"
    )
    commit_id: Optional[str] = Field(
        None, description="ID of the commit if a commit operation was performed"
    )
    diff: Optional[str] = Field(
        None, description="Diff output if a diff operation was performed"
    )


class CodeSummary(BaseModel):
    """
    Summary of a Python file.

    Contains a structured summary of a Python file's contents,
    including classes, functions, imports, and global variables.
    """

    file_path: str = Field(..., description="Path to the file that was summarized")
    classes: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Information about classes defined in the file",
    )
    functions: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Information about functions defined in the file",
    )
    imports: List[str] = Field(
        default_factory=list, description="Import statements found in the file"
    )
    global_vars: List[Dict[str, Any]] = Field(
        default_factory=list, description="Global variables defined in the file"
    )
    docstring: Optional[str] = Field(
        None, description="Module-level docstring if present"
    )
    loc: int = Field(..., description="Total lines of code in the file")
    summary: str = Field(
        ..., description="High-level summary of the file's purpose and contents"
    )


# =============================================
# AST Transformer Classes
# =============================================


@dataclass
class TransformerContext:
    """
    Context for AST transformers with metadata.

    Holds the AST tree, metadata, file path, and a record of changes
    made during AST transformations.

    Attributes:
        tree: The LibCST module representing the AST
        metadata: Optional metadata wrapper for the AST
        file_path: Path to the file being transformed
        changes: List of changes made during transformation
    """

    tree: cst.Module
    metadata: Optional[MetadataWrapper] = None
    file_path: Optional[str] = None
    changes: List[Dict[str, Any]] = None

    def __post_init__(self):
        """Initialize default values and metadata if not provided."""
        if self.changes is None:
            self.changes = []
        if self.metadata is None and self.tree is not None:
            self.metadata = MetadataWrapper(self.tree)


class BaseTransformer(cst.CSTTransformer):
    """
    Base class for all AST transformers.

    Provides common functionality for AST transformers, including
    access to the transformation context and change tracking.

    Attributes:
        context: The transformation context
        changes: Reference to the list of changes in the context
    """

    def __init__(self, context: TransformerContext):
        """
        Initialize the transformer with a context.

        Args:
            context: The transformation context
        """
        super().__init__()
        self.context = context
        self.changes = context.changes

    def add_change(self, change_type: str, **kwargs):
        """
        Add a change record to the context.

        Args:
            change_type: Type of change being made
            **kwargs: Additional details about the change
        """
        change = {"type": change_type, **kwargs}
        self.changes.append(change)


class RenameFunctionTransformer(BaseTransformer):
    """
    Transformer to rename a function in the AST.

    Finds and renames a function with the specified name.

    Attributes:
        old_name: Current name of the function
        new_name: New name for the function
    """

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        """
        Initialize the function renaming transformer.

        Args:
            context: The transformation context
            old_name: Current name of the function to rename
            new_name: New name for the function
        """
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node
        """
        if original_node.name.value == self.old_name:
            self.add_change(
                "rename_function",
                old_name=self.old_name,
                new_name=self.new_name,
                line=(
                    original_node.name.lineno
                    if hasattr(original_node.name, "lineno")
                    else None
                ),
            )
            return updated_node.with_changes(name=cst.Name(value=self.new_name))
        return updated_node


class RenameClassTransformer(BaseTransformer):
    """
    Transformer to rename a class in the AST.

    Finds and renames a class with the specified name.

    Attributes:
        old_name: Current name of the class
        new_name: New name for the class
    """

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        """
        Initialize the class renaming transformer.

        Args:
            context: The transformation context
            old_name: Current name of the class to rename
            new_name: New name for the class
        """
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        """
        Process a class definition node.

        Args:
            original_node: The original class definition node
            updated_node: The updated class definition node

        Returns:
            The transformed class definition node
        """
        if original_node.name.value == self.old_name:
            self.add_change(
                "rename_class",
                old_name=self.old_name,
                new_name=self.new_name,
                line=(
                    original_node.name.lineno
                    if hasattr(original_node.name, "lineno")
                    else None
                ),
            )
            return updated_node.with_changes(name=cst.Name(value=self.new_name))
        return updated_node


class AddDocstringTransformer(BaseTransformer):
    """
    Transformer to add or modify a docstring.

    Adds a new docstring or updates an existing one for a function or class.

    Attributes:
        target_name: Name of the function or class to add/update the docstring for
        docstring: Content of the docstring
        transformed: Whether the docstring has been added/updated
    """

    def __init__(self, context: TransformerContext, target_name: str, docstring: str):
        """
        Initialize the docstring transformer.

        Args:
            context: The transformation context
            target_name: Name of the function or class to modify
            docstring: Content of the docstring to add
        """
        super().__init__(context)
        self.target_name = target_name
        self.docstring = docstring
        self.transformed = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node with added/updated docstring
        """
        if original_node.name.value == self.target_name:
            # Create a new docstring node
            docstring_node = cst.SimpleString(value=f'"""{self.docstring}"""')

            # Check if there's an existing docstring
            has_docstring = False
            if (
                original_node.body.body
                and isinstance(original_node.body.body[0], cst.SimpleStatementLine)
                and isinstance(original_node.body.body[0].body[0], cst.Expr)
                and isinstance(
                    original_node.body.body[0].body[0].value, cst.SimpleString
                )
            ):

                has_docstring = True
                new_body = list(original_node.body.body)
                new_body[0] = new_body[0].with_changes(
                    body=[new_body[0].body[0].with_changes(value=docstring_node)]
                )

                self.add_change(
                    "update_docstring",
                    target=self.target_name,
                    old_docstring=original_node.body.body[0].body[0].value.value,
                    new_docstring=docstring_node.value,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )

                self.transformed = True
                return updated_node.with_changes(
                    body=updated_node.body.with_changes(body=new_body)
                )

            # Add a new docstring if none exists
            if not has_docstring:
                new_body = [
                    cst.SimpleStatementLine(body=[cst.Expr(value=docstring_node)]),
                    *original_node.body.body,
                ]

                self.add_change(
                    "add_docstring",
                    target=self.target_name,
                    docstring=docstring_node.value,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )

                self.transformed = True
                return updated_node.with_changes(
                    body=updated_node.body.with_changes(body=new_body)
                )

        return updated_node

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        """
        Process a class definition node.

        Args:
            original_node: The original class definition node
            updated_node: The updated class definition node

        Returns:
            The transformed class definition node with added/updated docstring
        """
        if original_node.name.value == self.target_name:
            # Create a new docstring node
            docstring_node = cst.SimpleString(value=f'"""{self.docstring}"""')

            # Check if there's an existing docstring
            has_docstring = False
            if (
                original_node.body.body
                and isinstance(original_node.body.body[0], cst.SimpleStatementLine)
                and isinstance(original_node.body.body[0].body[0], cst.Expr)
                and isinstance(
                    original_node.body.body[0].body[0].value, cst.SimpleString
                )
            ):

                has_docstring = True
                new_body = list(original_node.body.body)
                new_body[0] = new_body[0].with_changes(
                    body=[new_body[0].body[0].with_changes(value=docstring_node)]
                )

                self.add_change(
                    "update_docstring",
                    target=self.target_name,
                    old_docstring=original_node.body.body[0].body[0].value.value,
                    new_docstring=docstring_node.value,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )

                self.transformed = True
                return updated_node.with_changes(
                    body=updated_node.body.with_changes(body=new_body)
                )

            # Add a new docstring if none exists
            if not has_docstring:
                new_body = [
                    cst.SimpleStatementLine(body=[cst.Expr(value=docstring_node)]),
                    *original_node.body.body,
                ]

                self.add_change(
                    "add_docstring",
                    target=self.target_name,
                    docstring=docstring_node.value,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )

                self.transformed = True
                return updated_node.with_changes(
                    body=updated_node.body.with_changes(body=new_body)
                )

        return updated_node


class AddTypeHintsTransformer(BaseTransformer):
    """
    Transformer to add type hints to functions.

    Adds or updates type annotations for function parameters and return values.

    Attributes:
        target_name: Optional name of the function to add type hints to
        type_annotations: Dictionary mapping parameter names to type annotations
        changes_made: Whether any type hints were added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: Optional[str] = None,
        type_annotations: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize the type hints transformer.

        Args:
            context: The transformation context
            target_name: Optional name of the function to modify
            type_annotations: Dictionary mapping parameter names to type annotations
        """
        super().__init__(context)
        self.target_name = target_name
        self.type_annotations = type_annotations or {}
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node with added type hints
        """
        # Skip if we have a target and this isn't it
        if self.target_name and original_node.name.value != self.target_name:
            return updated_node

        modified = False
        updated_params = []

        # Add type hints to parameters
        for param in updated_node.params.params:
            param_name = param.name.value
            if param_name in self.type_annotations:
                type_str = self.type_annotations[param_name]
                annotation = cst.Annotation(annotation=cst.parse_expression(type_str))
                updated_param = param.with_changes(annotation=annotation)
                updated_params.append(updated_param)

                self.add_change(
                    "add_parameter_type_hint",
                    function=original_node.name.value,
                    parameter=param_name,
                    type_hint=type_str,
                    line=param.lineno if hasattr(param, "lineno") else None,
                )

                modified = True
            else:
                updated_params.append(param)

        # Add return type hint if specified
        return_type = self.type_annotations.get("return")
        if return_type and not updated_node.returns:
            returns_annotation = cst.Annotation(
                annotation=cst.parse_expression(return_type)
            )

            self.add_change(
                "add_return_type_hint",
                function=original_node.name.value,
                type_hint=return_type,
                line=(
                    original_node.name.lineno
                    if hasattr(original_node.name, "lineno")
                    else None
                ),
            )

            modified = True
        else:
            returns_annotation = updated_node.returns

        if modified:
            self.changes_made = True
            updated_params_list = updated_node.params.with_changes(
                params=updated_params
            )
            return updated_node.with_changes(
                params=updated_params_list, returns=returns_annotation
            )

        return updated_node


class AddLoggingTransformer(BaseTransformer):
    """
    Transformer to add logging statements.

    Adds logging statements to functions at specified points.

    Attributes:
        target_name: Name of the function to add logging to
        log_level: Logging level to use (info, debug, warning, error)
        log_points: List of locations to add logging statements
        changes_made: Whether any logging statements were added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        log_level: str = "info",
        log_points: Optional[List[Dict[str, Any]]] = None,
    ):
        """
        Initialize the logging transformer.

        Args:
            context: The transformation context
            target_name: Name of the function to modify
            log_level: Logging level to use (info, debug, warning, error)
            log_points: List of locations to add logging statements
        """
        super().__init__(context)
        self.target_name = target_name
        self.log_level = log_level.lower()
        self.log_points = log_points or [
            {"position": "start"}
        ]  # Default to function start
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node with added logging statements
        """
        if original_node.name.value != self.target_name:
            return updated_node

        new_body = list(updated_node.body.body)
        modified = False

        for log_point in self.log_points:
            position = log_point.get("position", "start")
            message = log_point.get("message", f"Executing {self.target_name}")
            variables = log_point.get("variables", [])

            # Construct the logging statement
            var_part = ""
            if variables:
                var_str = ", ".join([f"{var}={{{var}}}" for var in variables])
                var_part = f", {var_str}"
                var_args = ", ".join(variables)
                log_stmt = (
                    f'logger.{self.log_level}(f"{message}{var_part}", {var_args})'
                )
            else:
                log_stmt = f'logger.{self.log_level}("{message}")'

            log_node = cst.parse_statement(log_stmt)

            # Add logging statement based on position
            if position == "start":
                new_body.insert(0, log_node)
                self.add_change(
                    "add_logging",
                    function=self.target_name,
                    position="start",
                    message=message,
                    variables=variables,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )
                modified = True
            elif position == "end":
                new_body.append(log_node)
                self.add_change(
                    "add_logging",
                    function=self.target_name,
                    position="end",
                    message=message,
                    variables=variables,
                    line=(
                        original_node.name.lineno
                        if hasattr(original_node.name, "lineno")
                        else None
                    ),
                )
                modified = True

        if modified:
            self.changes_made = True
            return updated_node.with_changes(
                body=updated_node.body.with_changes(body=new_body)
            )

        return updated_node


class AddErrorHandlingTransformer(BaseTransformer):
    """
    Transformer to add try-except blocks.

    Wraps a function's body in a try-except block for error handling.

    Attributes:
        target_name: Name of the function to add error handling to
        exception_type: Type of exception to catch
        error_message: Error message to log when an exception is caught
        changes_made: Whether error handling was added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        exception_type: str = "Exception",
        error_message: Optional[str] = None,
    ):
        """
        Initialize the error handling transformer.

        Args:
            context: The transformation context
            target_name: Name of the function to modify
            exception_type: Type of exception to catch
            error_message: Error message to log when an exception is caught
        """
        super().__init__(context)
        self.target_name = target_name
        self.exception_type = exception_type
        self.error_message = error_message or f"Error in {target_name}"
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node with added error handling
        """
        if original_node.name.value != self.target_name:
            return updated_node

        # Create a try-except block around the function body
        function_body = updated_node.body.body

        # Create the except handler
        except_body = [
            cst.parse_statement(f'logger.error(f"{self.error_message}: {{e}}")'),
            cst.parse_statement(f"raise"),
        ]

        except_handler = cst.ExceptHandler(
            type=cst.parse_expression(self.exception_type),
            name=cst.Name("e"),
            body=cst.IndentedBlock(body=except_body),
        )

        # Create the try block
        try_node = cst.Try(
            body=cst.IndentedBlock(body=function_body),
            handlers=[except_handler],
            orelse=None,
            finalbody=None,
        )

        self.add_change(
            "add_error_handling",
            function=self.target_name,
            exception_type=self.exception_type,
            error_message=self.error_message,
            line=(
                original_node.name.lineno
                if hasattr(original_node.name, "lineno")
                else None
            ),
        )

        self.changes_made = True
        return updated_node.with_changes(body=cst.IndentedBlock(body=[try_node]))


class AddParameterTransformer(BaseTransformer):
    """
    Transformer to add a parameter to a function.

    Adds a new parameter to a function definition.

    Attributes:
        target_name: Name of the function to add the parameter to
        param_name: Name of the parameter to add
        param_type: Optional type annotation for the parameter
        param_default: Optional default value for the parameter
        changes_made: Whether the parameter was added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        param_name: str,
        param_type: Optional[str] = None,
        param_default: Optional[str] = None,
    ):
        """
        Initialize the parameter transformer.

        Args:
            context: The transformation context
            target_name: Name of the function to modify
            param_name: Name of the parameter to add
            param_type: Optional type annotation for the parameter
            param_default: Optional default value for the parameter
        """
        super().__init__(context)
        self.target_name = target_name
        self.param_name = param_name
        self.param_type = param_type
        self.param_default = param_default
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """
        Process a function definition node.

        Args:
            original_node: The original function definition node
            updated_node: The updated function definition node

        Returns:
            The transformed function definition node with the added parameter
        """
        if original_node.name.value != self.target_name:
            return updated_node

        # Check if parameter already exists
        for param in updated_node.params.params:
            if param.name.value == self.param_name:
                return updated_node  # Parameter already exists

        # Create new parameter
        annotation = None
        if self.param_type:
            annotation = cst.Annotation(
                annotation=cst.parse_expression(self.param_type)
            )

        default = None
        if self.param_default:
            default = cst.parse_expression(self.param_default)

        new_param = cst.Param(
            name=cst.Name(self.param_name), annotation=annotation, default=default
        )

        # Add to parameter list
        params = list(updated_node.params.params) + [new_param]
        updated_params = updated_node.params.with_changes(params=params)

        self.add_change(
            "add_parameter",
            function=self.target_name,
            parameter=self.param_name,
            type_hint=self.param_type,
            default=self.param_default,
            line=(
                original_node.name.lineno
                if hasattr(original_node.name, "lineno")
                else None
            ),
        )

        self.changes_made = True
        return updated_node.with_changes(params=updated_params)


# =============================================
# Core Tool Implementation
# =============================================


class CodeStyleConfig(BaseModel):
    """
    Configuration for code formatting and style enforcement.

    Defines settings for code formatting tools like Black, isort, and autoflake.
    """

    line_length: int = Field(88, description="Maximum line length for formatted code")
    use_black: bool = Field(
        True, description="Whether to use the Black formatter for code styling"
    )
    use_isort: bool = Field(
        True, description="Whether to use isort for sorting imports"
    )
    use_autoflake: bool = Field(
        True, description="Whether to use autoflake to remove unused imports"
    )
    fix: bool = Field(
        True, description="Whether to automatically fix detected style issues"
    )
    show_diff: bool = Field(
        True, description="Whether to show a diff of changes made by formatting tools"
    )


class CodeEditorTool:
    """
    Advanced tool for AST-based code editing with debugging and logging.

    Provides high-level functionality for code editing, including AST-based
    transformations, backup creation, and diff generation.
    """

    def __init__(
        self, debug: bool = False, style_config: Optional[CodeStyleConfig] = None
    ):
        """
        Initialize the Code Editor Tool with debugging and code style settings.

        Args:
            debug: Enable detailed debug logging
            style_config: Code formatting settings
        """
        self.debug = debug
        self.style_config = style_config or CodeStyleConfig()

        if self.debug:
            logger.setLevel(logging.DEBUG)
            logger.debug("Debugging enabled for CodeEditorTool")

    @staticmethod
    def create_backup(file_path: str, suffix: str = ".bak") -> str:
        """
        Create a backup of the file.

        Args:
            file_path: Path to the file to back up
            suffix: Suffix to add to the backup file name

        Returns:
            Path to the created backup file
        """
        backup_path = f"{file_path}{suffix}"
        with open(file_path, "r") as src, open(backup_path, "w") as dst:
            dst.write(src.read())
        logger.info(f"Backup created at {backup_path}")
        return backup_path

    @staticmethod
    def generate_diff(original: str, modified: str) -> str:
        """
        Generate a diff between original and modified code.

        Args:
            original: Original code content
            modified: Modified code content

        Returns:
            Unified diff string showing the changes
        """
        diff = "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                modified.splitlines(keepends=True),
                fromfile="original",
                tofile="modified",
                n=3,
            )
        )
        return diff

    def perform_ast_edit(self, config: "ASTEditConfig") -> "EditResult":
        """
        Perform an AST-based edit on a Python file.

        Uses the LibCST library to safely parse and transform Python code
        based on the provided configuration.

        Args:
            config: Configuration for the AST edit operation

        Returns:
            Result of the edit operation
        """
        if not os.path.exists(config.file_path):
            return EditResult(
                success=False,
                file_path=config.file_path,
                edit_type=config.edit_type,
                message="File not found",
                error="File not found",
            )

        if config.create_backup:
            backup_path = self.create_backup(config.file_path, config.backup_suffix)

        with open(config.file_path, "r") as f:
            original_code = f.read()

        tree = cst.parse_module(original_code)
        context = TransformerContext(tree=tree, file_path=config.file_path)

        # Apply AST transformations based on config
        # Example: Rename function
        if (
            config.edit_type == EditType.RENAME_FUNCTION
            and config.target_name
            and config.new_name
        ):
            transformer = RenameFunctionTransformer(
                context, config.target_name, config.new_name
            )
            modified_tree = tree.visit(transformer)
        else:
            return EditResult(
                success=False,
                file_path=config.file_path,
                edit_type=config.edit_type,
                message="Invalid transformation parameters",
                error="Transformation parameters missing",
            )

        modified_code = modified_tree.code
        diff = self.generate_diff(original_code, modified_code)

        if self.debug:
            logger.debug(f"Code diff:\n{diff}")

        # Write the modified file
        with open(config.file_path, "w") as f:
            f.write(modified_code)

        return EditResult(
            success=True,
            file_path=config.file_path,
            edit_type=config.edit_type,
            message="AST edit applied successfully",
            diff=diff,
        )

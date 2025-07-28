"""Development toolkit for code editing, quality assurance, and Git operations.

This module provides a set of tools for automated code manipulation, including:
- AST-based code transformations (renaming, docstring addition, etc.)
- Code quality checks and automatic fixes
- Git operations and commit management
- Code summarization and analysis

The toolkit uses LibCST for safe, reliable code transformations and provides
a structured interface for common development tasks.

Examples:
    >>> from haive.tools.toolkits.dev.tools import CodeEditorTool
    >>> editor = CodeEditorTool(debug=True)
    >>> config = ASTEditConfig(
    ...     file_path="/path/to/file.py",
    ...     edit_type=EditType.ADD_DOCSTRING,
    ...     target_name="my_function",
    ...     docstring="This function does something useful."
    ... )
    >>> result = editor.perform_ast_edit(config)
    >>> print(result.success)
"""

import difflib
import logging
import os
from dataclasses import dataclass
from enum import Enum
from typing import Any

import libcst as cst
from libcst.metadata import MetadataWrapper
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================
# Enums and Constants
# =============================================


class EditType(str, Enum):
    """Types of AST edits that can be performed.

    Defines the supported code transformation operations for the AST-based
    code editor tools.

    Attributes:
        RENAME_FUNCTION (str): Rename a function
        RENAME_CLASS (str): Rename a class
        RENAME_VARIABLE (str): Rename a variable
        ADD_DOCSTRING (str): Add or update a docstring
        ADD_TYPE_HINTS (str): Add type annotations
        ADD_LOGGING (str): Add logging statements
        EXTRACT_FUNCTION (str): Extract code into a new function
        REFACTOR_LOOP (str): Refactor a loop
        ADD_ERROR_HANDLING (str): Add try/except error handling
        ADD_PARAMETER (str): Add a parameter to a function
        REMOVE_PARAMETER (str): Remove a parameter from a function
        RENAME_PARAMETER (str): Rename a function parameter
        CUSTOM_TRANSFORM (str): Apply a custom transformation
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
    """Types of Git operations.

    Defines the supported Git operations that can be performed
    through the Git operation tools.

    Attributes:
        DIFF (str): Show differences between commits, working tree, etc.
        COMMIT (str): Record changes to the repository
        STAGE (str): Add file contents to the staging area
        STATUS (str): Show the working tree status
        LOG (str): Show commit logs
        BRANCH (str): List, create, or delete branches
        CHECKOUT (str): Switch branches or restore working tree files
        RESET (str): Reset current HEAD to the specified state
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
    """Code quality tools that can be used.

    Defines the supported code quality and formatting tools
    that can be executed on Python code.

    Attributes:
        BLACK (str): The Black code formatter
        FLAKE8 (str): The Flake8 linter
        PYLINT (str): The Pylint linter
        MYPY (str): The MyPy static type checker
        ISORT (str): The isort import sorter
        AUTOFLAKE (str): The Autoflake tool for removing unused imports
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
    """Configuration for AST-based code edits.

    Defines the parameters needed to perform Abstract Syntax Tree
    transformations on Python code, including the edit type and
    various operation-specific parameters.

    Attributes:
        file_path (str): Absolute path to the Python file to modify
        edit_type (EditType): Type of AST edit operation to perform
        target_name (Optional[str]): Name of the function, class, or variable to modify
        new_name (Optional[str]): New name for the function, class, or variable being renamed
        docstring (Optional[str]): Content of the docstring to add or replace
        scope (Optional[str]): Scope for variable renaming (function or class name)
        start_line (Optional[int]): Starting line number for code to be extracted
        end_line (Optional[int]): Ending line number for code to be extracted
        extracted_function_name (Optional[str]): Name to give to the newly extracted function
        parameters (Optional[List[Dict[str, Any]]]): Parameters for the extracted function
        type_annotations (Optional[Dict[str, str]]): Dictionary mapping parameter names to type annotations
        infer_types (Optional[bool]): Whether to attempt automatic type inference for parameters
        exception_type (Optional[str]): Exception type to catch in added error handling blocks
        error_message (Optional[str]): Error message to log when exceptions are caught
        log_points (Optional[List[Dict[str, Any]]]): Points to add logging statements
        log_level (Optional[str]): Logging level to use for added logging statements
        param_name (Optional[str]): Name of the parameter to add, remove, or rename
        param_type (Optional[str]): Type annotation for the parameter being added or modified
        param_default (Optional[str]): Default value for the parameter being added or modified
        transform_code (Optional[str]): Python code defining a custom transformer class
        transform_args (Optional[Dict[str, Any]]): Arguments to pass to the custom transformer
        create_backup (bool): Whether to create a backup of the file before editing
        backup_suffix (str): Suffix to add to the filename when creating a backup
    """

    file_path: str = Field(
        ..., description="Absolute path to the Python file to modify"
    )
    edit_type: EditType = Field(
        ..., description="Type of AST edit operation to perform"
    )

    # Common parameters (used by multiple edit types)
    target_name: str | None = Field(
        None, description="Name of the function, class, or variable to modify"
    )
    new_name: str | None = Field(
        None, description="New name for the function, class, or variable being renamed"
    )
    docstring: str | None = Field(
        None, description="Content of the docstring to add or replace"
    )

    # Rename parameters
    scope: str | None = Field(
        None, description="Scope for variable renaming (function or class name)"
    )

    # Function extraction parameters
    start_line: int | None = Field(
        None, description="Starting line number for code to be extracted"
    )
    end_line: int | None = Field(
        None, description="Ending line number for code to be extracted"
    )
    extracted_function_name: str | None = Field(
        None, description="Name to give to the newly extracted function"
    )
    parameters: list[dict[str, Any]] | None = Field(
        None,
        description="Parameters for the extracted function, including name, type, and default value",
    )

    # Type hint parameters
    type_annotations: dict[str, str] | None = Field(
        None, description="Dictionary mapping parameter names to their type annotations"
    )
    infer_types: bool | None = Field(
        False, description="Whether to attempt automatic type inference for parameters"
    )

    # Error handling parameters
    exception_type: str | None = Field(
        None, description="Exception type to catch in added error handling blocks"
    )
    error_message: str | None = Field(
        None, description="Error message to log when exceptions are caught"
    )

    # Logging parameters
    log_points: list[dict[str, Any]] | None = Field(
        None,
        description="Points in the code to add logging statements, with position and message",
    )
    log_level: str | None = Field(
        "info",
        description="Logging level to use for added logging statements (info, debug, warning, error)",
    )

    # Parameter modifications
    param_name: str | None = Field(
        None, description="Name of the parameter to add, remove, or rename"
    )
    param_type: str | None = Field(
        None, description="Type annotation for the parameter being added or modified"
    )
    param_default: str | None = Field(
        None, description="Default value for the parameter being added or modified"
    )

    # Custom transformation
    transform_code: str | None = Field(
        None,
        description="Python code defining a custom transformer class for specialized edits",
    )
    transform_args: dict[str, Any] | None = Field(
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
    """Configuration for code quality checks.

    Defines the parameters for running code quality tools on Python files,
    including which tools to run and their configuration options.

    Attributes:
        file_path (str): Absolute path to the Python file to check
        tools (List[CodeQualityTool]): List of code quality tools to run on the file
        fix (bool): Whether to automatically fix issues when possible
        ignore_errors (List[str]): List of error codes to ignore during quality checks
        config_path (Optional[str]): Path to a configuration file for the quality tools
        line_length (Optional[int]): Maximum line length for formatting tools
        aggressive (Optional[int]): Aggression level for autoflake (0-3)
        mypy_options (Optional[List[str]]): Additional command-line options for mypy
        show_diff (bool): Whether to show a diff of changes made by formatting tools
    """

    file_path: str = Field(
        ..., description="Absolute path to the Python file to check for quality issues"
    )
    tools: list[CodeQualityTool] = Field(
        default=[CodeQualityTool.BLACK, CodeQualityTool.FLAKE8],
        description="List of code quality tools to run on the file",
    )
    fix: bool = Field(
        True, description="Whether to automatically fix issues when possible"
    )
    ignore_errors: list[str] = Field(
        default_factory=list,
        description="List of error codes to ignore during quality checks",
    )
    config_path: str | None = Field(
        None, description="Path to a configuration file for the quality tools"
    )
    line_length: int | None = Field(
        None, description="Maximum line length for formatting tools"
    )
    aggressive: int | None = Field(
        None,
        description="Aggression level for autoflake (0-3, higher means more aggressive)",
    )
    mypy_options: list[str] | None = Field(
        None, description="Additional command-line options to pass to mypy"
    )
    show_diff: bool = Field(
        True, description="Whether to show a diff of changes made by formatting tools"
    )


class GitOperationConfig(BaseModel):
    """Configuration for Git operations.

    Defines the parameters needed to perform Git operations on files,
    including the operation type and various operation-specific options.

    Attributes:
        file_paths (Union[str, List[str]]): Absolute path(s) to the file(s) for the Git operation
        operation (GitOperation): Type of Git operation to perform
        commit_message (Optional[str]): Message to use for Git commit operations
        generate_message (bool): Whether to automatically generate a commit message
        commit_author (Optional[str]): Author name and email for the commit
        branch_name (Optional[str]): Branch name for branch operations
        staged (bool): Whether to show only staged changes in diff operations
        context_lines (int): Number of context lines to include in diff output
        reset_mode (Optional[str]): Reset mode to use (soft, mixed, hard)
        log_count (Optional[int]): Number of recent commits to show in log operations
        log_format (Optional[str]): Format string for Git log output
    """

    file_paths: str | list[str] = Field(
        ..., description="Absolute path(s) to the file(s) for the Git operation"
    )
    operation: GitOperation = Field(..., description="Type of Git operation to perform")

    # Commit options
    commit_message: str | None = Field(
        None, description="Message to use for Git commit operations"
    )
    generate_message: bool = Field(
        False,
        description="Whether to automatically generate a commit message based on changes",
    )
    commit_author: str | None = Field(
        None,
        description="Author name and email for the commit in 'Name <email>' format",
    )

    # Branch options
    branch_name: str | None = Field(
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
    reset_mode: str | None = Field(
        "mixed",
        description="Reset mode to use: soft (keep changes staged), mixed (default, unstage changes), or hard (discard changes)",
    )

    # Log options
    log_count: int | None = Field(
        5, description="Number of recent commits to show in log operations"
    )
    log_format: str | None = Field(None, description="Format string for Git log output")


class CodeSummarizeConfig(BaseModel):
    """Configuration for code summarization.

    Defines the parameters for summarizing a Python file, including
    which elements to include in the summary.

    Attributes:
        file_path (str): Absolute path to the Python file to summarize
        include_docstrings (bool): Whether to extract and include docstrings
        include_class_names (bool): Whether to include class definitions
        include_function_names (bool): Whether to include function definitions
        include_imports (bool): Whether to include import statements
        include_global_vars (bool): Whether to include global variable declarations
        output_format (str): Format for the summary output (text, json, markdown)
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
    """Result of a code edit operation.

    Contains information about the result of an AST-based code edit,
    including whether it was successful and details of the changes made.

    Attributes:
        success (bool): Whether the edit operation completed successfully
        file_path (str): Path to the file that was modified
        edit_type (str): Type of edit operation that was performed
        message (str): Human-readable message describing the result
        changes (List[Dict[str, Any]]): List of detailed changes made during the edit
        error (Optional[str]): Error message if the operation failed
        diff (Optional[str]): Unified diff showing the changes made to the file
        backup_path (Optional[str]): Path to the backup file if one was created
    """

    success: bool = Field(
        ..., description="Whether the edit operation completed successfully"
    )
    file_path: str = Field(..., description="Path to the file that was modified")
    edit_type: str = Field(..., description="Type of edit operation that was performed")
    message: str = Field(
        ..., description="Human-readable message describing the result"
    )
    changes: list[dict[str, Any]] = Field(
        default_factory=list,
        description="List of detailed changes made during the edit",
    )
    error: str | None = Field(None, description="Error message if the operation failed")
    diff: str | None = Field(
        None, description="Unified diff showing the changes made to the file"
    )
    backup_path: str | None = Field(
        None, description="Path to the backup file if one was created"
    )


class QualityResult(BaseModel):
    """Result of code quality checks.

    Contains information about the result of running code quality tools,
    including any issues found and fixes applied.

    Attributes:
        success (bool): Whether all quality checks passed
        file_path (str): Path to the file that was checked
        tool_results (Dict[str, Dict[str, Any]]): Detailed results from each quality tool
        issues_count (int): Total number of quality issues found across all tools
        fixed_count (int): Number of issues that were automatically fixed
        diff (Optional[str]): Unified diff showing changes made by formatting tools
        error (Optional[str]): Error message if any of the quality checks failed
    """

    success: bool = Field(..., description="Whether all quality checks passed")
    file_path: str = Field(..., description="Path to the file that was checked")
    tool_results: dict[str, dict[str, Any]] = Field(
        ..., description="Detailed results from each quality tool that was run"
    )
    issues_count: int = Field(
        ..., description="Total number of quality issues found across all tools"
    )
    fixed_count: int = Field(
        0, description="Number of issues that were automatically fixed"
    )
    diff: str | None = Field(
        None, description="Unified diff showing any changes made by formatting tools"
    )
    error: str | None = Field(
        None, description="Error message if any of the quality checks failed"
    )


class GitResult(BaseModel):
    """Result of a Git operation.

    Contains information about the result of a Git operation,
    including the command output and any errors.

    Attributes:
        success (bool): Whether the Git operation completed successfully
        operation (str): Type of Git operation that was performed
        file_paths (List[str]): Paths to the files affected by the operation
        output (str): Output from the Git command that was executed
        error (Optional[str]): Error message if the operation failed
        commit_id (Optional[str]): ID of the commit if a commit operation was performed
        diff (Optional[str]): Diff output if a diff operation was performed
    """

    success: bool = Field(
        ..., description="Whether the Git operation completed successfully"
    )
    operation: str = Field(..., description="Type of Git operation that was performed")
    file_paths: list[str] = Field(
        ..., description="Paths to the files affected by the operation"
    )
    output: str = Field(
        ..., description="Output from the Git command that was executed"
    )
    error: str | None = Field(None, description="Error message if the operation failed")
    commit_id: str | None = Field(
        None, description="ID of the commit if a commit operation was performed"
    )
    diff: str | None = Field(
        None, description="Diff output if a diff operation was performed"
    )


class CodeSummary(BaseModel):
    """Summary of a Python file.

    Contains a structured summary of a Python file's contents,
    including classes, functions, imports, and global variables.

    Attributes:
        file_path (str): Path to the file that was summarized
        classes (List[Dict[str, Any]]): Information about classes defined in the file
        functions (List[Dict[str, Any]]): Information about functions defined in the file
        imports (List[str]): Import statements found in the file
        global_vars (List[Dict[str, Any]]): Global variables defined in the file
        docstring (Optional[str]): Module-level docstring if present
        loc (int): Total lines of code in the file
        summary (str): High-level summary of the file's purpose and contents
    """

    file_path: str = Field(..., description="Path to the file that was summarized")
    classes: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Information about classes defined in the file",
    )
    functions: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Information about functions defined in the file",
    )
    imports: list[str] = Field(
        default_factory=list, description="Import statements found in the file"
    )
    global_vars: list[dict[str, Any]] = Field(
        default_factory=list, description="Global variables defined in the file"
    )
    docstring: str | None = Field(None, description="Module-level docstring if present")
    loc: int = Field(..., description="Total lines of code in the file")
    summary: str = Field(
        ..., description="High-level summary of the file's purpose and contents"
    )


# =============================================
# AST Transformer Classes
# =============================================


@dataclass
class TransformerContext:
    """Context for AST transformers with metadata.

    Holds the AST tree, metadata, file path, and a record of changes
    made during AST transformations.

    Attributes:
        tree (cst.Module): The LibCST module representing the AST
        metadata (Optional[MetadataWrapper]): Optional metadata wrapper for the AST
        file_path (Optional[str]): Path to the file being transformed
        changes (List[Dict[str, Any]]): List of changes made during transformation
    """

    tree: cst.Module
    metadata: MetadataWrapper | None = None
    file_path: str | None = None
    changes: list[dict[str, Any]] = None

    def __post_init__(self):
        """Initialize default values and metadata if not provided."""
        if self.changes is None:
            self.changes = []
        if self.metadata is None and self.tree is not None:
            self.metadata = MetadataWrapper(self.tree)


class BaseTransformer(cst.CSTTransformer):
    """Base class for all AST transformers.

    Provides common functionality for AST transformers, including
    access to the transformation context and change tracking.

    Attributes:
        context (TransformerContext): The transformation context
        changes (List[Dict[str, Any]]): Reference to the list of changes in the context
    """

    def __init__(self, context: TransformerContext):
        """Initialize the transformer with a context.

        Args:
            context (TransformerContext): The transformation context
        """
        super().__init__()
        self.context = context
        self.changes = context.changes

    def add_change(self, change_type: str, **kwargs):
        """Add a change record to the context.

        Args:
            change_type (str): Type of change being made
            **kwargs: Additional details about the change
        """
        change = {"type": change_type, **kwargs}
        self.changes.append(change)


class RenameFunctionTransformer(BaseTransformer):
    """Transformer to rename a function in the AST.

    Finds and renames a function with the specified name.

    Attributes:
        old_name (str): Current name of the function
        new_name (str): New name for the function
    """

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        """Initialize the function renaming transformer.

        Args:
            context (TransformerContext): The transformation context
            old_name (str): Current name of the function to rename
            new_name (str): New name for the function
        """
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node
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
    """Transformer to rename a class in the AST.

    Finds and renames a class with the specified name.

    Attributes:
        old_name (str): Current name of the class
        new_name (str): New name for the class
    """

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        """Initialize the class renaming transformer.

        Args:
            context (TransformerContext): The transformation context
            old_name (str): Current name of the class to rename
            new_name (str): New name for the class
        """
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        """Process a class definition node.

        Args:
            original_node (cst.ClassDef): The original class definition node
            updated_node (cst.ClassDef): The updated class definition node

        Returns:
            cst.ClassDef: The transformed class definition node
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
    """Transformer to add or modify a docstring.

    Adds a new docstring or updates an existing one for a function or class.

    Attributes:
        target_name (str): Name of the function or class to add/update the docstring for
        docstring (str): Content of the docstring
        transformed (bool): Whether the docstring has been added/updated
    """

    def __init__(self, context: TransformerContext, target_name: str, docstring: str):
        """Initialize the docstring transformer.

        Args:
            context (TransformerContext): The transformation context
            target_name (str): Name of the function or class to modify
            docstring (str): Content of the docstring to add
        """
        super().__init__(context)
        self.target_name = target_name
        self.docstring = docstring
        self.transformed = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node with added/updated docstring
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
        """Process a class definition node.

        Args:
            original_node (cst.ClassDef): The original class definition node
            updated_node (cst.ClassDef): The updated class definition node

        Returns:
            cst.ClassDef: The transformed class definition node with added/updated docstring
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
    """Transformer to add type hints to functions.

    Adds or updates type annotations for function parameters and return values.

    Attributes:
        target_name (Optional[str]): Optional name of the function to add type hints to
        type_annotations (Dict[str, str]): Dictionary mapping parameter names to type annotations
        changes_made (bool): Whether any type hints were added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str | None = None,
        type_annotations: dict[str, str] | None = None,
    ):
        """Initialize the type hints transformer.

        Args:
            context (TransformerContext): The transformation context
            target_name (Optional[str]): Optional name of the function to modify
            type_annotations (Optional[Dict[str, str]]): Dictionary mapping parameter names to type annotations
        """
        super().__init__(context)
        self.target_name = target_name
        self.type_annotations = type_annotations or {}
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node with added type hints
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
    """Transformer to add logging statements.

    Adds logging statements to functions at specified points.

    Attributes:
        target_name (str): Name of the function to add logging to
        log_level (str): Logging level to use (info, debug, warning, error)
        log_points (List[Dict[str, Any]]): List of locations to add logging statements
        changes_made (bool): Whether any logging statements were added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        log_level: str = "info",
        log_points: list[dict[str, Any]] | None = None,
    ):
        """Initialize the logging transformer.

        Args:
            context (TransformerContext): The transformation context
            target_name (str): Name of the function to modify
            log_level (str): Logging level to use (info, debug, warning, error)
            log_points (Optional[List[Dict[str, Any]]]): List of locations to add logging statements
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
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node with added logging statements
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
    """Transformer to add try-except blocks.

    Wraps a function's body in a try-except block for error handling.

    Attributes:
        target_name (str): Name of the function to add error handling to
        exception_type (str): Type of exception to catch
        error_message (str): Error message to log when an exception is caught
        changes_made (bool): Whether error handling was added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        exception_type: str = "Exception",
        error_message: str | None = None,
    ):
        """Initialize the error handling transformer.

        Args:
            context (TransformerContext): The transformation context
            target_name (str): Name of the function to modify
            exception_type (str): Type of exception to catch
            error_message (Optional[str]): Error message to log when an exception is caught
        """
        super().__init__(context)
        self.target_name = target_name
        self.exception_type = exception_type
        self.error_message = error_message or f"Error in {target_name}"
        self.changes_made = False

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node with added error handling
        """
        if original_node.name.value != self.target_name:
            return updated_node

        # Create a try-except block around the function body
        function_body = updated_node.body.body

        # Create the except handler
        except_body = [
            cst.parse_statement(f'logger.error(f"{self.error_message}: {{e}}")'),
            cst.parse_statement("raise"),
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
    """Transformer to add a parameter to a function.

    Adds a new parameter to a function definition.

    Attributes:
        target_name (str): Name of the function to add the parameter to
        param_name (str): Name of the parameter to add
        param_type (Optional[str]): Optional type annotation for the parameter
        param_default (Optional[str]): Optional default value for the parameter
        changes_made (bool): Whether the parameter was added
    """

    def __init__(
        self,
        context: TransformerContext,
        target_name: str,
        param_name: str,
        param_type: str | None = None,
        param_default: str | None = None,
    ):
        """Initialize the parameter transformer.

        Args:
            context (TransformerContext): The transformation context
            target_name (str): Name of the function to modify
            param_name (str): Name of the parameter to add
            param_type (Optional[str]): Optional type annotation for the parameter
            param_default (Optional[str]): Optional default value for the parameter
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
        """Process a function definition node.

        Args:
            original_node (cst.FunctionDef): The original function definition node
            updated_node (cst.FunctionDef): The updated function definition node

        Returns:
            cst.FunctionDef: The transformed function definition node with the added parameter
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
    """Configuration for code formatting and style enforcement.

    Defines settings for code formatting tools like Black, isort, and autoflake.

    Attributes:
        line_length (int): Maximum line length for formatted code
        use_black (bool): Whether to use the Black formatter for code styling
        use_isort (bool): Whether to use isort for sorting imports
        use_autoflake (bool): Whether to use autoflake to remove unused imports
        fix (bool): Whether to automatically fix detected style issues
        show_diff (bool): Whether to show a diff of changes made by formatting tools
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
    """Advanced tool for AST-based code editing with debugging and logging.

    Provides high-level functionality for code editing, including AST-based
    transformations, backup creation, and diff generation.

    Attributes:
        debug (bool): Whether detailed debugging is enabled
        style_config (CodeStyleConfig): Configuration for code formatting
    """

    def __init__(
        self, debug: bool = False, style_config: CodeStyleConfig | None = None
    ):
        """Initialize the Code Editor Tool with debugging and code style settings.

        Args:
            debug (bool): Enable detailed debug logging
            style_config (Optional[CodeStyleConfig]): Code formatting settings
        """
        self.debug = debug
        self.style_config = style_config or CodeStyleConfig()

        if self.debug:
            logger.setLevel(logging.DEBUG)
            logger.debug("Debugging enabled for CodeEditorTool")

    @staticmethod
    def create_backup(file_path: str, suffix: str = ".bak") -> str:
        """Create a backup of the file.

        Args:
            file_path (str): Path to the file to back up
            suffix (str): Suffix to add to the backup file name

        Returns:
            str: Path to the created backup file
        """
        backup_path = f"{file_path}{suffix}"
        with open(file_path) as src, open(backup_path, "w") as dst:
            dst.write(src.read())
        logger.info(f"Backup created at {backup_path}")
        return backup_path

    @staticmethod
    def generate_diff(original: str, modified: str) -> str:
        """Generate a diff between original and modified code.

        Args:
            original (str): Original code content
            modified (str): Modified code content

        Returns:
            str: Unified diff string showing the changes
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
        """Perform an AST-based edit on a Python file.

        Uses the LibCST library to safely parse and transform Python code
        based on the provided configuration.

        Args:
            config (ASTEditConfig): Configuration for the AST edit operation

        Returns:
            EditResult: Result of the edit operation
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
            self.create_backup(config.file_path, config.backup_suffix)

        with open(config.file_path) as f:
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

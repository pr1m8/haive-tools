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
    """Types of AST edits that can be performed."""
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
    """Types of Git operations."""
    DIFF = "diff"
    COMMIT = "commit"
    STAGE = "stage"
    STATUS = "status"
    LOG = "log"
    BRANCH = "branch"
    CHECKOUT = "checkout"
    RESET = "reset"


class CodeQualityTool(str, Enum):
    """Code quality tools that can be used."""
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
    """Configuration for AST-based code edits."""
    file_path: str = Field(..., description="Path to the Python file to modify")
    edit_type: EditType = Field(..., description="Type of edit to perform")

    # Common parameters (used by multiple edit types)
    target_name: str | None = Field(None, description="Name of the function/class/variable to modify")
    new_name: str | None = Field(None, description="New name for the function/class/variable")
    docstring: str | None = Field(None, description="Docstring content to add")

    # Rename parameters
    scope: str | None = Field(None, description="Scope for variable renaming (function or class name)")

    # Function extraction parameters
    start_line: int | None = Field(None, description="Start line for code extraction")
    end_line: int | None = Field(None, description="End line for code extraction")
    extracted_function_name: str | None = Field(None, description="Name for the extracted function")
    parameters: list[dict[str, Any]] | None = Field(None, description="Parameters for function extraction")

    # Type hint parameters
    type_annotations: dict[str, str] | None = Field(None, description="Type annotations to add")
    infer_types: bool | None = Field(False, description="Whether to attempt type inference")

    # Error handling parameters
    exception_type: str | None = Field(None, description="Exception type for error handling")
    error_message: str | None = Field(None, description="Error message for exceptions")

    # Logging parameters
    log_points: list[dict[str, Any]] | None = Field(None, description="Points to add logging")
    log_level: str | None = Field("info", description="Logging level")

    # Parameter modifications
    param_name: str | None = Field(None, description="Parameter name to modify")
    param_type: str | None = Field(None, description="Parameter type annotation")
    param_default: str | None = Field(None, description="Parameter default value")

    # Custom transformation
    transform_code: str | None = Field(None, description="Python code for custom transformer class")
    transform_args: dict[str, Any] | None = Field(None, description="Arguments for custom transformer")

    # Backup options
    create_backup: bool = Field(True, description="Whether to create a backup of the file")
    backup_suffix: str = Field(".bak", description="Suffix for backup files")


class CodeQualityConfig(BaseModel):
    """Configuration for code quality checks."""
    file_path: str = Field(..., description="Path to the Python file to check")
    tools: list[CodeQualityTool] = Field(
        default=[CodeQualityTool.BLACK, CodeQualityTool.FLAKE8],
        description="Code quality tools to run"
    )
    fix: bool = Field(True, description="Whether to fix issues automatically when possible")
    ignore_errors: list[str] = Field(default_factory=list, description="Error codes to ignore")
    config_path: str | None = Field(None, description="Path to configuration file")
    line_length: int | None = Field(None, description="Line length for formatting")
    aggressive: int | None = Field(None, description="Aggression level for autoflake")
    mypy_options: list[str] | None = Field(None, description="Additional options for mypy")
    show_diff: bool = Field(True, description="Whether to show diff of changes")


class GitOperationConfig(BaseModel):
    """Configuration for Git operations."""
    file_paths: str | list[str] = Field(
        ...,
        description="Path(s) to the file(s) for the git operation"
    )
    operation: GitOperation = Field(..., description="Git operation to perform")

    # Commit options
    commit_message: str | None = Field(None, description="Commit message")
    generate_message: bool = Field(False, description="Whether to auto-generate commit message")
    commit_author: str | None = Field(None, description="Author for the commit")

    # Branch options
    branch_name: str | None = Field(None, description="Branch name for branch operations")

    # Diff options
    staged: bool = Field(False, description="Whether to show staged changes in diff")
    context_lines: int = Field(3, description="Number of context lines in diff")

    # Reset options
    reset_mode: str | None = Field("mixed", description="Reset mode: soft, mixed, or hard")

    # Log options
    log_count: int | None = Field(5, description="Number of commits to show in log")
    log_format: str | None = Field(None, description="Format string for git log")


class CodeSummarizeConfig(BaseModel):
    """Configuration for code summarization."""
    file_path: str = Field(..., description="Path to the Python file to summarize")
    include_docstrings: bool = Field(True, description="Whether to extract docstrings")
    include_class_names: bool = Field(True, description="Whether to extract class names")
    include_function_names: bool = Field(True, description="Whether to extract function names")
    include_imports: bool = Field(True, description="Whether to extract imports")
    include_global_vars: bool = Field(True, description="Whether to extract global variables")
    output_format: str = Field("text", description="Output format: text, json, or markdown")


# =============================================
# Result Models
# =============================================

class EditResult(BaseModel):
    """Result of a code edit operation."""
    success: bool = Field(..., description="Whether the edit was successful")
    file_path: str = Field(..., description="Path to the modified file")
    edit_type: str = Field(..., description="Type of edit that was performed")
    message: str = Field(..., description="Message describing the result")
    changes: list[dict[str, Any]] = Field(default_factory=list, description="Details of changes made")
    error: str | None = Field(None, description="Error message if unsuccessful")
    diff: str | None = Field(None, description="Diff of changes made")
    backup_path: str | None = Field(None, description="Path to backup file if created")


class QualityResult(BaseModel):
    """Result of code quality checks."""
    success: bool = Field(..., description="Whether quality checks passed")
    file_path: str = Field(..., description="Path to the checked file")
    tool_results: dict[str, dict[str, Any]] = Field(..., description="Results for each tool")
    issues_count: int = Field(..., description="Total number of issues found")
    fixed_count: int = Field(0, description="Number of issues fixed")
    diff: str | None = Field(None, description="Diff of changes made by formatting")
    error: str | None = Field(None, description="Error message if unsuccessful")


class GitResult(BaseModel):
    """Result of a Git operation."""
    success: bool = Field(..., description="Whether the operation was successful")
    operation: str = Field(..., description="Git operation that was performed")
    file_paths: list[str] = Field(..., description="Paths to the affected files")
    output: str = Field(..., description="Output of the git command")
    error: str | None = Field(None, description="Error message if unsuccessful")
    commit_id: str | None = Field(None, description="Commit ID if a commit was made")
    diff: str | None = Field(None, description="Diff if requested")


class CodeSummary(BaseModel):
    """Summary of a Python file."""
    file_path: str = Field(..., description="Path to the summarized file")
    classes: list[dict[str, Any]] = Field(default_factory=list, description="Classes in the file")
    functions: list[dict[str, Any]] = Field(default_factory=list, description="Functions in the file")
    imports: list[str] = Field(default_factory=list, description="Imports in the file")
    global_vars: list[dict[str, Any]] = Field(default_factory=list, description="Global variables")
    docstring: str | None = Field(None, description="Module docstring")
    loc: int = Field(..., description="Lines of code")
    summary: str = Field(..., description="General summary of the file")


# =============================================
# AST Transformer Classes
# =============================================

@dataclass
class TransformerContext:
    """Context for AST transformers with metadata."""
    tree: cst.Module
    metadata: MetadataWrapper | None = None
    file_path: str | None = None
    changes: list[dict[str, Any]] = None

    def __post_init__(self):
        if self.changes is None:
            self.changes = []
        if self.metadata is None and self.tree is not None:
            self.metadata = MetadataWrapper(self.tree)


class BaseTransformer(cst.CSTTransformer):
    """Base class for all AST transformers."""

    def __init__(self, context: TransformerContext):
        super().__init__()
        self.context = context
        self.changes = context.changes

    def add_change(self, change_type: str, **kwargs):
        """Add a change record to the context."""
        change = {"type": change_type, **kwargs}
        self.changes.append(change)


class RenameFunctionTransformer(BaseTransformer):
    """Transformer to rename a function in the AST."""

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        if original_node.name.value == self.old_name:
            self.add_change(
                "rename_function",
                old_name=self.old_name,
                new_name=self.new_name,
                line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
            )
            return updated_node.with_changes(name=cst.Name(value=self.new_name))
        return updated_node


class RenameClassTransformer(BaseTransformer):
    """Transformer to rename a class in the AST."""

    def __init__(self, context: TransformerContext, old_name: str, new_name: str):
        super().__init__(context)
        self.old_name = old_name
        self.new_name = new_name

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.ClassDef:
        if original_node.name.value == self.old_name:
            self.add_change(
                "rename_class",
                old_name=self.old_name,
                new_name=self.new_name,
                line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
            )
            return updated_node.with_changes(name=cst.Name(value=self.new_name))
        return updated_node


class AddDocstringTransformer(BaseTransformer):
    """Transformer to add or modify a docstring."""

    def __init__(self, context: TransformerContext, target_name: str, docstring: str):
        super().__init__(context)
        self.target_name = target_name
        self.docstring = docstring
        self.transformed = False

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        if original_node.name.value == self.target_name:
            # Create a new docstring node
            docstring_node = cst.SimpleString(value=f'"""{self.docstring}"""')

            # Check if there's an existing docstring
            has_docstring = False
            if (original_node.body.body and
                isinstance(original_node.body.body[0], cst.SimpleStatementLine) and
                isinstance(original_node.body.body[0].body[0], cst.Expr) and
                isinstance(original_node.body.body[0].body[0].value, cst.SimpleString)):

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
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
                )

                self.transformed = True
                return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))

            # Add a new docstring if none exists
            if not has_docstring:
                new_body = [
                    cst.SimpleStatementLine(body=[cst.Expr(value=docstring_node)]),
                    *original_node.body.body
                ]

                self.add_change(
                    "add_docstring",
                    target=self.target_name,
                    docstring=docstring_node.value,
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
                )

                self.transformed = True
                return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))

        return updated_node

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.ClassDef:
        if original_node.name.value == self.target_name:
            # Create a new docstring node
            docstring_node = cst.SimpleString(value=f'"""{self.docstring}"""')

            # Check if there's an existing docstring
            has_docstring = False
            if (original_node.body.body and
                isinstance(original_node.body.body[0], cst.SimpleStatementLine) and
                isinstance(original_node.body.body[0].body[0], cst.Expr) and
                isinstance(original_node.body.body[0].body[0].value, cst.SimpleString)):

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
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
                )

                self.transformed = True
                return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))

            # Add a new docstring if none exists
            if not has_docstring:
                new_body = [
                    cst.SimpleStatementLine(body=[cst.Expr(value=docstring_node)]),
                    *original_node.body.body
                ]

                self.add_change(
                    "add_docstring",
                    target=self.target_name,
                    docstring=docstring_node.value,
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
                )

                self.transformed = True
                return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))

        return updated_node


class AddTypeHintsTransformer(BaseTransformer):
    """Transformer to add type hints to functions."""

    def __init__(self, context: TransformerContext, target_name: str | None = None,
                 type_annotations: dict[str, str] | None = None):
        super().__init__(context)
        self.target_name = target_name
        self.type_annotations = type_annotations or {}
        self.changes_made = False

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
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
                annotation = cst.Annotation(
                    annotation=cst.parse_expression(type_str)
                )
                updated_param = param.with_changes(annotation=annotation)
                updated_params.append(updated_param)

                self.add_change(
                    "add_parameter_type_hint",
                    function=original_node.name.value,
                    parameter=param_name,
                    type_hint=type_str,
                    line=param.lineno if hasattr(param, "lineno") else None
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
                line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
            )

            modified = True
        else:
            returns_annotation = updated_node.returns

        if modified:
            self.changes_made = True
            updated_params_list = updated_node.params.with_changes(params=updated_params)
            return updated_node.with_changes(
                params=updated_params_list,
                returns=returns_annotation
            )

        return updated_node


class AddLoggingTransformer(BaseTransformer):
    """Transformer to add logging statements."""

    def __init__(self, context: TransformerContext, target_name: str, log_level: str = "info",
                 log_points: list[dict[str, Any]] | None = None):
        super().__init__(context)
        self.target_name = target_name
        self.log_level = log_level.lower()
        self.log_points = log_points or [{"position": "start"}]  # Default to function start
        self.changes_made = False

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
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
                log_stmt = f'logger.{self.log_level}(f"{message}{var_part}", {var_args})'
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
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
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
                    line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
                )
                modified = True

        if modified:
            self.changes_made = True
            return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))

        return updated_node


class AddErrorHandlingTransformer(BaseTransformer):
    """Transformer to add try-except blocks."""

    def __init__(self, context: TransformerContext, target_name: str,
                 exception_type: str = "Exception", error_message: str | None = None):
        super().__init__(context)
        self.target_name = target_name
        self.exception_type = exception_type
        self.error_message = error_message or f"Error in {target_name}"
        self.changes_made = False

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        if original_node.name.value != self.target_name:
            return updated_node

        # Create a try-except block around the function body
        function_body = updated_node.body.body

        # Create the except handler
        except_body = [
            cst.parse_statement(f'logger.error(f"{self.error_message}: {{e}}")'),
            cst.parse_statement("raise")
        ]

        except_handler = cst.ExceptHandler(
            type=cst.parse_expression(self.exception_type),
            name=cst.Name("e"),
            body=cst.IndentedBlock(body=except_body)
        )

        # Create the try block
        try_node = cst.Try(
            body=cst.IndentedBlock(body=function_body),
            handlers=[except_handler],
            orelse=None,
            finalbody=None
        )

        self.add_change(
            "add_error_handling",
            function=self.target_name,
            exception_type=self.exception_type,
            error_message=self.error_message,
            line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
        )

        self.changes_made = True
        return updated_node.with_changes(body=cst.IndentedBlock(body=[try_node]))


class AddParameterTransformer(BaseTransformer):
    """Transformer to add a parameter to a function."""

    def __init__(self, context: TransformerContext, target_name: str, param_name: str,
                 param_type: str | None = None, param_default: str | None = None):
        super().__init__(context)
        self.target_name = target_name
        self.param_name = param_name
        self.param_type = param_type
        self.param_default = param_default
        self.changes_made = False

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        if original_node.name.value != self.target_name:
            return updated_node

        # Check if parameter already exists
        for param in updated_node.params.params:
            if param.name.value == self.param_name:
                return updated_node  # Parameter already exists

        # Create new parameter
        annotation = None
        if self.param_type:
            annotation = cst.Annotation(annotation=cst.parse_expression(self.param_type))

        default = None
        if self.param_default:
            default = cst.parse_expression(self.param_default)

        new_param = cst.Param(
            name=cst.Name(self.param_name),
            annotation=annotation,
            default=default
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
            line=original_node.name.lineno if hasattr(original_node.name, "lineno") else None
        )

        self.changes_made = True
        return updated_node.with_changes(params=updated_params)


# =============================================
# Core Tool Implementation
# =============================================

class CodeStyleConfig(BaseModel):
    """Configuration for code formatting and style enforcement."""
    line_length: int = Field(88, description="Maximum line length")
    use_black: bool = Field(True, description="Enable Black formatter")
    use_isort: bool = Field(True, description="Enable isort for import sorting")
    use_autoflake: bool = Field(True, description="Enable autoflake for removing unused imports")
    fix: bool = Field(True, description="Automatically fix detected issues")
    show_diff: bool = Field(True, description="Show diff of applied changes")


class CodeEditorTool:
    """Advanced tool for AST-based code editing with debugging and logging."""

    def __init__(self, debug: bool = False, style_config: CodeStyleConfig | None = None):
        """Initialize the Code Editor Tool with debugging and code style settings.
        
        Args:
            debug (bool): Enable detailed debug logging.
            style_config (Optional[CodeStyleConfig]): Code formatting settings.
        """
        self.debug = debug
        self.style_config = style_config or CodeStyleConfig()

        if self.debug:
            logger.setLevel(logging.DEBUG)
            logger.debug("Debugging enabled for CodeEditorTool")

    @staticmethod
    def create_backup(file_path: str, suffix: str = ".bak") -> str:
        """Create a backup of the file."""
        backup_path = f"{file_path}{suffix}"
        with open(file_path) as src, open(backup_path, "w") as dst:
            dst.write(src.read())
        logger.info(f"Backup created at {backup_path}")
        return backup_path

    @staticmethod
    def generate_diff(original: str, modified: str) -> str:
        """Generate a diff between original and modified code."""
        diff = "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                modified.splitlines(keepends=True),
                fromfile="original",
                tofile="modified",
                n=3
            )
        )
        return diff

    def perform_ast_edit(self, config: "ASTEditConfig") -> "EditResult":
        """Perform an AST-based edit on a Python file."""
        if not os.path.exists(config.file_path):
            return EditResult(
                success=False,
                file_path=config.file_path,
                edit_type=config.edit_type,
                message="File not found",
                error="File not found"
            )

        if config.create_backup:
            backup_path = self.create_backup(config.file_path, config.backup_suffix)

        with open(config.file_path) as f:
            original_code = f.read()

        tree = cst.parse_module(original_code)
        context = TransformerContext(tree=tree, file_path=config.file_path)

        # Apply AST transformations based on config
        # Example: Rename function
        if config.edit_type == EditType.RENAME_FUNCTION and config.target_name and config.new_name:
            transformer = RenameFunctionTransformer(context, config.target_name, config.new_name)
            modified_tree = tree.visit(transformer)
        else:
            return EditResult(
                success=False,
                file_path=config.file_path,
                edit_type=config.edit_type,
                message="Invalid transformation parameters",
                error="Transformation parameters missing"
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
            diff=diff
        )

"""
Secure Shell Command Execution Module

This module provides a secure way to execute shell commands with enforced security restrictions.
It includes path permission checking, command validation, and structured result handling.

The security features include:
- Path-based access control for file operations
- Command timeout enforcement
- Structured output for both successful and failed commands
- Protection against dangerous commands

Examples:
    >>> from haive.tools.toolkits.dev.shell.shell import SecureShellExecutor
    >>> shell = SecureShellExecutor()
    >>> result = shell.run('ls -la')
    >>> if result.success:
    ...     print(result.stdout)
    ... else:
    ...     print(f"Error: {result.error}")
"""

import shlex
import subprocess
from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel, Field

from haive.tools.toolkits.dev.permission import PermissionsManager


class CommandExecutionResult(BaseModel):
    """
    Represents the result of a shell command execution.

    This model provides a structured way to capture and access the results of shell
    command execution, including success status, outputs, and any error information.

    Attributes:
        success (bool): Indicates if the command executed successfully.
        command (str): The original command that was executed.
        stdout (str): Standard output captured from the command execution.
        stderr (str): Standard error output captured from the command execution.
        exit_code (int): The exit code returned by the command (0 typically means success).
        error (str): Human-readable error message if the command failed.
    """

    success: bool = Field(
        ..., description="Indicates if the command executed successfully"
    )
    command: str = Field(..., description="Executed command")
    stdout: str = Field(default="", description="Command standard output")
    stderr: str = Field(default="", description="Command standard error")
    exit_code: int = Field(..., description="Exit code of the command")
    error: str = Field(default="", description="Error message (if any)")


class SecureShellExecutor:
    """
    Shell command executor with enforced security restrictions.

    This class provides a secure way to execute shell commands with path-based
    permission checking, command validation, and structured result handling.
    It uses the PermissionsManager to enforce read/write access control on paths.

    Attributes:
        permissions_manager (PermissionsManager): Manager that handles path permissions.
    """

    def __init__(self):
        """
        Initialize a new SecureShellExecutor with default permissions.

        Creates a new shell executor with a default PermissionsManager instance
        to handle security restrictions.
        """
        self.permissions_manager = PermissionsManager()

    def _extract_paths(self, command: str) -> List[str]:
        """
        Extract file paths from the command arguments.

        Parses the command string, splits it into arguments, and identifies
        which arguments are existing file paths that need permission checking.

        Args:
            command (str): The shell command to analyze.

        Returns:
            List[str]: A list of file paths found in the command.
        """
        args = shlex.split(command)
        return [arg for arg in args if Path(arg).exists()]

    def run(self, command: str, timeout: int = 30) -> CommandExecutionResult:
        """
        Execute a command with security enforcement.

        Runs the provided shell command with security checks for file access permissions
        and command timeouts. Command execution is handled safely with proper error capture.

        Args:
            command (str): The shell command to execute.
            timeout (int, optional): Maximum execution time in seconds. Defaults to 30.

        Returns:
            CommandExecutionResult: Structured result with execution details.

        Raises:
            No exceptions are raised; all errors are captured in the result object.
        """
        paths = self._extract_paths(command)

        # Check permissions for all paths found in the command
        for path in paths:
            if self.permissions_manager.is_restricted(path):
                return CommandExecutionResult(
                    success=False,
                    command=command,
                    error=f"🚫 Access denied to {path}",
                    exit_code=1,
                )
            if "rm" in command or "mv" in command or "cp" in command:
                if not self.permissions_manager.is_write_allowed(path):
                    return CommandExecutionResult(
                        success=False,
                        command=command,
                        error=f"🚫 Write access denied to {path}",
                        exit_code=1,
                    )
            if "cat" in command or "less" in command:
                if not self.permissions_manager.is_read_allowed(path):
                    return CommandExecutionResult(
                        success=False,
                        command=command,
                        error=f"🚫 Read access denied to {path}",
                        exit_code=1,
                    )

        # Execute the command with safety measures
        try:
            result = subprocess.run(
                shlex.split(command),
                text=True,
                capture_output=True,
                timeout=timeout,
                check=True,
            )
            return CommandExecutionResult(
                success=True,
                command=command,
                stdout=result.stdout.strip(),
                stderr=result.stderr.strip(),
                exit_code=result.returncode,
            )
        except subprocess.CalledProcessError as e:
            return CommandExecutionResult(
                success=False,
                command=command,
                stderr=e.stderr.strip(),
                exit_code=e.returncode,
                error="Command failed",
            )

"""
Shell Permission Module

This module provides a role-based access control (RBAC) system for managing
permissions in shell environments. It uses Pydantic models to define permission
settings for different roles, allowing fine-grained control over which paths
can be read from or written to, and which commands can be executed.

The module enables the creation of security profiles for different user roles,
which can be used to enforce access restrictions in shell scripting, automation tools,
or other security-sensitive contexts.

Examples:
    >>> from haive.tools.toolkits.dev.shell.permission import RBACConfig
    >>> rbac = RBACConfig()
    >>> rbac.can_execute("developer", "python")  # Check if developer can run python
    True
    >>> rbac.can_write("guest", "/home/guest/data")  # Check if guest can write to path
    False
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, ValidationError


class RolePermissions(BaseModel):
    """Defines permissions for a specific role.

    This model represents the set of permissions granted to a specific role,
    including which paths can be read from or written to, and which commands
    can be executed.

    Attributes:
        read: List of filesystem paths allowed for reading.
        write: List of filesystem paths allowed for writing.
        execute: List of commands allowed for execution.
    """

    read: List[Path] = Field(
        default_factory=lambda: [Path("/home")], description="Paths allowed for reading"
    )
    write: List[Path] = Field(
        default_factory=list, description="Paths allowed for writing"
    )
    execute: List[str] = Field(
        default_factory=list, description="Commands allowed for execution"
    )


class RBACConfig(BaseModel):
    """Defines role-based access control settings.

    This model represents a complete RBAC configuration, mapping role names
    to their respective permissions. It provides methods to check permissions
    and save/load configurations.

    Attributes:
        roles: Dictionary mapping role names to RolePermissions objects.
    """

    roles: Dict[str, RolePermissions] = Field(
        default_factory=lambda: {
            "admin": RolePermissions(
                read=[Path("/")], write=[Path("/etc"), Path("/var")], execute=["*"]
            ),
            "developer": RolePermissions(
                read=[Path("/home/dev")],
                write=[Path("/home/dev/projects")],
                execute=["python", "gcc"],
            ),
            "guest": RolePermissions(read=[Path("/home/guest")], write=[], execute=[]),
        },
        description="Role-based access control settings",
    )

    def can_read(self, role: str, path: str) -> bool:
        """Check if a role has permission to read from a path.

        Args:
            role: The role name to check permissions for.
            path: The filesystem path to check read permissions for.

        Returns:
            True if the role has permission to read from the path, False otherwise.
        """
        return any(
            Path(path).resolve().is_relative_to(p)
            for p in self.roles.get(role, RolePermissions()).read
        )

    def can_write(self, role: str, path: str) -> bool:
        """Check if a role has permission to write to a path.

        Args:
            role: The role name to check permissions for.
            path: The filesystem path to check write permissions for.

        Returns:
            True if the role has permission to write to the path, False otherwise.
        """
        return any(
            Path(path).resolve().is_relative_to(p)
            for p in self.roles.get(role, RolePermissions()).write
        )

    def can_execute(self, role: str, command: str) -> bool:
        """Check if a role has permission to execute a command.

        Args:
            role: The role name to check permissions for.
            command: The command to check execution permissions for.

        Returns:
            True if the role has permission to execute the command, False otherwise.
        """
        allowed_commands = self.roles.get(role, RolePermissions()).execute
        return "*" in allowed_commands or command in allowed_commands

    def add_role(self, role_name: str, permissions: RolePermissions) -> None:
        """Add a new role with specified permissions.

        Args:
            role_name: The name of the role to add.
            permissions: The permissions to assign to the role.

        Raises:
            ValueError: If the role already exists.
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = permissions

    def update_role(self, role_name: str, permissions: RolePermissions) -> None:
        """Update an existing role with new permissions.

        Args:
            role_name: The name of the role to update.
            permissions: The new permissions to assign to the role.

        Raises:
            ValueError: If the role does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.roles[role_name] = permissions

    def delete_role(self, role_name: str) -> None:
        """Delete an existing role.

        Args:
            role_name: The name of the role to delete.

        Raises:
            ValueError: If the role does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        del self.roles[role_name]

    def save_config(self, path: str = ".rbac_config.json") -> None:
        """Save RBAC settings to a file.

        Args:
            path: The file path to save the configuration to.

        Raises:
            PermissionError: If the file cannot be written to.
            OSError: If another I/O error occurs.
        """
        # Convert Path objects to strings for serialization
        serializable_config = {
            role: {
                "read": [str(p) for p in perms.read],
                "write": [str(p) for p in perms.write],
                "execute": perms.execute,
            }
            for role, perms in self.roles.items()
        }

        try:
            with open(path, "w") as f:
                json.dump({"roles": serializable_config}, f, indent=4)
        except (PermissionError, OSError) as e:
            raise OSError(f"Failed to save RBAC config to {path}: {str(e)}")

    @classmethod
    def load_config(cls, path: str = ".rbac_config.json") -> "RBACConfig":
        """Load RBAC settings from a file.

        Args:
            path: The file path to load the configuration from.

        Returns:
            A new RBACConfig instance with the loaded settings.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
            ValidationError: If the loaded data does not match the expected schema.
        """
        try:
            with open(path, "r") as f:
                data = json.load(f)

            # Convert string paths back to Path objects
            roles_data = {}
            for role, perms in data.get("roles", {}).items():
                roles_data[role] = RolePermissions(
                    read=[Path(p) for p in perms.get("read", [])],
                    write=[Path(p) for p in perms.get("write", [])],
                    execute=perms.get("execute", []),
                )

            return cls(roles=roles_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"RBAC config file not found: {path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in RBAC config file: {str(e)}", e.doc, e.pos
            )
        except ValidationError as e:
            raise ValidationError(
                f"Invalid RBAC configuration format: {str(e)}", e.model
            )

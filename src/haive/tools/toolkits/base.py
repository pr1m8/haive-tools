"""Base module for all toolkit implementations.

This module defines common interfaces and functionality shared across all toolkits.
It provides abstract base classes and utility functions for creating consistent
toolkit implementations.

Toolkits are collections of related tools that can be used together to perform
complex tasks. For example, a database toolkit might include tools for querying,
inserting, updating, and deleting data.

Typical usage:
    from haive.tools.toolkits.base import BaseToolkit

    class MyCustomToolkit(BaseToolkit):
        # Implementation details...
"""

from abc import ABC, abstractmethod

from langchain_core.tools import BaseTool, BaseToolkit
from pydantic import BaseModel, ConfigDict, Field


class HaiveToolkitConfig(BaseModel):
    """Base configuration class for Haive toolkits.

    All toolkit configurations should inherit from this class to ensure
    consistent configuration patterns across the platform.

    Attributes:
        name: A human-readable name for the toolkit.
        description: A detailed description of what the toolkit does.
    """

    name: str = Field(..., description="Human-readable name for the toolkit")
    description: str = Field(
        ..., description="Detailed description of the toolkit's purpose"
    )


class HaiveToolkit(BaseToolkit, ABC):
    """Base class for all Haive toolkits.

    This abstract class defines the interface that all toolkit implementations
    must follow. It provides common functionality and ensures consistent
    behavior across toolkit implementations.

    Attributes:
        config: The configuration for this toolkit.
    """

    config: HaiveToolkitConfig

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @abstractmethod
    def get_tools(self) -> list[BaseTool]:
        """Get the list of tools in this toolkit.

        Returns:
            A list of BaseTool instances that make up this toolkit.
        """

    @classmethod
    @abstractmethod
    def from_config(cls, config: HaiveToolkitConfig) -> "HaiveToolkit":
        """Create a toolkit instance from a configuration.

        Args:
            config: The configuration to use for creating the toolkit.

        Returns:
            A new instance of the toolkit.
        """

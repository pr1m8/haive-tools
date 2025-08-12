
:py:mod:`shell`
===============

.. py:module:: shell

Secure Shell Command Execution Module.

This module provides a secure way to execute shell commands with enforced security restrictions.
It includes path permission checking, command validation, and structured result handling.

The security features include:
- Path-based access control for file operations
- Command timeout enforcement
- Structured output for both successful and failed commands
- Protection against dangerous commands

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.shell.shell import SecureShellExecutor
>>> shell = SecureShellExecutor()
>>> result = shell.run('ls -la')
>>> if result.success:
...     print(result.stdout)
... else:
...     print(f"Error: {result.error}")


.. autolink-examples:: shell
   :collapse:

Classes
-------

.. autoapisummary::

   shell.CommandExecutionResult
   shell.SecureShellExecutor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CommandExecutionResult:

   .. graphviz::
      :align: center

      digraph inheritance_CommandExecutionResult {
        node [shape=record];
        "CommandExecutionResult" [label="CommandExecutionResult"];
        "pydantic.BaseModel" -> "CommandExecutionResult";
      }

.. autopydantic_model:: shell.CommandExecutionResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SecureShellExecutor:

   .. graphviz::
      :align: center

      digraph inheritance_SecureShellExecutor {
        node [shape=record];
        "SecureShellExecutor" [label="SecureShellExecutor"];
      }

.. autoclass:: shell.SecureShellExecutor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: shell
   :collapse:
   
.. autolink-skip:: next

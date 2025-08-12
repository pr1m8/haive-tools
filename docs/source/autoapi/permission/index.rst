
:py:mod:`permission`
====================

.. py:module:: permission

Shell Permission Module.

This module provides a role-based access control (RBAC) system for managing
permissions in shell environments. It uses Pydantic models to define permission
settings for different roles, allowing fine-grained control over which paths
can be read from or written to, and which commands can be executed.

The module enables the creation of security profiles for different user roles,
which can be used to enforce access restrictions in shell scripting, automation tools,
or other security-sensitive contexts.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.shell.permission import RBACConfig
>>> rbac = RBACConfig()
>>> rbac.can_execute("developer", "python")  # Check if developer can run python
True
>>> rbac.can_write("guest", "/home/guest/data")  # Check if guest can write to path
False


.. autolink-examples:: permission
   :collapse:

Classes
-------

.. autoapisummary::

   permission.RBACConfig
   permission.RolePermissions


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RBACConfig:

   .. graphviz::
      :align: center

      digraph inheritance_RBACConfig {
        node [shape=record];
        "RBACConfig" [label="RBACConfig"];
        "pydantic.BaseModel" -> "RBACConfig";
      }

.. autopydantic_model:: permission.RBACConfig
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

   Inheritance diagram for RolePermissions:

   .. graphviz::
      :align: center

      digraph inheritance_RolePermissions {
        node [shape=record];
        "RolePermissions" [label="RolePermissions"];
        "pydantic.BaseModel" -> "RolePermissions";
      }

.. autopydantic_model:: permission.RolePermissions
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





.. rubric:: Related Links

.. autolink-examples:: permission
   :collapse:
   
.. autolink-skip:: next

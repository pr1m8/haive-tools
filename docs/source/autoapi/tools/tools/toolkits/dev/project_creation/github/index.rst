
:py:mod:`tools.tools.toolkits.dev.project_creation.github`
==========================================================

.. py:module:: tools.tools.toolkits.dev.project_creation.github

GitHub Project Creation Module.

This module provides utilities for creating and initializing GitHub repositories
programmatically. It offers functionality to create repositories, set up branch
protection rules, configure GitHub Actions workflows, and manage repository
settings through the GitHub API.

The module abstracts the complexities of GitHub repository setup and provides
a simple interface for creating standardized projects with best practices
automatically applied.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.project_creation.github import GitHubProjectCreator
>>> creator = GitHubProjectCreator(token="your-github-token")
>>> creator.create_repository("my-new-project", private=True, team_access=["engineering"])


.. autolink-examples:: tools.tools.toolkits.dev.project_creation.github
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.dev.project_creation.github.BranchProtectionRule
   tools.tools.toolkits.dev.project_creation.github.GitHubProjectCreator
   tools.tools.toolkits.dev.project_creation.github.RepositorySettings


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BranchProtectionRule:

   .. graphviz::
      :align: center

      digraph inheritance_BranchProtectionRule {
        node [shape=record];
        "BranchProtectionRule" [label="BranchProtectionRule"];
        "pydantic.BaseModel" -> "BranchProtectionRule";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.project_creation.github.BranchProtectionRule
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

   Inheritance diagram for GitHubProjectCreator:

   .. graphviz::
      :align: center

      digraph inheritance_GitHubProjectCreator {
        node [shape=record];
        "GitHubProjectCreator" [label="GitHubProjectCreator"];
      }

.. autoclass:: tools.tools.toolkits.dev.project_creation.github.GitHubProjectCreator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RepositorySettings:

   .. graphviz::
      :align: center

      digraph inheritance_RepositorySettings {
        node [shape=record];
        "RepositorySettings" [label="RepositorySettings"];
        "pydantic.BaseModel" -> "RepositorySettings";
      }

.. autopydantic_model:: tools.tools.toolkits.dev.project_creation.github.RepositorySettings
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

.. autolink-examples:: tools.tools.toolkits.dev.project_creation.github
   :collapse:
   
.. autolink-skip:: next

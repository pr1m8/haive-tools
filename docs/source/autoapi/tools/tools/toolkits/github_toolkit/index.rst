
:py:mod:`tools.tools.toolkits.github_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.github_toolkit

GitHub Toolkit Module.

This module provides a toolkit for interacting with GitHub repositories and API.
It wraps the GitHubToolkit from LangChain community tools, providing access to
GitHub issues, repositories, pull requests, and other GitHub features using
the GitHub API.

The toolkit requires GitHub App credentials (App ID and Private Key) which can
be obtained by creating a GitHub App in your GitHub account settings.

.. rubric:: Examples

>>> from haive.tools.toolkits.github_toolkit import github_toolkit
>>> tools = github_toolkit.get_tools()
>>> # Use tools to interact with GitHub repositories


.. autolink-examples:: tools.tools.toolkits.github_toolkit
   :collapse:





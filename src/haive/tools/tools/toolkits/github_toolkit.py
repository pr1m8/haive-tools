"""GitHub Toolkit Module.

This module provides a toolkit for interacting with GitHub repositories and API.
It wraps the GitHubToolkit from LangChain community tools, providing access to
GitHub issues, repositories, pull requests, and other GitHub features using
the GitHub API.

The toolkit requires GitHub App credentials (App ID and Private Key) which can
be obtained by creating a GitHub App in your GitHub account settings.

Examples:
    >>> from haive.tools.toolkits.github_toolkit import github_toolkit
    >>> tools = github_toolkit.get_tools()
    >>> # Use tools to interact with GitHub repositories

"""

import getpass

from haive.config.config import Config
from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper

# Check if GitHub credentials are available, prompt for them if not
if not Config.GITHUB_APP_ID or not Config.GITHUB_APP_PRIVATE_KEY:
    Config.GITHUB_APP_ID = getpass.getpass("Enter your GitHub App ID: ")
    Config.GITHUB_APP_PRIVATE_KEY = getpass.getpass(
        "Enter your GitHub App Private Key: "
    )

# Initialize GitHub API wrapper with credentials
github = GitHubAPIWrapper(
    app_id=Config.GITHUB_APP_ID, private_key=Config.GITHUB_APP_PRIVATE_KEY
)

# Create GitHub toolkit from the API wrapper
github_toolkit = GitHubToolkit.from_github_api_wrapper(github)

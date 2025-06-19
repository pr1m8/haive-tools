"""
GitHub Project Creation Module

This module provides utilities for creating and initializing GitHub repositories
programmatically. It offers functionality to create repositories, set up branch
protection rules, configure GitHub Actions workflows, and manage repository
settings through the GitHub API.

The module abstracts the complexities of GitHub repository setup and provides
a simple interface for creating standardized projects with best practices
automatically applied.

Examples:
    >>> from haive.tools.toolkits.dev.project_creation.github import GitHubProjectCreator
    >>> creator = GitHubProjectCreator(token="your-github-token")
    >>> creator.create_repository("my-new-project", private=True, team_access=["engineering"])
"""

import os
from typing import Any, Dict, List, Optional, Union

import requests
from pydantic import BaseModel, Field, SecretStr


class RepositorySettings(BaseModel):
    """Configuration settings for GitHub repository creation.

    Attributes:
        name: Name of the repository to create.
        description: A short description of the repository purpose.
        private: Whether the repository should be private or public.
        auto_init: Whether to initialize with a README.
        gitignore_template: Which gitignore template to apply.
        license_template: Which license template to apply.
        team_access: List of team names to grant access to.
        branch_protection: Whether to set up branch protection rules.
        default_branch: The default branch name.
    """

    name: str = Field(..., description="Name of the repository to create")
    description: str = Field(
        "", description="A short description of the repository purpose"
    )
    private: bool = Field(
        True, description="Whether the repository should be private or public"
    )
    auto_init: bool = Field(True, description="Whether to initialize with a README")
    gitignore_template: Optional[str] = Field(
        None, description="Which gitignore template to apply"
    )
    license_template: Optional[str] = Field(
        None, description="Which license template to apply"
    )
    team_access: List[str] = Field(
        default_factory=list, description="List of team names to grant access to"
    )
    branch_protection: bool = Field(
        True, description="Whether to set up branch protection rules"
    )
    default_branch: str = Field("main", description="The default branch name")


class BranchProtectionRule(BaseModel):
    """Configuration for branch protection rules.

    Attributes:
        required_approvals: Number of required approving reviews.
        dismiss_stale_reviews: Whether to dismiss approvals when new commits are pushed.
        require_code_owner_reviews: Whether to require review from code owners.
        required_status_checks: List of status checks that must pass before merging.
        enforce_admins: Whether to enforce restrictions for repository administrators.
    """

    required_approvals: int = Field(
        1, description="Number of required approving reviews"
    )
    dismiss_stale_reviews: bool = Field(
        True, description="Whether to dismiss approvals when new commits are pushed"
    )
    require_code_owner_reviews: bool = Field(
        False, description="Whether to require review from code owners"
    )
    required_status_checks: List[str] = Field(
        default_factory=list,
        description="List of status checks that must pass before merging",
    )
    enforce_admins: bool = Field(
        False,
        description="Whether to enforce restrictions for repository administrators",
    )


class GitHubProjectCreator:
    """Handles GitHub repository creation and configuration.

    This class provides methods to create GitHub repositories with standardized
    settings, set up branch protection rules, manage team access, and configure
    GitHub Actions workflows.

    Attributes:
        token: GitHub personal access token with repo permissions.
        api_url: Base URL for GitHub API requests.
        headers: HTTP headers for API requests.
    """

    def __init__(self, token: str, api_url: str = "https://api.github.com"):
        """Initialize the GitHub project creator.

        Args:
            token: GitHub personal access token with repo permissions.
            api_url: Base URL for GitHub API requests. Defaults to GitHub.com.

        Raises:
            ValueError: If the token is empty or None.
        """
        if not token:
            raise ValueError("GitHub token cannot be empty")

        self.token = token
        self.api_url = api_url
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def create_repository(
        self, name: str, description: str = "", private: bool = True, **kwargs
    ) -> Dict[str, Any]:
        """Create a new GitHub repository.

        Args:
            name: Name of the repository to create.
            description: A short description of the repository purpose.
            private: Whether the repository should be private or public.
            **kwargs: Additional parameters for repository creation.

        Returns:
            Dict containing repository information if creation is successful.

        Raises:
            requests.HTTPError: If the repository creation fails.
        """
        settings = RepositorySettings(
            name=name, description=description, private=private, **kwargs
        )

        payload = settings.model_dump(exclude={"team_access", "branch_protection"})
        response = requests.post(
            f"{self.api_url}/user/repos", headers=self.headers, json=payload
        )
        response.raise_for_status()

        repo_data = response.json()

        # Handle additional configuration
        if settings.branch_protection:
            self.set_branch_protection(
                owner=repo_data["owner"]["login"],
                repo=repo_data["name"],
                branch=settings.default_branch,
            )

        if settings.team_access:
            for team in settings.team_access:
                self.add_team_access(
                    owner=repo_data["owner"]["login"], repo=repo_data["name"], team=team
                )

        return repo_data

    def set_branch_protection(
        self,
        owner: str,
        repo: str,
        branch: str,
        rules: Optional[BranchProtectionRule] = None,
    ) -> Dict[str, Any]:
        """Set up branch protection rules for a repository.

        Args:
            owner: The GitHub username or organization that owns the repository.
            repo: The repository name.
            branch: The branch to protect.
            rules: Branch protection rule configuration.

        Returns:
            Dict containing the response from the GitHub API.

        Raises:
            requests.HTTPError: If setting branch protection fails.
        """
        if rules is None:
            rules = BranchProtectionRule()

        payload = {
            "required_status_checks": {
                "strict": True,
                "contexts": rules.required_status_checks,
            },
            "enforce_admins": rules.enforce_admins,
            "required_pull_request_reviews": {
                "dismissal_restrictions": {},
                "dismiss_stale_reviews": rules.dismiss_stale_reviews,
                "require_code_owner_reviews": rules.require_code_owner_reviews,
                "required_approving_review_count": rules.required_approvals,
            },
            "restrictions": None,
        }

        response = requests.put(
            f"{self.api_url}/repos/{owner}/{repo}/branches/{branch}/protection",
            headers=self.headers,
            json=payload,
        )
        response.raise_for_status()

        return response.json()

    def add_team_access(
        self, owner: str, repo: str, team: str, permission: str = "push"
    ) -> Dict[str, Any]:
        """Add team access to a repository.

        Args:
            owner: The GitHub organization that owns the repository.
            repo: The repository name.
            team: The team name to give access to.
            permission: The permission level (pull, push, admin).

        Returns:
            Dict containing the response from the GitHub API.

        Raises:
            requests.HTTPError: If adding team access fails.
        """
        payload = {"permission": permission}

        response = requests.put(
            f"{self.api_url}/orgs/{owner}/teams/{team}/repos/{owner}/{repo}",
            headers=self.headers,
            json=payload,
        )
        response.raise_for_status()

        return response.json()

    def create_workflow(
        self, owner: str, repo: str, workflow_file: str, workflow_content: str
    ) -> Dict[str, Any]:
        """Create a GitHub Actions workflow file.

        Args:
            owner: The GitHub username or organization that owns the repository.
            repo: The repository name.
            workflow_file: The filename for the workflow (e.g., "ci.yml").
            workflow_content: The YAML content of the workflow file.

        Returns:
            Dict containing the response from the GitHub API.

        Raises:
            requests.HTTPError: If creating the workflow file fails.
        """
        import base64

        path = f".github/workflows/{workflow_file}"
        content = base64.b64encode(workflow_content.encode()).decode()

        payload = {
            "message": f"Add {workflow_file} workflow",
            "content": content,
            "branch": "main",
        }

        response = requests.put(
            f"{self.api_url}/repos/{owner}/{repo}/contents/{path}",
            headers=self.headers,
            json=payload,
        )
        response.raise_for_status()

        return response.json()

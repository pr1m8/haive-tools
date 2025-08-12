
:py:mod:`tools.tools.toolkits.gitlab_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.gitlab_toolkit

Gitlab Toolkit The Gitlab toolkit contains tools that enable an LLM agent to interact.
with a gitlab repository. The tool is a wrapper for the python-gitlab library.

Quickstart
Install the python-gitlab library
Create a Gitlab personal access token
Set your environmental variables
Pass the tools to your agent with toolkit.get_tools()
Each of these steps will be explained in great detail below.

Get Issues- fetches issues from the repository.

Get Issue- fetches details about a specific issue.

Comment on Issue- posts a comment on a specific issue.

Create Merge Request- creates a merge request from the bot's working branch to the base branch.

Create File- creates a new file in the repository.

Read File- reads a file from the repository.

Update File- updates a file in the repository.

Delete File- deletes a file from the repository.

Setup
1. Install the python-gitlab library
%pip install --upgrade --quiet  python-gitlab langchain-community

2. Create a Gitlab personal access token
Follow the instructions here to create a Gitlab personal access token. Make sure your app has the following repository permissions:

read_api
read_repository
write_repository
3. Set Environmental Variables
Before initializing your agent, the following environmental variables need to be set:

GITLAB_URL - The URL hosted Gitlab. Defaults to "https://gitlab.com".
GITLAB_PERSONAL_ACCESS_TOKEN- The personal access token you created in the last step
GITLAB_REPOSITORY- The name of the Gitlab repository you want your bot to act upon. Must follow the format {username}/{repo-name}.
GITLAB_BRANCH- The branch where the bot will make its commits. Defaults to 'main.'
GITLAB_BASE_BRANCH- The base branch of your repo, usually either 'main' or 'master.' This is where merge requests will base from. Defaults to 'main.'

Example: Simple Agent


.. autolink-examples:: tools.tools.toolkits.gitlab_toolkit
   :collapse:





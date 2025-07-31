from __future__ import annotations

import os
from typing import Annotated

from dotenv import load_dotenv
from langchain_community.utilities.reddit_search import RedditSearchAPIWrapper
from langchain_core.tools import StructuredTool
from pydantic import Field

"""Reddit Search Tool Module.

This module provides a structured tool for searching Reddit posts based on
specified parameters like subreddit, query, sort method, and time filter.
It leverages the RedditSearchAPIWrapper from langchain_community to interface
with the Reddit API.

The module exports a StructuredTool that can be used in LangChain-based agents
to search and retrieve Reddit content programmatically.

Example:
    >>> from haive.tools.tools.reddit_search import RedditStructuredTool
    >>> result = RedditStructuredTool.invoke({
    >>>     "query": "machine learning",
    >>>     "sort": "new",
    >>>     "time_filter": "week",
    >>>     "subreddit": "python",
    >>>     "limit": 3
    >>> })

Note:
    Requires Reddit API credentials (client ID, client secret, user agent)
    to be set in the environment variables.
"""


# -----------------------------
# ✅ Load credentials
# -----------------------------
load_dotenv(".env")

for var in ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"]:
    if not os.getenv(var):
        raise ValueError(f"❌ {var} is not set in .env")

# -----------------------------
# ✅ Define function + wrapper
# -----------------------------
reddit_api = RedditSearchAPIWrapper()


def search_reddit(
    query: Annotated[str, Field(description="Query string to search post titles for")],
    sort: Annotated[
        str,
        Field(
            description="Sort method: 'relevance', 'hot', 'top', 'new', or 'comments'"
        ),
    ],
    time_filter: Annotated[
        str,
        Field(
            description="Time period: 'all', 'day', 'hour', 'month', 'week', or 'year'"
        ),
    ],
    subreddit: Annotated[
        str, Field(description="Subreddit name like 'python' or 'all'")
    ],
    limit: Annotated[int, Field(description="Max number of results to return")],
) -> str:
    """Search for posts on Reddit with specified parameters.

    Args:
        query: Query string to search post titles for
        sort: Sort method: 'relevance', 'hot', 'top', 'new', or 'comments'
        time_filter: Time period: 'all', 'day', 'hour', 'month', 'week', or 'year'
        subreddit: Subreddit name like 'python' or 'all'
        limit: Max number of results to return

    Returns:
        str: Formatted results from Reddit posts matching the query parameters

    Raises:
        ValueError: If the Reddit API returns an error

    """
    return reddit_api.run(
        query=query,
        sort=sort,
        time_filter=time_filter,
        subreddit=subreddit,
        limit=limit,
    )


# -----------------------------
# ✅ Create StructuredTool
# -----------------------------
RedditStructuredTool = StructuredTool.from_function(
    name="reddit_search",
    description="Search posts on Reddit using subreddit, time filter, and query.",
    func=search_reddit,
)

# -----------------------------
# 🧪 CLI Test
# -----------------------------
if __name__ == "__main__":
    result = RedditStructuredTool.invoke(
        {
            "query": "langchain",
            "sort": "new",
            "time_filter": "week",
            "subreddit": "python",
            "limit": 3,
        }
    )

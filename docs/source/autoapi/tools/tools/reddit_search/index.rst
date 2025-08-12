
:py:mod:`tools.tools.reddit_search`
===================================

.. py:module:: tools.tools.reddit_search



Functions
---------

.. autoapisummary::

   tools.tools.reddit_search.initialize_reddit_search
   tools.tools.reddit_search.search_reddit

.. py:function:: initialize_reddit_search()

   Initialize the Reddit Search API wrapper with credentials from environment variables.

   :returns: Configured Reddit API wrapper.
   :rtype: RedditSearchAPIWrapper

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_reddit_search
      :collapse:

.. py:function:: search_reddit(query: Annotated[str, Field(description='Query string to search post titles for')], sort: Annotated[str, Field(description="Sort method: 'relevance', 'hot', 'top', 'new', or 'comments'")], time_filter: Annotated[str, Field(description="Time period: 'all', 'day', 'hour', 'month', 'week', or 'year'")], subreddit: Annotated[str, Field(description="Subreddit name like 'python' or 'all'")], limit: Annotated[int, Field(description='Max number of results to return')]) -> str

   Search for posts on Reddit with specified parameters.

   :param query: Query string to search post titles for
   :param sort: Sort method: 'relevance', 'hot', 'top', 'new', or 'comments'
   :param time_filter: Time period: 'all', 'day', 'hour', 'month', 'week', or 'year'
   :param subreddit: Subreddit name like 'python' or 'all'
   :param limit: Max number of results to return

   :returns: Formatted results from Reddit posts matching the query parameters
   :rtype: str

   :raises ValueError: If the Reddit API returns an error


   .. autolink-examples:: search_reddit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.reddit_search
   :collapse:
   
.. autolink-skip:: next

"""Ionic Commerce Shopping Tool for product search and recommendations.

This module provides a Langchain-compatible tool for searching products across
thousands of online retailers using the Ionic Commerce platform. The tool
allows agents to find, discover, and compare products based on user queries
and optional price range specifications.

Example:
    ```python
    from haive.tools.tools.ionic_tool import tools
    ```

Attributes:
    ionic_tool: Configured Ionic Commerce shopping tool
    tools: List containing the Ionic tool for easy integration

"""

from ionic_langchain.tool import IonicTool


# Initialize the Ionic Commerce shopping tool
ionic_tool = IonicTool().tool()

# Configure the tool description to provide detailed usage instructions
ionic_tool.description = """
Ionic is an e-commerce shopping tool. Assistant uses the Ionic Commerce Shopping Tool to find, discover, and compare products from thousands of online retailers. Assistant should use the tool when the user is looking for a product recommendation or trying to find a specific product.

The user may specify the number of results, minimum price, and maximum price for which they want to see results.
Ionic Tool input is a comma-separated string of values:
  - query string (required, must not include commas)
  - number of results (default to 4, no more than 10)
  - minimum price in cents ($5 becomes 500)
  - maximum price in cents
For example, if looking for coffee beans between 5 and 10 dollars, the tool input would be `coffee beans, 5, 500, 1000`.

Return them as a markdown formatted list with each recommendation from tool results, being sure to include the full PDP URL. For example:

1. Product 1: [Price] -- link
2. Product 2: [Price] -- link
3. Product 3: [Price] -- link
4. Product 4: [Price] -- link
"""

# List of tools for easy integration with agents
tools = [ionic_tool]

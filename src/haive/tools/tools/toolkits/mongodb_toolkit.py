"""MongoDB Database Toolkit for Haive.

This module provides a toolkit for interacting with MongoDB databases through the
LangChain MongoDB agent toolkit. It leverages the MongoDB Database toolkit to
create a set of tools that can be used to query and analyze MongoDB data.

The toolkit includes functionality for:
- Connecting to MongoDB databases
- Executing MongoDB queries
- Exploring collections and their schemas
- Analyzing data from MongoDB databases

Typical usage:
    ```python
    from haive.tools.toolkits.mongodb_toolkit import get_mongodb_toolkit

    # Create a toolkit with a connection string
    toolkit = get_mongodb_toolkit(
        connection_string="mongodb://localhost:27017/mydatabase",
        temperature=0
    )
    ```

"""

from langchain_mongodb.agent_toolkit.database import MongoDBDatabase
from langchain_mongodb.agent_toolkit.toolkit import MongoDBDatabaseToolkit
from langchain_openai import ChatOpenAI


def get_mongodb_toolkit(
    connection_string: str = "mongodb://localhost:27017/chinook",
    temperature: float = 0,
    llm: ChatOpenAI | None = None,
) -> MongoDBDatabaseToolkit:
    """Create a MongoDB Database toolkit for querying and analyzing MongoDB data.

    This function creates a MongoDB toolkit with the provided connection string
    and language model. The toolkit can be used to interact with MongoDB databases,
    run queries, and analyze data.

    Args:
        connection_string: MongoDB connection string including database name.
            Default is "mongodb://localhost:27017/chinook".
        temperature: The temperature parameter for the ChatOpenAI model if no LLM is provided.
            Default is 0.
        llm: Optional ChatOpenAI instance. If not provided, a new instance will be
            created with the specified temperature.

    Returns:
        MongoDBDatabaseToolkit: A toolkit for working with MongoDB databases.

    Example:
        ```python
        # Basic usage with default connection
        toolkit = get_mongodb_toolkit()

        # Custom connection and temperature
        toolkit = get_mongodb_toolkit(
            connection_string="mongodb://username:password@host:27017/database",
            temperature=0.1
        )

        # With custom LLM
        my_llm = ChatOpenAI(temperature=0.1, model="gpt-4")
        toolkit = get_mongodb_toolkit(
            connection_string="mongodb://localhost:27017/analytics",
            llm=my_llm
        )
        ```

    """
    db = MongoDBDatabase.from_connection_string(connection_string)

    if llm is None:
        llm = ChatOpenAI(temperature=temperature)

    return MongoDBDatabaseToolkit(db=db, llm=llm)


:py:mod:`tools.tools.toolkits.mongodb_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.mongodb_toolkit

MongoDB Database Toolkit for Haive.

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


.. autolink-examples:: tools.tools.toolkits.mongodb_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.mongodb_toolkit.get_mongodb_toolkit

.. py:function:: get_mongodb_toolkit(connection_string: str = 'mongodb://localhost:27017/chinook', temperature: float = 0, llm: langchain_openai.ChatOpenAI | None = None) -> langchain_mongodb.agent_toolkit.toolkit.MongoDBDatabaseToolkit

   Create a MongoDB Database toolkit for querying and analyzing MongoDB data.

   This function creates a MongoDB toolkit with the provided connection string
   and language model. The toolkit can be used to interact with MongoDB databases,
   run queries, and analyze data.

   :param connection_string: MongoDB connection string including database name.
                             Default is "mongodb://localhost:27017/chinook".
   :param temperature: The temperature parameter for the ChatOpenAI model if no LLM is provided.
                       Default is 0.
   :param llm: Optional ChatOpenAI instance. If not provided, a new instance will be
               created with the specified temperature.

   :returns: A toolkit for working with MongoDB databases.
   :rtype: MongoDBDatabaseToolkit

   .. rubric:: Example

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


   .. autolink-examples:: get_mongodb_toolkit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.mongodb_toolkit
   :collapse:
   
.. autolink-skip:: next

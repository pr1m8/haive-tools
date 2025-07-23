"""SQL Database Toolkit Module.

This module provides a toolkit for interacting with SQL databases through LangChain's
SQL Database Toolkit. It initializes a connection to a SQLite database and creates
a toolkit that can be used by agents to query and manipulate the database.

The module leverages LangChain's utilities and agent toolkits to provide a comprehensive
set of tools for SQL operations, including schema inspection, query generation,
and data retrieval.

Example:
    >>> from haive.tools.toolkits.sql_db_toolkit import toolkit
    >>> from langchain.agents import create_sql_agent
    >>> agent = create_sql_agent(toolkit=toolkit, llm=llm)
    >>> agent.run("How many tracks are in the database?")

Note:
    This module is configured to use a SQLite database named "Chinook.db" by default.
    You can modify the database URI to connect to other SQL database types.
"""

from langchain import hub
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI

# Initialize a connection to the database
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Initialize the language model required for SQL operations
llm = ChatOpenAI(temperature=0, model="gpt-4")

# Create the SQL Database Toolkit with the database and language model
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Pull a premade prompt template for SQL agents
prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")

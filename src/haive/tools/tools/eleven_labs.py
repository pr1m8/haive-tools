"""Eleven Labs text-to-speech tool integration.

This module provides integration with Eleven Labs' text-to-speech API through the LangChain
tools interface. It allows for converting text to speech using Eleven Labs' high-quality
voice synthesis technology.

The module loads environment variables from a .env file and initializes the Eleven Labs
text-to-speech tool, making it available for use in agent workflows.

Requires:
    - A valid Eleven Labs API key set in the environment variables
    - langchain_community package
    - python-dotenv package

Example:
    To use the Eleven Labs text-to-speech tool in an agent:
    ```python
    from haive.tools.tools.eleven_labs import eleven_labs_text2speech_tool

    # Add to your agent's toolkit
    agent = Agent(tools=[eleven_labs_text2speech_tool[0]])
    ```
"""

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools

# Load environment variables from .env file
load_dotenv(".env")

# Initialize the Eleven Labs text-to-speech tool
eleven_labs_text2speech_tool = load_tools(["eleven_labs_text2speech"])

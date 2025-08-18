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

Examples:
    To use the Eleven Labs text-to-speech tool in an agent:
            from haive.tools.tools.eleven_labs import eleven_labs_text2speech_tool

            # Add to your agent's toolkit
            agent = Agent(tools=[eleven_labs_text2speech_tool[0]])

"""

from dotenv import load_dotenv
from langchain.agents import load_tools

# Load environment variables from .env file
load_dotenv(".env")


def get_eleven_labs_text2speech_tool():
    """Get Eleven Labs text-to-speech tool with proper error handling for missing credentials.

    Returns:
        list: List containing Eleven Labs text-to-speech tool if credentials are available,
              empty list otherwise.
    """
    try:
        return load_tools(["eleven_labs_text2speech"])
    except Exception as e:
        # Return empty list if credentials are missing or other issues occur
        print(f"Warning: Eleven Labs text-to-speech tool unavailable: {e}")
        return []


# Initialize the Eleven Labs text-to-speech tool
eleven_labs_text2speech_tool = get_eleven_labs_text2speech_tool()

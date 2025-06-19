"""
DALL-E Image Generator Tool Module.

This module provides a tool for generating images using OpenAI's DALL-E model
through the LangChain interface. It loads the DALL-E image generator tool from
langchain_community's agent_toolkits and makes it available for use in agents.

The tool allows agents to create images based on text prompts by interfacing with
OpenAI's DALL-E API.

Example:
    >>> from haive.tools.tools.dalle_image_generator_tool import tools
    >>> image_url = tools[0].run("A photorealistic image of a quantum computer")

Note:
    Requires an OpenAI API key with DALL-E access to be set in the environment variables.
    The API key should be available in your .env file or environment.
"""

from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools

# Load environment variables from .env file
load_dotenv(".env")

# Load the DALL-E image generator tool
tools = load_tools(["dalle-image-generator"])

"""Scene Explain Tool Module.

This module provides a tool for explaining and analyzing images through the
SceneXplain API. It leverages langchain_community's agent_toolkits to load
a pre-configured SceneXplain tool that can process images and generate textual
descriptions of their content.

The SceneXplain tool can be used to identify objects, scenes, and contexts
within images, allowing agents to work with visual information.

Example:
    >>> from haive.tools.tools.scene_explain_tool import scene_explain_tool
    >>> description = scene_explain_tool[0].run("https://example.com/image.jpg")

Note:
    Requires API credentials for SceneXplain to be set in environment variables.
    Make sure to include these in your .env file.

"""

from dotenv import load_dotenv
from langchain.agents import load_tools

# Load environment variables from .env file
load_dotenv(".env")


def get_scene_explain_tool():
    """Get SceneXplain tool with proper error handling for missing credentials.

    Returns:
        list: List containing SceneXplain tool if credentials are available,
              empty list otherwise.
    """
    try:
        return load_tools(["sceneXplain"])
    except Exception as e:
        # Return empty list if credentials are missing or other issues occur
        print(f"Warning: SceneXplain tool unavailable: {e}")
        return []


# Load the SceneXplain tool
scene_explain_tool = get_scene_explain_tool()

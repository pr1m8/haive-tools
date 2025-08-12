
:py:mod:`tools.tools.dalle_image_generator_tool`
================================================

.. py:module:: tools.tools.dalle_image_generator_tool

DALL-E Image Generator Tool Module.

This module provides a tool for generating images using OpenAI's DALL-E model
through the LangChain interface. It loads the DALL-E image generator tool from
langchain_community's agent_toolkits and makes it available for use in agents.

The tool allows agents to create images based on text prompts by interfacing with
OpenAI's DALL-E API.

.. rubric:: Example

>>> from haive.tools.tools.dalle_image_generator_tool import tools
>>> image_url = tools[0].run("A photorealistic image of a quantum computer")

.. note::

   Requires an OpenAI API key with DALL-E access to be set in the environment variables.
   The API key should be available in your .env file or environment.


.. autolink-examples:: tools.tools.dalle_image_generator_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.dalle_image_generator_tool.get_dalle_image_generator_tool

.. py:function:: get_dalle_image_generator_tool()

   Get DALL-E image generator tool with proper error handling for missing credentials.

   :returns:

             List containing DALL-E image generator tool if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_dalle_image_generator_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.dalle_image_generator_tool
   :collapse:
   
.. autolink-skip:: next

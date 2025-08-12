
:py:mod:`tools.tools.scene_explain_tool`
========================================

.. py:module:: tools.tools.scene_explain_tool

Scene Explain Tool Module.

This module provides a tool for explaining and analyzing images through the
SceneXplain API. It leverages langchain_community's agent_toolkits to load
a pre-configured SceneXplain tool that can process images and generate textual
descriptions of their content.

The SceneXplain tool can be used to identify objects, scenes, and contexts
within images, allowing agents to work with visual information.

.. rubric:: Example

>>> from haive.tools.tools.scene_explain_tool import scene_explain_tool
>>> description = scene_explain_tool[0].run("https://example.com/image.jpg")

.. note::

   Requires API credentials for SceneXplain to be set in environment variables.
   Make sure to include these in your .env file.


.. autolink-examples:: tools.tools.scene_explain_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.scene_explain_tool.get_scene_explain_tool

.. py:function:: get_scene_explain_tool()

   Get SceneXplain tool with proper error handling for missing credentials.

   :returns:

             List containing SceneXplain tool if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_scene_explain_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.scene_explain_tool
   :collapse:
   
.. autolink-skip:: next

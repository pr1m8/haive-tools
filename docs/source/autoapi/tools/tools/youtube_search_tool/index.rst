
:py:mod:`tools.tools.youtube_search_tool`
=========================================

.. py:module:: tools.tools.youtube_search_tool

YouTube Search Tool Module.

This module provides a tool for searching YouTube for videos using the
langchain_community.tools.YouTubeSearchTool implementation. It allows searching
for YouTube videos by query terms and returns results with video titles, URLs,
and other metadata.

.. rubric:: Examples

>>> from haive.tools.tools.youtube_search_tool import youtube_search_tool
>>> result = youtube_search_tool[0].invoke("machine learning tutorial")
>>> print(result)


.. autolink-examples:: tools.tools.youtube_search_tool
   :collapse:





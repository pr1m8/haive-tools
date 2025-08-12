
:py:mod:`tools.tools.eleven_labs`
=================================

.. py:module:: tools.tools.eleven_labs

Eleven Labs text-to-speech tool integration.

This module provides integration with Eleven Labs' text-to-speech API through the LangChain
tools interface. It allows for converting text to speech using Eleven Labs' high-quality
voice synthesis technology.

The module loads environment variables from a .env file and initializes the Eleven Labs
text-to-speech tool, making it available for use in agent workflows.

Requires:
    - A valid Eleven Labs API key set in the environment variables
    - langchain_community package
    - python-dotenv package

.. rubric:: Example

To use the Eleven Labs text-to-speech tool in an agent:
```python
from haive.tools.tools.eleven_labs import eleven_labs_text2speech_tool

# Add to your agent's toolkit
agent = Agent(tools=[eleven_labs_text2speech_tool[0]])
```


.. autolink-examples:: tools.tools.eleven_labs
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.eleven_labs.get_eleven_labs_text2speech_tool

.. py:function:: get_eleven_labs_text2speech_tool()

   Get Eleven Labs text-to-speech tool with proper error handling for missing credentials.

   :returns:

             List containing Eleven Labs text-to-speech tool if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_eleven_labs_text2speech_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.eleven_labs
   :collapse:
   
.. autolink-skip:: next

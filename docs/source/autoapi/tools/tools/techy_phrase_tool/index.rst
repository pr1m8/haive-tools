
:py:mod:`tools.tools.techy_phrase_tool`
=======================================

.. py:module:: tools.tools.techy_phrase_tool

Techy Phrase Generator Tool Module.

This module provides tools for generating random technology-related phrases using the Techy API.
It offers functionality to retrieve phrases in both plain text and structured JSON formats,
which can be used to add technical flavor to conversations or generate mock tech content.

.. rubric:: Examples

>>> from haive.tools.tools.techy_phrase_tool import get_techy_phrase_text
>>> phrase = get_techy_phrase_text()
>>> print(phrase)
'We need to back up the wireless SSL driver!'

>>> from haive.tools.tools.techy_phrase_tool import get_techy_phrase_json
>>> phrase_data = get_techy_phrase_json()
>>> print(phrase_data['text'])
'Try to quantify the EXE application, maybe it will index the multi-byte port!'


.. autolink-examples:: tools.tools.techy_phrase_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.techy_phrase_tool.get_techy_phrase_json
   tools.tools.techy_phrase_tool.get_techy_phrase_text

.. py:function:: get_techy_phrase_json() -> dict

   Fetch a random technology-related phrase in structured JSON format.

   This function retrieves a randomly generated tech-sounding phrase from the
   Techy API in JSON format, which includes additional metadata.

   :returns: A dictionary containing the tech phrase and possibly other metadata.
   :rtype: dict

   :raises requests.RequestException: If the API request fails.
   :raises ValueError: If the response cannot be parsed as JSON.


   .. autolink-examples:: get_techy_phrase_json
      :collapse:

.. py:function:: get_techy_phrase_text() -> str

   Fetch a random technology-related phrase in plain text format.

   This function retrieves a randomly generated tech-sounding phrase from the
   Techy API in simple text format.

   :returns: A randomly generated tech phrase as a string.
   :rtype: str

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_techy_phrase_text
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.techy_phrase_tool
   :collapse:
   
.. autolink-skip:: next

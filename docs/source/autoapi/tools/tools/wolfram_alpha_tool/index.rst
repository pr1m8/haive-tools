
:py:mod:`tools.tools.wolfram_alpha_tool`
========================================

.. py:module:: tools.tools.wolfram_alpha_tool

Wolfram Alpha Integration Tool Module.

This module provides tools for accessing Wolfram Alpha's computational knowledge engine API.
It enables solving complex mathematical, scientific, and general knowledge queries with
Wolfram Alpha's powerful computational capabilities.

Wolfram Alpha can handle various types of queries including:
- Mathematical calculations and equations
- Unit conversions and physical constants
- Scientific data and formulas
- Statistical analyses
- Date and time calculations
- General knowledge questions

Required Environment Variables:
    - WOLFRAM_ALPHA_APPID: Your Wolfram Alpha App ID (will prompt if not found)

.. rubric:: Examples

>>> from haive.tools.tools.wolfram_alpha_tool import wolfram
>>> result = wolfram.run("solve x^2 + 2x + 1 = 0")
>>> print(result)
x = -1

>>> # Using the tool directly
>>> from haive.tools.tools.wolfram_alpha_tool import wolfram_alpha_tools
>>> result = wolfram_alpha_tools[0].run("distance from Earth to Mars")
>>> print(result)
The average distance from Earth to Mars is approximately 225 million kilometers (140 million miles).


.. autolink-examples:: tools.tools.wolfram_alpha_tool
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.wolfram_alpha_tool.get_wolfram_alpha_tools

.. py:function:: get_wolfram_alpha_tools()

   Get Wolfram Alpha tools with proper error handling for missing credentials.

   :returns:

             List containing Wolfram Alpha tools if credentials are available,
                   empty list otherwise.
   :rtype: list


   .. autolink-examples:: get_wolfram_alpha_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.wolfram_alpha_tool
   :collapse:
   
.. autolink-skip:: next

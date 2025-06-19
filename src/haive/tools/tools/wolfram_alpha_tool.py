"""
Wolfram Alpha Integration Tool Module

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

Examples:
    >>> from haive.tools.tools.wolfram_alpha_tool import wolfram
    >>> result = wolfram.run("solve x^2 + 2x + 1 = 0")
    >>> print(result)
    x = -1

    >>> # Using the tool directly
    >>> from haive.tools.tools.wolfram_alpha_tool import wolfram_alpha_tools
    >>> result = wolfram_alpha_tools[0].run("distance from Earth to Mars")
    >>> print(result)
    The average distance from Earth to Mars is approximately 225 million kilometers (140 million miles).
"""

import getpass
import os
from typing import Any, List

from dotenv import load_dotenv
from haive.config.config import Config
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper

# Load environment variables
load_dotenv(".env")

# Ensure the Wolfram Alpha App ID is available
if not Config.WOLFRAM_ALPHA_APPID:
    try:
        os.environ["WOLFRAM_ALPHA_APPID"] = getpass.getpass(
            "Enter your Wolfram Alpha App ID: "
        )
    except Exception:
        raise ValueError(
            "WOLFRAM_ALPHA_APPID is required to use the Wolfram Alpha tool"
        )

# Initialize the Wolfram Alpha API wrapper
wolfram = WolframAlphaAPIWrapper()

# Load the Wolfram Alpha tools from LangChain
wolfram_alpha_tools = load_tools(["wolfram-alpha"])

# Update tool metadata for clarity
if wolfram_alpha_tools and len(wolfram_alpha_tools) > 0:
    wolfram_alpha_tools[0].name = "wolfram_alpha"
    wolfram_alpha_tools[0].description = (
        "Use Wolfram Alpha to solve mathematical, scientific, and computational questions. "
        "Useful for calculations, solving equations, unit conversions, and factual queries "
        "that require precise answers. Input should be a clear, specific question."
    )

"""
Translation Tools Module.

This module provides a tool for translating text between languages using the
DeepL API. It creates a LangChain-compatible structured tool that can be
integrated into agents to perform high-quality translations between multiple
languages.

The module defines the DeepLTranslateTool class which implements a BaseTool
interface for integrating with LangChain's agent frameworks. It supports both
DeepL's free and pro API modes, and includes validation for language codes.

Example:
    >>> from haive.tools.tools.translate_tools import DeepLTranslateTool
    >>> translate_tool = DeepLTranslateTool(
    >>>     target_lang="EN-US",
    >>>     source_lang="FR",
    >>>     api_key="your_deepl_api_key"
    >>> )
    >>> translation = translate_tool.run("Bonjour le monde")

Note:
    Requires a DeepL API key, which can be obtained from https://www.deepl.com/pro#developer
    The API key should be available in your .env file or environment variables.
"""

import os
from typing import Literal, Optional, Type

import dotenv
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

dotenv.load_dotenv(".env")

# DeepL-supported languages
DEEPL_TARGET_LANGUAGES = Literal[
    "BG",
    "CS",
    "DA",
    "DE",
    "EL",
    "EN-GB",
    "EN-US",
    "ES",
    "ET",
    "FI",
    "FR",
    "HU",
    "ID",
    "IT",
    "JA",
    "KO",
    "LT",
    "LV",
    "NB",
    "NL",
    "PL",
    "PT-BR",
    "PT-PT",
    "RO",
    "RU",
    "SK",
    "SL",
    "SV",
    "TR",
    "UK",
    "ZH",
]

DEEPL_SOURCE_LANGUAGES = Literal[
    "BG",
    "CS",
    "DA",
    "DE",
    "EL",
    "EN",
    "ES",
    "ET",
    "FI",
    "FR",
    "HU",
    "ID",
    "IT",
    "JA",
    "KO",
    "LT",
    "LV",
    "NB",
    "NL",
    "PL",
    "PT",
    "RO",
    "RU",
    "SK",
    "SL",
    "SV",
    "TR",
    "UK",
    "ZH",
]


# Input Schema for Translation
class DeepLInput(BaseModel):
    """Input schema for DeepL translation.

    Attributes:
        text: Text to translate
    """

    text: str = Field(..., description="Text to translate")


# DeepL Translation Tool
class DeepLTranslateTool(BaseTool):
    """
    LangChain-compatible structured tool for translating text using the DeepL API.

    This tool provides high-quality translation between multiple languages by
    leveraging DeepL's translation service. It supports both free and pro API tiers
    and validates language codes using Pydantic Literal types.

    Attributes:
        name: Tool name for agent identification
        description: Description of the tool for agent instructions
        target_lang: Target language code for translation output
        source_lang: Optional source language code (auto-detect if None)
        mode: DeepL API mode ('free' or 'pro')
        api_key: DeepL API key
        args_schema: Pydantic schema for validating inputs
    """

    name: str = "deepl_translate"
    description: str = (
        "Translate text using DeepL API. "
        "Supports structured input and 'free' or 'pro' modes. "
        "Target language must be one of DeepL's supported codes."
    )

    target_lang: DEEPL_TARGET_LANGUAGES = Field(
        ..., description="Target language (e.g., 'EN-US')"
    )
    source_lang: Optional[DEEPL_SOURCE_LANGUAGES] = Field(
        default=None, description="Optional source language (e.g., 'FR')"
    )
    mode: Literal["free", "pro"] = Field(
        default="free", description="DeepL API mode: 'free' or 'pro'"
    )
    api_key: str = Field(
        default_factory=lambda: os.getenv("DEEPL_API_KEY", ""),
        description="Your DeepL API key",
    )

    args_schema: Type[BaseModel] = DeepLInput

    def _run(self, text: str) -> str:
        """
        Run translation on the provided text.

        Args:
            text: The text to translate

        Returns:
            str: The translated text

        Raises:
            Exception: If the DeepL API returns an error
        """
        try:
            import deepl

            server_url = (
                "https://api-free.deepl.com"
                if self.mode == "free"
                else "https://api.deepl.com"
            )
            translator = deepl.Translator(auth_key=self.api_key, server_url=server_url)

            result = translator.translate_text(
                text=text,
                target_lang=self.target_lang,
                source_lang=self.source_lang,
            )
            return result.text
        except Exception as e:
            return f"❌ DeepL error: {e}"

    def _arun(self, text: str) -> str:
        """
        Async version of the run method (not implemented).

        Args:
            text: The text to translate

        Raises:
            NotImplementedError: Always raised as async is not supported
        """
        raise NotImplementedError("Async not supported for DeepLTranslateTool")


# Export the tool for use in agents
deepl_translate_tool = [DeepLTranslateTool]

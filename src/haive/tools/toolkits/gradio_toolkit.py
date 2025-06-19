"""Gradio Toolkit for AI model inference through Gradio-hosted apps.

This toolkit provides tools for interacting with various AI models hosted on
Hugging Face Spaces via Gradio interfaces. It includes tools for tasks like
image generation, audio transcription, image captioning, and more.

Note: Some tools may be unavailable if the corresponding Gradio spaces are
experiencing runtime errors or other issues. Make sure to handle potential
errors gracefully when using these tools.

Example:
    ```python
    from haive.tools.toolkits.gradio_toolkit import gradio_toolkit
    ```

Attributes:
    gradio_toolkit: List of Langchain-compatible tools for various AI tasks
"""

from gradio_tools.tools import (
    BarkTextToSpeechTool,
    ClipInterrogatorTool,
    DocQueryDocumentAnsweringTool,
    ImageCaptioningTool,
    ImageToMusicTool,
    SAMImageSegmentationTool,
    StableDiffusionPromptGeneratorTool,
    StableDiffusionTool,
    TextToVideoTool,
    WhisperAudioTranscriptionTool,
)

# Create a list of Langchain-compatible tools from Gradio-hosted models
# Note: Tool initialization may fail if the Gradio space is unavailable
# Each tool requires communication with a hosted Gradio space on Hugging Face
gradio_toolkit = [
    StableDiffusionTool().langchain,  # Text-to-image generation
    ClipInterrogatorTool().langchain,  # Analyzes images to generate prompts
    ImageCaptioningTool().langchain,  # Generates descriptions for images
    ImageToMusicTool().langchain,  # Creates music inspired by images
    WhisperAudioTranscriptionTool().langchain,  # Transcribes speech to text
    StableDiffusionPromptGeneratorTool().langchain,  # Generates text-to-image prompts
    TextToVideoTool().langchain,  # Generates videos from text descriptions
    DocQueryDocumentAnsweringTool().langchain,  # Answers questions about documents
    BarkTextToSpeechTool().langchain,  # Converts text to natural-sounding speech
    SAMImageSegmentationTool().langchain,  # Segments objects in images
]

# Display the loaded tools when the module is run directly
if __name__ == "__main__":
    print(f"Loaded Gradio tools: {[t.name for t in gradio_toolkit]}")

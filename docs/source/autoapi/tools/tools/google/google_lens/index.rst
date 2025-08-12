
:py:mod:`tools.tools.google.google_lens`
========================================

.. py:module:: tools.tools.google.google_lens

Google Lens Tool Module.

This module provides a tool for visual search and image recognition using Google Lens API.
It leverages LangChain's GoogleLensAPIWrapper to analyze images, identify objects, text,
and provide information about the content in images.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key
   - GOOGLE_LENS_API_KEY: Your Google Lens API key (if different)

.. rubric:: Examples

>>> from haive.tools.tools.google.google_lens import google_lens_tool
>>> result = google_lens_tool[0].invoke({"image_url": "https://example.com/image.jpg"})
>>> print(result)
['The image shows a Siberian Husky dog in a snowy environment...']


.. autolink-examples:: tools.tools.google.google_lens
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_lens.GoogleLensInput
   tools.tools.google.google_lens.GoogleLensResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleLensInput:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleLensInput {
        node [shape=record];
        "GoogleLensInput" [label="GoogleLensInput"];
        "pydantic.BaseModel" -> "GoogleLensInput";
      }

.. autopydantic_model:: tools.tools.google.google_lens.GoogleLensInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleLensResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleLensResult {
        node [shape=record];
        "GoogleLensResult" [label="GoogleLensResult"];
        "pydantic.BaseModel" -> "GoogleLensResult";
      }

.. autopydantic_model:: tools.tools.google.google_lens.GoogleLensResult
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   tools.tools.google.google_lens.initialize_google_lens

.. py:function:: initialize_google_lens()

   Initialize the Google Lens API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Lens API client.

   :returns: A list containing the Google Lens tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_lens
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_lens
   :collapse:
   
.. autolink-skip:: next

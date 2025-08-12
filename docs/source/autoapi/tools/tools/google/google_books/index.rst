
:py:mod:`tools.tools.google.google_books`
=========================================

.. py:module:: tools.tools.google.google_books

Google Books Tool Module.

This module provides a tool for searching and retrieving information from Google Books.
It leverages LangChain's GoogleBooksQueryRun to perform searches on the Google Books database
and retrieve relevant book information.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key

.. rubric:: Examples

>>> from haive.tools.tools.google.google_books import google_books_tool
>>> result = google_books_tool[0].invoke("quantum physics introductions")
>>> print(result)
['Introduction to Quantum Physics by John Doe...']


.. autolink-examples:: tools.tools.google.google_books
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_books.GoogleBooksResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleBooksResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleBooksResult {
        node [shape=record];
        "GoogleBooksResult" [label="GoogleBooksResult"];
        "pydantic.BaseModel" -> "GoogleBooksResult";
      }

.. autopydantic_model:: tools.tools.google.google_books.GoogleBooksResult
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

   tools.tools.google.google_books.initialize_google_books

.. py:function:: initialize_google_books()

   Initialize the Google Books API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Books API client.

   :returns: A list containing the Google Books search tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_books
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_books
   :collapse:
   
.. autolink-skip:: next

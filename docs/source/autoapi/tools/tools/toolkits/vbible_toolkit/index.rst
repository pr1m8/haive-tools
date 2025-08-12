
:py:mod:`tools.tools.toolkits.vbible_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.vbible_toolkit

Virtual Bible Toolkit for accessing Bible verses and translations.

This toolkit provides tools for interacting with the Bible API,
allowing agents to look up verses by reference, get random verses,
list available translations, and retrieve full chapters. It helps
create agents that can work with biblical text and references.

.. rubric:: Example

```python
tools = vbible_toolkit
```

.. attribute:: BASE_URL

   The base URL for the Bible API

.. attribute:: DATA_URL

   The data URL for extended Bible API operations


.. autolink-examples:: tools.tools.toolkits.vbible_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.vbible_toolkit.BibleQueryInput
   tools.tools.toolkits.vbible_toolkit.ChapterVersesInput
   tools.tools.toolkits.vbible_toolkit.RandomVerseInput
   tools.tools.toolkits.vbible_toolkit.TranslationBooksInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BibleQueryInput:

   .. graphviz::
      :align: center

      digraph inheritance_BibleQueryInput {
        node [shape=record];
        "BibleQueryInput" [label="BibleQueryInput"];
        "pydantic.BaseModel" -> "BibleQueryInput";
      }

.. autopydantic_model:: tools.tools.toolkits.vbible_toolkit.BibleQueryInput
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

   Inheritance diagram for ChapterVersesInput:

   .. graphviz::
      :align: center

      digraph inheritance_ChapterVersesInput {
        node [shape=record];
        "ChapterVersesInput" [label="ChapterVersesInput"];
        "pydantic.BaseModel" -> "ChapterVersesInput";
      }

.. autopydantic_model:: tools.tools.toolkits.vbible_toolkit.ChapterVersesInput
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

   Inheritance diagram for RandomVerseInput:

   .. graphviz::
      :align: center

      digraph inheritance_RandomVerseInput {
        node [shape=record];
        "RandomVerseInput" [label="RandomVerseInput"];
        "pydantic.BaseModel" -> "RandomVerseInput";
      }

.. autopydantic_model:: tools.tools.toolkits.vbible_toolkit.RandomVerseInput
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

   Inheritance diagram for TranslationBooksInput:

   .. graphviz::
      :align: center

      digraph inheritance_TranslationBooksInput {
        node [shape=record];
        "TranslationBooksInput" [label="TranslationBooksInput"];
        "pydantic.BaseModel" -> "TranslationBooksInput";
      }

.. autopydantic_model:: tools.tools.toolkits.vbible_toolkit.TranslationBooksInput
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

   tools.tools.toolkits.vbible_toolkit.get_chapter_verses
   tools.tools.toolkits.vbible_toolkit.get_random_verse
   tools.tools.toolkits.vbible_toolkit.list_books
   tools.tools.toolkits.vbible_toolkit.list_translations
   tools.tools.toolkits.vbible_toolkit.query_bible_by_reference
   tools.tools.toolkits.vbible_toolkit.test_get_random_verse
   tools.tools.toolkits.vbible_toolkit.test_get_verses_in_chapter
   tools.tools.toolkits.vbible_toolkit.test_list_books_for_translation
   tools.tools.toolkits.vbible_toolkit.test_list_translations
   tools.tools.toolkits.vbible_toolkit.test_query_multi_verse
   tools.tools.toolkits.vbible_toolkit.test_query_single_verse

.. py:function:: get_chapter_verses(translation_id: str, book_id: str, chapter: int) -> str

   Fetches all verses in a specific book chapter.

   :param translation_id: ID of the translation to use
   :param book_id: Book ID (e.g., 'JHN' for John)
   :param chapter: Chapter number to retrieve

   :returns: All verses in the specified chapter with verse numbers
   :rtype: str

   :raises None: Returns an error message string if the request fails


   .. autolink-examples:: get_chapter_verses
      :collapse:

.. py:function:: get_random_verse(book_ids: list[str] | None = None) -> str

   Fetches a random verse, optionally from specific books or testaments.

   :param book_ids: Optional list of book IDs to limit the random selection

   :returns: A random verse with book, chapter, and verse reference
   :rtype: str

   :raises None: Returns an error message string if the request fails


   .. autolink-examples:: get_random_verse
      :collapse:

.. py:function:: list_books(translation_id: str) -> str

   Lists books available in a specified Bible translation.

   :param translation_id: ID of the translation to list books for

   :returns: A list of books with IDs and names for the specified translation
   :rtype: str

   :raises None: Returns an error message string if the request fails


   .. autolink-examples:: list_books
      :collapse:

.. py:function:: list_translations() -> str

   Gets all available Bible translations.

   :returns: A list of available Bible translations with IDs and names
   :rtype: str

   :raises None: Returns an error message string if the request fails


   .. autolink-examples:: list_translations
      :collapse:

.. py:function:: query_bible_by_reference(reference: str) -> str

   Looks up one or more Bible verses using a human-readable reference.

   :param reference: Bible reference (e.g., 'John 3:16', 'Matt 5:1-10')

   :returns: The verse text with book, chapter, and verse references
   :rtype: str

   :raises None: Returns an error message string if the request fails


   .. autolink-examples:: query_bible_by_reference
      :collapse:

.. py:function:: test_get_random_verse()

.. py:function:: test_get_verses_in_chapter()

.. py:function:: test_list_books_for_translation()

.. py:function:: test_list_translations()

.. py:function:: test_query_multi_verse()

.. py:function:: test_query_single_verse()



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.vbible_toolkit
   :collapse:
   
.. autolink-skip:: next

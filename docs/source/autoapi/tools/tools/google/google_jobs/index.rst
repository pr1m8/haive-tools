
:py:mod:`tools.tools.google.google_jobs`
========================================

.. py:module:: tools.tools.google.google_jobs

Google Jobs Tool Module.

This module provides a tool for searching job listings using Google Jobs API.
It leverages LangChain's GoogleJobsQueryRun to search for job postings, retrieve job details,
and find employment opportunities based on various criteria like location, title, and company.

.. note::

   This tool requires Google API credentials to be set in environment variables:
   - GOOGLE_API_KEY: Your Google API key
   - GOOGLE_CSE_ID: Your Custom Search Engine ID

.. rubric:: Examples

>>> from haive.tools.tools.google.google_jobs import google_job_search_tool
>>> result = google_job_search_tool[0].invoke("software engineer positions in San Francisco")
>>> print(result)
['Senior Software Engineer at Tech Co. - San Francisco, CA...']


.. autolink-examples:: tools.tools.google.google_jobs
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.google.google_jobs.GoogleJobsInput
   tools.tools.google.google_jobs.GoogleJobsResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoogleJobsInput:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleJobsInput {
        node [shape=record];
        "GoogleJobsInput" [label="GoogleJobsInput"];
        "pydantic.BaseModel" -> "GoogleJobsInput";
      }

.. autopydantic_model:: tools.tools.google.google_jobs.GoogleJobsInput
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

   Inheritance diagram for GoogleJobsResult:

   .. graphviz::
      :align: center

      digraph inheritance_GoogleJobsResult {
        node [shape=record];
        "GoogleJobsResult" [label="GoogleJobsResult"];
        "pydantic.BaseModel" -> "GoogleJobsResult";
      }

.. autopydantic_model:: tools.tools.google.google_jobs.GoogleJobsResult
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

   tools.tools.google.google_jobs.initialize_google_jobs

.. py:function:: initialize_google_jobs()

   Initialize the Google Jobs API wrapper with credentials from environment.
   variables.

   This function loads environment variables and configures the Google Jobs API client.

   :returns: A list containing the Google Jobs search tool.
   :rtype: list

   :raises ValueError: If required environment variables are not set.


   .. autolink-examples:: initialize_google_jobs
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.google.google_jobs
   :collapse:
   
.. autolink-skip:: next

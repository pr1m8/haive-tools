
:py:mod:`tools.tools.toolkits.google_calendar`
==============================================

.. py:module:: tools.tools.toolkits.google_calendar

Google Calendar Toolkit Module.

This module provides a toolkit for interacting with Google Calendar services.
It leverages LangChain's CalendarToolkit to provide tools for creating, reading,
updating, and deleting calendar events, as well as querying calendar availability.

.. note::

   This toolkit requires a valid 'credentials.json' file with Google OAuth2 credentials
   in the root directory. These credentials must have appropriate Google Calendar API permissions.

.. rubric:: Examples

>>> from haive.tools.toolkits.google_calendar import google_calendar_toolkit
>>> # Access the list of calendar tools
>>> calendar_tools = google_calendar_toolkit
>>> # Use a specific tool (e.g., to create an event)
>>> create_event_tool = [t for t in calendar_tools if 'create' in t.name.lower()][0]
>>> result = create_event_tool.invoke({"summary": "Team Meeting", "start": "2023-07-21T10:00:00", "end": "2023-07-21T11:00:00"})


.. autolink-examples:: tools.tools.toolkits.google_calendar
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.google_calendar.CalendarEvent
   tools.tools.toolkits.google_calendar.CalendarResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CalendarEvent:

   .. graphviz::
      :align: center

      digraph inheritance_CalendarEvent {
        node [shape=record];
        "CalendarEvent" [label="CalendarEvent"];
        "pydantic.BaseModel" -> "CalendarEvent";
      }

.. autopydantic_model:: tools.tools.toolkits.google_calendar.CalendarEvent
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

   Inheritance diagram for CalendarResponse:

   .. graphviz::
      :align: center

      digraph inheritance_CalendarResponse {
        node [shape=record];
        "CalendarResponse" [label="CalendarResponse"];
        "pydantic.BaseModel" -> "CalendarResponse";
      }

.. autopydantic_model:: tools.tools.toolkits.google_calendar.CalendarResponse
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

   tools.tools.toolkits.google_calendar.initialize_google_calendar_toolkit

.. py:function:: initialize_google_calendar_toolkit()

   Initialize the Google Calendar toolkit with OAuth2 credentials.

   This function checks for the existence of the credentials file and initializes
   the Google Calendar toolkit if the file exists.

   :returns: A list of Google Calendar tools provided by the toolkit.
   :rtype: list

   :raises FileNotFoundError: If the credentials.json file is not found.
   :raises Exception: If initialization fails for any other reason.


   .. autolink-examples:: initialize_google_calendar_toolkit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.google_calendar
   :collapse:
   
.. autolink-skip:: next

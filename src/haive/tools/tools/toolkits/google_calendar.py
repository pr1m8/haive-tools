"""Google Calendar Toolkit Module.

This module provides a toolkit for interacting with Google Calendar services.
It leverages LangChain's CalendarToolkit to provide tools for creating, reading,
updating, and deleting calendar events, as well as querying calendar availability.

Note:
    This toolkit requires a valid 'credentials.json' file with Google OAuth2 credentials
    in the root directory. These credentials must have appropriate Google Calendar API permissions.

Examples:
    >>> from haive.tools.toolkits.google_calendar import google_calendar_toolkit
    >>> # Access the list of calendar tools
    >>> calendar_tools = google_calendar_toolkit
    >>> # Use a specific tool (e.g., to create an event)
    >>> create_event_tool = [t for t in calendar_tools if 'create' in t.name.lower()][0]
    >>> result = create_event_tool.invoke({"summary": "Team Meeting", "start": "2023-07-21T10:00:00", "end": "2023-07-21T11:00:00"})
"""

import os
from typing import Any

from langchain_google_community.calendar.toolkit import CalendarToolkit
from pydantic import BaseModel, Field


class CalendarEvent(BaseModel):
    """Model representing a Google Calendar event.

    Attributes:
        summary (str): The title/summary of the calendar event.
        start (str): The start time of the event in ISO format (YYYY-MM-DDTHH:MM:SS).
        end (str): The end time of the event in ISO format (YYYY-MM-DDTHH:MM:SS).
        description (Optional[str]): Optional description for the event.
        location (Optional[str]): Optional location for the event.
        attendees (Optional[List[str]]): Optional list of attendee email addresses.
    """

    summary: str = Field(..., description="The title/summary of the calendar event")
    start: str = Field(
        ..., description="The start time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    )
    end: str = Field(
        ..., description="The end time in ISO format (YYYY-MM-DDTHH:MM:SS)"
    )
    description: str | None = Field(
        None, description="Optional description for the event"
    )
    location: str | None = Field(None, description="Optional location for the event")
    attendees: list[str] | None = Field(
        None, description="Optional list of attendee email addresses"
    )


class CalendarResponse(BaseModel):
    """Response model for Google Calendar operations.

    Attributes:
        success (bool): Whether the operation was successful.
        data (Optional[Dict[str, Any]]): Optional data returned from the operation.
        message (Optional[str]): Optional message providing details about the operation result.
    """

    success: bool = Field(..., description="Whether the operation was successful")
    data: dict[str, Any] | None = Field(
        None, description="Optional data returned from the operation"
    )
    message: str | None = Field(
        None, description="Optional message about the operation result"
    )


def initialize_google_calendar_toolkit():
    """Initialize the Google Calendar toolkit with OAuth2 credentials.

    This function checks for the existence of the credentials file and initializes
    the Google Calendar toolkit if the file exists.

    Returns:
        list: A list of Google Calendar tools provided by the toolkit.

    Raises:
        FileNotFoundError: If the credentials.json file is not found.
        Exception: If initialization fails for any other reason.
    """
    # Define the credentials file path
    CREDENTIALS_FILE = "credentials.json"

    # Check if the credentials file exists in the root directory
    if not os.path.exists(CREDENTIALS_FILE):
        error_msg = f"Error: '{CREDENTIALS_FILE}' not found in the root directory."
        print(f"❌ {error_msg}")
        print(
            "🔹 Please ensure the credentials file is present before running the script."
        )
        raise FileNotFoundError(error_msg)

    # Initialize the Google Calendar toolkit
    try:
        toolkit = CalendarToolkit().get_tools()
        print("✅ Google CalendarToolkit initialized successfully.")
        return toolkit
    except Exception as e:
        error_msg = f"Failed to initialize Google CalendarToolkit: {e}"
        print(f"❌ {error_msg}")
        raise Exception(error_msg)


# Initialize the Google Calendar toolkit
try:
    google_calendar_toolkit = initialize_google_calendar_toolkit()
except Exception:
    # Set to empty list if initialization fails, allowing the application to continue
    # but with calendar functionality disabled
    google_calendar_toolkit = []

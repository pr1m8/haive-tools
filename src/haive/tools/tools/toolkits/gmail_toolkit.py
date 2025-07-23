"""Gmail Toolkit Module

This toolkit provides a collection of tools to interact with the Gmail API,
allowing agents to read, send, and manage emails through a Google account.
The toolkit requires proper authentication via Google OAuth credentials.

The toolkit leverages the langchain_google_community.gmail.toolkit package
which provides a convenient wrapper around the Gmail API.

Examples:
    >>> from haive.tools.toolkits.gmail_toolkit import gmail_toolkit
    >>> # Use the tools for various Gmail operations
    >>> # For example, to send an email:
    >>> send_email_tool = [t for t in gmail_toolkit if t.name == "gmail_send"][0]
    >>> send_email_tool.invoke({
    ...     "message": "Hello from Haive!",
    ...     "to": "recipient@example.com",
    ...     "subject": "Testing Gmail Toolkit"
    ... })
"""

import os
import sys

from langchain_google_community.gmail.toolkit import GmailToolkit

# Define the credentials file path
CREDENTIALS_FILE = "credentials.json"

# Check if the credentials file exists in the root directory
if not os.path.exists(CREDENTIALS_FILE):
    print(f"❌ Error: '{CREDENTIALS_FILE}' not found in the root directory.")
    print("🔹 Please ensure the credentials file is present before running the script.")
    sys.exit(1)  # Exit the program if credentials are missing

# Initialize the Gmail toolkit only if credentials exist
try:
    gmail_toolkit = GmailToolkit().get_tools()
    print("✅ GmailToolkit initialized successfully.")
except Exception as e:
    print(f"❌ Failed to initialize GmailToolkit: {e}")

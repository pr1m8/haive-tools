"""Office 365 Toolkit for accessing Microsoft 365 services.

This toolkit provides a Langchain-compatible interface to Microsoft 365 services,
allowing agents to work with calendars, emails, and other Microsoft 365 data.
It handles authentication and provides ready-to-use tools for common operations.

Example:
    ```python
    # Tools are already initialized in this module
    from haive.tools.toolkits.office_365 import tools
    ```

Attributes:
    tools: The list of available Office 365 tools
"""

from haive.config.config import Config
from langchain_community.agent_toolkits import O365Toolkit
from langchain_community.tools.office365.events_search import O365SearchEvents

# 🔧 Required by Pydantic v2
O365SearchEvents.model_rebuild()

# 🔐 Validate environment variables
if not Config.AZURE_CLIENT_ID or not Config.AZURE_SECRET_ID:
    raise ValueError(
        "Error: The CLIENT_ID and CLIENT_SECRET environmental variables have not been set. "
        "Visit https://learn.microsoft.com/en-us/graph/auth/"
    )

# ✅ Initialize O365 Toolkit
toolkit = O365Toolkit(
    client_id=Config.AZURE_CLIENT_ID,
    client_secret=Config.AZURE_SECRET_ID,
    tenant_id=Config.AZURE_TENANT_ID,
    scopes=[
        "offline_access",
        "https://graph.microsoft.com/Calendars.Read",
        "https://graph.microsoft.com/Mail.Read",
        "https://graph.microsoft.com/User.Read",
    ],
)

# Get all available tools from the toolkit
tools = toolkit.get_tools()
print(f"✅ Loaded O365 tools: {[t.name for t in tools]}")

# The tools include:
# - O365SearchEvents: Search for calendar events
# - O365SendMessage: Send an email message
# - O365SearchMessages: Search for email messages
# - O365GetMessage: Get a specific email message by ID

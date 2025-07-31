"""Twilio toolkit for sending SMS messages and making phone calls.

This module provides tools for interacting with the Twilio API to send SMS
messages and make phone calls. The toolkit leverages LangChain's TwilioAPIWrapper
to interact with the Twilio API.

To use this toolkit, you need to have Twilio credentials set in your environment
variables:
- TWILIO_ACCOUNT_SID: Your Twilio account SID
- TWILIO_AUTH_TOKEN: Your Twilio auth token

You can obtain these credentials by signing up at https://www.twilio.com/.

Typical usage:
    from haive.tools.toolkits.twilio_toolkit import twilio_toolkit

    # Use in an agent
    agent = Agent(tools=twilio_toolkit)
    agent.run("Send a text message to +1234567890 with the message 'Hello!'")

"""

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities.twilio import TwilioAPIWrapper
from langchain_core.tools import BaseTool

from haive.config.config import Config


def get_twilio_tools() -> list[BaseTool]:
    """Get tools for interacting with the Twilio API.

    This function creates and returns tools for sending SMS messages and making
    phone calls using the Twilio API. It requires Twilio credentials to be set
    in the environment.

    Returns:
        A list of BaseTool instances for interacting with Twilio.

    Raises:
        ValueError: If TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN is not set.

    """
    # Check if Twilio credentials are set
    if not Config.TWILIO_ACCOUNT_SID:
        raise ValueError("TWILIO_ACCOUNT_SID is not set")
    if not Config.TWILIO_AUTH_TOKEN:
        raise ValueError("TWILIO_AUTH_TOKEN is not set")

    # Load the Twilio tools
    return load_tools(["twilio"])


# Create the Twilio API wrapper
twilio_wrapper = TwilioAPIWrapper()

# Load the Twilio tools
twilio_toolkit = get_twilio_tools()

# Example usage (commented out to prevent accidental execution)
# twilio_toolkit[0].invoke(
#     input={'query': 'send a text message to +1234567890 with the message "Hello, world!"'}
# )

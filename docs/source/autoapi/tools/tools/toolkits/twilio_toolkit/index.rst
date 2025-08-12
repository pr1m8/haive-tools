
:py:mod:`tools.tools.toolkits.twilio_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.twilio_toolkit

Twilio toolkit for sending SMS messages and making phone calls.

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


.. autolink-examples:: tools.tools.toolkits.twilio_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.twilio_toolkit.get_twilio_tools
   tools.tools.toolkits.twilio_toolkit.get_twilio_wrapper

.. py:function:: get_twilio_tools() -> list[langchain_core.tools.BaseTool]

   Get tools for interacting with the Twilio API.

   This function creates and returns tools for sending SMS messages and making
   phone calls using the Twilio API. It requires Twilio credentials to be set
   in the environment.

   :returns: A list of BaseTool instances for interacting with Twilio,
             empty list if credentials are missing or other issues occur.


   .. autolink-examples:: get_twilio_tools
      :collapse:

.. py:function:: get_twilio_wrapper()

   Get Twilio API wrapper with proper error handling.

   :returns: TwilioAPIWrapper instance if credentials are available, None otherwise.


   .. autolink-examples:: get_twilio_wrapper
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.twilio_toolkit
   :collapse:
   
.. autolink-skip:: next


:py:mod:`tools.tools.hinge_tools`
=================================

.. py:module:: tools.tools.hinge_tools

Hinge Dating App API Integration Module.

This module provides tools for interacting with the Hinge dating app through the
squeaky_hinge unofficial API. It allows programmatic access to Hinge functionalities
like fetching messages and sending messages to matches.

NOTE: This is an example integration that would require proper authentication
with a valid Hinge account. The current implementation uses a placeholder phone number
and is meant for demonstration purposes only.

.. rubric:: Examples

>>> from haive.tools.tools.hinge_tools import api
>>> # After proper authentication:
>>> conversations = api.fetch_messages()
>>> print(f"You have {len(conversations)} conversations")

>>> # To send a message to a match:
>>> # api.send_message(user_id="USER_ID", text="Hello!")


.. autolink-examples:: tools.tools.hinge_tools
   :collapse:





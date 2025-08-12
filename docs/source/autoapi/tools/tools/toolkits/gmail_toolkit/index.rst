
:py:mod:`tools.tools.toolkits.gmail_toolkit`
============================================

.. py:module:: tools.tools.toolkits.gmail_toolkit

Gmail Toolkit Module.

This toolkit provides a collection of tools to interact with the Gmail API,
allowing agents to read, send, and manage emails through a Google account.
The toolkit requires proper authentication via Google OAuth credentials.

The toolkit leverages the langchain_google_community.gmail.toolkit package
which provides a convenient wrapper around the Gmail API.

.. rubric:: Examples

>>> from haive.tools.toolkits.gmail_toolkit import gmail_toolkit
>>> # Use the tools for various Gmail operations
>>> # For example, to send an email:
>>> send_email_tool = [t for t in gmail_toolkit if t.name == "gmail_send"][0]
>>> send_email_tool.invoke({
...     "message": "Hello from Haive!",
...     "to": "recipient@example.com",
...     "subject": "Testing Gmail Toolkit"
... })


.. autolink-examples:: tools.tools.toolkits.gmail_toolkit
   :collapse:





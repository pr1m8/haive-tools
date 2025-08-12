
:py:mod:`tools.tools.toolkits.stripe_toolkit`
=============================================

.. py:module:: tools.tools.toolkits.stripe_toolkit

Stripe Toolkit Module.

This module provides a toolkit for interacting with the Stripe API for payment processing
and financial operations. It leverages the stripe-agent-toolkit package to provide
a comprehensive set of tools for Stripe operations.

The toolkit provides access to various Stripe features including:
- Payment link creation and management
- Customer data management
- Subscription handling
- Invoice operations
- Product and price management
- Payment method operations

A Stripe secret key is required to use these tools. You can obtain a key from your
Stripe dashboard: https://dashboard.stripe.com/apikeys

Required Environment Variables:
    - STRIPE_SECRET_KEY: Your Stripe secret key

.. rubric:: Examples

>>> from haive.tools.toolkits.stripe_toolkit import stripe_agent_toolkit
>>> # Access tools from the toolkit
>>> payment_link_tools = stripe_agent_toolkit.get_tools_for_category("payment_links")

>>> # Or create a custom instance with specific permissions
>>> from haive.tools.toolkits.stripe_toolkit import create_stripe_toolkit
>>> custom_config = {
...     "actions": {
...         "payment_links": {"create": True, "list": True},
...         "customers": {"create": True, "retrieve": True}
...     }
... }
>>> custom_toolkit = create_stripe_toolkit("sk_test_your_key", custom_config)


.. autolink-examples:: tools.tools.toolkits.stripe_toolkit
   :collapse:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.stripe_toolkit.create_stripe_toolkit

.. py:function:: create_stripe_toolkit(secret_key: str | None = None, configuration: dict[str, Any] | None = None) -> stripe_agent_toolkit.crewai.toolkit.StripeAgentToolkit

   Create a Stripe toolkit instance with the provided or environment API key.

   This function initializes a Stripe Agent Toolkit with the specified configuration
   for accessing various Stripe API endpoints and operations.

   :param secret_key: Stripe secret key. If not provided, will use
                      the STRIPE_SECRET_KEY environment variable.
   :type secret_key: Optional[str]
   :param configuration: Configuration dictionary specifying
                         which Stripe operations should be enabled. Default enables payment link creation.
   :type configuration: Optional[Dict[str, Any]]

   :returns: A toolkit containing tools for interacting with Stripe API.
   :rtype: StripeAgentToolkit

   :raises ValueError: If no secret key is available (neither provided nor in environment).


   .. autolink-examples:: create_stripe_toolkit
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.stripe_toolkit
   :collapse:
   
.. autolink-skip:: next

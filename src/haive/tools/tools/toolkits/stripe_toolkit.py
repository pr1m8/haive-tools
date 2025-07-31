"""Stripe Toolkit Module.

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

Examples:
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

"""

import os
from typing import Any
import warnings

from dotenv import load_dotenv
from stripe_agent_toolkit.crewai.toolkit import StripeAgentToolkit


# Load environment variables from .env file if it exists
load_dotenv(".env")


def create_stripe_toolkit(
    secret_key: str | None = None, configuration: dict[str, Any] | None = None
) -> StripeAgentToolkit:
    """Create a Stripe toolkit instance with the provided or environment API key.

    This function initializes a Stripe Agent Toolkit with the specified configuration
    for accessing various Stripe API endpoints and operations.

    Args:
        secret_key (Optional[str]): Stripe secret key. If not provided, will use
            the STRIPE_SECRET_KEY environment variable.
        configuration (Optional[Dict[str, Any]]): Configuration dictionary specifying
            which Stripe operations should be enabled. Default enables payment link creation.

    Returns:
        StripeAgentToolkit: A toolkit containing tools for interacting with Stripe API.

    Raises:
        ValueError: If no secret key is available (neither provided nor in environment).

    """
    if not secret_key:
        secret_key = os.getenv("STRIPE_SECRET_KEY")

    if not secret_key:
        raise ValueError(
            "Stripe secret key is required. Set STRIPE_SECRET_KEY environment variable or provide secret_key parameter."
        )

    if not configuration:
        configuration = {
            "actions": {
                "payment_links": {
                    "create": True,
                },
            }
        }

    return StripeAgentToolkit(secret_key=secret_key, configuration=configuration)


# Create a default toolkit instance for easy importing with minimal permissions
# Only enables payment link creation by default
try:
    stripe_agent_toolkit = create_stripe_toolkit()
except ValueError as e:
    warnings.warn(
        f"Stripe toolkit initialization failed: {e}. Set STRIPE_SECRET_KEY environment variable.",
        stacklevel=2,
    )
    # Create a None value that will raise proper errors if accessed
    stripe_agent_toolkit = None

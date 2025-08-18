"""Bank Identification Number (BIN) lookup tool using the Binlist.net API.

This module provides a tool for looking up information about payment cards based on their
Bank Identification Number (BIN) or Issuer Identification Number (IIN), which is the first
6 to 8 digits of a card number. The tool uses the Binlist.net API to retrieve information
such as the card scheme, type, brand, country of issuance, and issuing bank.

This information can be useful for payment processing, fraud detection, and understanding
the origin of payment cards.

Examples:
            from haive.tools.tools.binlist_lookup import bin_lookup_tool

            # Add to your agent's toolkit
            agent = Agent(tools=[bin_lookup_tool])

            # Example use in an agent
            response = agent.run("Look up information about a Visa card with BIN 411111")

Note:
    - The Binlist.net API has rate limits and usage restrictions
    - Only the first 6-8 digits should be provided, not the full card number
    - No authentication is required for basic lookups

"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class BinLookupInput(BaseModel):
    """Input model for the BIN lookup tool.

    Attributes:
        bin_number: The first 6 to 8 digits of a payment card number, also known as
                    the Bank Identification Number (BIN) or Issuer Identification Number (IIN).
                    This identifies the issuing bank or financial institution.

    """

    bin_number: str = Field(..., description="The first 6 to 8 digits of a card number")


def lookup_bin(bin_input: BinLookupInput) -> dict:
    """Look up information about a payment card based on its BIN/IIN using the.
    Binlist.net API.

    Args:
        bin_input: A BinLookupInput object containing the bin_number to look up.

    Returns:
        dict: A dictionary containing information about the card, including:
            - scheme (e.g., visa, mastercard)
            - type (e.g., debit, credit)
            - brand
            - country information
            - bank information
            - Or an error message if the BIN is not found

    Raises:
        requests.exceptions.HTTPError: If the API request fails for any reason other than a 404.

    """
    headers = {"Accept-Version": "3"}
    response = requests.get(
        f"https://lookup.binlist.net/{bin_input.bin_number}", headers=headers
    )
    if response.status_code == 404:
        return {"error": "No matching card found"}
    response.raise_for_status()
    return response.json()


# Create a structured tool from the lookup_bin function
bin_lookup_tool = StructuredTool.from_function(
    name="lookup_card_bin_info",
    description="Look up card information based on the first 6 to 8 digits (BIN/IIN) using Binlist.net API",
    func=lookup_bin,
)

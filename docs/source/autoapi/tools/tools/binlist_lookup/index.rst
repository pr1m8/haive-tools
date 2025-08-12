
:py:mod:`tools.tools.binlist_lookup`
====================================

.. py:module:: tools.tools.binlist_lookup

Bank Identification Number (BIN) lookup tool using the Binlist.net API.

This module provides a tool for looking up information about payment cards based on their
Bank Identification Number (BIN) or Issuer Identification Number (IIN), which is the first
6 to 8 digits of a card number. The tool uses the Binlist.net API to retrieve information
such as the card scheme, type, brand, country of issuance, and issuing bank.

This information can be useful for payment processing, fraud detection, and understanding
the origin of payment cards.

.. rubric:: Example

```python
from haive.tools.tools.binlist_lookup import bin_lookup_tool

# Add to your agent's toolkit
agent = Agent(tools=[bin_lookup_tool])

# Example use in an agent
response = agent.run("Look up information about a Visa card with BIN 411111")
```

.. note::

   - The Binlist.net API has rate limits and usage restrictions
   - Only the first 6-8 digits should be provided, not the full card number
   - No authentication is required for basic lookups


.. autolink-examples:: tools.tools.binlist_lookup
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.binlist_lookup.BinLookupInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BinLookupInput:

   .. graphviz::
      :align: center

      digraph inheritance_BinLookupInput {
        node [shape=record];
        "BinLookupInput" [label="BinLookupInput"];
        "pydantic.BaseModel" -> "BinLookupInput";
      }

.. autopydantic_model:: tools.tools.binlist_lookup.BinLookupInput
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   tools.tools.binlist_lookup.lookup_bin

.. py:function:: lookup_bin(bin_input: BinLookupInput) -> dict

   Look up information about a payment card based on its BIN/IIN using the.
   Binlist.net API.

   :param bin_input: A BinLookupInput object containing the bin_number to look up.

   :returns:

             A dictionary containing information about the card, including:
                 - scheme (e.g., visa, mastercard)
                 - type (e.g., debit, credit)
                 - brand
                 - country information
                 - bank information
                 - Or an error message if the BIN is not found
   :rtype: dict

   :raises requests.exceptions.HTTPError: If the API request fails for any reason other than a 404.


   .. autolink-examples:: lookup_bin
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.binlist_lookup
   :collapse:
   
.. autolink-skip:: next

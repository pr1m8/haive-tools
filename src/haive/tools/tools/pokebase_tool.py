"""Pokebase Tool Module

This module provides a tool for accessing Pokémon data from the PokéAPI using the pokebase
library. It allows querying various Pokémon resources including Pokémon species, moves,
abilities, items, berries, locations, and types.

The PokéAPI is a comprehensive RESTful API providing data about the Pokémon video game series,
and pokebase is a Python wrapper that simplifies interaction with this API.

Examples:
    >>> from haive.tools.tools.pokebase_tool import query_pokebase_resource, PokeBaseQueryInput
    >>> input_data = PokeBaseQueryInput(resource_type="pokemon", identifier="pikachu")
    >>> result = query_pokebase_resource(input_data)
    >>> print(result["name"])  # Outputs: pikachu
"""

from typing import Literal

import pokebase as pb
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class PokeBaseQueryInput(BaseModel):
    """Input model for querying PokéAPI resources via the Pokebase library.

    This model defines the parameters needed to query different types of
    Pokémon-related resources from the PokéAPI.

    Attributes:
        resource_type (Literal): The type of resource to query, limited to supported
            PokéAPI resource types.
        identifier (str): The name or ID of the specific resource to retrieve.
    """

    resource_type: Literal[
        "pokemon", "berry", "move", "type_", "ability", "location", "item"
    ] = Field(
        ...,
        description="Type of the PokéAPI resource (e.g., 'pokemon', 'berry', 'move', etc.)",
    )
    identifier: str = Field(
        ..., description="Name or ID of the resource (e.g., 'pikachu', 'chesto', '1')"
    )


def query_pokebase_resource(input: PokeBaseQueryInput) -> dict:
    """Query a PokéAPI resource using the pokebase library.

    This function retrieves data for a specified Pokémon-related resource
    from the PokéAPI using the pokebase library and returns the data as
    a dictionary.

    Args:
        input (PokeBaseQueryInput): The input parameters specifying the resource
            type and identifier to query.

    Returns:
        dict: A dictionary containing the requested resource data with attributes
            such as name, ID, and resource-specific properties. Returns an error
            dictionary if the query fails.

    Raises:
        AttributeError: If an invalid resource_type is provided.
        ValueError: If the resource cannot be found with the given identifier.
    """
    resource_type = input.resource_type
    identifier = input.identifier

    try:
        resource_func = getattr(pb, resource_type)
        resource = resource_func(identifier)
        # Turn resource into dict, excluding private and complex attributes
        result = {
            k: v
            for k, v in resource.__dict__.items()
            if not k.startswith("_")
            and isinstance(v, (str, int, float, list, dict, bool, type(None)))
        }
        return result
    except Exception as e:
        return {"error": str(e)}


pokebase_tool = StructuredTool.from_function(
    func=query_pokebase_resource,
    name="pokebase_query_tool",
    description="Query PokeAPI resources like Pokémon, moves, items, and berries using Pokebase",
    return_direct=False,
)

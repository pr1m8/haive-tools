# pokebase_tool.py

from typing import Literal, Optional

import pokebase as pb
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class PokeBaseQueryInput(BaseModel):
    """Query any supported PokéAPI resource via Pokebase."""

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

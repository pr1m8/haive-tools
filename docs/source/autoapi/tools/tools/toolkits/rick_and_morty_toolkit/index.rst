
:py:mod:`tools.tools.toolkits.rick_and_morty_toolkit`
=====================================================

.. py:module:: tools.tools.toolkits.rick_and_morty_toolkit


Classes
-------

.. autoapisummary::

   tools.tools.toolkits.rick_and_morty_toolkit.FilterCharactersInput
   tools.tools.toolkits.rick_and_morty_toolkit.GetCharacterByIDInput
   tools.tools.toolkits.rick_and_morty_toolkit.GraphQLCharactersQueryInput
   tools.tools.toolkits.rick_and_morty_toolkit.GraphQLLocationByIDInput
   tools.tools.toolkits.rick_and_morty_toolkit.RickAndMortyToolkit


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FilterCharactersInput:

   .. graphviz::
      :align: center

      digraph inheritance_FilterCharactersInput {
        node [shape=record];
        "FilterCharactersInput" [label="FilterCharactersInput"];
        "pydantic.BaseModel" -> "FilterCharactersInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rick_and_morty_toolkit.FilterCharactersInput
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetCharacterByIDInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetCharacterByIDInput {
        node [shape=record];
        "GetCharacterByIDInput" [label="GetCharacterByIDInput"];
        "pydantic.BaseModel" -> "GetCharacterByIDInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rick_and_morty_toolkit.GetCharacterByIDInput
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphQLCharactersQueryInput:

   .. graphviz::
      :align: center

      digraph inheritance_GraphQLCharactersQueryInput {
        node [shape=record];
        "GraphQLCharactersQueryInput" [label="GraphQLCharactersQueryInput"];
        "pydantic.BaseModel" -> "GraphQLCharactersQueryInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rick_and_morty_toolkit.GraphQLCharactersQueryInput
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GraphQLLocationByIDInput:

   .. graphviz::
      :align: center

      digraph inheritance_GraphQLLocationByIDInput {
        node [shape=record];
        "GraphQLLocationByIDInput" [label="GraphQLLocationByIDInput"];
        "pydantic.BaseModel" -> "GraphQLLocationByIDInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rick_and_morty_toolkit.GraphQLLocationByIDInput
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RickAndMortyToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_RickAndMortyToolkit {
        node [shape=record];
        "RickAndMortyToolkit" [label="RickAndMortyToolkit"];
        "langchain_core.tools.BaseToolkit" -> "RickAndMortyToolkit";
      }

.. autoclass:: tools.tools.toolkits.rick_and_morty_toolkit.RickAndMortyToolkit
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   tools.tools.toolkits.rick_and_morty_toolkit.filter_characters
   tools.tools.toolkits.rick_and_morty_toolkit.get_character_by_id
   tools.tools.toolkits.rick_and_morty_toolkit.graphql_characters_query
   tools.tools.toolkits.rick_and_morty_toolkit.graphql_location_by_id

.. py:function:: filter_characters(name: str | None = None, status: str | None = None, species: str | None = None, gender: str | None = None) -> dict[str, Any]

   Filter Rick and Morty characters by various attributes.

   This function allows filtering characters by name, status, species, and gender.
   Filters can be combined to narrow down results.

   :param name: Filter by character name. Defaults to None.
   :type name: Optional[str], optional
   :param status: Filter by character status. Defaults to None.
                  Valid values: "alive", "dead", "unknown".
   :type status: Optional[str], optional
   :param species: Filter by character species. Defaults to None.
   :type species: Optional[str], optional
   :param gender: Filter by character gender. Defaults to None.
                  Valid values: "male", "female", "genderless", "unknown".
   :type gender: Optional[str], optional

   :returns: Dictionary containing filtered character results and pagination info.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: filter_characters
      :collapse:

.. py:function:: get_character_by_id(id: int) -> dict[str, Any]

   Get detailed information about a specific Rick and Morty character by ID.

   This function retrieves a character's complete information including their
   status, species, gender, origin, location, and episode appearances.

   :param id: The unique identifier of the character to retrieve.
   :type id: int

   :returns:

             Character data including name, status, species, gender,
                 origin, location, and episode appearances.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_character_by_id
      :collapse:

.. py:function:: graphql_characters_query(name: str | None = None, page: int | None = None) -> dict[str, Any]

   Query Rick and Morty characters using the GraphQL API.

   This function sends a GraphQL query to retrieve character information
   with optional filtering by name and pagination support.

   :param name: Character name to filter by. Defaults to None.
   :type name: Optional[str], optional
   :param page: Page number for paginated results. Defaults to None.
   :type page: Optional[int], optional

   :returns: GraphQL response containing character data and metadata.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: graphql_characters_query
      :collapse:

.. py:function:: graphql_location_by_id(id: int) -> dict[str, Any]

   Get detailed information about a specific location by ID using GraphQL.

   This function retrieves information about a location from the Rick and Morty
   universe, including its name, type, and dimension.

   :param id: The unique identifier of the location to retrieve.
   :type id: int

   :returns: GraphQL response containing location data.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: graphql_location_by_id
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.rick_and_morty_toolkit
   :collapse:
   
.. autolink-skip:: next

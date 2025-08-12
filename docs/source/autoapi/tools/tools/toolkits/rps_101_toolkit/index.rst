
:py:mod:`tools.tools.toolkits.rps_101_toolkit`
==============================================

.. py:module:: tools.tools.toolkits.rps_101_toolkit

Rock-Paper-Scissors 101 Toolkit Module.

This toolkit provides a collection of tools to interact with the RPS-101 API,
allowing users to access the expanded version of Rock-Paper-Scissors that includes 101
different objects. The API provides information about all objects, their winning outcomes,
and match results between any two objects. The API is provided by https://rps101.pythonanywhere.com/.

.. rubric:: Examples

>>> from haive.tools.toolkits.rps_101_toolkit import RPS101Toolkit
>>> toolkit = RPS101Toolkit()
>>> tools = toolkit.get_tools()
>>> # Get all RPS-101 objects
>>> objects = tools[0].invoke()
>>> print(objects[:3])  # First three objects
['Dynamite', 'Tornado', 'Quicksand']

>>> # Get winning outcomes for an object
>>> outcomes = tools[1].invoke({"object_name": "rock"})
>>> print(outcomes["defeats"][0])
{'name': 'fire', 'outcome': 'extinguishes'}

>>> # Get the result of a match between two objects
>>> match = tools[2].invoke({"object_one": "paper", "object_two": "rock"})
>>> print(f"{match['winner']} {match['outcome']} {match['loser']}")
'paper covers rock'


.. autolink-examples:: tools.tools.toolkits.rps_101_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.rps_101_toolkit.ObjectNameInput
   tools.tools.toolkits.rps_101_toolkit.RPS101Toolkit
   tools.tools.toolkits.rps_101_toolkit.RPSMatchInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ObjectNameInput:

   .. graphviz::
      :align: center

      digraph inheritance_ObjectNameInput {
        node [shape=record];
        "ObjectNameInput" [label="ObjectNameInput"];
        "pydantic.BaseModel" -> "ObjectNameInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rps_101_toolkit.ObjectNameInput
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

   Inheritance diagram for RPS101Toolkit:

   .. graphviz::
      :align: center

      digraph inheritance_RPS101Toolkit {
        node [shape=record];
        "RPS101Toolkit" [label="RPS101Toolkit"];
        "langchain_core.tools.BaseToolkit" -> "RPS101Toolkit";
      }

.. autoclass:: tools.tools.toolkits.rps_101_toolkit.RPS101Toolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RPSMatchInput:

   .. graphviz::
      :align: center

      digraph inheritance_RPSMatchInput {
        node [shape=record];
        "RPSMatchInput" [label="RPSMatchInput"];
        "pydantic.BaseModel" -> "RPSMatchInput";
      }

.. autopydantic_model:: tools.tools.toolkits.rps_101_toolkit.RPSMatchInput
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

   tools.tools.toolkits.rps_101_toolkit._get_all_rps101_objects
   tools.tools.toolkits.rps_101_toolkit._get_rps101_match_result
   tools.tools.toolkits.rps_101_toolkit._get_rps101_object_outcomes

.. py:function:: _get_all_rps101_objects() -> list[str]

   Get a list of all 101 objects in the RPS-101 game.

   :returns: A list of all object names in the RPS-101 game.
   :rtype: List[str]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: _get_all_rps101_objects
      :collapse:

.. py:function:: _get_rps101_match_result(object_one: str, object_two: str) -> dict

   Get the result of a match between two RPS-101 objects.

   :param object_one: The name of the first object in the match.
   :type object_one: str
   :param object_two: The name of the second object in the match.
   :type object_two: str

   :returns:

             A dictionary containing the match result information.
                 Format: {"winner": str, "loser": str, "outcome": str}
   :rtype: dict

   :raises requests.RequestException: If the API request fails or the object names are invalid.


   .. autolink-examples:: _get_rps101_match_result
      :collapse:

.. py:function:: _get_rps101_object_outcomes(object_name: str) -> dict

   Get detailed information about a specific RPS-101 object, including what it.
   defeats.

   :param object_name: The name of the RPS-101 object to get information about.
   :type object_name: str

   :returns:

             A dictionary containing information about the object and what it defeats.
                 Format: {"name": str, "defeats": List[{"name": str, "outcome": str}]}
   :rtype: dict

   :raises requests.RequestException: If the API request fails or the object name is invalid.


   .. autolink-examples:: _get_rps101_object_outcomes
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.rps_101_toolkit
   :collapse:
   
.. autolink-skip:: next

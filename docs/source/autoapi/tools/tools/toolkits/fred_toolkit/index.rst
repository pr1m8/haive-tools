
:py:mod:`tools.tools.toolkits.fred_toolkit`
===========================================

.. py:module:: tools.tools.toolkits.fred_toolkit

Federal Reserve Economic Data (FRED) Toolkit Module.

This toolkit provides tools for accessing economic data from the Federal Reserve Bank of St. Louis
FRED API. It allows retrieval of economic time series data, categories, and related metadata.

FRED is a comprehensive database containing hundreds of thousands of economic time series
from dozens of national, international, public, and private sources.

Required Environment Variables:
    - FRED_API_KEY: Your FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html

.. rubric:: Examples

>>> from haive.tools.toolkits.fred_toolkit import get_series
>>> # Get information about GDP series
>>> gdp_info = get_series("GDP")
>>> print(f"Series title: {gdp_info['seriess'][0]['title']}")
Series title: Gross Domestic Product

>>> from haive.tools.toolkits.fred_toolkit import get_series_observations
>>> # Get GDP values for 2020-2022
>>> gdp_data = get_series_observations("GDP", "2020-01-01", "2022-12-31")
>>> for obs in gdp_data['observations'][:3]:
...     print(f"Date: {obs['date']}, Value: ${obs['value']} billion")
Date: 2020-01-01, Value: $21477.597 billion


.. autolink-examples:: tools.tools.toolkits.fred_toolkit
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.fred_toolkit.CategoryInput
   tools.tools.toolkits.fred_toolkit.FREDToolkit
   tools.tools.toolkits.fred_toolkit.SeriesInput
   tools.tools.toolkits.fred_toolkit.SeriesObservationsInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CategoryInput:

   .. graphviz::
      :align: center

      digraph inheritance_CategoryInput {
        node [shape=record];
        "CategoryInput" [label="CategoryInput"];
        "pydantic.BaseModel" -> "CategoryInput";
      }

.. autopydantic_model:: tools.tools.toolkits.fred_toolkit.CategoryInput
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

   Inheritance diagram for FREDToolkit:

   .. graphviz::
      :align: center

      digraph inheritance_FREDToolkit {
        node [shape=record];
        "FREDToolkit" [label="FREDToolkit"];
        "langchain_core.tools.BaseToolkit" -> "FREDToolkit";
      }

.. autoclass:: tools.tools.toolkits.fred_toolkit.FREDToolkit
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SeriesInput:

   .. graphviz::
      :align: center

      digraph inheritance_SeriesInput {
        node [shape=record];
        "SeriesInput" [label="SeriesInput"];
        "pydantic.BaseModel" -> "SeriesInput";
      }

.. autopydantic_model:: tools.tools.toolkits.fred_toolkit.SeriesInput
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

   Inheritance diagram for SeriesObservationsInput:

   .. graphviz::
      :align: center

      digraph inheritance_SeriesObservationsInput {
        node [shape=record];
        "SeriesObservationsInput" [label="SeriesObservationsInput"];
        "pydantic.BaseModel" -> "SeriesObservationsInput";
      }

.. autopydantic_model:: tools.tools.toolkits.fred_toolkit.SeriesObservationsInput
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

   tools.tools.toolkits.fred_toolkit.fred_get
   tools.tools.toolkits.fred_toolkit.get_category
   tools.tools.toolkits.fred_toolkit.get_category_children
   tools.tools.toolkits.fred_toolkit.get_category_series
   tools.tools.toolkits.fred_toolkit.get_series
   tools.tools.toolkits.fred_toolkit.get_series_observations

.. py:function:: fred_get(endpoint: str, params: dict[str, Any]) -> dict[str, Any]

   Helper function to call the FRED API with proper authentication and formatting.

   This function adds the API key and sets the response format to JSON before
   making the request to the specified FRED API endpoint.

   :param endpoint: The FRED API endpoint to call (e.g., "series", "category").
   :type endpoint: str
   :param params: Parameters to include in the API request.
   :type params: Dict[str, Any]

   :returns: The JSON response from the FRED API.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.
   :raises ValueError: If FRED_API_KEY is not set in the environment.


   .. autolink-examples:: fred_get
      :collapse:

.. py:function:: get_category(category_id: int) -> dict[str, Any]

   Get information about a FRED category by its ID.

   Categories in FRED organize data series into groups like 'Money, Banking, & Finance',
   'Population, Employment, & Labor Markets', etc.

   :param category_id: The FRED category ID to fetch (e.g., 0 for root category).
   :type category_id: int

   :returns: Category information including name and notes.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_category
      :collapse:

.. py:function:: get_category_children(category_id: int) -> dict[str, Any]

   Get the child categories of a specified FRED category.

   This function retrieves subcategories for a given parent category,
   allowing exploration of the FRED category hierarchy.

   :param category_id: The parent category ID to get children for.
   :type category_id: int

   :returns: List of child categories with their IDs and names.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_category_children
      :collapse:

.. py:function:: get_category_series(category_id: int) -> dict[str, Any]

   Get all series belonging to a specified FRED category.

   This function retrieves the economic data series that are classified under
   the specified category.

   :param category_id: The category ID to get series for.
   :type category_id: int

   :returns: List of series in the category with metadata.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_category_series
      :collapse:

.. py:function:: get_series(series_id: str) -> dict[str, Any]

   Get metadata about a specific FRED data series.

   This function retrieves detailed information about an economic data series,
   including its title, units, frequency, seasonal adjustment, and more.

   :param series_id: The FRED series ID (e.g., 'GDP', 'UNRATE', 'CPIAUCSL').
   :type series_id: str

   :returns: Detailed metadata about the requested series.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_series
      :collapse:

.. py:function:: get_series_observations(series_id: str, start_date: str | None = None, end_date: str | None = None) -> dict[str, Any]

   Get the actual data values (observations) for a FRED time series.

   This function retrieves the time series data points for a specified economic indicator,
   with optional date range filtering.

   :param series_id: The FRED series ID to fetch observations for.
   :type series_id: str
   :param start_date: Start date in YYYY-MM-DD format. Defaults to None.
   :type start_date: Optional[str], optional
   :param end_date: End date in YYYY-MM-DD format. Defaults to None.
   :type end_date: Optional[str], optional

   :returns: Series observations with dates and values.
   :rtype: Dict[str, Any]

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_series_observations
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.fred_toolkit
   :collapse:
   
.. autolink-skip:: next

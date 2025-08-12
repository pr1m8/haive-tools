
:py:mod:`tools.tools.report_of_the_week_tool`
=============================================

.. py:module:: tools.tools.report_of_the_week_tool

Report Of The Week API Tools Module.

This module provides tools for accessing food and drink review data from "The Report Of The Week"
API, which contains reviews by the popular YouTube food reviewer known as "Reviewbrah". The tools
allow fetching all reviews, filtering by category, and retrieving reviews within a date range.

The Report Of The Week is a YouTube channel featuring food and beverage reviews, presented in a
unique style with categories like "Running On Empty" (food reviews) and "Energy Crisis" (energy drink reviews).

.. rubric:: Examples

>>> from haive.tools.tools.report_of_the_week_tool import get_all_reports, GetAllReportsInput
>>> results = get_all_reports(GetAllReportsInput())
>>> print(f"Found {len(results)} reviews")

>>> from haive.tools.tools.report_of_the_week_tool import get_reports_by_category, GetReportsByCategoryInput
>>> energy_reviews = get_reports_by_category(GetReportsByCategoryInput(category="Energy Crisis"))
>>> print(f"Found {len(energy_reviews)} energy drink reviews")


.. autolink-examples:: tools.tools.report_of_the_week_tool
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.report_of_the_week_tool.GetAllReportsInput
   tools.tools.report_of_the_week_tool.GetReportsByCategoryInput
   tools.tools.report_of_the_week_tool.GetReportsByDateRangeInput


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GetAllReportsInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetAllReportsInput {
        node [shape=record];
        "GetAllReportsInput" [label="GetAllReportsInput"];
        "pydantic.BaseModel" -> "GetAllReportsInput";
      }

.. autopydantic_model:: tools.tools.report_of_the_week_tool.GetAllReportsInput
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

   Inheritance diagram for GetReportsByCategoryInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetReportsByCategoryInput {
        node [shape=record];
        "GetReportsByCategoryInput" [label="GetReportsByCategoryInput"];
        "pydantic.BaseModel" -> "GetReportsByCategoryInput";
      }

.. autopydantic_model:: tools.tools.report_of_the_week_tool.GetReportsByCategoryInput
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

   Inheritance diagram for GetReportsByDateRangeInput:

   .. graphviz::
      :align: center

      digraph inheritance_GetReportsByDateRangeInput {
        node [shape=record];
        "GetReportsByDateRangeInput" [label="GetReportsByDateRangeInput"];
        "pydantic.BaseModel" -> "GetReportsByDateRangeInput";
      }

.. autopydantic_model:: tools.tools.report_of_the_week_tool.GetReportsByDateRangeInput
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

   tools.tools.report_of_the_week_tool.get_all_reports
   tools.tools.report_of_the_week_tool.get_reports_by_category
   tools.tools.report_of_the_week_tool.get_reports_by_date_range

.. py:function:: get_all_reports(_: GetAllReportsInput) -> list

   Retrieve all food and drink reviews from The Report Of The Week API.

   This function fetches the complete collection of reviews from the API
   without any filtering.

   :param _: Empty input model (placeholder).
   :type _: GetAllReportsInput

   :returns:

             A list of dictionaries, each containing a review with fields such as
                 product name, category, rating, and date.
   :rtype: list

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_all_reports
      :collapse:

.. py:function:: get_reports_by_category(category_input: GetReportsByCategoryInput) -> list

   Retrieve reviews filtered by a specific category.

   This function fetches reviews from The Report Of The Week API that match
   the specified category.

   :param category_input: Input containing the category to filter by.
   :type category_input: GetReportsByCategoryInput

   :returns:

             A list of dictionaries, each containing a review in the specified category
                 with fields such as product name, rating, and date.
   :rtype: list

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_reports_by_category
      :collapse:

.. py:function:: get_reports_by_date_range(date_range_input: GetReportsByDateRangeInput) -> list

   Retrieve reviews published within a specific date range.

   This function fetches reviews from The Report Of The Week API that were
   published between the specified start and end dates.

   :param date_range_input: Input containing the start and end dates.
   :type date_range_input: GetReportsByDateRangeInput

   :returns:

             A list of dictionaries, each containing a review published within the
                 specified date range with fields such as product name, category, and rating.
   :rtype: list

   :raises requests.RequestException: If the API request fails.


   .. autolink-examples:: get_reports_by_date_range
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.report_of_the_week_tool
   :collapse:
   
.. autolink-skip:: next

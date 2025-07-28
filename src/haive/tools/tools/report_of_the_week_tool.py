"""Report Of The Week API Tools Module.

This module provides tools for accessing food and drink review data from "The Report Of The Week"
API, which contains reviews by the popular YouTube food reviewer known as "Reviewbrah". The tools
allow fetching all reviews, filtering by category, and retrieving reviews within a date range.

The Report Of The Week is a YouTube channel featuring food and beverage reviews, presented in a
unique style with categories like "Running On Empty" (food reviews) and "Energy Crisis" (energy drink reviews).

Examples:
    >>> from haive.tools.tools.report_of_the_week_tool import get_all_reports, GetAllReportsInput
    >>> results = get_all_reports(GetAllReportsInput())
    >>> print(f"Found {len(results)} reviews")

    >>> from haive.tools.tools.report_of_the_week_tool import get_reports_by_category, GetReportsByCategoryInput
    >>> energy_reviews = get_reports_by_category(GetReportsByCategoryInput(category="Energy Crisis"))
    >>> print(f"Found {len(energy_reviews)} energy drink reviews")
"""

import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

BASE_URL = "https://thereportoftheweek-api.herokuapp.com"


# --- Tool: Get All Reports ---
class GetAllReportsInput(BaseModel):
    """Input model for retrieving all reports from The Report Of The Week API.

    This empty model is used as a placeholder for the get_all_reports function
    to maintain a consistent API pattern across tools.
    """


def get_all_reports(_: GetAllReportsInput) -> list:
    """Retrieve all food and drink reviews from The Report Of The Week API.

    This function fetches the complete collection of reviews from the API
    without any filtering.

    Args:
        _ (GetAllReportsInput): Empty input model (placeholder).

    Returns:
        list: A list of dictionaries, each containing a review with fields such as
            product name, category, rating, and date.

    Raises:
        requests.RequestException: If the API request fails.
    """
    response = requests.get(f"{BASE_URL}/reports")
    response.raise_for_status()
    return response.json()


get_all_reports_tool = StructuredTool.from_function(
    name="get_all_report_of_the_week_reviews",
    description="Retrieve all food and drink reviews from The Report Of The Week.",
    func=get_all_reports,
    args_schema=GetAllReportsInput,
)


# --- Tool: Filter by Category ---
class GetReportsByCategoryInput(BaseModel):
    """Input model for retrieving reports filtered by category.

    This model defines the parameters needed to filter reviews by their
    category designation.

    Attributes:
        category (str): The category to filter reviews by, such as 'Energy Crisis'
            for energy drinks or 'Running On Empty' for food reviews.
    """

    category: str = Field(
        ...,
        description="The category to filter by, such as 'Energy Crisis' or 'Running On Empty'.",
    )


def get_reports_by_category(input: GetReportsByCategoryInput) -> list:
    """Retrieve reviews filtered by a specific category.

    This function fetches reviews from The Report Of The Week API that match
    the specified category.

    Args:
        input (GetReportsByCategoryInput): Input containing the category to filter by.

    Returns:
        list: A list of dictionaries, each containing a review in the specified category
            with fields such as product name, rating, and date.

    Raises:
        requests.RequestException: If the API request fails.
    """
    response = requests.get(f"{BASE_URL}/reports", params={"category": input.category})
    response.raise_for_status()
    return response.json()


get_reports_by_category_tool = StructuredTool.from_function(
    name="get_report_of_the_week_by_category",
    description="Get reviews by category, such as 'Energy Crisis' for energy drinks or 'Running On Empty' for food.",
    func=get_reports_by_category,
    args_schema=GetReportsByCategoryInput,
)


# --- Tool: Filter by Date Range ---
class GetReportsByDateRangeInput(BaseModel):
    """Input model for retrieving reports within a specific date range.

    This model defines the parameters needed to filter reviews by their
    publication date.

    Attributes:
        start_date (str): The beginning date of the range in YYYY-M-D format.
        end_date (str): The ending date of the range in YYYY-M-D format.
    """

    start_date: str = Field(..., description="Start date in YYYY-M-D format.")
    end_date: str = Field(..., description="End date in YYYY-M-D format.")


def get_reports_by_date_range(input: GetReportsByDateRangeInput) -> list:
    """Retrieve reviews published within a specific date range.

    This function fetches reviews from The Report Of The Week API that were
    published between the specified start and end dates.

    Args:
        input (GetReportsByDateRangeInput): Input containing the start and end dates.

    Returns:
        list: A list of dictionaries, each containing a review published within the
            specified date range with fields such as product name, category, and rating.

    Raises:
        requests.RequestException: If the API request fails.
    """
    query = f"{input.start_date}|{input.end_date}"
    response = requests.get(f"{BASE_URL}/reports", params={"between": query})
    response.raise_for_status()
    return response.json()


get_reports_by_date_range_tool = StructuredTool.from_function(
    name="get_report_of_the_week_by_date_range",
    description="Get reviews posted between two dates (format: YYYY-M-D).",
    func=get_reports_by_date_range,
    args_schema=GetReportsByDateRangeInput,
)


import requests
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class GenderizeResponse(BaseModel):
    """Response from the Genderize API"""
    name: str = Field(description="The name to predict gender for")
    gender: str | None = Field(description="The predicted gender of the name")
    probability: float | None = Field(description="The probability of the predicted gender")
    count: int = Field(description="The number of people with the name in the country")
    country_id: str | None = Field(description="The country code of the name")


def predict_gender(name: str, country_id: str | None = None) -> GenderizeResponse:
    url = "https://api.genderize.io"
    params = {"name": name}
    if country_id:
        params["country_id"] = country_id
    res = requests.get(url, params=params)
    res.raise_for_status()
    return GenderizeResponse(**res.json())




genderize_tool = StructuredTool.from_function(
        func=predict_gender,
        name="predict_gender",
        description="Predict gender from a single first name, with optional country scope.")


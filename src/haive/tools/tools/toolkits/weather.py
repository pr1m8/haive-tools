"""Weather Information Toolkit Module.

This toolkit provides tools for retrieving current weather information using the OpenWeatherMap API.
It supports structured data parsing and temperature unit conversion between Celsius and Fahrenheit.

Features:
- City and country-based weather lookups
- Structured data output with detailed weather metrics
- Customizable temperature units (Celsius/Fahrenheit)
- Automatic parsing of OpenWeatherMap API responses

Required Environment Variables:
    - OPENWEATHERMAP_API_KEY: Your OpenWeatherMap API key (will prompt if not found)

Examples:
    >>> from haive.tools.toolkits.weather import get_weather_by_city_country
    >>> # Get structured weather data for Tokyo, Japan
    >>> weather = get_weather_by_city_country("Tokyo", "jp", parse=True, temperature_unit="celsius")
    >>> print(f"Current temperature in {weather['location']}: {weather['temp_current_c']}°C")
    Current temperature in Tokyo, JP: 15.2°C

    >>> # Get raw weather data for New York, US in Fahrenheit
    >>> weather = get_weather_by_city_country("New York", "us", parse=True, temperature_unit="fahrenheit")
    >>> print(f"Feels like: {weather['temp_feels_like_c']}°F")
    Feels like: 46.58°F

"""

import getpass
import os
import re
from typing import Literal

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from haive.config.config import Config


class CityCountryWeatherInput(BaseModel):
    """Input schema for weather query by city and country.

    This model defines the parameters needed to request weather information
    from the OpenWeatherMap API, including location and formatting options.

    Attributes:
        city (str): The name of the city to get weather for.
        country (str): The 2-letter ISO country code in lowercase.
        parse (bool): Whether to return structured data or raw API response.
        temperature_unit (str): Unit for temperature values (celsius or fahrenheit).

    """

    city: str = Field(..., description="City name, e.g. 'Tokyo'")
    country: str = Field(
        ..., description="2-letter country code in lowercase, e.g. 'jp'"
    )
    parse: bool = Field(
        default=True, description="Whether to parse structured weather data"
    )
    temperature_unit: Literal["celsius", "fahrenheit"] = Field(
        default="celsius", description="Return temperatures in Celsius or Fahrenheit"
    )


class WeatherData(BaseModel):
    """Structured weather data model.

    This model represents parsed weather information from the OpenWeatherMap API,
    with fields for various weather metrics including temperature, wind, humidity,
    and precipitation.

    Attributes:
        location (Optional[str]): Location name in "City, Country" format.
        status (Optional[str]): Weather condition description (e.g., "Clear sky").
        wind_speed_mps (Optional[float]): Wind speed in meters per second.
        wind_direction_deg (Optional[int]): Wind direction in degrees.
        humidity_percent (Optional[int]): Relative humidity percentage.
        temp_current_c (Optional[float]): Current temperature in Celsius.
        temp_high_c (Optional[float]): Maximum temperature in Celsius.
        temp_low_c (Optional[float]): Minimum temperature in Celsius.
        temp_feels_like_c (Optional[float]): "Feels like" temperature in Celsius.
        rain_mm_last_hour (Optional[float]): Rainfall in millimeters over the last hour.
        cloud_cover_percent (Optional[int]): Cloud coverage percentage.

    """

    location: str | None = Field(
        None, description="Location name in City, Country format"
    )
    status: str | None = Field(None, description="Weather condition description")
    wind_speed_mps: float | None = Field(
        None, description="Wind speed in meters per second"
    )
    wind_direction_deg: int | None = Field(
        None, description="Wind direction in degrees"
    )
    humidity_percent: int | None = Field(
        None, description="Relative humidity percentage"
    )
    temp_current_c: float | None = Field(
        None, description="Current temperature in Celsius/Fahrenheit"
    )
    temp_high_c: float | None = Field(
        None, description="Maximum temperature in Celsius/Fahrenheit"
    )
    temp_low_c: float | None = Field(
        None, description="Minimum temperature in Celsius/Fahrenheit"
    )
    temp_feels_like_c: float | None = Field(
        None, description="'Feels like' temperature in Celsius/Fahrenheit"
    )
    rain_mm_last_hour: float | None = Field(
        None, description="Rainfall in millimeters over the last hour"
    )
    cloud_cover_percent: int | None = Field(
        None, description="Cloud coverage percentage"
    )

    def convert_to_fahrenheit(self) -> "WeatherData":
        """Convert all temperature values from Celsius to Fahrenheit.

        Returns:
            WeatherData: A new WeatherData instance with temperatures in Fahrenheit.

        """

        def c_to_f(c: float | None) -> float | None:
            return round(c * 9 / 5 + 32, 2) if c is not None else None

        return WeatherData(
            **self.dict(
                exclude={
                    "temp_current_c",
                    "temp_high_c",
                    "temp_low_c",
                    "temp_feels_like_c",
                }
            ),
            temp_current_c=c_to_f(self.temp_current_c),
            temp_high_c=c_to_f(self.temp_high_c),
            temp_low_c=c_to_f(self.temp_low_c),
            temp_feels_like_c=c_to_f(self.temp_feels_like_c),
        )

    @classmethod
    def from_openweather_response(cls, response: str) -> "WeatherData":
        """Parse the text response from OpenWeatherMap API into structured data.

        This method uses regular expressions to extract weather information from
        the text-based API response and creates a structured WeatherData object.

        Args:
            response (str): Raw text response from the OpenWeatherMap API.

        Returns:
            WeatherData: Structured weather data extracted from the response.

        """
        data = {}

        if match := re.search(
            r"In (.+?), the current weather is as follows:", response
        ):
            data["location"] = match.group(1).strip()

        if match := re.search(r"Detailed status: (.+)", response):
            data["status"] = match.group(1).strip()

        if match := re.search(r"Wind speed: ([\d.]+) m/s, direction: ()°", response):
            data["wind_speed_mps"] = float(match.group(1))
            data["wind_direction_deg"] = int(match.group(2))

        if match := re.search(r"Humidity: ()%", response):
            data["humidity_percent"] = int(match.group(1))

        if match := re.search(
            r"Temperature: - Current: ([\d.]+)°C - High: ([\d.]+)°C - Low: ([\d.]+)°C - Feels like: ([\d.]+)°C",
            response,
            re.DOTALL,
        ):
            data["temp_current_c"] = float(match.group(1))
            data["temp_high_c"] = float(match.group(2))
            data["temp_low_c"] = float(match.group(3))
            data["temp_feels_like_c"] = float(match.group(4))

        if match := re.search(r"Rain: \{[^}]*'1h': ([\d.]+)[^}]*\}", response):
            data["rain_mm_last_hour"] = float(match.group(1))

        if match := re.search(r"Cloud cover: ()%", response):
            data["cloud_cover_percent"] = int(match.group(1))

        return cls(**data)


def get_weather_by_city_country(
    city: str,
    country: str,
    parse: bool = True,
    temperature_unit: Literal["celsius", "fahrenheit"] = "celsius",
):
    """Fetch current weather information for a specific city and country.

    This function retrieves weather data from the OpenWeatherMap API for the
    specified location. It can return either raw API response or structured
    data with various weather metrics.

    Args:
        city (str): The name of the city (e.g., "London", "Tokyo").
        country (str): The 2-letter ISO country code in lowercase (e.g., "gb", "jp").
        parse (bool, optional): Whether to parse the response into structured data.
            Defaults to True.
        temperature_unit (str, optional): Unit for temperature values, either "celsius"
            or "fahrenheit". Defaults to "celsius".

    Returns:
        Union[dict, str]: Structured weather data as a dictionary if parse=True,
            otherwise the raw API response as a string.

    Raises:
        ValueError: If the API key is not provided and the user cancels the prompt.
        Exception: If the weather API request fails.

    """
    if not Config.OPENWEATHERMAP_API_KEY:
        os.environ["OPENWEATHERMAP_API_KEY"] = getpass.getpass(
            "Enter your OpenWeatherMap API Key: "
        )

    location = f"{city},{country}"
    tool = load_tools(["openweathermap-api"])[0]
    result = tool.run(location)

    if parse:
        data = WeatherData.from_openweather_response(result)
        if temperature_unit == "fahrenheit":
            data = data.convert_to_fahrenheit()
        return data.model_dump()

    return result


# --- Exported Tool ---
weather_tool = StructuredTool.from_function(
    func=get_weather_by_city_country,
    name="get_weather_by_city_country",
    description="Fetch current weather using city and 2-letter country code with optional structured output",
    args_schema=CityCountryWeatherInput,
    return_direct=True,
)

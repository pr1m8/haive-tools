
:py:mod:`tools.tools.toolkits.weather`
======================================

.. py:module:: tools.tools.toolkits.weather

Weather Information Toolkit Module.

This toolkit provides tools for retrieving current weather information using the OpenWeatherMap API.
It supports structured data parsing and temperature unit conversion between Celsius and Fahrenheit.

Features:
- City and country-based weather lookups
- Structured data output with detailed weather metrics
- Customizable temperature units (Celsius/Fahrenheit)
- Automatic parsing of OpenWeatherMap API responses

Required Environment Variables:
    - OPENWEATHERMAP_API_KEY: Your OpenWeatherMap API key (will prompt if not found)

.. rubric:: Examples

>>> from haive.tools.toolkits.weather import get_weather_by_city_country
>>> # Get structured weather data for Tokyo, Japan
>>> weather = get_weather_by_city_country("Tokyo", "jp", parse=True, temperature_unit="celsius")
>>> print(f"Current temperature in {weather['location']}: {weather['temp_current_c']}°C")
Current temperature in Tokyo, JP: 15.2°C

>>> # Get raw weather data for New York, US in Fahrenheit
>>> weather = get_weather_by_city_country("New York", "us", parse=True, temperature_unit="fahrenheit")
>>> print(f"Feels like: {weather['temp_feels_like_c']}°F")
Feels like: 46.58°F


.. autolink-examples:: tools.tools.toolkits.weather
   :collapse:

Classes
-------

.. autoapisummary::

   tools.tools.toolkits.weather.CityCountryWeatherInput
   tools.tools.toolkits.weather.WeatherData


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CityCountryWeatherInput:

   .. graphviz::
      :align: center

      digraph inheritance_CityCountryWeatherInput {
        node [shape=record];
        "CityCountryWeatherInput" [label="CityCountryWeatherInput"];
        "pydantic.BaseModel" -> "CityCountryWeatherInput";
      }

.. autopydantic_model:: tools.tools.toolkits.weather.CityCountryWeatherInput
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

   Inheritance diagram for WeatherData:

   .. graphviz::
      :align: center

      digraph inheritance_WeatherData {
        node [shape=record];
        "WeatherData" [label="WeatherData"];
        "pydantic.BaseModel" -> "WeatherData";
      }

.. autopydantic_model:: tools.tools.toolkits.weather.WeatherData
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

   tools.tools.toolkits.weather.get_weather_by_city_country

.. py:function:: get_weather_by_city_country(city: str, country: str, parse: bool = True, temperature_unit: Literal['celsius', 'fahrenheit'] = 'celsius')

   Fetch current weather information for a specific city and country.

   This function retrieves weather data from the OpenWeatherMap API for the
   specified location. It can return either raw API response or structured
   data with various weather metrics.

   :param city: The name of the city (e.g., "London", "Tokyo").
   :type city: str
   :param country: The 2-letter ISO country code in lowercase (e.g., "gb", "jp").
   :type country: str
   :param parse: Whether to parse the response into structured data.
                 Defaults to True.
   :type parse: bool, optional
   :param temperature_unit: Unit for temperature values, either "celsius"
                            or "fahrenheit". Defaults to "celsius".
   :type temperature_unit: str, optional

   :returns:

             Structured weather data as a dictionary if parse=True,
                 otherwise the raw API response as a string.
   :rtype: Union[dict, str]

   :raises ValueError: If the API key is not provided and the user cancels the prompt.
   :raises Exception: If the weather API request fails.


   .. autolink-examples:: get_weather_by_city_country
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: tools.tools.toolkits.weather
   :collapse:
   
.. autolink-skip:: next

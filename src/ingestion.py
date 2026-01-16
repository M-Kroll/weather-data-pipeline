"""
ingestion.py

This module is responsible for retrieving historical hourly weather data
from the Open-Meteo API and returning it as a pandas DataFrame.
"""

import logging
import pandas as pd
import requests_cache
from retry_requests import retry
import openmeteo_requests


def fetch_weather_data():
    """
    Fetches historical hourly weather data for Dortmund from the Open-Meteo API.

    Returns:
        pandas.DataFrame: Hourly weather data
    """
    
    logging.info("Starting ingestion module")
    logging.info("Fetching weather data from Open-Meteo API")

    # Setup API client with caching and retry logic
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # API endpoint and parameters
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 51.5149,
        "longitude": 7.466,
        "start_date": "2025-01-01",
        "end_date": "2025-01-31",
        "hourly": [
            "temperature_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ],
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    logging.info("Weather data successfully retrieved")

    # Extract hourly data
    hourly = response.Hourly()

    hourly_data = {
        "timestamp": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left",
        ),
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
        "precipitation": hourly.Variables(1).ValuesAsNumpy(),
        "weather_code": hourly.Variables(2).ValuesAsNumpy(),
        "wind_speed_10m": hourly.Variables(3).ValuesAsNumpy(),
    }

    df = pd.DataFrame(hourly_data)

    logging.info("Weather data converted to DataFrame")
    logging.info("Finished ingestion module")
    
    return df


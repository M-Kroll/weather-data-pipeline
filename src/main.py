"""
main.py

Entry point for the weather data pipeline.
Coordinates ingestion, validation and storage.
"""

import logging

from logging_config import setup_logging
from ingestion import fetch_weather_data
from validation import validate_weather_data
from storage import store_weather_data


def main():
    setup_logging()
    logging.info("Weather Data Pipeline started")

    df = fetch_weather_data()
    df = validate_weather_data(df)
    store_weather_data(df)

    logging.info("Weather Data Pipeline finished")


if __name__ == "__main__":
    main()

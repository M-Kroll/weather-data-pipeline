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
    
    # Configure centralized logging for the entire pipeline
    setup_logging()
    
    logging.info("Weather Data Pipeline started")

    # Ingest weather data from Open-Meteo API
    df = fetch_weather_data()

    # Validate the ingested data (schema, plausibility, time-series consistency)
    df = validate_weather_data(df)
    
    # Store the validated data in SQLite database
    store_weather_data(df)

    logging.info("Weather Data Pipeline finished")


if __name__ == "__main__":
    main()

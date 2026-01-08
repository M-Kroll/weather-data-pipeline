"""
validation.py

This module contains basic data validation logic.
"""

import logging


def validate_weather_data(df):
    """
    Validates the weather data.

    Args:
        df (pandas.DataFrame): Raw weather data

    Returns:
        pandas.DataFrame: Validated weather data
    """
    logging.info("Validating weather data (basic checks)")

    if df.empty:
        logging.warning("Weather data DataFrame is empty")

    return df

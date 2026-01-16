"""
validation.py

This module contains data validation logic for weather time-series data.
It performs schema validation, plausibility checks, and time-series
consistency checks to ensure reliable downstream processing.
"""

import logging
import pandas as pd


def validate_weather_data(df):
    """
    Validates the weather data.

    The function performs:
    - Schema validation
    - Plausibility validation
    - Time-series consistency checks

    Args:
        df (pandas.DataFrame): Raw weather data

    Returns:
        pandas.DataFrame: Validated and cleaned weather data

    Raises:
        ValueError: If critical schema checks fail
    """
    
    logging.info("Starting validation module")

    # ==========================================================
    # Schema validation
    # ==========================================================

    # Check 1: DataFrame must not be empty
    if df.empty:
        logging.error("Weather data DataFrame is empty")
        raise ValueError("Weather data DataFrame is empty")

    # Check 2: Required columns must exist
    required_columns = [
        "timestamp",
        "temperature_2m",
        "precipitation",
        "weather_code",
        "wind_speed_10m",
    ]

    for column in required_columns:
        if column not in df.columns:
            logging.error(f"Missing required column: {column}")
            raise ValueError(f"Missing required column: {column}")

    # Check 3: Timestamp column must be datetime
    if not pd.api.types.is_datetime64_any_dtype(df["timestamp"]):
        logging.error("Column 'timestamp' is not a datetime type")
        raise ValueError("Column 'timestamp' must be a datetime type")

    # Check 4: Timestamps must be unique
    if df["timestamp"].duplicated().any():
        logging.error("Duplicate timestamps found in weather data")
        raise ValueError("Duplicate timestamps found in weather data")

    logging.info("Schema validation completed successfully")

    # ==========================================================
    # Plausibility validation
    # ==========================================================
    
    # Check: Filter physically implausible values
    initial_row_count = len(df)

    df = df[
        (df["temperature_2m"] >= -50) &
        (df["temperature_2m"] <= 60) &
        (df["precipitation"] >= 0) &
        (df["wind_speed_10m"] >= 0) &
        (df["wind_speed_10m"] <= 75)
    ]

    removed_rows = initial_row_count - len(df)

    if removed_rows > 0:
        logging.warning(
            f"Removed {removed_rows} rows due to implausible values"
        )

    logging.info("Plausibility validation completed successfully")

    # ==========================================================
    # Time-series consistency checks
    # ==========================================================

    # Check 1: Ensure chronological order
    if not df["timestamp"].is_monotonic_increasing:
        logging.warning(
            "Timestamps are not in chronological order. Sorting data."
        )
        df = df.sort_values("timestamp")

    # Check 2: Check for regular hourly intervals
    time_deltas = df["timestamp"].diff().dropna()
    expected_delta = pd.Timedelta(hours=1)

    irregular_intervals = time_deltas[time_deltas != expected_delta]

    if not irregular_intervals.empty:
        logging.warning(
            f"Detected {len(irregular_intervals)} irregular time intervals. "
            "Possible gaps or missing hours in the data."
        )

    logging.info("Time-series consistency checks completed")
    logging.info("Finished validation module")
    
    return df

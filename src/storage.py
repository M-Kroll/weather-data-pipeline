"""
storage.py

This module handles data persistence.
"""

import logging
import os
import sqlite3


def store_weather_data(df, db_path="data/processed/weather.db"):
    """
    Stores weather data in a SQLite database.

    Args:
        df (pandas.DataFrame): Validated weather data
        db_path (str): Path to the SQLite database file
    """
    
    logging.info("Starting storage module")
    logging.info(f"Storing weather data in database: {db_path}")

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    connection = sqlite3.connect(db_path)
    df.to_sql("weather", connection, if_exists="replace", index=False)
    connection.close()

    logging.info(f"Data successfully stored ({len(df)} rows)")
    logging.info("Finished storage module")
"""
storage.py

This module handles persistence of validated weather time-series data.
"""

import logging
import os
import sqlite3


def store_weather_data(df, db_path="data/processed/weather.db"):
    """
    Stores validated weather data in a SQLite database.

    The storage logic is idempotent:
    running the pipeline multiple times will not create duplicate rows.

    Args:
        df (pandas.DataFrame): Validated weather data
        db_path (str): Path to the SQLite database file
    """
    logging.info("Starting storage module")

    # --------------------------------------------------
    # Step 1: Pre-flight checks and setup
    # --------------------------------------------------
    
    # Skip storage if there is no data
    if df.empty:
        logging.warning("No data to store. Skipping database write.")
        return

    # Ensure database directory exists
    database_directory = os.path.dirname(db_path)
    os.makedirs(database_directory, exist_ok=True)

    # --------------------------------------------------
    # Step 2: Open connection and ensure schema
    # --------------------------------------------------
    
    logging.info(f"Connecting to SQLite database at: {db_path}")
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Create table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather (
        timestamp TEXT PRIMARY KEY,
        temperature_2m REAL,
        precipitation REAL,
        weather_code INTEGER,
        wind_speed_10m REAL
    );
    """
    cursor.execute(create_table_query)

    # --------------------------------------------------
    # Step 3: Insert data (idempotent) and finalize
    # --------------------------------------------------
    
    # Insert data with "INSERT OR IGNORE" to avoid duplicates
    insert_query = """
    INSERT OR IGNORE INTO weather (
        timestamp,
        temperature_2m,
        precipitation,
        weather_code,
        wind_speed_10m
    )
    VALUES (?, ?, ?, ?, ?);
    """

    # Track number of inserted rows
    inserted_rows = 0

    # Insert each row from DataFrame
    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            (
                row["timestamp"].isoformat(),
                row["temperature_2m"],
                row["precipitation"],
                int(row["weather_code"]),
                row["wind_speed_10m"],
            ),
        )
        inserted_rows += cursor.rowcount

    # Commit changes and close connection
    connection.commit()
    connection.close()

    logging.info(f"{inserted_rows} new rows inserted into database")
    logging.info("Finished storage module")

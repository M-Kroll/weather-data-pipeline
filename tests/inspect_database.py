"""
inspect_database.py

This script is used to manually inspect the SQLite database
created by the weather data pipeline.

It demonstrates how to:
- connect to a SQLite database
- list available tables
- load data into a pandas DataFrame
- perform basic sanity checks

This is NOT an automated test.
It is an inspection and validation helper.
"""

import sqlite3
import pandas as pd
from pathlib import Path


def inspect_weather_database():
    """
    Connects to the SQLite database and inspects its contents.
    """

    # Path to the SQLite database (relative to project root)
    db_path = Path("data/processed/weather.db")

    if not db_path.exists():
        print(f"Database not found at: {db_path}")
        return

    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # List all tables in the database
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables_df = pd.read_sql_query(tables_query, connection)

    print("Tables in the database:")
    print(tables_df, "\n")

    if tables_df.empty:
        print("No tables found in database.")
        connection.close()
        return

    # Load weather table
    weather_df = pd.read_sql_query("SELECT * FROM weather;", connection)
    connection.close()

    # Basic inspection
    print("Weather table preview:")
    print(weather_df.head(), "\n")

    print("Weather table info:")
    weather_df.info()

    # Simple sanity checks
    print("\nSanity checks:")
    print(f"Number of rows: {len(weather_df)}")
    print(f"Number of columns: {len(weather_df.columns)}")
    print(f"Missing values per column:\n{weather_df.isna().sum()}")


if __name__ == "__main__":
    inspect_weather_database()

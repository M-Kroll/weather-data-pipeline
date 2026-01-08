"""
logging_config.py

This module is responsible for configuring logging for the entire application.
It ensures that log messages are written both to the console and to a log file.
"""

import logging
import os


def setup_logging():
    """
    Sets up the logging configuration.

    - Creates a logs directory if it does not exist
    - Logs messages to both console and file
    """
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler()
        ]
    )

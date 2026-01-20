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

    # Ensure log directory exists
    os.makedirs("logs", exist_ok=True)

    # Configure logging:
    # - INFO level for general pipeline tracking
    # - Custom format showing timestamp, level, and message
    # - Handlers:
    #   * FileHandler: write logs to a file for persistence and review
    #   * StreamHandler: also display logs in the console for immediate feedback

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler()
        ]
    )

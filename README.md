# Weather Data Pipeline

## Description

This project implements a small, modular data pipeline in Python for ingesting, validating,
and storing weather data retrieved from the Open-Meteo API.

The pipeline focuses on clean software structure, reproducibility and transparency rather than
dataset size. It is designed as a foundation for learning and demonstrating core data engineering
concepts such as API-based ingestion, modular processing, logging and relational data storage.

## Objectives

- Build a reproducible Python-based data pipeline without relying on notebooks
- Practice working with external APIs and structured JSON data
- Apply modular software design (ingestion, validation, storage, orchestration)
- Store processed data in a relational database
- Provide a clear and extendable project structure suitable for a public GitHub portfolio

## Project Structure
```
weather-data-pipeline/
│
├── src/
│   ├── main.py              # Pipeline orchestration
│   ├── ingestion.py         # API data retrieval
│   ├── validation.py        # Data quality checks
│   ├── storage.py           # Database persistence
│   └── logging_config.py    # Central logging configuration
│
├── data/
│   └── processed/           # SQLite database
│
├── logs/                    # Application logs
│
├── requirements.txt
├── README.md
└── LICENSE
```
## Methodology

The project follows a structured, engineering-oriented workflow similar to small production
pipelines.

### Objective Definition
The goal was defined as building a minimal yet realistic data pipeline that can be executed
repeatedly and extended over time, while keeping the initial scope intentionally small.

### Data Ingestion
Weather data is retrieved from the Open-Meteo API via HTTP requests and transformed into
a structured Python representation suitable for further processing.

### Validation
Basic data quality checks are applied, such as schema consistency, missing values and
plausibility checks for selected weather parameters.

### Storage
Validated data is persisted in a SQLite database. Tables are created automatically if they
do not yet exist, allowing repeated pipeline executions.

### Orchestration and Logging
A central entry point coordinates the pipeline execution. Logging is used across all modules
to make execution steps and potential errors transparent.

## Tools & Libraries

- Python
- Pandas
- Requests
- SQLite
- Python logging

## Key Features

- Modular, readable Python codebase
- API-based data ingestion
- Centralized logging configuration
- Relational data storage
- Clear separation of responsibilities between pipeline components

## Project Status

In progress. Planned extensions include:

- Support for multiple locations and time ranges
- Scheduling for regular pipeline execution
- Migration to PostgreSQL or a cloud-based database
- Reimplementation of the pipeline using PySpark for larger datasets

## Author

Matthias Kroll

## License

Code is licensed under the MIT License. See LICENSE for details.

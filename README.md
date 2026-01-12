# Weather Data Pipeline

## Description

This project implements a small, reproducible Python-based batch data pipeline that ingests hourly historical weather data from the Open-Meteo Archive API for a single geographic location and stores validated results in a relational database.

The focus is not on dataset size, but on reliability, transparency, and explicit engineering decisions typically required when working with third-party APIs that cannot be fully controlled. The pipeline demonstrates core data engineering concepts such as API-based ingestion, modular processing, logging, validation, and relational data storage in a compact and extensible design.

---

## Objectives

- Build a reproducible Python batch pipeline with clear separation of concerns  
- Ingest structured JSON time-series data from an external API with limited guarantees  
- Apply explicit data validation rules and make data quality decisions transparent  
- Persist weather time-series data in a relational schema suitable for repeated ingestion  
- Provide a modular, well-documented project structure designed for maintainability and extension  

---

## Project Structure

```
weather-data-pipeline/
│
├── src/
│   ├── main.py              # Pipeline orchestration
│   ├── ingestion.py         # Open-Meteo API data retrieval
│   ├── validation.py        # Data quality and consistency checks
│   ├── storage.py           # SQLite persistence layer
│   └── logging_config.py    # Central logging configuration
│
├── data/
│   └── processed/           # Generated SQLite database
│
├── logs/                    # Application logs
│
├── tests/
│   └── inspect_database.py  # Database inspection and sanity checks
│
├── requirements.txt
├── README.md
└── LICENSE

```

---

## Methodology

The project follows a structured, engineering-oriented workflow similar to small production batch pipelines. Emphasis is placed on reproducibility, transparency, and explicit handling of data quality decisions.

### Objective Definition

The goal was defined as building a minimal yet realistic data pipeline that can be executed repeatedly, extended over time, and used to demonstrate engineering decisions rather than exploratory analysis.

### Data Ingestion

Weather data is retrieved from the Open-Meteo Archive API using HTTP requests and transformed into a structured tabular representation. The current implementation ingests hourly historical data for Dortmund, Germany, for a configurable time range.

Basic error handling and request retries are implemented to deal with transient API failures.

### Validation

The validation module is designed to support three classes of checks:

- **Schema validation** (field presence, data types, duplicate timestamps)  
- **Plausibility checks** (e.g. realistic temperature, precipitation, and wind speed ranges)  
- **Time-series consistency checks** (chronological order, regular intervals, detection of gaps)

At the current stage, foundational checks are implemented. The validation layer is intentionally structured to allow incremental extension without modifying the ingestion logic.

### Storage

Validated data is persisted in a SQLite database. Tables are created automatically if they do not yet exist, allowing repeated executions without manual setup.

SQLite was chosen to focus on schema design, idempotent writes, and reproducibility while avoiding infrastructure complexity. Known limitations regarding concurrency and scaling are accepted by design and documented.

### Orchestration and Logging

A single entry point coordinates ingestion, validation, and storage. Centralized logging across all modules provides transparency into execution steps, validation outcomes, and data quality decisions.

### Design Decisions

- **Batch processing** was chosen over streaming to prioritize reproducibility and simplicity  
- **SQLite** was selected as a lightweight relational backend for local execution  
- **No notebooks** are used to ensure non-interactive, script-based execution  
- The codebase is structured to allow future migration to PostgreSQL or PySpark without rewriting core logic  

---

## Tools & Libraries

- Python  
- Pandas  
- NumPy  
- Open-Meteo Requests  
- Requests-Cache and Retry-Requests  
- SQLite  
- Python logging  

---

## Key Features

- Modular, readable Python codebase  
- API-based ingestion of hourly weather data  
- Explicit data validation and logging of quality issues  
- Relational storage with repeatable batch execution  
- Clear separation of ingestion, validation, and persistence layers  

---

## Project Status

In progress. The project is intentionally developed incrementally. Core ingestion and orchestration are implemented; validation and persistence layers are designed for extension and currently contain foundational logic.

Planned extensions include:

- Support for multiple locations and configurable time windows  
- Extended validation and aggregation logic  
- Scheduling for regular execution  
- Migration to PostgreSQL or cloud-based storage  
- Reimplementation using PySpark for larger-scale processing  

---

## Author

Matthias Kroll

---

## License

Code is licensed under the MIT License. See LICENSE for details.

# Weather Data Pipeline

## Description

This project implements a small, reproducible data pipeline in Python that ingests time-series weather data from an external API and stores validated results in a relational database.

The focus is not on dataset size, but on reliability, transparency, and engineering decisions typically required when working with third-party data sources that cannot be fully controlled. This project demonstrates core data engineering concepts such as API-based ingestion, modular processing, logging, and relational data storage in a small, extendable pipeline.

---

## Objectives

- Build a reproducible Python-based batch pipeline with clear separation of concerns  
- Handle structured JSON data from an external API with limited guarantees  
- Apply explicit data validation rules and make data quality decisions transparent  
- Persist time-series data in a relational schema designed for repeated ingestion  
- Provide a modular, well-documented project structure to facilitate maintainability, easy extension, and reuse  

---

## Project Structure
```
weather-data-pipeline/
│
├── src/
│   ├── main.py              # Pipeline orchestration
│   ├── ingestion.py         # API data retrieval
│   ├── validation.py        # Schema, plausibility, and time-series consistency checks
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

---

## Methodology

The project follows a structured, engineering-oriented workflow similar to small production pipelines. It is designed for reproducibility, transparency, and easy extension.

### Objective Definition

The goal was defined as building a minimal yet realistic data pipeline that can be executed repeatedly, extended over time, and serves as a foundation for demonstrating engineering decisions and problem-solving in data workflows.

### Data Ingestion

Weather data is retrieved from the Open-Meteo API via HTTP requests and transformed into a structured Python representation suitable for further processing. The pipeline handles limited guarantees from the external API and implements basic error handling for missing or malformed data.

### Validation

Data quality is verified through three types of checks:

1. **Schema Validation** – ensures all expected fields are present, data types are correct, and there are no duplicate timestamps.  
2. **Plausibility Checks** – validates domain-specific constraints, e.g., temperature between −50 °C and +60 °C, precipitation ≥ 0, realistic wind speeds.  
3. **Time-Series Consistency** – checks for regular intervals, chronological order, and flags gaps without discarding all data.

Validation errors are handled explicitly: schema violations halt the pipeline, individual record inconsistencies are logged and discarded, and time gaps are flagged in the logs.

### Storage

Validated data is persisted in a SQLite database. Tables are created automatically if they do not yet exist, enabling repeated executions. The choice of SQLite allows focus on schema design, idempotent writes, and reproducibility without infrastructure overhead. Limitations for scaling and concurrency are documented in the README.

### Orchestration and Logging

A central entry point coordinates pipeline execution. Logging is used across all modules to provide transparency on execution steps, validation outcomes, and errors, ensuring traceability of decisions and data quality issues.

### Design Decisions

- **Batch processing** was chosen over streaming for simplicity and reproducibility while reflecting common daily ingestion jobs.  
- **SQLite** was used as a lightweight relational database to focus on core engineering tasks.  
- **No notebooks** are used to ensure the pipeline can run non-interactively and is suitable for extension or deployment.  
- Planned extensions, such as migration to PostgreSQL or PySpark implementation, are designed to scale without changing the core logic.

---

## Tools & Libraries

- Python  
- Pandas  
- Requests  
- SQLite  
- Python logging  

---

## Key Features

- Modular, readable Python codebase  
- API-based data ingestion with error handling  
- Schema, plausibility, and time-series validation  
- Centralized logging and traceable pipeline execution  
- Relational data storage with repeatable ingestion  
- Clear separation of responsibilities between pipeline components  

---

## Project Status

In progress. Planned extensions include:

- Support for multiple locations and time ranges  
- Scheduling for regular pipeline execution  
- Migration to PostgreSQL or a cloud-based database  
- Reimplementation of the pipeline using PySpark for larger datasets  

---

## Author

Matthias Kroll

---

## License

Code is licensed under the MIT License. See LICENSE for details.


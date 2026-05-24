# Weather ETL Pipeline
## Overview
A simple ETL pipeline in Python that extracts weather data from an API, transforms it, and saves it as a CSV file.

## Features
- API data extraction (from Open-Meteo)
- Data transformation using Pandas
- CSV data storage
- Logging for monitoring and debugging

## Tech Stack
- Python
- Pandas
- Requests

## Project Structure

weather_etl_pipeline/
├── src/ # ETL script
├── data/ # Output CSV
├── logs/ # Log files
├── requirements.txt
└── README.md

## How to Run

pip install -r requirements.txt
python src/etl_pipeline.py

## Output
- `/data/weather_data.csv`
- `/logs/pipeline.log`
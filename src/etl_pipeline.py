import pandas as pd
import requests
from datetime import datetime
import logging

logging.basicConfig(
    filename = "./logs/pipeline.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Pipeline started")
try:
    logging.info("Starting data extraction")
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : 8.7274,
        "longitude" : 77.6838,
        "current_weather" : True
    }
    response = requests.get(url , params = params)
    if response.status_code == 200:
        logging.info("Extraction Successful")
    else:
        logging.error(f"Extraction failed with status code: {response.status_code}")
    data = response.json()
    logging.info("JSON data extracted")
    logging.info("Starting transformation")
    current = data["current_weather"]
    weather_data = {
        "city" : "Tirunelveli",
        "temperature_2m" : current["temperature"],
        "weathercode" : current["weathercode"],
        "windspeed" : current["windspeed"],
        "wind_direction" : current["winddirection"],
        "time" : current["time"],
        "ingestion_time" : datetime.now()
    }
    df = pd.DataFrame([weather_data])
    logging.info("Transformation completed")
    logging.info("Loading data")
    df.to_csv("./data/weather_data.csv" , index=False)
    logging.info("Loading completed")
except Exception as e:
    logging.exception(f"Pipeline failed due to exception {e}")
    print("Pipeline failed")
    
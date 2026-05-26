import pandas as pd
import requests
from datetime import datetime
import logging
import os

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
    base_path = "./data/raw"
    month_folder = datetime.now().strftime("%Y-%m")
    folder_path = os.path.join(base_path , month_folder)
    os.makedirs(folder_path , exist_ok = True)
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".parquet"
    file_path = os.path.join(folder_path , file_name)
    df.to_parquet(file_path , index=False)
    logging.info("Loading completed - New file created")
except Exception as e:
    logging.exception(f"Pipeline failed due to exception {e}")
    print("Pipeline failed")
    
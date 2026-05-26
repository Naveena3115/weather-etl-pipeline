import glob
import logging
from datetime import datetime
import pandas as pd
import os

logging.basicConfig(
    filename = "./logs/rollup.log",
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Monthly rollup initiated")
try:
    month = datetime.now().strftime("%Y-%m")
    month_path = f"./data/raw/{month}"
    files = glob.glob(f"{month_path}/*.parquet")

    df= [pd.read_parquet(f) for f in files]
    df_final = pd.concat(df , ignore_index=True)

    os.makedirs("./data/processed" , exist_ok =True)
    path = f"./data/processed/{month}.parquet"
    df_final.to_parquet(path , index  =False)
    logging.info("Monthly rollup completed")
except Exception as e:
    logging.exception(f"Monthly rollup failed : {e}")
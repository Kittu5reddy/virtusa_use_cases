from dotenv import load_dotenv
import os
import json

load_dotenv()

RATES: dict = json.loads(os.getenv("RATES"))

NORMAL_HOUR_SURGE: float = float(os.getenv("NORMAL_HOUR_SURGE"))
PEAK_HOUR_SURGE: float = float(os.getenv("PEAK_HOUR_SURGE"))
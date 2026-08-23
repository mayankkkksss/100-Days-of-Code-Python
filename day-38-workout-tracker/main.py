import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

API_ENDPOINT = "https://app.100daysofpython.dev"

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_AUTHENTICATION = os.environ["SHEETY_AUTHENTICATION"]

calories_calculate_endpoint = f"{API_ENDPOINT}/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=calories_calculate_endpoint, json=data, headers=headers)
response.raise_for_status()
result = response.json()["exercises"][0]

today = datetime.now()
formated_date = today.strftime("%d/%m/%Y")
formated_time = today.strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": SHEETY_AUTHENTICATION,
}

new_record = {
    "workout": {
        "date": formated_date,
        "time": formated_time,
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=new_record, headers=sheety_headers)
response.raise_for_status()


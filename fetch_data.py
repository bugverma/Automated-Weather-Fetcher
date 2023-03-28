import requests
import json
from dotenv import load_dotenv
import constants
import os

def fetch_data():

    load_dotenv()

    # Readings Data
    readings_url = f"{os.getenv(constants.READINGS_URL)}"
    readings_payload={}
    readings_headers = {
    'Cookie': f"{os.getenv(constants.READINGS_HEADERS)}"
    }
    readings_response = requests.request("GET", readings_url, headers=readings_headers, data=readings_payload)
    readings_info = readings_response.text
    readings_data = json.loads(readings_info)

    # Forecast Data
    forecast_url = f"{os.getenv(constants.FORECAST_URL)}"
    forecast_payload={}
    forecast_headers = {
    'Cookie': f"{os.getenv(constants.FORECAST_HEADERS)}"
    }
    forecast_response = requests.request("GET", forecast_url, headers=forecast_headers, data=forecast_payload)
    forecast_info = forecast_response.text
    forecast_data = json.loads(forecast_info)

    # Measurement Dictionary
    measurements = {
        "currentTemp": readings_data["temp_c"],
        "maxTemp": readings_data["temp_hi_c"],
        "maxTempTime": readings_data["temp_hi_time"],
        "minTemp": readings_data["temp_lo_c"],
        "minTempTime": readings_data["temp_lo_time"],
        "rainfallToday": readings_data["precip_today_metric"],
        "rainfall1hr": readings_data["precip_1hr_metric"],
        "rainfall12hr": readings_data["precip_12hr_metric"],
        "forecastToday": forecast_data["forecast"]["txt_forecast"]["forecastday"][0]["fcttext"],
        "forecastTonight": forecast_data["forecast"]["txt_forecast"]["forecastday"][1]["fcttext"]
    }

    return measurements

'''
OUTPUT
------

{'currentTemp': '20.7', 'maxTemp': '20.7', 'maxTempTime': '02:00PM', 'minTemp': '9.5', 'minTempTime': '06:00AM', 'rainfallToday': '0', 'rainfall1hr': '0', 'rainfall12hr': '0', 'forecastToday': 'Sunny. High 67F. Winds light and variable.', 'forecastTonight': 'A clear sky. Low around 45F. Winds light and variable.'}

{
  "currentTemp": "20.7",
  "maxTemp": "20.7",
  "maxTempTime": "02:00PM",
  "minTemp": "9.5",
  "minTempTime": "06:00AM",
  "rainfallToday": "0",
  "rainfall1hr": "0",
  "rainfall12hr": "0",
  "forecastToday": "Sunny. High 67F. Winds light and variable.",
  "forecastTonight": "A clear sky. Low around 45F. Winds light and variable."
}

'''

from twilio.rest import Client
from dotenv import load_dotenv
import constants
import os

def send_message(measurements):

  load_dotenv()

  client = Client(os.getenv(constants.ACCOUNT_SID), os.getenv(constants.AUTH_TOKEN)) 
  
  message = client.messages.create(  
                                messaging_service_sid=f"{os.getenv(constants.MESSAGING_SERVICE_ID)}", 
                                body=f'''
  TEMPERATURE
  --------------------------
  Current Temperature (8:00 AM): {measurements["currentTemp"]} C
  Maximum Temperature: {measurements["maxTemp"]} C
  Maximum Temperature Time: {measurements["maxTempTime"]}
  Minimum Temperature: {measurements["minTemp"]} C
  Minimum Temperature Time: {measurements["minTempTime"]}

  RAINFALL
  --------------------------
  Rainfall Today: {measurements["rainfallToday"]}mm
  Rainfall (1 Hr): {measurements["rainfall1hr"]}mm
  Rainfall (12 Hr): {measurements["rainfall12hr"]}mm
  Rainfall Cumulative: {measurements["rainfallCumulative"]}mm

  WEATHER FORECAST
  --------------------------
  Today: {measurements["forecastToday"]}
  Tonight: {measurements["forecastTonight"]}
  ''',      
                                to=f"{os.getenv(constants.TO_NUMBER)}"
                            ) 
  
  f = open("./sent_message.log", "w")
  f.write(str(message.date_created))
  f.close()

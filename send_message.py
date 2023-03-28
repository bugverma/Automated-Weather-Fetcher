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

  '''
  # EXAMPLE JSON RESPONSE

  {
    "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "api_version": "2010-04-01",
    "body": "Revenge of the Sith was clearly the best of the prequel trilogy.",
    "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
    "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
    "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
    "direction": "outbound-api",
    "error_code": null,
    "error_message": null,
    "from": null,
    "messaging_service_sid": "MG9752274e9e519418a7406176694466fa",
    "num_media": "0",
    "num_segments": "1",
    "price": null,
    "price_unit": null,
    "sid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "status": "sent",
    "subresource_uris": {
      "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
    },
    "to": "+441632960675",
    "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
  }

  '''
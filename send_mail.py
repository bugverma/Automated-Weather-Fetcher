import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from dotenv import load_dotenv
import constants
import os



def send_mail(measurements):

    load_dotenv()

    msg = EmailMessage() 
    
    msg.add_alternative(
        f'''
            <html>
                <body>
                    <h3><u>TEMPERATURE</u></h3>
                    <p><strong>Current Temperature (8:00 AM):</strong> {measurements["currentTemp"]} C</p>
                    <p><strong>Maximum Temperature:</strong> {measurements["maxTemp"]} C</p>
                    <p><strong>Maximum Temperature Time:</strong> {measurements["maxTempTime"]}</p>
                    <p><strong>Minimum Temperature:</strong> {measurements["minTemp"]} C</p>
                    <p><strong>Minimum Temperature Time:</strong> {measurements["minTempTime"]}</p>
                    <br>
                    <h3><u>RAINFALL</u></h3>
                    <p><strong>Rainfall Today:</strong> {measurements["rainfallToday"]}mm</p>
                    <p><strong>Rainfall (1 Hr):</strong> {measurements["rainfall1hr"]}mm</p>
                    <p><strong>Rainfall (12 Hr):</strong> {measurements["rainfall12hr"]}mm</p>
                    <p><strong>Rainfall Cumulative:</strong> {measurements["rainfallCumulative"]}mm</p>
                    <br>
                    <h3><u>WEATHER FORECAST</u></h3>
                    <p><strong>Today:</strong> {measurements["forecastToday"]}</p>
                    <p><strong>Tonight:</strong> {measurements["forecastTonight"]}</p>
                </body>
            </html>
        ''', 
        subtype = "html",
    )

    msg['Subject'] = f"{os.getenv(constants.SUBJECT)}"
    msg['From'] = formataddr((f"{os.getenv(constants.FROM_COMPANY)}", f"{os.getenv(constants.FROM)}"))
    msg['To'] = f"{os.getenv(constants.TO)}"
    msg['BCC'] = f"{os.getenv(constants.BCC)}"

    server = smtplib.SMTP_SSL(f"{os.getenv(constants.SMTP_EMAIL)}", os.getenv(constants.SMTP_PORT))
    server.login(f"{os.getenv(constants.FROM)}", f"{os.getenv(constants.SMTP_PASSWORD)}")

    server.send_message(msg)

    server.quit()

'''

send_mail({
  "currentTemp": "20.7",
  "maxTemp": "20.7",
  "maxTempTime": "02:00PM",
  "minTemp": "9.5",
  "minTempTime": "06:00AM",
  "rainfallToday": "0",
  "rainfall1hr": "0",
  "rainfall12hr": "0",
  "rainfallCumulative": "0",
  "forecastToday": "Sunny. High 67F. Winds light and variable.",
  "forecastTonight": "A clear sky. Low around 45F. Winds light and variable."
})

'''

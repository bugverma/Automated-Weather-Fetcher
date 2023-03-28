from fetch_data import fetch_data
from send_mail import send_mail
from cumulative_rainfall import cumulative_rainfall
from send_message import send_message

def main():
    
    # Fetching Data
    measurements = fetch_data()

    # Adding Cumulative Rainfall to the Measurements
    measurements["rainfallCumulative"] = cumulative_rainfall(measurements['rainfallToday'])

    # Sending Mail
    send_mail(measurements)
    # Mail Sent

    # Sending SMS
    send_message(measurements)
    # SMS Sent

main()

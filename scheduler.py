from main import main
import schedule
import time

schedule.every().day.at("17:10").do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)
